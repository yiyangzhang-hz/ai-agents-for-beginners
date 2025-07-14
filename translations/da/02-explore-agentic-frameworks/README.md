<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:04:33+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "da"
}
-->
. Ifølge Wikipedia er en aktør _den grundlæggende byggesten i samtidig beregning. Som svar på en besked, den modtager, kan en aktør: træffe lokale beslutninger, oprette flere aktører, sende flere beskeder og bestemme, hvordan den skal reagere på den næste modtagne besked_.

**Brugstilfælde**: Automatisering af kodegenerering, dataanalyseopgaver og opbygning af brugerdefinerede agenter til planlægnings- og forskningsfunktioner.

Her er nogle vigtige kernebegreber i AutoGen:

- **Agenter**. En agent er en softwareenhed, der:
  - **Kommunikerer via beskeder**, disse beskeder kan være synkrone eller asynkrone.
  - **Opretholder sin egen tilstand**, som kan ændres af indkommende beskeder.
  - **Udfører handlinger** som svar på modtagne beskeder eller ændringer i sin tilstand. Disse handlinger kan ændre agentens tilstand og skabe eksterne effekter, såsom opdatering af beskedlogfiler, afsendelse af nye beskeder, udførelse af kode eller kald til API'er.
    
  Her har du et kort kodeeksempel, hvor du opretter din egen agent med chatfunktioner:

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
    
    I den tidligere kode er `MyAssistant` oprettet og arver fra `RoutedAgent`. Den har en beskedbehandler, der udskriver indholdet af beskeden og derefter sender et svar ved hjælp af `AssistantAgent`-delegeringen. Bemærk især, hvordan vi tildeler `self._delegate` en instans af `AssistantAgent`, som er en forudbygget agent, der kan håndtere chatkompletteringer.

    Lad os fortælle AutoGen om denne agenttype og starte programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I den tidligere kode registreres agenterne i runtime, og derefter sendes en besked til agenten, hvilket resulterer i følgende output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Flere agenter**. AutoGen understøtter oprettelsen af flere agenter, der kan arbejde sammen om at løse komplekse opgaver. Agenter kan kommunikere, dele information og koordinere deres handlinger for at løse problemer mere effektivt. For at oprette et multi-agent system kan du definere forskellige typer agenter med specialiserede funktioner og roller, såsom dataindsamling, analyse, beslutningstagning og brugerinteraktion. Lad os se, hvordan en sådan oprettelse ser ud, så vi får en fornemmelse af det:

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

    I den tidligere kode har vi en `GroupChatManager`, der er registreret i runtime. Denne manager er ansvarlig for at koordinere interaktionerne mellem forskellige typer agenter, såsom forfattere, illustratorer, redaktører og brugere.

- **Agent Runtime**. Frameworket leverer et runtime-miljø, der muliggør kommunikation mellem agenter, håndterer deres identiteter og livscyklusser samt håndhæver sikkerheds- og privatlivsgrænser. Det betyder, at du kan køre dine agenter i et sikkert og kontrolleret miljø, hvilket sikrer, at de kan interagere sikkert og effektivt. Der er to runtime-miljøer af interesse:
  - **Stand-alone runtime**. Dette er et godt valg til enkeltproces-applikationer, hvor alle agenter er implementeret i samme programmeringssprog og kører i samme proces. Her er en illustration af, hvordan det fungerer:

Applikationsstak

    *agenter kommunikerer via beskeder gennem runtime, og runtime håndterer agenternes livscyklus*

  - **Distribueret agent runtime**, som er egnet til multi-proces-applikationer, hvor agenter kan være implementeret i forskellige programmeringssprog og køre på forskellige maskiner. Her er en illustration af, hvordan det fungerer:

## Semantic Kernel + Agent Framework

Semantic Kernel er et enterprise-klar AI Orchestration SDK. Det består af AI- og hukommelsesforbindelser samt et Agent Framework.

Lad os først gennemgå nogle kernekomponenter:

- **AI Connectors**: Dette er en grænseflade til eksterne AI-tjenester og datakilder til brug i både Python og C#.

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

    Her har du et simpelt eksempel på, hvordan du kan oprette en kernel og tilføje en chatkompletteringstjeneste. Semantic Kernel opretter en forbindelse til en ekstern AI-tjeneste, i dette tilfælde Azure OpenAI Chat Completion.

- **Plugins**: Disse indkapsler funktioner, som en applikation kan bruge. Der findes både færdiglavede plugins og brugerdefinerede, som du kan oprette. Et beslægtet koncept er "prompt functions". I stedet for at give naturlige sprogkommandoer til funktionskald, udsender du visse funktioner til modellen. Baseret på den aktuelle chatkontekst kan modellen vælge at kalde en af disse funktioner for at fuldføre en anmodning eller forespørgsel. Her er et eksempel:

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

    Her har du først en skabelonprompt `skPrompt`, der giver plads til, at brugeren kan indtaste tekst, `$userInput`. Derefter opretter du kernelfunktionen `SummarizeText` og importerer den til kernen med plugin-navnet `SemanticFunctions`. Bemærk funktionsnavnet, som hjælper Semantic Kernel med at forstå, hvad funktionen gør, og hvornår den skal kaldes.

- **Native function**: Der findes også native funktioner, som frameworket kan kalde direkte for at udføre opgaven. Her er et eksempel på en sådan funktion, der henter indholdet fra en fil:

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

- **Memory**: Abstraherer og forenkler kontekststyring for AI-apps. Ideen med hukommelse er, at dette er noget, LLM’en skal kende til. Du kan gemme denne information i en vektorbutik, som ender med at være en in-memory database, en vektordatabase eller lignende. Her er et eksempel på et meget forenklet scenarie, hvor *fakta* tilføjes til hukommelsen:

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

    Disse fakta gemmes derefter i hukommelsessamlingen `SummarizedAzureDocs`. Dette er et meget forenklet eksempel, men du kan se, hvordan du kan gemme information i hukommelsen, som LLM’en kan bruge.
## Forrige lektion

[Introduktion til AI-agenter og agentbrugssager](../01-intro-to-ai-agents/README.md)

## Næste lektion

[Forståelse af agentiske designmønstre](../03-agentic-design-patterns/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.