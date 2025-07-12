<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:51:50+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "de"
}
-->
. Laut Wikipedia ist ein Actor _der grundlegende Baustein der nebenläufigen Berechnung. Als Reaktion auf eine empfangene Nachricht kann ein Actor: lokale Entscheidungen treffen, weitere Actors erstellen, weitere Nachrichten senden und bestimmen, wie auf die nächste empfangene Nachricht reagiert wird_.

**Anwendungsfälle**: Automatisierung der Codegenerierung, Datenanalyseaufgaben und Erstellung benutzerdefinierter Agenten für Planungs- und Forschungsfunktionen.

Hier sind einige wichtige Kernkonzepte von AutoGen:

- **Agenten**. Ein Agent ist eine Softwareeinheit, die:
  - **über Nachrichten kommuniziert**, diese Nachrichten können synchron oder asynchron sein.
  - **ihren eigenen Zustand verwaltet**, der durch eingehende Nachrichten verändert werden kann.
  - **Aktionen ausführt** als Reaktion auf empfangene Nachrichten oder Änderungen ihres Zustands. Diese Aktionen können den Zustand des Agenten verändern und externe Effekte erzeugen, wie das Aktualisieren von Nachrichtenprotokollen, das Senden neuer Nachrichten, das Ausführen von Code oder das Aufrufen von APIs.
    
  Hier ein kurzer Codeausschnitt, in dem du deinen eigenen Agenten mit Chat-Fähigkeiten erstellst:

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
    
    Im vorherigen Code wurde `MyAssistant` erstellt und erbt von `RoutedAgent`. Es gibt einen Nachrichten-Handler, der den Inhalt der Nachricht ausgibt und dann eine Antwort über den `AssistantAgent`-Delegaten sendet. Besonders zu beachten ist, wie wir `self._delegate` eine Instanz von `AssistantAgent` zuweisen, einem vorgefertigten Agenten, der Chat-Komplettierungen verarbeiten kann.

    Lassen wir AutoGen nun diesen Agententyp kennen und starten das Programm:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Im vorherigen Code werden die Agenten bei der Laufzeit registriert und dann eine Nachricht an den Agenten gesendet, was zu folgender Ausgabe führt:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Mehrere Agenten**. AutoGen unterstützt die Erstellung mehrerer Agenten, die zusammenarbeiten können, um komplexe Aufgaben zu lösen. Agenten können kommunizieren, Informationen teilen und ihre Aktionen koordinieren, um Probleme effizienter zu lösen. Um ein Multi-Agenten-System zu erstellen, kannst du verschiedene Agententypen mit spezialisierten Funktionen und Rollen definieren, wie Datenabruf, Analyse, Entscheidungsfindung und Benutzerinteraktion. So sieht eine solche Erstellung aus, damit du ein Gefühl dafür bekommst:

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

    Im vorherigen Code haben wir einen `GroupChatManager`, der bei der Laufzeit registriert ist. Dieser Manager ist verantwortlich für die Koordination der Interaktionen zwischen verschiedenen Agententypen, wie Autoren, Illustratoren, Redakteuren und Nutzern.

- **Agent Runtime**. Das Framework stellt eine Laufzeitumgebung bereit, die die Kommunikation zwischen Agenten ermöglicht, deren Identitäten und Lebenszyklen verwaltet und Sicherheits- sowie Datenschutzgrenzen durchsetzt. Das bedeutet, dass du deine Agenten in einer sicheren und kontrollierten Umgebung ausführen kannst, die eine sichere und effiziente Interaktion gewährleistet. Es gibt zwei relevante Laufzeiten:
  - **Standalone-Laufzeit**. Diese ist eine gute Wahl für Single-Process-Anwendungen, bei denen alle Agenten in derselben Programmiersprache implementiert sind und im selben Prozess laufen. Hier eine Illustration, wie das funktioniert:

Anwendungsstack

    *Agenten kommunizieren über Nachrichten durch die Laufzeit, und die Laufzeit verwaltet den Lebenszyklus der Agenten*

  - **Verteilte Agenten-Laufzeit**, geeignet für Multi-Process-Anwendungen, bei denen Agenten in verschiedenen Programmiersprachen implementiert sind und auf unterschiedlichen Maschinen laufen. Hier eine Illustration, wie das funktioniert:

## Semantic Kernel + Agent Framework

Semantic Kernel ist ein unternehmensreifes AI-Orchestrierungs-SDK. Es besteht aus AI- und Memory-Connectors sowie einem Agent Framework.

Zuerst einige Kernkomponenten:

- **AI Connectors**: Dies ist eine Schnittstelle zu externen AI-Diensten und Datenquellen, nutzbar sowohl in Python als auch in C#.

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

    Hier ein einfaches Beispiel, wie du einen Kernel erstellen und einen Chat-Completion-Service hinzufügen kannst. Semantic Kernel stellt eine Verbindung zu einem externen AI-Dienst her, in diesem Fall Azure OpenAI Chat Completion.

- **Plugins**: Diese kapseln Funktionen, die eine Anwendung nutzen kann. Es gibt sowohl fertige Plugins als auch eigene, die du erstellen kannst. Ein verwandtes Konzept sind "Prompt-Funktionen". Anstatt natürliche Sprachhinweise für Funktionsaufrufe zu geben, sendest du bestimmte Funktionen an das Modell. Basierend auf dem aktuellen Chat-Kontext kann das Modell entscheiden, eine dieser Funktionen aufzurufen, um eine Anfrage oder Abfrage zu erfüllen. Hier ein Beispiel:

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

    Hier hast du zuerst eine Template-Eingabe `skPrompt`, die Platz für die Nutzereingabe `$userInput` lässt. Dann erstellst du die Kernel-Funktion `SummarizeText` und importierst sie mit dem Plugin-Namen `SemanticFunctions` in den Kernel. Beachte den Funktionsnamen, der Semantic Kernel hilft zu verstehen, was die Funktion macht und wann sie aufgerufen werden soll.

- **Native Funktion**: Es gibt auch native Funktionen, die das Framework direkt aufrufen kann, um Aufgaben auszuführen. Hier ein Beispiel für eine Funktion, die den Inhalt einer Datei abruft:

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

- **Memory**: Abstrahiert und vereinfacht das Kontextmanagement für AI-Anwendungen. Die Idee hinter Memory ist, dass dies etwas ist, das das LLM kennen sollte. Du kannst diese Informationen in einem Vektor-Store speichern, der letztlich eine In-Memory-Datenbank, eine Vektor-Datenbank oder Ähnliches ist. Hier ein Beispiel für ein sehr vereinfachtes Szenario, in dem *Fakten* zum Memory hinzugefügt werden:

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

    Diese Fakten werden dann in der Memory-Collection `SummarizedAzureDocs` gespeichert. Das ist ein sehr einfaches Beispiel, aber du siehst, wie du Informationen im Memory speichern kannst, damit das LLM sie nutzen kann.
## Vorherige Lektion

[Einführung in KI-Agenten und Anwendungsfälle für Agenten](../01-intro-to-ai-agents/README.md)

## Nächste Lektion

[Verstehen von agentischen Designmustern](../03-agentic-design-patterns/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.