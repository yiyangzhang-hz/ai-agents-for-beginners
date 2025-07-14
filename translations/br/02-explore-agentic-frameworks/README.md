<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:00:18+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "br"
}
-->
. De acordo com a Wikipedia, um ator é _o bloco básico da computação concorrente. Em resposta a uma mensagem que recebe, um ator pode: tomar decisões locais, criar mais atores, enviar mais mensagens e determinar como responder à próxima mensagem recebida_.

**Casos de Uso**: Automatização de geração de código, tarefas de análise de dados e construção de agentes personalizados para funções de planejamento e pesquisa.

Aqui estão alguns conceitos centrais importantes do AutoGen:

- **Agentes**. Um agente é uma entidade de software que:
  - **Se comunica via mensagens**, que podem ser síncronas ou assíncronas.
  - **Mantém seu próprio estado**, que pode ser modificado por mensagens recebidas.
  - **Executa ações** em resposta às mensagens recebidas ou mudanças em seu estado. Essas ações podem modificar o estado do agente e produzir efeitos externos, como atualizar logs de mensagens, enviar novas mensagens, executar código ou fazer chamadas de API.
    
  Aqui você tem um pequeno trecho de código onde cria seu próprio agente com capacidades de chat:

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
    
    No código anterior, `MyAssistant` foi criado e herda de `RoutedAgent`. Ele possui um manipulador de mensagens que imprime o conteúdo da mensagem e então envia uma resposta usando o delegado `AssistantAgent`. Note especialmente como atribuímos a `self._delegate` uma instância de `AssistantAgent`, que é um agente pré-construído capaz de lidar com completions de chat.

    Vamos informar ao AutoGen sobre esse tipo de agente e iniciar o programa a seguir:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    No código anterior, os agentes são registrados no runtime e então uma mensagem é enviada ao agente, resultando na seguinte saída:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agentes**. O AutoGen suporta a criação de múltiplos agentes que podem trabalhar juntos para realizar tarefas complexas. Os agentes podem se comunicar, compartilhar informações e coordenar suas ações para resolver problemas de forma mais eficiente. Para criar um sistema multiagente, você pode definir diferentes tipos de agentes com funções e papéis especializados, como recuperação de dados, análise, tomada de decisão e interação com o usuário. Vamos ver como essa criação se parece para termos uma ideia:

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

    No código anterior, temos um `GroupChatManager` que está registrado no runtime. Esse gerente é responsável por coordenar as interações entre diferentes tipos de agentes, como escritores, ilustradores, editores e usuários.

- **Agent Runtime**. O framework fornece um ambiente de execução que possibilita a comunicação entre agentes, gerencia suas identidades e ciclos de vida, e impõe limites de segurança e privacidade. Isso significa que você pode executar seus agentes em um ambiente seguro e controlado, garantindo que eles possam interagir de forma segura e eficiente. Existem dois runtimes de interesse:
  - **Runtime independente**. É uma boa escolha para aplicações de processo único onde todos os agentes são implementados na mesma linguagem de programação e executados no mesmo processo. Aqui está uma ilustração de como funciona:

Pilha de aplicação

    *agentes se comunicam via mensagens através do runtime, e o runtime gerencia o ciclo de vida dos agentes*

  - **Runtime distribuído de agentes**, adequado para aplicações multiprocessos onde agentes podem ser implementados em diferentes linguagens de programação e executados em máquinas distintas. Aqui está uma ilustração de como funciona:

## Semantic Kernel + Agent Framework

Semantic Kernel é um SDK de orquestração de IA pronto para uso empresarial. Ele consiste em conectores de IA e memória, junto com um Agent Framework.

Vamos primeiro cobrir alguns componentes centrais:

- **Conectores de IA**: Interface com serviços externos de IA e fontes de dados para uso tanto em Python quanto em C#.

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

    Aqui você tem um exemplo simples de como criar um kernel e adicionar um serviço de chat completion. O Semantic Kernel cria uma conexão com um serviço externo de IA, neste caso, Azure OpenAI Chat Completion.

- **Plugins**: Encapsulam funções que uma aplicação pode usar. Existem plugins prontos e também personalizados que você pode criar. Um conceito relacionado são as "funções de prompt". Em vez de fornecer comandos em linguagem natural para invocar funções, você transmite certas funções para o modelo. Com base no contexto atual do chat, o modelo pode escolher chamar uma dessas funções para completar uma solicitação ou consulta. Veja um exemplo:

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

    Aqui, você primeiro tem um template de prompt `skPrompt` que deixa espaço para o usuário inserir texto, `$userInput`. Depois você cria a função do kernel `SummarizeText` e a importa para o kernel com o nome do plugin `SemanticFunctions`. Note o nome da função que ajuda o Semantic Kernel a entender o que a função faz e quando deve ser chamada.

- **Função nativa**: Também existem funções nativas que o framework pode chamar diretamente para executar a tarefa. Aqui está um exemplo de uma função que recupera o conteúdo de um arquivo:

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

- **Memória**: Abstrai e simplifica o gerenciamento de contexto para apps de IA. A ideia da memória é que isso é algo que o LLM deve conhecer. Você pode armazenar essa informação em um vetor store, que acaba sendo um banco de dados em memória, um banco de dados vetorial ou similar. Aqui está um exemplo de um cenário muito simplificado onde *fatos* são adicionados à memória:

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

    Esses fatos são então armazenados na coleção de memória `SummarizedAzureDocs`. Este é um exemplo muito simplificado, mas você pode ver como armazenar informações na memória para o LLM usar.
## Aula Anterior

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Aula

[Entendendo Padrões de Design Agêntico](../03-agentic-design-patterns/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.