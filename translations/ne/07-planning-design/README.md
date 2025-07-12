<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:39:22+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ne"
}
-->
छिटो अवलोकनका लागि।

तलको Python कोडले एउटा साधारण योजना एजेन्टले लक्ष्यलाई उपकार्यहरूमा विभाजन गरी संरचित योजना बनाउने तरिका देखाउँछ:

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

### बहु-एजेन्ट समन्वय सहित योजना एजेन्ट

यस उदाहरणमा, Semantic Router Agent ले प्रयोगकर्ताको अनुरोध (जस्तै, "मेरो यात्राको लागि होटल योजना चाहिन्छ।") प्राप्त गर्छ।

योजनाकारले त्यसपछि:

* होटल योजना प्राप्त गर्छ: योजनाकारले प्रयोगकर्ताको सन्देश लिन्छ र प्रणाली प्रॉम्प्ट (उपलब्ध एजेन्ट विवरण सहित) को आधारमा संरचित यात्रा योजना बनाउँछ।
* एजेन्टहरू र तिनीहरूको उपकरणहरूको सूची बनाउँछ: एजेन्ट रजिस्ट्रीमा एजेन्टहरूको सूची हुन्छ (जस्तै, उडान, होटल, कार भाडामा लिने, र गतिविधिहरूका लागि) र तिनीहरूले प्रदान गर्ने कार्यहरू वा उपकरणहरू।
* योजना सम्बन्धित एजेन्टहरूमा पठाउँछ: उपकार्यहरूको सङ्ख्याको आधारमा, योजनाकारले सन्देशलाई सिधै समर्पित एजेन्टलाई पठाउँछ (एकल कार्यका लागि) वा बहु-एजेन्ट सहकार्यका लागि समूह च्याट प्रबन्धकमार्फत समन्वय गर्छ।
* नतिजा सारांश गर्छ: अन्तमा, योजनाकारले स्पष्टताको लागि बनाइएको योजनाको सारांश दिन्छ।
तलको Python कोड नमूनाले यी चरणहरू देखाउँछ:

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

अघिल्लो कोडबाट प्राप्त आउटपुट तल छ र तपाईं यस संरचित आउटपुटलाई `assigned_agent` मा पठाएर अन्तिम प्रयोगकर्तालाई यात्रा योजना सारांश गर्न प्रयोग गर्न सक्नुहुन्छ।

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

अघिल्लो कोड नमूनासहितको उदाहरण नोटबुक [यहाँ](../../../07-planning-design/07-autogen.ipynb) उपलब्ध छ।

### पुनरावृत्त योजना

केही कार्यहरूमा दोहोरो संवाद वा पुनः योजना आवश्यक पर्छ, जहाँ एउटा उपकार्यको नतिजाले अर्को उपकार्यलाई प्रभाव पार्छ। उदाहरणका लागि, यदि एजेन्टले उडान बुक गर्दा अप्रत्याशित डेटा ढाँचा पत्ता लगाउँछ भने, यसले होटल बुकिङ अघि आफ्नो रणनीति समायोजन गर्नुपर्ने हुन सक्छ।

थप रूपमा, प्रयोगकर्ताको प्रतिक्रिया (जस्तै, मान्छेले पहिलेको उडान रोज्न चाहन्छ) ले आंशिक पुनः योजना ट्रिगर गर्न सक्छ। यो गतिशील, पुनरावृत्त प्रक्रिया अन्तिम समाधानलाई वास्तविक विश्वका सिमाना र विकासशील प्रयोगकर्ता प्राथमिकतासँग मेल खाने सुनिश्चित गर्छ।

जस्तै कोड नमूना

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

अधिक व्यापक योजनाका लागि Magnetic One हेर्नुहोस्।

## सारांश

यस लेखमा हामीले कसरी उपलब्ध एजेन्टहरूलाई गतिशील रूपमा चयन गर्ने योजना बनाउने सकिन्छ भन्ने उदाहरण हेर्यौं। योजनाकारको आउटपुटले कार्यहरूलाई उपकार्यहरूमा विभाजन गरी एजेन्टहरूलाई कार्यहरू सुम्पन्छ ताकि तिनीहरू कार्यान्वयन गर्न सकून्। एजेन्टहरूले आवश्यक कार्यहरू गर्नका लागि आवश्यक फङ्सन/उपकरणहरू पहुँच गर्न सक्ने मानिन्छ। एजेन्टहरूका अतिरिक्त, तपाईं प्रतिबिम्ब, सारांशकर्ता, र राउन्ड रोबिन च्याट जस्ता अन्य ढाँचाहरू पनि समावेश गरेर थप अनुकूलन गर्न सक्नुहुन्छ।

## थप स्रोतहरू

* AutoGen Magnetic One - जटिल कार्यहरू समाधान गर्नका लागि एक सामान्य बहु-एजेन्ट प्रणाली हो र यसले धेरै चुनौतीपूर्ण एजेन्टिक मापनहरूमा प्रभावशाली परिणामहरू प्राप्त गरेको छ। सन्दर्भ:

यस कार्यान्वयनमा, समन्वयकर्ताले कार्य-विशिष्ट योजना बनाउँछ र ती कार्यहरू उपलब्ध एजेन्टहरूलाई सुम्पन्छ। योजनाबद्ध गर्ने बाहेक, समन्वयकर्ताले कार्यको प्रगति अनुगमन गर्न र आवश्यक परे पुनः योजना बनाउन ट्र्याकिङ मेकानिजम पनि प्रयोग गर्छ।

## अघिल्लो पाठ

[विश्वसनीय AI एजेन्टहरू निर्माण](../06-building-trustworthy-agents/README.md)

## अर्को पाठ

[बहु-एजेन्ट डिजाइन ढाँचा](../08-multi-agent/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।