<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:40:25+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "it"
}
-->
[![Planning Design Pattern](../../../translated_images/lesson-7-thumbnail.f7163ac557bea1236242cc86b178c3f1bbf5eb07b87f9cd7c256b366e32bcbb6.it.png)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Progettazione della Pianificazione

## Introduzione

Questa lezione tratterà

* Definire un obiettivo chiaro e suddividere un compito complesso in attività gestibili.
* Sfruttare output strutturati per risposte più affidabili e leggibili da macchine.
* Applicare un approccio basato su eventi per gestire compiti dinamici e input imprevisti.

## Obiettivi di Apprendimento

Al termine di questa lezione, avrai una comprensione di:

* Identificare e impostare un obiettivo generale per un agente AI, assicurandoti che sappia chiaramente cosa deve essere raggiunto.
* Scomporre un compito complesso in sotto-compiti gestibili e organizzarli in una sequenza logica.
* Dotare gli agenti degli strumenti giusti (ad esempio, strumenti di ricerca o di analisi dati), decidere quando e come usarli, e gestire situazioni impreviste.
* Valutare i risultati dei sotto-compiti, misurare le prestazioni e iterare sulle azioni per migliorare il risultato finale.

## Definire l'Obiettivo Generale e Suddividere un Compito

![Definire Obiettivi e Compiti](../../../translated_images/defining-goals-tasks.d70439e19e37c47ac76c48b209a4eb515bea5b8a5207f6b2e7b5e597f09ccf6a.it.png)

La maggior parte dei compiti nel mondo reale è troppo complessa per essere affrontata in un solo passaggio. Un agente AI ha bisogno di un obiettivo conciso per guidare la sua pianificazione e le sue azioni. Ad esempio, considera l'obiettivo:

    "Generare un itinerario di viaggio di 3 giorni."

Anche se è semplice da enunciare, necessita comunque di una definizione più precisa. Più l'obiettivo è chiaro, meglio l'agente (e qualsiasi collaboratore umano) può concentrarsi sul raggiungimento del risultato giusto, come creare un itinerario completo con opzioni di volo, raccomandazioni per hotel e suggerimenti per attività.

### Scomposizione del Compito

Compiti grandi o complessi diventano più gestibili se suddivisi in sotto-compiti orientati all'obiettivo.
Per l'esempio dell'itinerario di viaggio, potresti scomporre l'obiettivo in:

* Prenotazione Voli
* Prenotazione Hotel
* Noleggio Auto
* Personalizzazione

Ogni sotto-compito può poi essere affrontato da agenti o processi dedicati. Un agente potrebbe specializzarsi nella ricerca delle migliori offerte di volo, un altro concentrarsi sulle prenotazioni alberghiere, e così via. Un agente coordinatore o "downstream" può quindi compilare questi risultati in un unico itinerario coerente per l'utente finale.

Questo approccio modulare consente anche miglioramenti incrementali. Ad esempio, potresti aggiungere agenti specializzati per Raccomandazioni Culinarie o Suggerimenti per Attività Locali e perfezionare l'itinerario nel tempo.

### Output Strutturato

I Large Language Models (LLM) possono generare output strutturati (ad esempio JSON) che sono più facili da analizzare e processare per agenti o servizi downstream. Questo è particolarmente utile in un contesto multi-agente, dove possiamo agire su questi compiti dopo aver ricevuto l'output della pianificazione. Consulta questo per una panoramica rapida.

Il seguente snippet Python dimostra un semplice agente di pianificazione che scompone un obiettivo in sotto-compiti e genera un piano strutturato:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
                      Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Agente di Pianificazione con Orchestrazione Multi-Agente

In questo esempio, un Semantic Router Agent riceve una richiesta dell'utente (ad esempio, "Ho bisogno di un piano hotel per il mio viaggio.").

Il pianificatore quindi:

* Riceve il Piano Hotel: il pianificatore prende il messaggio dell'utente e, basandosi su un prompt di sistema (inclusi i dettagli degli agenti disponibili), genera un piano di viaggio strutturato.
* Elenca gli Agenti e i loro Strumenti: il registro degli agenti contiene una lista di agenti (ad esempio per voli, hotel, noleggio auto e attività) insieme alle funzioni o strumenti che offrono.
* Inoltra il Piano agli Agenti Competenti: a seconda del numero di sotto-compiti, il pianificatore invia il messaggio direttamente a un agente dedicato (per scenari a singolo compito) o coordina tramite un gestore di chat di gruppo per la collaborazione multi-agente.
* Riassume il Risultato: infine, il pianificatore riassume il piano generato per chiarezza.
Il seguente esempio di codice Python illustra questi passaggi:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Quello che segue è l'output del codice precedente e puoi quindi usare questo output strutturato per indirizzare al `assigned_agent` e riassumere il piano di viaggio per l'utente finale.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Un notebook di esempio con il codice precedente è disponibile [qui](../../../07-planning-design/07-autogen.ipynb).

### Pianificazione Iterativa

Alcuni compiti richiedono un processo di andata e ritorno o una ripianificazione, dove il risultato di un sotto-compito influenza il successivo. Ad esempio, se l'agente scopre un formato dati imprevisto durante la prenotazione dei voli, potrebbe dover adattare la sua strategia prima di passare alle prenotazioni alberghiere.

Inoltre, il feedback dell'utente (ad esempio, una persona che decide di preferire un volo anticipato) può innescare una ripianificazione parziale. Questo approccio dinamico e iterativo garantisce che la soluzione finale sia allineata con i vincoli reali e le preferenze in evoluzione dell'utente.

esempio di codice

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

Per una pianificazione più completa, dai un'occhiata a Magnetic One

per risolvere compiti complessi.

## Riepilogo

In questo articolo abbiamo visto un esempio di come creare un pianificatore che può selezionare dinamicamente gli agenti disponibili definiti. L'output del Pianificatore scompone i compiti e assegna gli agenti affinché possano essere eseguiti. Si assume che gli agenti abbiano accesso alle funzioni/strumenti necessari per svolgere il compito. Oltre agli agenti, puoi includere altri pattern come reflection, summarizer e round robin chat per personalizzare ulteriormente.

## Risorse Aggiuntive

* AutoGen Magnetic One - Un sistema multi-agente generalista per risolvere compiti complessi che ha ottenuto risultati impressionanti su molteplici benchmark agentici sfidanti. Riferimento:

. In questa implementazione l'orchestratore crea un piano specifico per il compito e delega questi compiti agli agenti disponibili. Oltre alla pianificazione, l'orchestratore impiega anche un meccanismo di monitoraggio per seguire l'avanzamento del compito e ripianificare se necessario.

## Lezione Precedente

[Costruire Agenti AI Affidabili](../06-building-trustworthy-agents/README.md)

## Lezione Successiva

[Pattern di Progettazione Multi-Agente](../08-multi-agent/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.