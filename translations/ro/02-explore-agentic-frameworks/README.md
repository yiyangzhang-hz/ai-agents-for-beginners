<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:11:32+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ro"
}
-->
. Conform Wikipedia, un actor este _unitatea de bază a calculului concurent. Ca răspuns la un mesaj primit, un actor poate: lua decizii locale, crea mai mulți actori, trimite mai multe mesaje și determina cum să răspundă la următorul mesaj primit_.

**Cazuri de utilizare**: Automatizarea generării de cod, sarcini de analiză a datelor și construirea de agenți personalizați pentru funcții de planificare și cercetare.

Iată câteva concepte de bază importante ale AutoGen:

- **Agenți**. Un agent este o entitate software care:
  - **Comunică prin mesaje**, aceste mesaje pot fi sincrone sau asincrone.
  - **Își menține propriul stadiu**, care poate fi modificat de mesajele primite.
  - **Execută acțiuni** ca răspuns la mesajele primite sau la schimbările din starea sa. Aceste acțiuni pot modifica starea agentului și pot produce efecte externe, cum ar fi actualizarea jurnalelor de mesaje, trimiterea de mesaje noi, executarea de cod sau apeluri API.
    
  Aici ai un scurt fragment de cod în care îți creezi propriul agent cu capabilități de chat:

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
    
    În codul anterior, `MyAssistant` a fost creat și moștenește din `RoutedAgent`. Are un handler pentru mesaje care afișează conținutul mesajului și apoi trimite un răspuns folosind delegatul `AssistantAgent`. Observă în special cum atribuim lui `self._delegate` o instanță a `AssistantAgent`, care este un agent predefinit ce poate gestiona completările de chat.

    Să anunțăm AutoGen despre acest tip de agent și să pornim programul:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    În codul anterior, agenții sunt înregistrați în runtime, iar apoi un mesaj este trimis agentului, rezultând următorul output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenti**. AutoGen suportă crearea mai multor agenți care pot lucra împreună pentru a realiza sarcini complexe. Agenții pot comunica, împărtăși informații și coordona acțiunile pentru a rezolva probleme mai eficient. Pentru a crea un sistem multi-agent, poți defini diferite tipuri de agenți cu funcții și roluri specializate, cum ar fi recuperarea datelor, analiza, luarea deciziilor și interacțiunea cu utilizatorul. Să vedem cum arată o astfel de creație pentru a ne face o idee:

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

    În codul anterior avem un `GroupChatManager` care este înregistrat în runtime. Acest manager este responsabil pentru coordonarea interacțiunilor între diferite tipuri de agenți, cum ar fi scriitori, ilustratori, editori și utilizatori.

- **Agent Runtime**. Framework-ul oferă un mediu de execuție care permite comunicarea între agenți, gestionează identitățile și ciclurile de viață ale acestora și impune limite de securitate și confidențialitate. Aceasta înseamnă că poți rula agenții într-un mediu sigur și controlat, asigurându-te că pot interacționa în siguranță și eficient. Există două tipuri de runtime-uri de interes:
  - **Runtime independent**. Este o alegere bună pentru aplicații cu un singur proces, unde toți agenții sunt implementați în același limbaj de programare și rulează în același proces. Iată o ilustrație a modului în care funcționează:

Stivă aplicațională

    *agenții comunică prin mesaje prin intermediul runtime-ului, iar runtime-ul gestionează ciclul de viață al agenților*

  - **Runtime distribuit pentru agenți**, este potrivit pentru aplicații multi-proces unde agenții pot fi implementați în diferite limbaje de programare și rulează pe mașini diferite. Iată o ilustrație a modului în care funcționează:

## Semantic Kernel + Agent Framework

Semantic Kernel este un SDK de orchestrare AI pregătit pentru mediul enterprise. Acesta constă în conectori AI și de memorie, împreună cu un Agent Framework.

Să acoperim mai întâi câteva componente de bază:

- **Conectori AI**: Aceasta este o interfață cu servicii AI externe și surse de date, utilizabilă atât în Python, cât și în C#.

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

    Aici ai un exemplu simplu despre cum poți crea un kernel și adăuga un serviciu de completare chat. Semantic Kernel creează o conexiune către un serviciu AI extern, în acest caz, Azure OpenAI Chat Completion.

- **Pluginuri**: Acestea încapsulează funcții pe care o aplicație le poate folosi. Există atât pluginuri gata făcute, cât și unele personalizate pe care le poți crea. Un concept înrudit este „funcțiile prompt”. În loc să oferi indicii în limbaj natural pentru invocarea funcțiilor, transmiți anumite funcții către model. Pe baza contextului curent al chatului, modelul poate alege să apeleze una dintre aceste funcții pentru a finaliza o cerere sau o interogare. Iată un exemplu:

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

    Aici, mai întâi ai un șablon de prompt `skPrompt` care lasă loc pentru ca utilizatorul să introducă text, `$userInput`. Apoi creezi funcția kernel `SummarizeText` și o imporți în kernel cu numele pluginului `SemanticFunctions`. Observă numele funcției care ajută Semantic Kernel să înțeleagă ce face funcția și când ar trebui apelată.

- **Funcție nativă**: Există și funcții native pe care framework-ul le poate apela direct pentru a îndeplini sarcina. Iată un exemplu de astfel de funcție care preia conținutul dintr-un fișier:

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

- **Memorie**: Abstractizează și simplifică gestionarea contextului pentru aplicațiile AI. Ideea cu memoria este că aceasta reprezintă ceva ce LLM-ul ar trebui să cunoască. Poți stoca aceste informații într-un vector store, care ajunge să fie o bază de date în memorie sau o bază de date vectorială sau similar. Iată un exemplu al unui scenariu foarte simplificat în care *faptele* sunt adăugate în memorie:

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

    Aceste fapte sunt apoi stocate în colecția de memorie `SummarizedAzureDocs`. Acesta este un exemplu foarte simplificat, dar poți vedea cum poți stoca informații în memorie pentru ca LLM-ul să le folosească.
## Lecția Anterioară

[Introducere în Agenții AI și Cazuri de Utilizare ale Agenților](../01-intro-to-ai-agents/README.md)

## Lecția Următoare

[Înțelegerea Pattern-urilor de Design Agentic](../03-agentic-design-patterns/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.