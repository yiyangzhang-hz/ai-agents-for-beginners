<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-29T23:19:19+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sl"
}
-->
[![Raziskovanje okvirov za AI agente](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.sl.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite zgornjo sliko za ogled videoposnetka te lekcije)_

# Raziskovanje okvirov za AI agente

Okviri za AI agente so programske platforme, zasnovane za poenostavitev ustvarjanja, uvajanja in upravljanja AI agentov. Ti okviri razvijalcem ponujajo vnaprej pripravljene komponente, abstrakcije in orodja, ki olajšajo razvoj kompleksnih AI sistemov.

Ti okviri razvijalcem omogočajo, da se osredotočijo na edinstvene vidike svojih aplikacij, saj zagotavljajo standardizirane pristope k skupnim izzivom pri razvoju AI agentov. Izboljšujejo skalabilnost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod

Ta lekcija bo obravnavala:

- Kaj so okviri za AI agente in kaj omogočajo razvijalcem?
- Kako lahko ekipe z njihovo pomočjo hitro prototipirajo, iterirajo in izboljšajo zmogljivosti svojih agentov?
- Kakšne so razlike med okviri in orodji, ki jih je ustvaril Microsoft, 
- in ali lahko neposredno integriram obstoječa orodja iz ekosistema Azure ali potrebujem samostojne rešitve?
- Kaj je storitev Azure AI Agents in kako mi lahko pomaga?

## Cilji učenja

Cilji te lekcije so, da razumete:

- Vlogo okvirov za AI agente pri razvoju AI.
- Kako izkoristiti okvire za AI agente za gradnjo inteligentnih agentov.
- Ključne zmogljivosti, ki jih omogočajo okviri za AI agente.
- Razlike med AutoGen, Semantic Kernel in Azure AI Agent Service.

## Kaj so okviri za AI agente in kaj omogočajo razvijalcem?

Tradicionalni AI okviri vam lahko pomagajo integrirati AI v vaše aplikacije in jih izboljšajo na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov ter ponudi personalizirana priporočila, vsebine in izkušnje.  
Primer: Pretakalne storitve, kot je Netflix, uporabljajo AI za predlaganje filmov in oddaj na podlagi zgodovine ogledov, kar povečuje angažiranost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoče se naloge, poenostavi delovne tokove in izboljša operativno učinkovitost.  
Primer: Aplikacije za podporo strankam uporabljajo AI-pogovorne bote za obravnavo pogostih vprašanj, kar skrajša čas odziva in omogoči človeškim agentom, da se osredotočijo na bolj zapletene težave.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša splošno uporabniško izkušnjo z zagotavljanjem inteligentnih funkcij, kot so prepoznavanje glasu, obdelava naravnega jezika in prediktivno besedilo.  
Primer: Virtualni pomočniki, kot sta Siri in Google Assistant, uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, kar uporabnikom olajša interakcijo z napravami.

### To vse zveni odlično, kajne? Zakaj potem potrebujemo okvir za AI agente?

Okviri za AI agente predstavljajo nekaj več kot le AI okvire. Zasnovani so za omogočanje ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem za dosego določenih ciljev. Ti agenti lahko izkazujejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se razmeram. Oglejmo si ključne zmogljivosti, ki jih omogočajo okviri za AI agente:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in koordinirajo za reševanje kompleksnih nalog.
- **Avtomatizacija in upravljanje nalog**: Zagotavljajo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, delegiranje nalog in dinamično upravljanje nalog med agenti.
- **Razumevanje konteksta in prilagoditev**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočemu se okolju in sprejemanja odločitev na podlagi informacij v realnem času.

Skratka, agenti omogočajo več, dvigujejo avtomatizacijo na višjo raven in ustvarjajo bolj inteligentne sisteme, ki se lahko prilagajajo in učijo iz svojega okolja.

## Kako hitro prototipirati, iterirati in izboljšati zmogljivosti agenta?

To je hitro razvijajoče se področje, vendar obstajajo nekatere skupne značilnosti večine okvirov za AI agente, ki vam lahko pomagajo hitro prototipirati in iterirati, in sicer modularne komponente, orodja za sodelovanje in učenje v realnem času. Poglobimo se v te:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej pripravljene komponente, kot so AI in Memory konektorji, klic funkcij z uporabo naravnega jezika ali vtičnikov za kodo, predloge za pozive in drugo.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente s specifičnimi vlogami in nalogami, kar omogoča testiranje in izboljšanje sodelovalnih delovnih tokov.
- **Učite se v realnem času**: Implementirajte povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporabite modularne komponente

SDK-ji, kot sta Microsoft Semantic Kernel in LangChain, ponujajo vnaprej pripravljene komponente, kot so AI konektorji, predloge za pozive in upravljanje pomnilnika.

**Kako lahko ekipe to uporabijo**: Ekipe lahko hitro sestavijo te komponente za ustvarjanje funkcionalnega prototipa brez potrebe po začetku iz nič, kar omogoča hitro eksperimentiranje in iteracijo.

**Kako to deluje v praksi**: Uporabite lahko vnaprej pripravljen razčlenjevalnik za pridobivanje informacij iz uporabniškega vnosa, modul za pomnilnik za shranjevanje in pridobivanje podatkov ter generator pozivov za interakcijo z uporabniki, vse to brez potrebe po gradnji teh komponent iz nič.

**Primer kode**. Oglejmo si primere, kako lahko uporabite vnaprej pripravljen AI konektor s Semantic Kernel Python in .Net, ki uporablja samodejno klicanje funkcij za odziv modela na uporabniški vnos:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```  
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Iz tega primera lahko vidite, kako lahko izkoristite vnaprej pripravljen razčlenjevalnik za pridobivanje ključnih informacij iz uporabniškega vnosa, kot so izvor, cilj in datum zahteve za rezervacijo leta. Ta modularni pristop vam omogoča, da se osredotočite na logiko na višji ravni.

### Izkoristite orodja za sodelovanje

Okviri, kot so CrewAI, Microsoft AutoGen in Semantic Kernel, omogočajo ustvarjanje več agentov, ki lahko sodelujejo.

**Kako lahko ekipe to uporabijo**: Ekipe lahko oblikujejo agente s specifičnimi vlogami in nalogami, kar omogoča testiranje in izboljšanje sodelovalnih delovnih tokov ter izboljšanje splošne učinkovitosti sistema.

**Kako to deluje v praksi**: Ustvarite lahko ekipo agentov, kjer ima vsak agent specializirano funkcijo, kot so pridobivanje podatkov, analiza ali sprejemanje odločitev. Ti agenti lahko komunicirajo in delijo informacije za dosego skupnega cilja, kot je odgovor na uporabniško vprašanje ali dokončanje naloge.

**Primer kode (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

V prejšnji kodi lahko vidite, kako lahko ustvarite nalogo, ki vključuje več agentov, ki sodelujejo pri analizi podatkov. Vsak agent opravlja določeno funkcijo, naloga pa se izvaja s koordinacijo agentov za dosego želenega rezultata. Z ustvarjanjem namenskih agentov s specializiranimi vlogami lahko izboljšate učinkovitost in zmogljivost nalog.

### Učite se v realnem času

Napredni okviri omogočajo zmožnosti za razumevanje konteksta in prilagajanje v realnem času.

**Kako lahko ekipe to uporabijo**: Ekipe lahko implementirajo povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje, kar vodi do nenehnega izboljševanja in izpopolnjevanja zmogljivosti.

**Kako to deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, podatke o okolju in rezultate nalog za posodobitev svoje baze znanja, prilagoditev algoritmov za sprejemanje odločitev in izboljšanje zmogljivosti skozi čas. Ta iterativni proces učenja omogoča agentom, da se prilagodijo spreminjajočim se razmeram in preferencam uporabnikov, kar izboljšuje splošno učinkovitost sistema.

## Kakšne so razlike med okviri AutoGen, Semantic Kernel in Azure AI Agent Service?

Obstaja veliko načinov za primerjavo teh okvirov, vendar si oglejmo ključne razlike glede na njihovo zasnovo, zmogljivosti in ciljne primere uporabe:

## AutoGen

AutoGen je odprtokodni okvir, ki ga je razvil Microsoft Research's AI Frontiers Lab. Osredotoča se na dogodkovno vodene, porazdeljene *agentne* aplikacije, ki omogočajo več LLM-jev in SLM-jev, orodij ter napredne vzorce oblikovanja več agentov.

AutoGen temelji na osnovnem konceptu agentov, ki so avtonomni subjekti, ki lahko zaznavajo svoje okolje, sprejemajo odločitve in izvajajo dejanja za dosego določenih ciljev. Agenti komunicirajo prek asinhronih sporočil, kar jim omogoča, da delujejo neodvisno in vzporedno, kar izboljšuje skalabilnost in odzivnost sistema.
Torej, to so osnove ogrodja Semantic Kernel, kaj pa ogrodje Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service je novejši dodatek, predstavljen na Microsoft Ignite 2024. Omogoča razvoj in uvajanje AI agentov z bolj prilagodljivimi modeli, kot je neposredno klicanje odprtokodnih LLM-jev, kot so Llama 3, Mistral in Cohere.

Azure AI Agent Service ponuja močnejše mehanizme za varnost v podjetjih in metode za shranjevanje podatkov, zaradi česar je primeren za poslovne aplikacije.

Deluje takoj z večagentnimi orkestracijskimi ogrodji, kot sta AutoGen in Semantic Kernel.

Ta storitev je trenutno v javnem predogledu in podpira Python ter C# za gradnjo agentov.

Z uporabo Semantic Kernel Python lahko ustvarimo Azure AI agenta z uporabniško določenim vtičnikom:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Osnovni koncepti

Azure AI Agent Service vključuje naslednje osnovne koncepte:

- **Agent**. Azure AI Agent Service se integrira z Azure AI Foundry. Znotraj AI Foundry AI agent deluje kot "pameten" mikrostoritev, ki se lahko uporablja za odgovarjanje na vprašanja (RAG), izvajanje dejanj ali popolno avtomatizacijo delovnih tokov. To doseže s kombinacijo moči generativnih AI modelov in orodij, ki mu omogočajo dostop do resničnih virov podatkov in interakcijo z njimi. Tukaj je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-4o-mini`, imenom `my-agent` in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Nit in sporočila**. Nit je še en pomemben koncept. Predstavlja pogovor ali interakcijo med agentom in uporabnikom. Niti se lahko uporabljajo za sledenje napredku pogovora, shranjevanje informacij o kontekstu in upravljanje stanja interakcije. Tukaj je primer niti:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V prejšnji kodi je ustvarjena nit. Nato je niti poslano sporočilo. Z uporabo `create_and_process_run` je agentu naročeno, naj opravi delo na niti. Na koncu so sporočila pridobljena in zabeležena, da se vidi odziv agenta. Sporočila kažejo napredek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da so lahko sporočila različnih vrst, kot so besedilo, slika ali datoteka, kar pomeni, da je delo agenta na primer privedlo do slike ali besedilnega odgovora. Kot razvijalec lahko te informacije nato uporabite za nadaljnjo obdelavo odgovora ali njegovo predstavitev uporabniku.

- **Integracija z drugimi AI ogrodji**. Azure AI Agent Service lahko sodeluje z drugimi ogrodji, kot sta AutoGen in Semantic Kernel, kar pomeni, da lahko del svoje aplikacije zgradite v enem od teh ogrodij, na primer z uporabo Agent Service kot orkestratorja, ali pa vse zgradite v Agent Service.

**Primeri uporabe**: Azure AI Agent Service je zasnovan za poslovne aplikacije, ki zahtevajo varno, razširljivo in prilagodljivo uvajanje AI agentov.

## Kakšna je razlika med temi ogrodji?

Zdi se, da se ta ogrodja precej prekrivajo, vendar obstajajo ključne razlike glede njihove zasnove, zmogljivosti in ciljnih primerov uporabe:

- **AutoGen**: Je eksperimentalno ogrodje, osredotočeno na najnovejše raziskave o večagentnih sistemih. Najboljše je za eksperimentiranje in prototipiranje naprednih večagentnih sistemov.
- **Semantic Kernel**: Je proizvodno pripravljena knjižnica agentov za gradnjo poslovnih aplikacij z agenti. Osredotoča se na dogodkovno vodene, porazdeljene aplikacije z agenti, omogoča uporabo več LLM-jev in SLM-jev, orodij ter enojnih/večagentnih vzorcev oblikovanja.
- **Azure AI Agent Service**: Je platforma in storitev za uvajanje agentov v Azure Foundry. Ponuja povezljivost s storitvami, ki jih podpira Azure Foundry, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.

Še vedno niste prepričani, katero izbrati?

### Primeri uporabe

Poglejmo, ali vam lahko pomagamo z nekaj pogostimi primeri uporabe:

> V: Eksperimentiram, se učim in gradim prototipne aplikacije z agenti, želim pa hitro graditi in eksperimentirati.
>
> O: AutoGen bi bila dobra izbira za ta scenarij, saj se osredotoča na dogodkovno vodene, porazdeljene aplikacije z agenti in podpira napredne večagentne vzorce oblikovanja.

> V: Kaj naredi AutoGen boljšo izbiro kot Semantic Kernel in Azure AI Agent Service za ta primer uporabe?
>
> O: AutoGen je posebej zasnovan za dogodkovno vodene, porazdeljene aplikacije z agenti, zaradi česar je zelo primeren za avtomatizacijo nalog, kot sta generiranje kode in analiza podatkov. Ponuja potrebna orodja in zmogljivosti za učinkovito gradnjo kompleksnih večagentnih sistemov.

> V: Zdi se, da bi Azure AI Agent Service lahko deloval tudi tukaj, saj ima orodja za generiranje kode in še več?
>
> O: Da, Azure AI Agent Service je platforma za agente in dodaja vgrajene zmogljivosti za več modelov, Azure AI Search, Bing Search in Azure Functions. Omogoča enostavno gradnjo vaših agentov v Foundry Portalu in njihovo uvajanje na večji obseg.

> V: Še vedno sem zmeden, samo dajte mi eno možnost.
>
> O: Odlična izbira je, da najprej zgradite svojo aplikacijo v Semantic Kernel in nato uporabite Azure AI Agent Service za uvajanje vašega agenta. Ta pristop vam omogoča enostavno shranjevanje vaših agentov, hkrati pa izkorišča moč za gradnjo večagentnih sistemov v Semantic Kernel. Poleg tega ima Semantic Kernel konektor v AutoGen, kar omogoča enostavno uporabo obeh ogrodij skupaj.

Povzemimo ključne razlike v tabeli:

| Ogrodje | Fokus | Osnovni koncepti | Primeri uporabe |
| --- | --- | --- | --- |
| AutoGen | Dogodkovno vodene, porazdeljene aplikacije z agenti | Agenti, Osebnosti, Funkcije, Podatki | Generiranje kode, naloge analize podatkov |
| Semantic Kernel | Razumevanje in generiranje besedil, podobnih človeškim | Agenti, Modularne komponente, Sodelovanje | Razumevanje naravnega jezika, generiranje vsebine |
| Azure AI Agent Service | Prilagodljivi modeli, varnost v podjetjih, Generiranje kode, Klicanje orodij | Modularnost, Sodelovanje, Orkestracija procesov | Varno, razširljivo in prilagodljivo uvajanje AI agentov |

Kakšen je idealen primer uporabe za vsako od teh ogrodij?

## Ali lahko neposredno integriram svoja obstoječa orodja iz ekosistema Azure ali potrebujem samostojne rešitve?

Odgovor je da, lahko neposredno integrirate svoja obstoječa orodja iz ekosistema Azure zlasti z Azure AI Agent Service, saj je zasnovan za brezhibno delovanje z drugimi Azure storitvami. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Obstaja tudi globoka integracija z Azure AI Foundry.

Za AutoGen in Semantic Kernel lahko prav tako integrirate Azure storitve, vendar boste morda morali klicati Azure storitve iz svoje kode. Drug način integracije je uporaba Azure SDK-jev za interakcijo z Azure storitvami iz vaših agentov. Poleg tega, kot je bilo omenjeno, lahko uporabite Azure AI Agent Service kot orkestrator za vaše agente, zgrajene v AutoGen ali Semantic Kernel, kar omogoča enostaven dostop do ekosistema Azure.

### Imate več vprašanj o ogrodjih AI Agent?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, se udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Reference

- 

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje vzorcev oblikovanja agentov](../03-agentic-design-patterns/README.md)

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.