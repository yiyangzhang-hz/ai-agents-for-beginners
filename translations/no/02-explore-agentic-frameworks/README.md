<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:05:03+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "no"
}
-->
. Ifølge Wikipedia er en aktør _den grunnleggende byggesteinen i samtidig beregning. Som svar på en melding den mottar, kan en aktør: ta lokale beslutninger, opprette flere aktører, sende flere meldinger, og bestemme hvordan den skal svare på neste mottatte melding_.

**Bruksområder**: Automatisering av kodegenerering, dataanalyseoppgaver, og bygging av tilpassede agenter for planlegging og forskningsfunksjoner.

Her er noen viktige kjernebegreper i AutoGen:

- **Agenter**. En agent er en programvareenhet som:
  - **Kommuniserer via meldinger**, disse meldingene kan være synkrone eller asynkrone.
  - **Opprettholder sin egen tilstand**, som kan endres av innkommende meldinger.
  - **Utfører handlinger** som svar på mottatte meldinger eller endringer i sin tilstand. Disse handlingene kan endre agentens tilstand og gi eksterne effekter, som å oppdatere meldingslogger, sende nye meldinger, kjøre kode eller gjøre API-kall.
    
  Her har du et kort kodeeksempel der du oppretter din egen agent med chat-funksjonalitet:

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
    
    I koden over er `MyAssistant` opprettet og arver fra `RoutedAgent`. Den har en meldingsbehandler som skriver ut innholdet i meldingen og deretter sender et svar ved hjelp av `AssistantAgent`-delegaten. Legg spesielt merke til hvordan vi tildeler `self._delegate` en instans av `AssistantAgent`, som er en ferdigbygd agent som kan håndtere chat-kompletteringer.

    La oss informere AutoGen om denne agenttypen og starte programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I koden over registreres agentene i runtime, og deretter sendes en melding til agenten som resulterer i følgende utskrift:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Flere agenter**. AutoGen støtter opprettelse av flere agenter som kan samarbeide for å løse komplekse oppgaver. Agentene kan kommunisere, dele informasjon og koordinere handlingene sine for å løse problemer mer effektivt. For å lage et multi-agent system kan du definere ulike typer agenter med spesialiserte funksjoner og roller, som datainnhenting, analyse, beslutningstaking og brukerinteraksjon. La oss se hvordan en slik opprettelse kan se ut:

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

    I koden over har vi en `GroupChatManager` som er registrert i runtime. Denne manageren er ansvarlig for å koordinere interaksjonene mellom ulike typer agenter, som forfattere, illustratører, redaktører og brukere.

- **Agent Runtime**. Rammeverket tilbyr et runtime-miljø som muliggjør kommunikasjon mellom agenter, håndterer deres identiteter og livssykluser, og håndhever sikkerhets- og personvernregler. Dette betyr at du kan kjøre agentene dine i et sikkert og kontrollert miljø, slik at de kan samhandle trygt og effektivt. Det finnes to runtime-miljøer av interesse:
  - **Frittstående runtime**. Dette er et godt valg for enkeltprosess-applikasjoner hvor alle agenter er implementert i samme programmeringsspråk og kjører i samme prosess. Her er en illustrasjon av hvordan det fungerer:

Applikasjonsstabel

    *agenter kommuniserer via meldinger gjennom runtime, og runtime håndterer agentenes livssyklus*

  - **Distribuert agent runtime**, egnet for flerprosess-applikasjoner hvor agenter kan være implementert i forskjellige programmeringsspråk og kjøre på ulike maskiner. Her er en illustrasjon av hvordan det fungerer:

## Semantic Kernel + Agent Framework

Semantic Kernel er et AI Orchestration SDK klart for bedriftsbruk. Det består av AI- og minnekoblinger, sammen med et Agent Framework.

La oss først gå gjennom noen kjernekomponenter:

- **AI Connectors**: Dette er et grensesnitt mot eksterne AI-tjenester og datakilder for bruk i både Python og C#.

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

    Her har du et enkelt eksempel på hvordan du kan opprette en kernel og legge til en chat-kompletteringstjeneste. Semantic Kernel oppretter en forbindelse til en ekstern AI-tjeneste, i dette tilfellet Azure OpenAI Chat Completion.

- **Plugins**: Disse innkapsler funksjoner som en applikasjon kan bruke. Det finnes både ferdige plugins og tilpassede du kan lage selv. Et relatert konsept er "prompt functions". I stedet for å gi naturlige språkledetråder for funksjonskall, sender du ut visse funksjoner til modellen. Basert på den nåværende chat-konteksten kan modellen velge å kalle en av disse funksjonene for å fullføre en forespørsel eller et spørsmål. Her er et eksempel:

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

    Her har du først en malprompt `skPrompt` som gir plass til at brukeren kan skrive inn tekst, `$userInput`. Deretter oppretter du kernelfunksjonen `SummarizeText` og importerer den til kernel med plugin-navnet `SemanticFunctions`. Legg merke til funksjonsnavnet som hjelper Semantic Kernel å forstå hva funksjonen gjør og når den skal kalles.

- **Native function**: Det finnes også native funksjoner som rammeverket kan kalle direkte for å utføre oppgaven. Her er et eksempel på en slik funksjon som henter innhold fra en fil:

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

- **Memory**: Abstraherer og forenkler kontekststyring for AI-applikasjoner. Ideen med minne er at dette er noe LLM-en bør kjenne til. Du kan lagre denne informasjonen i en vektorlagring som fungerer som en in-memory database, en vektordatabase eller lignende. Her er et eksempel på et veldig forenklet scenario hvor *fakta* legges til i minnet:

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

    Disse faktaene lagres deretter i minnesamlingen `SummarizedAzureDocs`. Dette er et veldig forenklet eksempel, men du kan se hvordan du kan lagre informasjon i minnet for at LLM-en skal kunne bruke det.
## Forrige leksjon

[Introduksjon til AI-agenter og bruksområder for agenter](../01-intro-to-ai-agents/README.md)

## Neste leksjon

[Forståelse av agentiske designmønstre](../03-agentic-design-patterns/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.