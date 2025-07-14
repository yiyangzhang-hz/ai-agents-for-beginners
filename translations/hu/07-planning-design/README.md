<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:45:33+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "hu"
}
-->
a gyors áttekintéshez.

A következő Python kódrészlet egy egyszerű tervező ügynököt mutat be, amely egy célt bont le részfeladatokra, és strukturált tervet generál:

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

### Tervező ügynök több ügynökös összehangolással

Ebben a példában egy Semantic Router Agent kap egy felhasználói kérést (pl. „Szükségem van egy szállás tervre az utazásomhoz.”).

A tervező ezután:

* Megkapja a szállás tervet: A tervező veszi a felhasználó üzenetét, és egy rendszerüzenet alapján (amely tartalmazza az elérhető ügynökök részleteit) strukturált utazási tervet generál.
* Felsorolja az ügynököket és eszközeiket: Az ügynökregiszter tartalmazza az ügynökök listáját (pl. repülőjegy, szállás, autókölcsönzés, programok) és az általuk kínált funkciókat vagy eszközöket.
* A tervet a megfelelő ügynökökhöz irányítja: A részfeladatok számától függően a tervező vagy közvetlenül elküldi az üzenetet egy dedikált ügynöknek (egytaskos esetben), vagy egy csoportos csevegés kezelőn keresztül koordinálja a több ügynökös együttműködést.
* Összefoglalja az eredményt: Végül a tervező összefoglalja a generált tervet az átláthatóság érdekében.
A következő Python kódminta bemutatja ezeket a lépéseket:

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

A következő a korábbi kód kimenete, ezt a strukturált kimenetet használhatod az `assigned_agent`-hez való irányításhoz, és összefoglalhatod az utazási tervet a végfelhasználónak.

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

A korábbi kódpéldát tartalmazó jegyzetfüzet elérhető [itt](../../../07-planning-design/07-autogen.ipynb).

### Iteratív tervezés

Néhány feladat igényel oda-vissza kommunikációt vagy újratervezést, ahol az egyik részfeladat eredménye befolyásolja a következőt. Például, ha az ügynök váratlan adatformátumot talál a repülőjegyfoglalás során, akkor módosítania kell a stratégiáját, mielőtt a szállásfoglalásra lépne.

Emellett a felhasználói visszajelzés (pl. ha egy ember korábbi járatot választana) részleges újratervezést indíthat el. Ez a dinamikus, iteratív megközelítés biztosítja, hogy a végső megoldás megfeleljen a valós világ korlátainak és a változó felhasználói igényeknek.

példakód

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

A komplexebb tervezéshez érdemes megnézni a Magnetic One-t

a komplex feladatok megoldásához.

## Összefoglalás

Ebben a cikkben megnéztünk egy példát arra, hogyan hozhatunk létre egy tervezőt, amely dinamikusan kiválasztja a rendelkezésre álló ügynököket. A tervező kimenete lebontja a feladatokat és hozzárendeli az ügynököket, hogy azok végrehajthatók legyenek. Feltételezzük, hogy az ügynökök hozzáférnek a feladat végrehajtásához szükséges funkciókhoz/eszközökhöz. Az ügynökök mellett további mintákat is beépíthetsz, mint például reflexió, összefoglaló vagy körkörös csevegés, hogy tovább testreszabhasd.

## További források

* AutoGen Magnetic One – Egy általános többügynökös rendszer komplex feladatok megoldására, amely több kihívást jelentő ügynöki benchmarkon is lenyűgöző eredményeket ért el. Referencia:

. Ebben a megvalósításban az összehangoló feladat-specifikus tervet készít, és ezeket a feladatokat kiosztja a rendelkezésre álló ügynököknek. A tervezés mellett az összehangoló nyomon követi a feladat előrehaladását, és szükség esetén újratervez.

## Előző lecke

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Következő lecke

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.