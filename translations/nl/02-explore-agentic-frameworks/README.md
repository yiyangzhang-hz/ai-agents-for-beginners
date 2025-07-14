<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:05:58+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "nl"
}
-->
. Volgens Wikipedia is een actor _de basisbouwsteen van gelijktijdige berekeningen. Als reactie op een bericht dat het ontvangt, kan een actor: lokale beslissingen nemen, meer actors creëren, meer berichten verzenden en bepalen hoe te reageren op het volgende ontvangen bericht_.

**Gebruiksscenario's**: Automatiseren van codegeneratie, data-analysetaken en het bouwen van aangepaste agents voor plannings- en onderzoeksfuncties.

Hier zijn enkele belangrijke kernconcepten van AutoGen:

- **Agents**. Een agent is een software-entiteit die:
  - **Communiceert via berichten**, deze berichten kunnen synchroon of asynchroon zijn.
  - **Houdt zijn eigen status bij**, die kan worden aangepast door binnenkomende berichten.
  - **Voert acties uit** als reactie op ontvangen berichten of veranderingen in zijn status. Deze acties kunnen de status van de agent wijzigen en externe effecten veroorzaken, zoals het bijwerken van berichtlogs, het verzenden van nieuwe berichten, het uitvoeren van code of het maken van API-aanroepen.
    
  Hier is een korte codevoorbeeld waarin je je eigen agent met chatmogelijkheden maakt:

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
    
    In de vorige code is `MyAssistant` aangemaakt en erft het van `RoutedAgent`. Het heeft een berichtverwerker die de inhoud van het bericht afdrukt en vervolgens een reactie verzendt met behulp van de `AssistantAgent` delegate. Let vooral op hoe we aan `self._delegate` een instantie van `AssistantAgent` toewijzen, wat een vooraf gebouwde agent is die chatcompletions kan afhandelen.

    Laten we AutoGen informeren over dit agenttype en het programma starten:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    In de vorige code worden de agents geregistreerd bij de runtime en wordt er een bericht naar de agent gestuurd, wat resulteert in de volgende uitvoer:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Meerdere agents**. AutoGen ondersteunt het creëren van meerdere agents die samen kunnen werken om complexe taken uit te voeren. Agents kunnen communiceren, informatie delen en hun acties coördineren om problemen efficiënter op te lossen. Om een multi-agent systeem te maken, kun je verschillende typen agents definiëren met gespecialiseerde functies en rollen, zoals data-ophaling, analyse, besluitvorming en gebruikersinteractie. Laten we eens kijken hoe zo'n creatie eruitziet zodat we er een idee van krijgen:

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

    In de vorige code hebben we een `GroupChatManager` die is geregistreerd bij de runtime. Deze manager is verantwoordelijk voor het coördineren van de interacties tussen verschillende typen agents, zoals schrijvers, illustratoren, redacteuren en gebruikers.

- **Agent Runtime**. Het framework biedt een runtime-omgeving die communicatie tussen agents mogelijk maakt, hun identiteiten en levenscycli beheert, en beveiligings- en privacygrenzen afdwingt. Dit betekent dat je je agents in een veilige en gecontroleerde omgeving kunt draaien, zodat ze veilig en efficiënt kunnen samenwerken. Er zijn twee runtimes van belang:
  - **Standalone runtime**. Dit is een goede keuze voor single-process applicaties waarbij alle agents in dezelfde programmeertaal zijn geïmplementeerd en in hetzelfde proces draaien. Hier is een illustratie van hoe het werkt:

Applicatiestack

    *agents communiceren via berichten via de runtime, en de runtime beheert de levenscyclus van agents*

  - **Distributed agent runtime**, is geschikt voor multi-process applicaties waarbij agents mogelijk in verschillende programmeertalen zijn geïmplementeerd en op verschillende machines draaien. Hier is een illustratie van hoe het werkt:

## Semantic Kernel + Agent Framework

Semantic Kernel is een enterprise-klare AI Orchestration SDK. Het bestaat uit AI- en geheugenconnectors, samen met een Agent Framework.

Laten we eerst enkele kerncomponenten behandelen:

- **AI Connectors**: Dit is een interface met externe AI-diensten en databronnen voor gebruik in zowel Python als C#.

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

    Hier zie je een eenvoudig voorbeeld van hoe je een kernel kunt maken en een chat completion service kunt toevoegen. Semantic Kernel maakt een verbinding met een externe AI-service, in dit geval Azure OpenAI Chat Completion.

- **Plugins**: Deze kapselen functies in die een applicatie kan gebruiken. Er zijn zowel kant-en-klare plugins als aangepaste die je zelf kunt maken. Een gerelateerd concept is "prompt functions". In plaats van natuurlijke taal aanwijzingen te geven voor functieaanroepen, zend je bepaalde functies uit naar het model. Op basis van de huidige chatcontext kan het model ervoor kiezen om een van deze functies aan te roepen om een verzoek of query te voltooien. Hier is een voorbeeld:

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

    Hier heb je eerst een template prompt `skPrompt` die ruimte laat voor de gebruiker om tekst in te voeren, `$userInput`. Daarna maak je de kernelfunctie `SummarizeText` en importeer je deze in de kernel met de pluginnaam `SemanticFunctions`. Let op de naam van de functie die Semantic Kernel helpt te begrijpen wat de functie doet en wanneer deze moet worden aangeroepen.

- **Native function**: Er zijn ook native functies die het framework direct kan aanroepen om de taak uit te voeren. Hier is een voorbeeld van zo'n functie die de inhoud van een bestand ophaalt:

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

- **Memory**: Abstract en vereenvoudigt contextbeheer voor AI-apps. Het idee achter memory is dat dit iets is waar de LLM van op de hoogte moet zijn. Je kunt deze informatie opslaan in een vector store, wat uiteindelijk een in-memory database, een vector database of iets dergelijks is. Hier is een voorbeeld van een zeer vereenvoudigd scenario waarin *feiten* aan het geheugen worden toegevoegd:

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

    Deze feiten worden vervolgens opgeslagen in de geheugenverzameling `SummarizedAzureDocs`. Dit is een heel eenvoudig voorbeeld, maar je ziet hoe je informatie kunt opslaan in het geheugen zodat de LLM deze kan gebruiken.
## Vorige les

[Introductie tot AI-agenten en gebruiksscenario's](../01-intro-to-ai-agents/README.md)

## Volgende les

[Begrip van agent-ontwerppatronen](../03-agentic-design-patterns/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.