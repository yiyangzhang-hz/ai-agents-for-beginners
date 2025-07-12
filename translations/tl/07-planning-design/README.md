<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:45:01+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "tl"
}
-->
para sa mabilisang pangkalahatang ideya.

Ang sumusunod na snippet ng Python ay nagpapakita ng isang simpleng planning agent na naghahati ng isang layunin sa mga subtasks at bumubuo ng isang istrukturadong plano:

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

### Planning Agent na may Multi-Agent Orchestration

Sa halimbawang ito, isang Semantic Router Agent ang tumatanggap ng kahilingan mula sa user (halimbawa, "Kailangan ko ng plano sa hotel para sa aking biyahe.").

Ang planner ay:

* Tumatanggap ng Hotel Plan: Kinukuha ng planner ang mensahe ng user at, batay sa isang system prompt (kasama ang mga detalye ng mga available na agent), bumubuo ng isang istrukturadong travel plan.
* Nagtatala ng mga Agent at Kanilang mga Tool: Ang agent registry ay naglalaman ng listahan ng mga agent (halimbawa, para sa flight, hotel, car rental, at mga aktibidad) kasama ang mga function o tool na kanilang inaalok.
* Ipinapasa ang Plano sa mga Kaukulang Agent: Depende sa bilang ng mga subtasks, ang planner ay direktang nagpapadala ng mensahe sa isang dedikadong agent (para sa mga single-task na senaryo) o nakikipag-coordinate sa pamamagitan ng group chat manager para sa multi-agent na kolaborasyon.
* Nilalagom ang Resulta: Sa huli, nilalagom ng planner ang nabuo na plano para sa kalinawan.
Ang sumusunod na halimbawa ng Python code ay nagpapakita ng mga hakbang na ito:

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

Ang sumusunod ay ang output mula sa naunang code at maaari mong gamitin ang istrukturadong output na ito upang ipasa sa `assigned_agent` at ilahad ang travel plan sa end user.

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

Isang halimbawa ng notebook na may naunang code sample ay makikita [dito](../../../07-planning-design/07-autogen.ipynb).

### Iterative Planning

Ang ilang mga gawain ay nangangailangan ng paulit-ulit na proseso o muling pagpaplano, kung saan ang resulta ng isang subtask ay nakakaapekto sa susunod. Halimbawa, kung matuklasan ng agent ang isang hindi inaasahang format ng data habang nagbu-book ng mga flight, maaaring kailanganin nitong baguhin ang estratehiya bago magpatuloy sa pagbu-book ng hotel.

Bukod dito, ang feedback ng user (halimbawa, kapag pinili ng tao na mas gusto nila ang mas maagang flight) ay maaaring mag-trigger ng partial re-plan. Ang ganitong dynamic at iterative na pamamaraan ay nagsisiguro na ang panghuling solusyon ay naaayon sa mga totoong limitasyon at nagbabagong kagustuhan ng user.

halimbawa ng code

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

Para sa mas komprehensibong pagpaplano, tingnan ang Magnetic One

para sa paglutas ng mga komplikadong gawain.

## Buod

Sa artikulong ito, tiningnan natin ang isang halimbawa kung paano tayo makakalikha ng isang planner na maaaring dynamic na pumili ng mga available na agent na naitakda. Ang output ng Planner ay naghahati ng mga gawain at nagtatalaga ng mga agent upang maisagawa ang mga ito. Ipinapalagay na ang mga agent ay may access sa mga function/tool na kinakailangan upang maisagawa ang gawain. Bukod sa mga agent, maaari kang magdagdag ng iba pang mga pattern tulad ng reflection, summarizer, at round robin chat upang higit pang i-customize.

## Karagdagang Mga Mapagkukunan

* AutoGen Magnetic One - Isang Generalist multi-agent system para sa paglutas ng mga komplikadong gawain at nakamit ang kahanga-hangang resulta sa maraming mahihirap na agentic benchmarks. Sanggunian:

. Sa implementasyong ito, ang orchestrator ay lumilikha ng task-specific na plano at nagtatalaga ng mga gawain sa mga available na agent. Bukod sa pagpaplano, gumagamit din ang orchestrator ng mekanismo sa pagsubaybay upang bantayan ang progreso ng gawain at muling magplano kung kinakailangan.

## Nakaraang Aralin

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Susunod na Aralin

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.