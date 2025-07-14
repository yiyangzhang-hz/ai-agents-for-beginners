<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:13:05+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hr"
}
-->
. Prema Wikipediji, glumac je _osnovna građevna jedinica konkurentnog računarstva. Kao odgovor na poruku koju primi, glumac može: donositi lokalne odluke, stvarati nove glumce, slati dodatne poruke i odlučiti kako će odgovoriti na sljedeću primljenu poruku_.

**Primjeri upotrebe**: Automatizacija generiranja koda, zadaci analize podataka i izrada prilagođenih agenata za planiranje i istraživačke funkcije.

Evo nekoliko važnih osnovnih pojmova AutoGen-a:

- **Agenti**. Agent je softverski entitet koji:
  - **Komunicira putem poruka**, te poruke mogu biti sinkrone ili asinkrone.
  - **Održava vlastito stanje**, koje se može mijenjati dolaznim porukama.
  - **Izvodi radnje** kao odgovor na primljene poruke ili promjene u svom stanju. Te radnje mogu mijenjati stanje agenta i proizvoditi vanjske efekte, poput ažuriranja zapisa poruka, slanja novih poruka, izvršavanja koda ili poziva API-ja.
    
  Ovdje imate kratak isječak koda u kojem kreirate vlastitog agenta s chat mogućnostima:

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
    
    U prethodnom kodu, `MyAssistant` je kreiran i nasljeđuje `RoutedAgent`. Ima handler za poruke koji ispisuje sadržaj poruke, a zatim šalje odgovor koristeći delegata `AssistantAgent`. Posebno obratite pažnju na to kako dodjeljujemo `self._delegate` instanci `AssistantAgent`, što je unaprijed izrađeni agent koji može rukovati chat dovršecima.

    Sada obavijestimo AutoGen o ovom tipu agenta i pokrenimo program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    U prethodnom kodu agenti su registrirani u runtime-u, a zatim je poslana poruka agentu što rezultira sljedećim ispisom:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Višestruki agenti**. AutoGen podržava kreiranje više agenata koji mogu surađivati kako bi ostvarili složene zadatke. Agenti mogu komunicirati, dijeliti informacije i koordinirati svoje radnje za učinkovitije rješavanje problema. Za kreiranje sustava s više agenata možete definirati različite tipove agenata sa specijaliziranim funkcijama i ulogama, poput dohvaćanja podataka, analize, donošenja odluka i interakcije s korisnikom. Pogledajmo kako takva kreacija izgleda da bismo stekli dojam:

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

    U prethodnom kodu imamo `GroupChatManager` koji je registriran u runtime-u. Ovaj menadžer je odgovoran za koordinaciju interakcija između različitih tipova agenata, poput pisaca, ilustratora, urednika i korisnika.

- **Agent Runtime**. Okvir pruža runtime okruženje koje omogućuje komunikaciju između agenata, upravlja njihovim identitetima i životnim ciklusima te provodi sigurnosne i privatnosne granice. To znači da možete pokretati svoje agente u sigurnom i kontroliranom okruženju, osiguravajući da mogu sigurno i učinkovito međusobno djelovati. Postoje dva runtime-a od interesa:
  - **Samostalni runtime**. Dobar je izbor za aplikacije s jednim procesom gdje su svi agenti implementirani u istom programskom jeziku i rade u istom procesu. Evo ilustracije kako to funkcionira:

Stog aplikacije

    *agenti komuniciraju putem poruka kroz runtime, a runtime upravlja životnim ciklusom agenata*

  - **Distribuirani agent runtime**, prikladan za aplikacije s više procesa gdje agenti mogu biti implementirani u različitim programskim jezicima i raditi na različitim računalima. Evo ilustracije kako to funkcionira:

## Semantic Kernel + Agent Framework

Semantic Kernel je SDK za orkestraciju AI-ja spreman za poduzeća. Sastoji se od AI i memorijskih konektora, zajedno s Agent Frameworkom.

Prvo ćemo pokriti neke osnovne komponente:

- **AI konektori**: Ovo je sučelje s vanjskim AI uslugama i izvorima podataka za korištenje u Pythonu i C#.

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

    Ovdje imate jednostavan primjer kako možete kreirati kernel i dodati uslugu chat dovršetka. Semantic Kernel uspostavlja vezu s vanjskom AI uslugom, u ovom slučaju Azure OpenAI Chat Completion.

- **Dodaci (Plugins)**: Oni enkapsuliraju funkcije koje aplikacija može koristiti. Postoje gotovi dodaci i prilagođeni koje možete sami kreirati. Povezan koncept su "prompt funkcije". Umjesto da se za pozivanje funkcija koriste prirodni jezični upiti, određene funkcije se emitiraju modelu. Na temelju trenutnog konteksta chata, model može odlučiti pozvati neku od tih funkcija za dovršetak zahtjeva ili upita. Evo primjera:

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

    Ovdje prvo imate predložak prompta `skPrompt` koji ostavlja prostor korisniku za unos teksta, `$userInput`. Zatim kreirate kernel funkciju `SummarizeText` i uvozite je u kernel s imenom dodatka `SemanticFunctions`. Obratite pažnju na ime funkcije koje pomaže Semantic Kernelu razumjeti što funkcija radi i kada bi trebala biti pozvana.

- **Nativna funkcija**: Postoje i nativne funkcije koje okvir može izravno pozvati za izvršenje zadatka. Evo primjera takve funkcije koja dohvaća sadržaj iz datoteke:

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

- **Memorija**: Apstrahira i pojednostavljuje upravljanje kontekstom za AI aplikacije. Ideja s memorijom je da je to nešto što LLM treba znati. Možete pohraniti te informacije u vektorsku bazu podataka koja može biti baza podataka u memoriji ili vektorska baza podataka ili slično. Evo primjera vrlo pojednostavljenog scenarija gdje se *činjenice* dodaju u memoriju:

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

    Te se činjenice zatim pohranjuju u memorijsku kolekciju `SummarizedAzureDocs`. Ovo je vrlo pojednostavljen primjer, ali možete vidjeti kako možete pohraniti informacije u memoriju za korištenje od strane LLM-a.
## Prethodna lekcija

[Uvod u AI agente i primjere upotrebe agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje agentnih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.