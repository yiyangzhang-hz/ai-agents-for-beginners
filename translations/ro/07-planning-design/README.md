<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:46:26+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ro"
}
-->
pentru o prezentare rapidă.

Fragmentul Python următor demonstrează un agent simplu de planificare care descompune un obiectiv în subtasks și generează un plan structurat:

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

### Agent de Planificare cu Orchestrare Multi-Agent

În acest exemplu, un Agent Semantic Router primește o cerere de la utilizator (de exemplu, „Am nevoie de un plan pentru hotel pentru călătoria mea.”).

Planificatorul apoi:

* Primește Planul pentru Hotel: Planificatorul preia mesajul utilizatorului și, pe baza unui prompt de sistem (inclusiv detalii despre agenții disponibili), generează un plan de călătorie structurat.
* Listează Agenții și Instrumentele Lor: Registrul de agenți conține o listă de agenți (de exemplu, pentru zboruri, hoteluri, închirieri auto și activități) împreună cu funcțiile sau instrumentele pe care le oferă.
* Direcționează Planul către Agenții Respectivi: În funcție de numărul de subtasks, planificatorul trimite mesajul direct unui agent dedicat (pentru scenarii cu o singură sarcină) sau coordonează printr-un manager de chat de grup pentru colaborare multi-agent.
* Rezumă Rezultatul: În final, planificatorul rezumă planul generat pentru claritate.
Următorul exemplu de cod Python ilustrează acești pași:

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

Ce urmează este output-ul din codul anterior și poți folosi acest output structurat pentru a-l direcționa către `assigned_agent` și pentru a rezuma planul de călătorie către utilizatorul final.

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

Un notebook exemplu cu codul anterior este disponibil [aici](../../../07-planning-design/07-autogen.ipynb).

### Planificare Iterativă

Unele sarcini necesită un proces de tip back-and-forth sau replanificare, unde rezultatul unui subtask influențează următorul. De exemplu, dacă agentul descoperă un format de date neașteptat în timpul rezervării zborurilor, ar putea fi nevoie să-și adapteze strategia înainte de a trece la rezervările de hotel.

În plus, feedback-ul utilizatorului (de exemplu, un om care decide că preferă un zbor mai devreme) poate declanșa o replanificare parțială. Această abordare dinamică și iterativă asigură că soluția finală se aliniază cu constrângerile din lumea reală și preferințele în evoluție ale utilizatorului.

exemplu de cod

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

Pentru o planificare mai cuprinzătoare, consultați Magnetic One

pentru rezolvarea sarcinilor complexe.

## Rezumat

În acest articol am analizat un exemplu despre cum putem crea un planificator care poate selecta dinamic agenții disponibili definiți. Output-ul planificatorului descompune sarcinile și atribuie agenții astfel încât acestea să poată fi executate. Se presupune că agenții au acces la funcțiile/instrumentele necesare pentru a îndeplini sarcina. Pe lângă agenți, poți include și alte modele precum reflection, summarizer și round robin chat pentru o personalizare suplimentară.

## Resurse Suplimentare

* AutoGen Magnetic One - Un sistem multi-agent generalist pentru rezolvarea sarcinilor complexe, care a obținut rezultate impresionante pe mai multe benchmark-uri provocatoare pentru agenți. Referință:

. În această implementare, orchestratorul creează un plan specific sarcinii și delegă aceste sarcini agenților disponibili. Pe lângă planificare, orchestratorul folosește și un mecanism de monitorizare pentru a urmări progresul sarcinii și replanifică după cum este necesar.

## Lecția Anterioară

[Construirea Agenților AI de Încredere](../06-building-trustworthy-agents/README.md)

## Lecția Următoare

[Modelul de Design Multi-Agent](../08-multi-agent/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.