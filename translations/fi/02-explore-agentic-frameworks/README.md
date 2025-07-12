<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:05:28+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fi"
}
-->
. Wikipedian mukaan aktori on _perusyksikkö rinnakkaislaskennassa. Vastauksena vastaanottamaansa viestiin aktori voi: tehdä paikallisia päätöksiä, luoda lisää aktoreita, lähettää lisää viestejä ja päättää, miten vastata seuraavaan vastaanotettuun viestiin_.

**Käyttötapaukset**: Koodin automaattinen generointi, data-analyysitehtävät ja räätälöityjen agenttien rakentaminen suunnittelu- ja tutkimustoimintoihin.

Tässä muutamia AutoGenin keskeisiä käsitteitä:

- **Agentit**. Agentti on ohjelmisto-olio, joka:
  - **Viestii viestien välityksellä**, nämä viestit voivat olla synkronisia tai asynkronisia.
  - **Ylläpitää omaa tilaa**, jota saapuvat viestit voivat muuttaa.
  - **Suorittaa toimintoja** vastaanotettuihin viesteihin tai tilan muutoksiin reagoiden. Nämä toiminnot voivat muuttaa agentin tilaa ja tuottaa ulkoisia vaikutuksia, kuten päivittää viestilokeja, lähettää uusia viestejä, suorittaa koodia tai tehdä API-kutsuja.
    
  Tässä on lyhyt koodiesimerkki, jossa luot oman agentin, jolla on chat-ominaisuudet:

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
    
    Edellisessä koodissa `MyAssistant` on luotu ja se perii `RoutedAgent`-luokan. Siinä on viestinkäsittelijä, joka tulostaa viestin sisällön ja lähettää sitten vastauksen käyttäen `AssistantAgent`-delegaattaa. Erityisesti huomaa, miten `self._delegate`-muuttujaan annetaan `AssistantAgent`-instanssi, joka on valmiiksi rakennettu agentti, joka osaa käsitellä chat-vastauksia.

    Kerrotaan AutoGenille tästä agenttityypistä ja käynnistetään ohjelma seuraavasti:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Edellisessä koodissa agentit rekisteröidään ajonaikaan ja sitten agentille lähetetään viesti, mikä tuottaa seuraavan tulosteen:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Moniagenttijärjestelmät**. AutoGen tukee useiden agenttien luomista, jotka voivat työskennellä yhdessä monimutkaisten tehtävien ratkaisemiseksi. Agentit voivat kommunikoida, jakaa tietoa ja koordinoida toimintaansa ongelmien tehokkaammaksi ratkaisemiseksi. Moniagenttijärjestelmän luomiseksi voit määritellä erilaisia agenttityyppejä, joilla on erikoistuneita toimintoja ja rooleja, kuten tiedonhaku, analyysi, päätöksenteko ja käyttäjävuorovaikutus. Katsotaan, miltä tällainen luominen näyttää:

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

    Edellisessä koodissa on `GroupChatManager`, joka on rekisteröity ajonaikaan. Tämä hallinnoija vastaa eri agenttityyppien, kuten kirjoittajien, kuvittajien, toimittajien ja käyttäjien vuorovaikutuksen koordinoinnista.

- **Agenttien ajonaika**. Kehys tarjoaa ajonaikaisen ympäristön, joka mahdollistaa agenttien välisen viestinnän, hallinnoi niiden identiteettejä ja elinkaarta sekä valvoo turvallisuus- ja yksityisyysrajoja. Tämä tarkoittaa, että voit ajaa agenttejasi turvallisessa ja hallitussa ympäristössä, varmistaen, että ne voivat toimia turvallisesti ja tehokkaasti. Kiinnostavia ajonaikoja on kaksi:
  - **Itsenäinen ajonaika**. Tämä on hyvä valinta yksiprosessisovelluksiin, joissa kaikki agentit on toteutettu samalla ohjelmointikielellä ja ne ajetaan samassa prosessissa. Tässä on havainnollistus siitä, miten se toimii:

Sovelluskerros

    *agentit kommunikoivat viestien välityksellä ajonaikaan, ja ajonaika hallinnoi agenttien elinkaarta*

  - **Jakautunut agenttiajonaika**, sopii moniprosessisovelluksiin, joissa agentit voivat olla toteutettu eri ohjelmointikielillä ja toimia eri koneilla. Tässä on havainnollistus siitä, miten se toimii:

## Semantic Kernel + Agent Framework

Semantic Kernel on yrityskäyttöön valmis tekoälyn orkestrointikehys. Se koostuu tekoäly- ja muistiliittimistä sekä agenttikehyksestä.

Käydään ensin läpi joitakin keskeisiä komponentteja:

- **AI-liittimet**: Tämä on rajapinta ulkoisiin tekoälypalveluihin ja tietolähteisiin, joita voi käyttää sekä Pythonissa että C#:ssa.

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

    Tässä on yksinkertainen esimerkki siitä, miten voit luoda kernelin ja lisätä chat-vastauspalvelun. Semantic Kernel luo yhteyden ulkoiseen tekoälypalveluun, tässä tapauksessa Azure OpenAI Chat Completion -palveluun.

- **Laajennukset (Plugins)**: Nämä kapseloivat sovelluksen käytettävissä olevia toimintoja. Saatavilla on valmiita laajennuksia sekä mahdollisuus luoda omia. Liittyvä käsite on "prompt-funktiot". Sen sijaan, että annettaisiin luonnollisen kielen vihjeitä funktioiden kutsumiseen, tietyt funktiot lähetetään mallille. Nykyisen chat-kontekstin perusteella malli voi valita kutsua jotakin näistä funktioista pyynnön tai kyselyn suorittamiseksi. Tässä esimerkki:

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

    Tässä sinulla on ensin mallipohja `skPrompt`, joka jättää tilaa käyttäjän syötteelle `$userInput`. Sitten luot kernel-funktion `SummarizeText` ja tuot sen kernelin käyttöön laajennuksella nimeltä `SemanticFunctions`. Huomaa funktion nimi, joka auttaa Semantic Kernelia ymmärtämään, mitä funktio tekee ja milloin sitä tulisi kutsua.

- **Natiivifunktio**: Kehyksessä on myös natiivifunktioita, joita voidaan kutsua suoraan tehtävän suorittamiseksi. Tässä esimerkki funktiosta, joka hakee tiedoston sisällön:

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

- **Muisti**: Abstrahoi ja yksinkertaistaa kontekstinhallintaa tekoälysovelluksissa. Ajatuksena on, että tämä on tietoa, jonka LLM:n tulisi tietää. Voit tallentaa tämän tiedon vektorivarastoon, joka toimii muistipohjaisena tietokantana tai vektoritietokantana tai vastaavana. Tässä esimerkki hyvin yksinkertaistetusta tilanteesta, jossa *faktoja* lisätään muistiin:

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

    Nämä faktat tallennetaan muistikokoelmaan `SummarizedAzureDocs`. Tämä on hyvin yksinkertaistettu esimerkki, mutta näet, miten voit tallentaa tietoa muistiin LLM:n käyttöä varten.
## Edellinen oppitunti

[Johdatus tekoälyagentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

## Seuraava oppitunti

[Agenttisuunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.