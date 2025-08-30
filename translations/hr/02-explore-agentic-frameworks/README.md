<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-29T23:06:18+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hr"
}
-->
[![Istraživanje AI Agent Frameworka](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.hr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na sliku iznad za pregled videa ove lekcije)_

# Istražite AI Agent Frameworke

AI agent frameworki su softverske platforme osmišljene kako bi pojednostavile stvaranje, implementaciju i upravljanje AI agentima. Ovi frameworki pružaju programerima unaprijed izgrađene komponente, apstrakcije i alate koji olakšavaju razvoj složenih AI sustava.

Ovi frameworki pomažu programerima da se usmjere na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe uobičajenim izazovima u razvoju AI agenata. Oni poboljšavaju skalabilnost, pristupačnost i učinkovitost u izgradnji AI sustava.

## Uvod 

Ova lekcija će obuhvatiti:

- Što su AI Agent Frameworki i što omogućuju programerima da postignu?
- Kako timovi mogu koristiti ove frameworke za brzo prototipiranje, iteraciju i poboljšanje sposobnosti svojih agenata?
- Koje su razlike između frameworka i alata koje je stvorio Microsoft, i drugih?
- Mogu li integrirati svoje postojeće Azure alate iz ekosustava izravno ili su mi potrebna samostalna rješenja?
- Što je Azure AI Agents usluga i kako mi to pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su pomoći vam da razumijete:

- Ulogu AI Agent Frameworka u razvoju AI-a.
- Kako iskoristiti AI Agent Frameworke za izgradnju inteligentnih agenata.
- Ključne sposobnosti koje omogućuju AI Agent Frameworki.
- Razlike između AutoGen-a, Semantic Kernel-a i Azure AI Agent usluge.

## Što su AI Agent Frameworki i što omogućuju programerima?

Tradicionalni AI Frameworki mogu vam pomoći da integrirate AI u svoje aplikacije i učinite ih boljima na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje i preferencije korisnika kako bi pružio personalizirane preporuke, sadržaj i iskustva.
Primjer: Streaming servisi poput Netflixa koriste AI za predlaganje filmova i serija na temelju povijesti gledanja, povećavajući angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati ponavljajuće zadatke, pojednostaviti radne procese i poboljšati operativnu učinkovitost.
Primjer: Aplikacije za korisničku podršku koriste AI chatbotove za rješavanje uobičajenih upita, smanjujući vrijeme odgovora i oslobađajući ljudske agente za složenije probleme.
- **Poboljšano korisničko iskustvo**: AI može poboljšati ukupno korisničko iskustvo pružanjem inteligentnih značajki poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.
Primjer: Virtualni asistenti poput Siri i Google Assistanta koriste AI za razumijevanje i odgovaranje na glasovne naredbe, olakšavajući korisnicima interakciju s uređajima.

### Sve to zvuči sjajno, zar ne? Pa zašto nam trebaju AI Agent Frameworki?

AI Agent Frameworki predstavljaju nešto više od običnih AI frameworka. Dizajnirani su za omogućavanje stvaranja inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okolinom kako bi postigli specifične ciljeve. Ovi agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenjivim uvjetima. Pogledajmo neke ključne sposobnosti koje omogućuju AI Agent Frameworki:

- **Suradnja i koordinacija agenata**: Omogućuju stvaranje više AI agenata koji mogu raditi zajedno, komunicirati i koordinirati kako bi riješili složene zadatke.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višekorakih radnih procesa, delegiranje zadataka i dinamičko upravljanje zadacima među agentima.
- **Razumijevanje konteksta i prilagodba**: Opremljuju agente sposobnošću razumijevanja konteksta, prilagodbe promjenjivim uvjetima i donošenja odluka na temelju informacija u stvarnom vremenu.

Ukratko, agenti vam omogućuju da postignete više, podignete automatizaciju na višu razinu i stvorite inteligentnije sustave koji se mogu prilagoditi i učiti iz svoje okoline.

## Kako brzo prototipirati, iterirati i poboljšati sposobnosti agenata?

Ovo je područje koje se brzo razvija, ali postoje neke zajedničke stvari kod većine AI Agent Frameworka koje vam mogu pomoći da brzo prototipirate i iterirate, poput modularnih komponenti, alata za suradnju i učenja u stvarnom vremenu. Pogledajmo detaljnije:

- **Koristite modularne komponente**: AI SDK-ovi nude unaprijed izgrađene komponente poput AI i Memory konektora, pozivanja funkcija pomoću prirodnog jezika ili dodataka za kod, predložaka upita i još mnogo toga.
- **Iskoristite alate za suradnju**: Dizajnirajte agente s određenim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih radnih procesa.
- **Učite u stvarnom vremenu**: Implementirajte povratne petlje gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Koristite modularne komponente

SDK-ovi poput Microsoft Semantic Kernel-a i LangChain-a nude unaprijed izgrađene komponente poput AI konektora, predložaka upita i upravljanja memorijom.

**Kako timovi mogu koristiti ovo**: Timovi mogu brzo sastaviti ove komponente kako bi stvorili funkcionalni prototip bez potrebe za početkom od nule, omogućujući brzo eksperimentiranje i iteraciju.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izgrađeni parser za izdvajanje informacija iz korisničkog unosa, modul memorije za pohranu i dohvaćanje podataka te generator upita za interakciju s korisnicima, sve bez potrebe za izgradnjom ovih komponenti od nule.

**Primjer koda**. Pogledajmo primjere kako možete koristiti unaprijed izgrađeni AI konektor sa Semantic Kernel Python i .Net koji koristi automatsko pozivanje funkcija kako bi model odgovorio na korisnički unos:

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

Iz ovog primjera možete vidjeti kako možete iskoristiti unaprijed izgrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput polazišta, odredišta i datuma zahtjeva za rezervaciju leta. Ovaj modularni pristup omogućuje vam da se usredotočite na logiku višeg nivoa.

### Iskoristite alate za suradnju

Frameworki poput CrewAI, Microsoft AutoGen i Semantic Kernel olakšavaju stvaranje više agenata koji mogu raditi zajedno.

**Kako timovi mogu koristiti ovo**: Timovi mogu dizajnirati agente s određenim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih radnih procesa te poboljšanje ukupne učinkovitosti sustava.

**Kako to funkcionira u praksi**: Možete stvoriti tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ovi agenti mogu komunicirati i dijeliti informacije kako bi postigli zajednički cilj, poput odgovaranja na korisnički upit ili dovršavanja zadatka.

**Primjer koda (AutoGen)**:

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

U prethodnom kodu možete vidjeti kako možete stvoriti zadatak koji uključuje više agenata koji zajedno rade na analizi podataka. Svaki agent obavlja specifičnu funkciju, a zadatak se izvršava koordinacijom agenata kako bi se postigao željeni rezultat. Stvaranjem posvećenih agenata sa specijaliziranim ulogama možete poboljšati učinkovitost i performanse zadatka.

### Učite u stvarnom vremenu

Napredni frameworki pružaju mogućnosti za razumijevanje konteksta u stvarnom vremenu i prilagodbu.

**Kako timovi mogu koristiti ovo**: Timovi mogu implementirati povratne petlje gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što dovodi do kontinuiranog poboljšanja i usavršavanja sposobnosti.

**Kako to funkcionira u praksi**: Agenti mogu analizirati povratne informacije korisnika, podatke iz okoline i ishode zadataka kako bi ažurirali svoju bazu znanja, prilagodili algoritme donošenja odluka i poboljšali performanse tijekom vremena. Ovaj iterativni proces učenja omogućuje agentima da se prilagode promjenjivim uvjetima i preferencijama korisnika, poboljšavajući ukupnu učinkovitost sustava.

## Koje su razlike između frameworka AutoGen, Semantic Kernel i Azure AI Agent usluge?

Postoji mnogo načina za usporedbu ovih frameworka, ali pogledajmo neke ključne razlike u pogledu njihovog dizajna, sposobnosti i ciljanih slučajeva upotrebe:

## AutoGen

AutoGen je open-source framework koji je razvio Microsoft Research's AI Frontiers Lab. Fokusira se na događajno vođene, distribuirane *agentne* aplikacije, omogućujući više LLM-ova i SLM-ova, alata i naprednih dizajnerskih obrazaca za više agenata.

AutoGen je izgrađen oko osnovnog koncepta agenata, koji su autonomni entiteti koji mogu percipirati svoju okolinu, donositi odluke i poduzimati radnje kako bi postigli specifične ciljeve. Agenti komuniciraju putem asinkronih poruka, omogućujući im da rade neovisno i paralelno, poboljšavajući skalabilnost i odzivnost sustava.
Dakle, to su osnove Semantic Kernel okvira, što je s Agent Frameworkom?

## Azure AI Agent Service

Azure AI Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućuje razvoj i implementaciju AI agenata s fleksibilnijim modelima, poput direktnog pozivanja open-source LLM-ova kao što su Llama 3, Mistral i Cohere.

Azure AI Agent Service pruža jače mehanizme sigurnosti za poduzeća i metode pohrane podataka, što ga čini prikladnim za poslovne aplikacije.

Radi odmah s okvirima za orkestraciju više agenata poput AutoGen i Semantic Kernel.

Ova usluga trenutno je u javnom pregledu i podržava Python i C# za izradu agenata.

Koristeći Semantic Kernel Python, možemo kreirati Azure AI agenta s korisnički definiranim dodatkom:

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

Azure AI Agent Service ima sljedeće osnovne koncepte:

- **Agent**. Azure AI Agent Service integrira se s Azure AI Foundry. Unutar AI Foundry, AI agent djeluje kao "pametan" mikroservis koji se može koristiti za odgovaranje na pitanja (RAG), izvršavanje radnji ili potpuno automatiziranje tijekova rada. To postiže kombiniranjem snage generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s izvorima podataka iz stvarnog svijeta. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru, agent je kreiran s modelom `gpt-4o-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za obavljanje zadataka interpretacije koda.

- **Nit i poruke**. Nit je još jedan važan koncept. Predstavlja razgovor ili interakciju između agenta i korisnika. Niti se mogu koristiti za praćenje napretka razgovora, pohranu informacija o kontekstu i upravljanje stanjem interakcije. Evo primjera niti:

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

    U prethodnom kodu, kreirana je nit. Nakon toga, poruka je poslana niti. Pozivanjem `create_and_process_run`, agentu se traži da obavi rad na niti. Na kraju, poruke se dohvaćaju i bilježe kako bi se vidio odgovor agenta. Poruke ukazuju na napredak razgovora između korisnika i agenta. Također je važno razumjeti da poruke mogu biti različitih vrsta, poput teksta, slike ili datoteke, što znači da je rad agenta rezultirao, na primjer, slikom ili tekstualnim odgovorom. Kao programer, možete koristiti te informacije za daljnju obradu odgovora ili njegovo predstavljanje korisniku.

- **Integracija s drugim AI okvirima**. Azure AI Agent Service može komunicirati s drugim okvirima poput AutoGen i Semantic Kernel, što znači da možete izgraditi dio svoje aplikacije u jednom od tih okvira, a na primjer koristiti Agent Service kao orkestrator ili možete sve izgraditi u Agent Service.

**Primjene**: Azure AI Agent Service je dizajniran za poslovne aplikacije koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih okvira?

Čini se da postoji puno preklapanja između ovih okvira, ali postoje ključne razlike u njihovom dizajnu, mogućnostima i ciljnim primjenama:

- **AutoGen**: Eksperimentalni okvir usmjeren na najnovija istraživanja o sustavima s više agenata. Najbolje mjesto za eksperimentiranje i prototipiranje sofisticiranih sustava s više agenata.
- **Semantic Kernel**: Proizvodno spremna biblioteka agenata za izgradnju poslovnih aplikacija s agentima. Fokusira se na aplikacije temeljene na događajima, distribuirane aplikacije s agentima, omogućujući više LLM-ova i SLM-ova, alata te dizajnerske obrasce za jednog ili više agenata.
- **Azure AI Agent Service**: Platforma i usluga implementacije u Azure Foundry za agente. Nudi povezivanje s uslugama koje podržava Azure, poput Azure OpenAI, Azure AI Search, Bing Search i izvršavanje koda.

Još uvijek niste sigurni koji odabrati?

### Primjene

Pogledajmo možemo li vam pomoći prolaskom kroz neke uobičajene primjene:

> P: Eksperimentiram, učim i gradim proof-of-concept aplikacije s agentima, i želim brzo graditi i eksperimentirati
>

> O: AutoGen bi bio dobar izbor za ovaj scenarij, jer se fokusira na aplikacije temeljene na događajima, distribuirane aplikacije s agentima i podržava napredne dizajnerske obrasce za više agenata.

> P: Što AutoGen čini boljim izborom od Semantic Kernel i Azure AI Agent Service za ovu primjenu?
>
> O: AutoGen je posebno dizajniran za aplikacije temeljene na događajima, distribuirane aplikacije s agentima, što ga čini prikladnim za automatizaciju zadataka generiranja koda i analize podataka. Pruža potrebne alate i mogućnosti za učinkovitu izgradnju složenih sustava s više agenata.

> P: Zvuči kao da bi Azure AI Agent Service također mogao raditi ovdje, ima alate za generiranje koda i više?
>
> O: Da, Azure AI Agent Service je platforma za agente i dodaje ugrađene mogućnosti za više modela, Azure AI Search, Bing Search i Azure Functions. Olakšava izgradnju vaših agenata u Foundry Portalu i njihovu implementaciju na velikoj skali.

> P: Još uvijek sam zbunjen, samo mi dajte jednu opciju
>
> O: Odličan izbor je izgraditi svoju aplikaciju u Semantic Kernelu prvo, a zatim koristiti Azure AI Agent Service za implementaciju vašeg agenta. Ovaj pristup omogućuje vam jednostavno trajno pohranjivanje vaših agenata dok koristite snagu za izgradnju sustava s više agenata u Semantic Kernelu. Osim toga, Semantic Kernel ima konektor u AutoGen, što olakšava korištenje oba okvira zajedno.

Sažmimo ključne razlike u tablici:

| Okvir | Fokus | Osnovni koncepti | Primjene |
| --- | --- | --- | --- |
| AutoGen | Aplikacije temeljene na događajima, distribuirane aplikacije s agentima | Agenti, Osobe, Funkcije, Podaci | Generiranje koda, zadaci analize podataka |
| Semantic Kernel | Razumijevanje i generiranje teksta nalik ljudskom | Agenti, Modularne komponente, Suradnja | Razumijevanje prirodnog jezika, generiranje sadržaja |
| Azure AI Agent Service | Fleksibilni modeli, sigurnost za poduzeća, Generiranje koda, Pozivanje alata | Modularnost, Suradnja, Orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

Koja je idealna primjena za svaki od ovih okvira?

## Mogu li direktno integrirati svoje postojeće alate iz Azure ekosustava ili trebam samostalna rješenja?

Odgovor je da, možete direktno integrirati svoje postojeće alate iz Azure ekosustava s Azure AI Agent Service, posebno zato što je izgrađen da radi besprijekorno s drugim Azure uslugama. Na primjer, mogli biste integrirati Bing, Azure AI Search i Azure Functions. Također postoji duboka integracija s Azure AI Foundry.

Za AutoGen i Semantic Kernel, također možete integrirati s Azure uslugama, ali možda ćete morati pozvati Azure usluge iz svog koda. Drugi način integracije je korištenje Azure SDK-ova za interakciju s Azure uslugama iz vaših agenata. Osim toga, kao što je spomenuto, možete koristiti Azure AI Agent Service kao orkestrator za vaše agente izgrađene u AutoGen ili Semantic Kernel, što bi omogućilo jednostavan pristup Azure ekosustavu.

### Imate još pitanja o AI Agent Frameworkovima?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Reference

- 

## Prethodna lekcija

[Uvod u AI agente i primjene agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje dizajnerskih obrazaca za agente](../03-agentic-design-patterns/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.