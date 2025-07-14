<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:59:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pt"
}
-->
. De acordo com a Wikipédia, um ator é _a unidade básica da computação concorrente. Em resposta a uma mensagem que recebe, um ator pode: tomar decisões locais, criar mais atores, enviar mais mensagens e determinar como responder à próxima mensagem recebida_.

**Casos de uso**: Automatizar geração de código, tarefas de análise de dados e construir agentes personalizados para funções de planeamento e investigação.

Aqui estão alguns conceitos fundamentais importantes do AutoGen:

- **Agentes**. Um agente é uma entidade de software que:
  - **Comunica-se via mensagens**, que podem ser síncronas ou assíncronas.
  - **Mantém o seu próprio estado**, que pode ser modificado por mensagens recebidas.
  - **Executa ações** em resposta a mensagens recebidas ou alterações no seu estado. Estas ações podem modificar o estado do agente e produzir efeitos externos, como atualizar registos de mensagens, enviar novas mensagens, executar código ou fazer chamadas a APIs.
    
  Aqui tem um pequeno excerto de código onde cria o seu próprio agente com capacidades de Chat:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    No código anterior, `MyAssistant` foi criado e herda de `RoutedAgent`. Tem um manipulador de mensagens que imprime o conteúdo da mensagem e depois envia uma resposta usando o delegado `AssistantAgent`. Note especialmente como atribuímos a `self._delegate` uma instância de `AssistantAgent`, que é um agente pré-construído capaz de lidar com chat completions.

    Vamos informar o AutoGen sobre este tipo de agente e iniciar o programa a seguir:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    No código anterior, os agentes são registados no runtime e depois é enviada uma mensagem ao agente, resultando na seguinte saída:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agentes**. O AutoGen suporta a criação de múltiplos agentes que podem trabalhar em conjunto para realizar tarefas complexas. Os agentes podem comunicar, partilhar informação e coordenar as suas ações para resolver problemas de forma mais eficiente. Para criar um sistema multi-agente, pode definir diferentes tipos de agentes com funções e papéis especializados, como recuperação de dados, análise, tomada de decisões e interação com o utilizador. Vamos ver como é feita essa criação para termos uma ideia:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    No código anterior temos um `GroupChatManager` que está registado no runtime. Este gestor é responsável por coordenar as interações entre diferentes tipos de agentes, como escritores, ilustradores, editores e utilizadores.

- **Agent Runtime**. O framework fornece um ambiente de execução que permite a comunicação entre agentes, gere as suas identidades e ciclos de vida, e aplica limites de segurança e privacidade. Isto significa que pode executar os seus agentes num ambiente seguro e controlado, garantindo que podem interagir de forma segura e eficiente. Existem dois runtimes de interesse:
  - **Runtime autónomo**. Esta é uma boa escolha para aplicações de processo único onde todos os agentes são implementados na mesma linguagem de programação e correm no mesmo processo. Aqui está uma ilustração de como funciona:

Stack da aplicação

    *os agentes comunicam via mensagens através do runtime, e o runtime gere o ciclo de vida dos agentes*

  - **Runtime distribuído de agentes**, adequado para aplicações multi-processo onde os agentes podem ser implementados em diferentes linguagens de programação e correr em máquinas diferentes. Aqui está uma ilustração de como funciona:

## Semantic Kernel + Agent Framework

Semantic Kernel é um SDK de orquestração de IA pronto para empresas. Consiste em conectores de IA e memória, juntamente com um Agent Framework.

Vamos primeiro abordar alguns componentes principais:

- **Conectores de IA**: Esta é uma interface com serviços externos de IA e fontes de dados para uso tanto em Python como em C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Aqui tem um exemplo simples de como pode criar um kernel e adicionar um serviço de chat completion. O Semantic Kernel cria uma ligação a um serviço externo de IA, neste caso, Azure OpenAI Chat Completion.

- **Plugins**: Estes encapsulam funções que uma aplicação pode usar. Existem plugins prontos a usar e outros personalizados que pode criar. Um conceito relacionado são as "funções prompt". Em vez de fornecer indicações em linguagem natural para invocar funções, transmite certas funções ao modelo. Com base no contexto atual do chat, o modelo pode escolher chamar uma dessas funções para completar um pedido ou consulta. Aqui está um exemplo:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Aqui, primeiro tem um template de prompt `skPrompt` que deixa espaço para o utilizador inserir texto, `$userInput`. Depois cria a função do kernel `SummarizeText` e importa-a para o kernel com o nome do plugin `SemanticFunctions`. Note o nome da função que ajuda o Semantic Kernel a entender o que a função faz e quando deve ser chamada.

- **Função nativa**: Existem também funções nativas que o framework pode chamar diretamente para executar a tarefa. Aqui está um exemplo de uma função que recupera o conteúdo de um ficheiro:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Memória**: Abstrai e simplifica a gestão de contexto para aplicações de IA. A ideia da memória é que isto é algo que o LLM deve conhecer. Pode armazenar esta informação numa loja de vetores que acaba por ser uma base de dados em memória, uma base de dados de vetores ou similar. Aqui está um exemplo de um cenário muito simplificado onde *factos* são adicionados à memória:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    Estes factos são depois armazenados na coleção de memória `SummarizedAzureDocs`. Este é um exemplo muito simplificado, mas pode ver como pode armazenar informação na memória para o LLM usar.
## Aula Anterior

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Compreender os Padrões de Design Agêntico](../03-agentic-design-patterns/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.