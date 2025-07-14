<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:13:34+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sl"
}
-->
. Po Wikipediji je igralec _osnovna gradbena enota sočasnega računalništva. Kot odgovor na prejeto sporočilo lahko igralec: sprejema lokalne odločitve, ustvarja več igralcev, pošilja več sporočil in določi, kako bo odgovoril na naslednje prejeto sporočilo_.

**Primeri uporabe**: avtomatizacija generiranja kode, naloge analize podatkov in izdelava prilagojenih agentov za načrtovanje in raziskovalne funkcije.

Tukaj je nekaj pomembnih osnovnih pojmov AutoGen:

- **Agenti**. Agent je programska entiteta, ki:
  - **Komunicira preko sporočil**, ta sporočila so lahko sinhrona ali asinhrona.
  - **Vzdržuje svoj lasten status**, ki ga lahko spreminjajo dohodna sporočila.
  - **Izvaja dejanja** kot odgovor na prejeta sporočila ali spremembe svojega stanja. Ta dejanja lahko spremenijo stanje agenta in povzročijo zunanje učinke, kot so posodabljanje dnevnikov sporočil, pošiljanje novih sporočil, izvajanje kode ali klici API-jev.
    
  Tukaj imate kratek primer kode, v katerem ustvarite svojega agenta s klepetalnimi zmožnostmi:

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
    
    V prejšnji kodi je bil ustvarjen `MyAssistant`, ki podeduje od `RoutedAgent`. Ima upravljalnik sporočil, ki izpiše vsebino sporočila in nato pošlje odgovor z uporabo delegata `AssistantAgent`. Posebej opazite, kako dodelimo `self._delegate` instanco `AssistantAgent`, ki je vnaprej izdelan agent, sposoben obravnavati klepetalne dokončanja.

    Nato obvestimo AutoGen o tej vrsti agenta in zaženemo program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    V prejšnji kodi so agenti registrirani v runtime okolju, nato pa je agentu poslano sporočilo, kar povzroči naslednji izpis:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Več agentov**. AutoGen podpira ustvarjanje več agentov, ki lahko sodelujejo pri doseganju kompleksnih nalog. Agenti lahko komunicirajo, delijo informacije in usklajujejo svoja dejanja za učinkovitejšo rešitev problemov. Za ustvarjanje sistema z več agenti lahko definirate različne vrste agentov s specializiranimi funkcijami in vlogami, kot so pridobivanje podatkov, analiza, odločanje in interakcija z uporabnikom. Poglejmo, kako takšna kreacija izgleda:

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

    V prejšnji kodi imamo `GroupChatManager`, ki je registriran v runtime okolju. Ta upravljalec je odgovoren za usklajevanje interakcij med različnimi vrstami agentov, kot so pisci, ilustratorji, uredniki in uporabniki.

- **Agent Runtime**. Okvir zagotavlja runtime okolje, ki omogoča komunikacijo med agenti, upravlja njihove identitete in življenjske cikle ter uveljavlja varnostne in zasebnostne meje. To pomeni, da lahko svoje agente poganjate v varnem in nadzorovanem okolju, kar zagotavlja varno in učinkovito interakcijo. Obstajata dve zanimivi runtime okolji:
  - **Samostojni runtime**. To je dobra izbira za enoprocesne aplikacije, kjer so vsi agenti implementirani v istem programskem jeziku in tečejo v istem procesu. Tukaj je ilustracija, kako to deluje:

Sklad aplikacije

    *agenti komunicirajo preko sporočil skozi runtime, runtime pa upravlja življenjski cikel agentov*

  - **Distribuirani agent runtime**, primeren za večprocesne aplikacije, kjer so agenti lahko implementirani v različnih programskih jezikih in tečejo na različnih računalnikih. Tukaj je ilustracija, kako to deluje:

## Semantic Kernel + Agent Framework

Semantic Kernel je SDK za orkestracijo AI, pripravljen za podjetja. Sestavljen je iz AI in pomnilniških konektorjev ter Agent Frameworka.

Najprej pokrijmo nekaj osnovnih komponent:

- **AI konektorji**: To je vmesnik z zunanjimi AI storitvami in podatkovnimi viri za uporabo tako v Pythonu kot v C#.

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

    Tukaj imate preprost primer, kako ustvariti kernel in dodati storitev za klepetalno dokončanje. Semantic Kernel vzpostavi povezavo z zunanjo AI storitvijo, v tem primeru Azure OpenAI Chat Completion.

- **Vtičniki**: Ti zajemajo funkcije, ki jih lahko aplikacija uporablja. Obstajajo tako že pripravljeni vtičniki kot tudi tisti, ki jih lahko ustvarite sami. Soroden pojem so "prompt funkcije". Namesto da bi za klic funkcije uporabljali naravni jezik, modelu posredujete določene funkcije. Glede na trenutni kontekst klepeta se model lahko odloči, da pokliče eno od teh funkcij za dokončanje zahteve ali poizvedbe. Tukaj je primer:

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

    Tukaj imate najprej predlogo poziva `skPrompt`, ki pusti prostor za uporabnikov vnos, `$userInput`. Nato ustvarite funkcijo jedra `SummarizeText` in jo uvozite v kernel z imenom vtičnika `SemanticFunctions`. Opazite ime funkcije, ki pomaga Semantic Kernelu razumeti, kaj funkcija počne in kdaj naj se pokliče.

- **Nativna funkcija**: Obstajajo tudi nativne funkcije, ki jih okvir lahko pokliče neposredno za izvedbo naloge. Tukaj je primer funkcije, ki pridobi vsebino iz datoteke:

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

- **Pomnilnik**: Poenostavlja in abstraktira upravljanje konteksta za AI aplikacije. Ideja pomnilnika je, da gre za informacije, ki jih mora LLM poznati. Te informacije lahko shranite v vektorski shrambi, ki je v bistvu baza podatkov v pomnilniku ali vektorska baza podatkov ali podobno. Tukaj je primer zelo poenostavljenega scenarija, kjer se *dejstva* dodajo v pomnilnik:

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

    Ta dejstva se nato shranijo v pomnilniško zbirko `SummarizedAzureDocs`. To je zelo poenostavljen primer, a vidite, kako lahko shranjujete informacije v pomnilnik, da jih LLM lahko uporablja.
## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje agentnih oblikovalskih vzorcev](../03-agentic-design-patterns/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.