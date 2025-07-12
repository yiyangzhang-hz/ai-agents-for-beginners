<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:00:44+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "it"
}
-->
. Secondo Wikipedia, un attore è _il blocco fondamentale del calcolo concorrente. In risposta a un messaggio ricevuto, un attore può: prendere decisioni locali, creare altri attori, inviare altri messaggi e determinare come rispondere al prossimo messaggio ricevuto_.

**Casi d'uso**: Automazione della generazione di codice, attività di analisi dei dati e creazione di agenti personalizzati per funzioni di pianificazione e ricerca.

Ecco alcuni concetti chiave di AutoGen:

- **Agenti**. Un agente è un'entità software che:
  - **Comunica tramite messaggi**, che possono essere sincroni o asincroni.
  - **Mantiene il proprio stato**, che può essere modificato dai messaggi in arrivo.
  - **Esegue azioni** in risposta ai messaggi ricevuti o ai cambiamenti del proprio stato. Queste azioni possono modificare lo stato dell’agente e produrre effetti esterni, come aggiornare i log dei messaggi, inviare nuovi messaggi, eseguire codice o effettuare chiamate API.
    
  Qui trovi un breve snippet di codice in cui crei il tuo agente con capacità di chat:

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
    
    Nel codice precedente, `MyAssistant` è stato creato ereditando da `RoutedAgent`. Ha un gestore di messaggi che stampa il contenuto del messaggio e poi invia una risposta usando il delegato `AssistantAgent`. Nota in particolare come assegniamo a `self._delegate` un’istanza di `AssistantAgent`, che è un agente predefinito in grado di gestire completamenti di chat.

    Ora facciamo sapere ad AutoGen di questo tipo di agente e avviamo il programma:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Nel codice precedente gli agenti sono registrati nel runtime e poi viene inviato un messaggio all’agente, con il seguente output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenti**. AutoGen supporta la creazione di più agenti che possono lavorare insieme per raggiungere compiti complessi. Gli agenti possono comunicare, condividere informazioni e coordinare le loro azioni per risolvere problemi in modo più efficiente. Per creare un sistema multi-agente, puoi definire diversi tipi di agenti con funzioni e ruoli specializzati, come recupero dati, analisi, presa di decisioni e interazione con l’utente. Vediamo come si presenta una creazione di questo tipo:

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

    Nel codice precedente abbiamo un `GroupChatManager` registrato nel runtime. Questo manager è responsabile di coordinare le interazioni tra diversi tipi di agenti, come scrittori, illustratori, editor e utenti.

- **Agent Runtime**. Il framework fornisce un ambiente di runtime che abilita la comunicazione tra agenti, gestisce le loro identità e cicli di vita, e applica confini di sicurezza e privacy. Questo significa che puoi eseguire i tuoi agenti in un ambiente sicuro e controllato, assicurando che possano interagire in modo sicuro ed efficiente. Ci sono due runtime di interesse:
  - **Runtime stand-alone**. È una buona scelta per applicazioni a processo singolo dove tutti gli agenti sono implementati nello stesso linguaggio di programmazione e girano nello stesso processo. Ecco un’illustrazione di come funziona:

Stack dell’applicazione

    *gli agenti comunicano tramite messaggi attraverso il runtime, e il runtime gestisce il ciclo di vita degli agenti*

  - **Runtime distribuito**, adatto per applicazioni multi-processo dove gli agenti possono essere implementati in diversi linguaggi di programmazione e girare su macchine diverse. Ecco un’illustrazione di come funziona:

## Semantic Kernel + Agent Framework

Semantic Kernel è un SDK di orchestrazione AI pronto per l’uso enterprise. Comprende connettori AI e di memoria, insieme a un Agent Framework.

Iniziamo con alcuni componenti chiave:

- **AI Connectors**: Interfaccia con servizi AI esterni e fonti di dati, utilizzabile sia in Python che in C#.

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

    Qui hai un semplice esempio di come creare un kernel e aggiungere un servizio di completamento chat. Semantic Kernel crea una connessione a un servizio AI esterno, in questo caso Azure OpenAI Chat Completion.

- **Plugins**: Incapsulano funzioni che un’applicazione può utilizzare. Ci sono plugin già pronti e altri personalizzati che puoi creare. Un concetto correlato è quello delle "funzioni prompt". Invece di fornire indicazioni in linguaggio naturale per l’invocazione di funzioni, si trasmettono certe funzioni al modello. In base al contesto attuale della chat, il modello può scegliere di chiamare una di queste funzioni per completare una richiesta o una query. Ecco un esempio:

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

    Qui, prima hai un template di prompt `skPrompt` che lascia spazio all’utente per inserire testo, `$userInput`. Poi crei la funzione kernel `SummarizeText` e la importi nel kernel con il nome plugin `SemanticFunctions`. Nota il nome della funzione che aiuta Semantic Kernel a capire cosa fa la funzione e quando dovrebbe essere chiamata.

- **Funzione nativa**: Ci sono anche funzioni native che il framework può chiamare direttamente per eseguire il compito. Ecco un esempio di una funzione che recupera il contenuto da un file:

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

- **Memoria**: Astrazione e semplificazione della gestione del contesto per app AI. L’idea della memoria è che sia qualcosa che il LLM dovrebbe conoscere. Puoi memorizzare queste informazioni in un archivio vettoriale che diventa un database in memoria o un database vettoriale o simili. Ecco un esempio di uno scenario molto semplificato in cui *fatti* vengono aggiunti alla memoria:

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

    Questi fatti vengono poi memorizzati nella collezione di memoria `SummarizedAzureDocs`. Questo è un esempio molto semplificato, ma puoi vedere come puoi memorizzare informazioni nella memoria affinché il LLM le utilizzi.
## Lezione precedente

[Introduzione agli agenti AI e casi d'uso degli agenti](../01-intro-to-ai-agents/README.md)

## Lezione successiva

[Comprendere i pattern di design agentico](../03-agentic-design-patterns/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.