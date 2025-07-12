<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:38:37+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "hi"
}
-->
तेज़ अवलोकन के लिए।

निम्नलिखित Python कोड एक सरल योजना एजेंट को दिखाता है जो एक लक्ष्य को उपकार्य में विभाजित करता है और एक संरचित योजना बनाता है:

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

### मल्टी-एजेंट समन्वय के साथ योजना एजेंट

इस उदाहरण में, एक सेमांटिक राउटर एजेंट उपयोगकर्ता का अनुरोध प्राप्त करता है (जैसे, "मुझे मेरी यात्रा के लिए होटल योजना चाहिए।")।

फिर योजनाकार:

* होटल योजना प्राप्त करता है: योजनाकार उपयोगकर्ता के संदेश को लेता है और सिस्टम प्रॉम्प्ट (जिसमें उपलब्ध एजेंट विवरण शामिल हैं) के आधार पर एक संरचित यात्रा योजना बनाता है।
* एजेंट और उनके टूल्स की सूची बनाता है: एजेंट रजिस्ट्री में एजेंटों की सूची होती है (जैसे, फ्लाइट, होटल, कार रेंटल, और गतिविधियों के लिए) साथ ही वे जो कार्य या टूल प्रदान करते हैं।
* योजना को संबंधित एजेंटों को भेजता है: उपकार्यों की संख्या के आधार पर, योजनाकार संदेश को सीधे एक समर्पित एजेंट को भेजता है (एकल कार्य परिदृश्यों के लिए) या मल्टी-एजेंट सहयोग के लिए समूह चैट प्रबंधक के माध्यम से समन्वय करता है।
* परिणाम का सारांश प्रस्तुत करता है: अंत में, योजनाकार स्पष्टता के लिए बनाई गई योजना का सारांश प्रस्तुत करता है।
निम्नलिखित Python कोड उदाहरण इन चरणों को दर्शाता है:

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

इसके बाद पिछले कोड का आउटपुट आता है और आप इस संरचित आउटपुट का उपयोग `assigned_agent` को रूट करने और अंतिम उपयोगकर्ता को यात्रा योजना का सारांश प्रस्तुत करने के लिए कर सकते हैं।

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

पिछले कोड उदाहरण के साथ एक नोटबुक [यहाँ](../../../07-planning-design/07-autogen.ipynb) उपलब्ध है।

### पुनरावृत्त योजना

कुछ कार्यों के लिए आगे-पीछे या पुनः योजना बनाना आवश्यक होता है, जहाँ एक उपकार्य का परिणाम अगले को प्रभावित करता है। उदाहरण के लिए, यदि एजेंट फ्लाइट बुकिंग के दौरान अप्रत्याशित डेटा फॉर्मेट पाता है, तो उसे होटल बुकिंग से पहले अपनी रणनीति को अनुकूलित करना पड़ सकता है।

इसके अलावा, उपयोगकर्ता की प्रतिक्रिया (जैसे, कोई व्यक्ति यह निर्णय लेता है कि वे पहले की फ्लाइट पसंद करते हैं) आंशिक पुनः योजना को ट्रिगर कर सकती है। यह गतिशील, पुनरावृत्त दृष्टिकोण सुनिश्चित करता है कि अंतिम समाधान वास्तविक दुनिया की सीमाओं और बदलती उपयोगकर्ता प्राथमिकताओं के अनुरूप हो।

उदाहरण कोड

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

ज्यादा व्यापक योजना के लिए Magnetic One देखें।

## जटिल कार्यों को हल करने के लिए।

## सारांश

इस लेख में हमने देखा कि कैसे हम एक ऐसा योजनाकार बना सकते हैं जो उपलब्ध एजेंटों को गतिशील रूप से चुन सके। योजनाकार का आउटपुट कार्यों को विभाजित करता है और एजेंटों को असाइन करता है ताकि वे निष्पादित हो सकें। यह माना जाता है कि एजेंटों के पास उन कार्यों को करने के लिए आवश्यक फ़ंक्शन/टूल्स तक पहुंच है। एजेंटों के अलावा, आप अन्य पैटर्न जैसे रिफ्लेक्शन, सारांशकर्ता, और राउंड रॉबिन चैट भी शामिल कर सकते हैं ताकि और अधिक अनुकूलन किया जा सके।

## अतिरिक्त संसाधन

* AutoGen Magnetic One - एक सामान्य मल्टी-एजेंट सिस्टम जो जटिल कार्यों को हल करता है और कई चुनौतीपूर्ण एजेंटिक बेंचमार्क पर प्रभावशाली परिणाम प्राप्त कर चुका है। संदर्भ:

. इस कार्यान्वयन में, ऑर्केस्ट्रेटर कार्य-विशिष्ट योजना बनाता है और इन कार्यों को उपलब्ध एजेंटों को सौंपता है। योजना बनाने के अलावा, ऑर्केस्ट्रेटर एक ट्रैकिंग तंत्र भी लागू करता है जो कार्य की प्रगति की निगरानी करता है और आवश्यकतानुसार पुनः योजना बनाता है।

## पिछला पाठ

[विश्वसनीय AI एजेंट बनाना](../06-building-trustworthy-agents/README.md)

## अगला पाठ

[मल्टी-एजेंट डिज़ाइन पैटर्न](../08-multi-agent/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।