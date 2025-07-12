<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:43:14+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "fi"
}
-->
Katso tästä nopea yleiskatsaus.

Seuraava Python-koodinpätkä havainnollistaa yksinkertaista suunnittelijaa, joka jakaa tavoitteen alitehtäviin ja luo rakenteellisen suunnitelman:

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

### Suunnittelija moni-agenttiorkestraatiolla

Tässä esimerkissä Semantic Router Agent vastaanottaa käyttäjän pyynnön (esim. "Tarvitsen hotellisuunnitelman matkalleni.").

Suunnittelija sitten:

* Vastaanottaa hotellisuunnitelman: Suunnittelija ottaa käyttäjän viestin ja järjestelmäkehotteen (joka sisältää käytettävissä olevien agenttien tiedot) perusteella luo rakenteellisen matkasuunnitelman.
* Listaa agentit ja niiden työkalut: Agenttirekisterissä on lista agenteista (esim. lento, hotelli, autonvuokraus ja aktiviteetit) sekä niiden tarjoamista toiminnoista tai työkaluista.
* Reitittää suunnitelman asianmukaisille agenteille: Alitehtävien lukumäärästä riippuen suunnittelija joko lähettää viestin suoraan omistautuneelle agentille (yksittäistehtävissä) tai koordinoi ryhmäkeskustelun hallinnan kautta moni-agenttiyhteistyössä.
* Tiivistää lopputuloksen: Lopuksi suunnittelija tiivistää luodun suunnitelman selkeyden vuoksi.
Seuraava Python-koodiesimerkki havainnollistaa nämä vaiheet:

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

Alla on edellisen koodin tuotos, ja voit käyttää tätä rakenteellista tulosta reitittääksesi sen `assigned_agent` -kenttään ja tiivistääksesi matkasuunnitelman loppukäyttäjälle.

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

Esimerkkimuistikirja edellisellä koodilla on saatavilla [tästä](../../../07-planning-design/07-autogen.ipynb).

### Iteratiivinen suunnittelu

Jotkin tehtävät vaativat edestakaista toimintaa tai uudelleensuunnittelua, jossa yhden alitehtävän tulos vaikuttaa seuraavaan. Esimerkiksi, jos agentti kohtaa odottamattoman tietomuodon lentojen varaamisen yhteydessä, sen täytyy ehkä mukauttaa strategiaansa ennen hotellivarauksia.

Lisäksi käyttäjäpalaute (esim. ihminen päättää haluavansa aikaisemman lennon) voi laukaista osittaisen uudelleensuunnittelun. Tämä dynaaminen, iteratiivinen lähestymistapa varmistaa, että lopullinen ratkaisu vastaa todellisia rajoitteita ja käyttäjän muuttuvia mieltymyksiä.

esim. koodia

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

Laajempaan suunnitteluun kannattaa tutustua Magnetic Oneen

## Yhteenveto

Tässä artikkelissa olemme tarkastelleet esimerkkiä siitä, miten voimme luoda suunnittelijan, joka voi dynaamisesti valita määritellyt käytettävissä olevat agentit. Suunnittelijan tuotos jakaa tehtävät ja osoittaa agentit, jotta ne voidaan suorittaa. Oletetaan, että agenteilla on pääsy tehtävän suorittamiseen tarvittaviin toimintoihin/työkaluihin. Agenttien lisäksi voit sisällyttää muita malleja, kuten reflektiota, tiivistäjää ja pyöröviestintää, mukautuksen lisäämiseksi.

## Lisäresurssit

* AutoGen Magnetic One - Yleistarkoituksellinen moni-agenttijärjestelmä monimutkaisten tehtävien ratkaisuun, joka on saavuttanut vaikuttavia tuloksia useilla haastavilla agenttiperusteisilla vertailuilla. Viite:

. Tässä toteutuksessa orkestroija luo tehtäväkohtaisen suunnitelman ja delegoi nämä tehtävät käytettävissä oleville agenteille. Suunnittelun lisäksi orkestroija käyttää myös seurantamekanismia tehtävän etenemisen valvomiseksi ja tarvittaessa uudelleensuunnittelee.

## Edellinen oppitunti

[Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)

## Seuraava oppitunti

[Moni-agenttisuunnittelumalli](../08-multi-agent/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.