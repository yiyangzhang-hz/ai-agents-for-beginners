<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:03:57+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sv"
}
-->
. Enligt Wikipedia är en aktör _den grundläggande byggstenen för samtidig beräkning. Som svar på ett meddelande den mottar kan en aktör: fatta lokala beslut, skapa fler aktörer, skicka fler meddelanden och bestämma hur den ska svara på nästa mottagna meddelande_.

**Användningsområden**: Automatisering av kodgenerering, dataanalysuppgifter och skapande av anpassade agenter för planering och forskningsfunktioner.

Här är några viktiga kärnbegrepp i AutoGen:

- **Agenter**. En agent är en mjukvaruenhet som:
  - **Kommunicerar via meddelanden**, dessa meddelanden kan vara synkrona eller asynkrona.
  - **Behåller sitt eget tillstånd**, vilket kan ändras av inkommande meddelanden.
  - **Utför åtgärder** som svar på mottagna meddelanden eller förändringar i sitt tillstånd. Dessa åtgärder kan ändra agentens tillstånd och ge externa effekter, såsom att uppdatera meddelandeloggar, skicka nya meddelanden, köra kod eller göra API-anrop.
    
  Här har du ett kort kodexempel där du skapar din egen agent med chattfunktioner:

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
    
    I föregående kod har `MyAssistant` skapats och ärver från `RoutedAgent`. Den har en meddelandehanterare som skriver ut innehållet i meddelandet och sedan skickar ett svar med hjälp av delegaten `AssistantAgent`. Notera särskilt hur vi tilldelar `self._delegate` en instans av `AssistantAgent` som är en förbyggd agent som kan hantera chattkompletteringar.

    Låt oss informera AutoGen om denna agenttyp och starta programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I föregående kod registreras agenterna i runtime och sedan skickas ett meddelande till agenten vilket resulterar i följande utskrift:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Flera agenter**. AutoGen stödjer skapandet av flera agenter som kan samarbeta för att utföra komplexa uppgifter. Agenter kan kommunicera, dela information och samordna sina handlingar för att lösa problem mer effektivt. För att skapa ett multi-agent-system kan du definiera olika typer av agenter med specialiserade funktioner och roller, såsom datainsamling, analys, beslutsfattande och användarinteraktion. Låt oss se hur en sådan skapelse kan se ut för att få en känsla för det:

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

    I föregående kod har vi en `GroupChatManager` som är registrerad i runtime. Denna manager ansvarar för att samordna interaktionerna mellan olika typer av agenter, såsom skribenter, illustratörer, redaktörer och användare.

- **Agent Runtime**. Ramverket tillhandahåller en runtime-miljö som möjliggör kommunikation mellan agenter, hanterar deras identiteter och livscykler samt upprätthåller säkerhets- och sekretessgränser. Det innebär att du kan köra dina agenter i en säker och kontrollerad miljö, vilket säkerställer att de kan interagera på ett säkert och effektivt sätt. Det finns två intressanta runtime-miljöer:
  - **Fristående runtime**. Detta är ett bra val för applikationer med en enda process där alla agenter är implementerade i samma programmeringsspråk och körs i samma process. Här är en illustration av hur det fungerar:

Applikationsstack

    *agenter kommunicerar via meddelanden genom runtime, och runtime hanterar agenternas livscykel*

  - **Distribuerad agent-runtime**, är lämplig för applikationer med flera processer där agenter kan vara implementerade i olika programmeringsspråk och köras på olika maskiner. Här är en illustration av hur det fungerar:

## Semantic Kernel + Agent Framework

Semantic Kernel är ett företagsklart AI-orchestration SDK. Det består av AI- och minneskopplingar tillsammans med ett agentramverk.

Låt oss först gå igenom några kärnkomponenter:

- **AI Connectors**: Detta är ett gränssnitt mot externa AI-tjänster och datakällor för användning i både Python och C#.

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

    Här har du ett enkelt exempel på hur du kan skapa en kernel och lägga till en chattkompletteringstjänst. Semantic Kernel skapar en koppling till en extern AI-tjänst, i detta fall Azure OpenAI Chat Completion.

- **Plugins**: Dessa kapslar in funktioner som en applikation kan använda. Det finns både färdiga plugins och anpassade som du kan skapa själv. Ett relaterat begrepp är "prompt functions". Istället för att ge naturliga språkledtrådar för funktionsanrop, sänder du ut vissa funktioner till modellen. Baserat på den aktuella chattkontexten kan modellen välja att anropa en av dessa funktioner för att slutföra en förfrågan eller fråga. Här är ett exempel:

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

    Här har du först en mallprompt `skPrompt` som lämnar plats för användarens textinmatning, `$userInput`. Sedan skapar du kernelfunktionen `SummarizeText` och importerar den till kerneln med plugin-namnet `SemanticFunctions`. Notera funktionsnamnet som hjälper Semantic Kernel att förstå vad funktionen gör och när den ska anropas.

- **Native function**: Det finns också inbyggda funktioner som ramverket kan anropa direkt för att utföra uppgiften. Här är ett exempel på en sådan funktion som hämtar innehållet från en fil:

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

- **Memory**: Abstraherar och förenklar kontexthantering för AI-appar. Idén med minnet är att detta är något som LLM ska känna till. Du kan lagra denna information i en vektordatabas som i praktiken blir en minnesdatabas eller liknande. Här är ett exempel på ett mycket förenklat scenario där *fakta* läggs till i minnet:

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

    Dessa fakta lagras sedan i minneskollektionen `SummarizedAzureDocs`. Detta är ett mycket förenklat exempel, men du kan se hur du kan lagra information i minnet för att LLM ska kunna använda den.
## Föregående lektion

[Introduktion till AI-agenter och användningsfall för agenter](../01-intro-to-ai-agents/README.md)

## Nästa lektion

[Förstå agentiska designmönster](../03-agentic-design-patterns/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.