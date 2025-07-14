<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:48:07+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "my"
}
-->
အောက်ပါ Python ကုတ်နမူနာသည် ရည်မှန်းချက်တစ်ခုကို အလုပ်ခွဲခြားပြီး ဖွဲ့စည်းထားသော စီမံကိန်းတစ်ခုကို ဖန်တီးနေသော ရိုးရှင်းသော စီမံကိန်းအေးဂျင့်ကို ပြသသည်-

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

### Multi-Agent စီမံခန့်ခွဲမှုဖြင့် စီမံကိန်းအေးဂျင့်

ဤနမူနာတွင် Semantic Router Agent သည် အသုံးပြုသူ၏ တောင်းဆိုချက် (ဥပမာ- "ကျွန်တော့်ခရီးစဉ်အတွက် ဟိုတယ်အစီအစဉ်လိုပါတယ်။") ကို လက်ခံသည်။

စီမံကိန်းရေးဆွဲသူကတော့-

* ဟိုတယ်အစီအစဉ် လက်ခံခြင်း- အသုံးပြုသူ၏ စာကို လက်ခံပြီး၊ စနစ် prompt (ရရှိနိုင်သော အေးဂျင့်အသေးစိတ်အပါအဝင်) အပေါ် မူတည်၍ ဖွဲ့စည်းထားသော ခရီးစဉ်အစီအစဉ်ကို ဖန်တီးသည်။
* အေးဂျင့်များနှင့် ၎င်းတို့၏ ကိရိယာများစာရင်းပြုစုခြင်း- အေးဂျင့်စာရင်းတွင် လေယာဉ်၊ ဟိုတယ်၊ ကားငှားခြင်းနှင့် လှုပ်ရှားမှုများအတွက် အေးဂျင့်များနှင့် ၎င်းတို့ပေးသော လုပ်ဆောင်ချက်များ သို့မဟုတ် ကိရိယာများ ပါဝင်သည်။
* အစီအစဉ်ကို သက်ဆိုင်ရာ အေးဂျင့်များသို့ ပို့ခြင်း- အလုပ်ခွဲအရေအတွက်ပေါ်မူတည်၍ စီမံကိန်းရေးဆွဲသူသည် တစ်ခုတည်းသော အလုပ်အတွက် တစ်ဦးချင်း အေးဂျင့်သို့ တိုက်ရိုက်ပို့ခြင်း သို့မဟုတ် multi-agent ပူးပေါင်းဆောင်ရွက်မှုအတွက် အုပ်စုစကားပြောမန်နေဂျာမှတဆင့် ညှိနှိုင်းပေးသည်။
* ရလဒ်ကို အကျဉ်းချုပ်တင်ပြခြင်း- နောက်ဆုံးတွင် စီမံကိန်းရေးဆွဲသူသည် ဖန်တီးထားသော အစီအစဉ်ကို ရှင်းလင်းစွာ အကျဉ်းချုပ်တင်ပြသည်။
အောက်ပါ Python ကုတ်နမူနာသည် ဤအဆင့်များကို ဖော်ပြထားသည်-

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

အောက်တွင် ယခင်ကုတ်မှ ထွက်ရှိလာသော အချက်အလက်ဖြစ်ပြီး ၎င်းကို `assigned_agent` သို့ လမ်းညွှန်ရန်နှင့် ခရီးစဉ်အစီအစဉ်ကို အသုံးပြုသူအတွက် အကျဉ်းချုပ်တင်ပြရန် အသုံးပြုနိုင်သည်။

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

ယခင်ကုတ်နမူနာပါသော နမူနာ notebook ကို [ဒီမှာ](../../../07-planning-design/07-autogen.ipynb) ရနိုင်သည်။

### အဆက်မပြတ် စီမံကိန်းရေးဆွဲခြင်း

အချို့အလုပ်များတွင် တစ်ခုချင်းစီ၏ ရလဒ်သည် နောက်တစ်ခုကို သက်ရောက်မှုရှိသောကြောင့် ပြန်လည်စီမံခြင်း သို့မဟုတ် ပြန်လည်စီမံရေးဆွဲခြင်း လိုအပ်သည်။ ဥပမာ- အေးဂျင့်သည် လေယာဉ်ဘွတ်ကင်လုပ်စဉ်တွင် မမျှော်လင့်ထားသော ဒေတာပုံစံတစ်ခုကို တွေ့ရှိပါက ဟိုတယ်ဘွတ်ကင်လုပ်ခြင်းမပြုမီ မိမိ၏ မဟာဗျူဟာကို ပြင်ဆင်ရန် လိုအပ်နိုင်သည်။

ထို့အပြင် အသုံးပြုသူတုံ့ပြန်ချက် (ဥပမာ- လူတစ်ဦးသည် ပိုမိုမနက်ပိုင်း လေယာဉ်ကို ကြိုက်နှစ်သက်သည်ဟု ဆုံးဖြတ်ခြင်း) သည် အပိုင်းအစ ပြန်လည်စီမံရေးဆွဲမှုကို ဖြစ်ပေါ်စေနိုင်သည်။ ဤအမျိုးအစား အဆက်မပြတ်၊ ပြောင်းလဲမှုရှိသော နည်းလမ်းသည် နောက်ဆုံးဖြေရှင်းချက်သည် အမှန်တကယ် ဖြစ်ပေါ်နေသော ကန့်သတ်ချက်များနှင့် အသုံးပြုသူ၏ စိတ်ကြိုက်မှုများနှင့် ကိုက်ညီစေရန် အာမခံပေးသည်။

ဥပမာ ကုတ်

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

ပိုမိုကျယ်ပြန့်သော စီမံကိန်းရေးဆွဲမှုအတွက် Magnetic One ကို စမ်းသပ်ကြည့်ပါ။

## အနှစ်ချုပ်

ဤဆောင်းပါးတွင် ကျွန်ုပ်တို့သည် ရရှိနိုင်သော အေးဂျင့်များကို အလိုအလျောက် ရွေးချယ်နိုင်သော စီမံကိန်းရေးဆွဲသူတစ်ဦးကို ဘယ်လို ဖန်တီးနိုင်သည်ကို ဥပမာဖြင့် ကြည့်ရှုခဲ့သည်။ စီမံကိန်းရေးဆွဲသူ၏ ထွက်ရှိမှုသည် အလုပ်ခွဲများကို ခွဲခြားပြီး အေးဂျင့်များအား တာဝန်ပေးသည်၊ ထို့ကြောင့် ၎င်းတို့ကို အကောင်အထည်ဖော်နိုင်သည်။ အေးဂျင့်များတွင် အလုပ်ဆောင်ရန် လိုအပ်သော လုပ်ဆောင်ချက်များ/ကိရိယာများကို အသုံးပြုခွင့်ရှိသည်ဟု သတ်မှတ်ထားသည်။ အေးဂျင့်များအပြင် reflection, summarizer, နှင့် round robin chat ကဲ့သို့သော နမူနာများကိုလည်း ထည့်သွင်း၍ ပိုမိုစိတ်ကြိုက်ပြင်ဆင်နိုင်သည်။

## အပိုဆောင်း အရင်းအမြစ်များ

* AutoGen Magnetic One - စိန်ခေါ်မှုများစွာရှိသော agentic benchmark များတွင် ထူးချွန်သောရလဒ်များရရှိထားပြီး စုံလင်သော multi-agent စနစ်တစ်ခုဖြစ်သည်။ ကိုးကားချက်-

. ဤအကောင်အထည်ဖော်မှုတွင် orchestrator သည် အလုပ်အတွက် သီးသန့် စီမံကိန်းတစ်ခု ဖန်တီးပြီး ရရှိနိုင်သော အေးဂျင့်များသို့ အလုပ်များကို တာဝန်ပေးသည်။ စီမံကိန်းရေးဆွဲခြင်းအပြင် orchestrator သည် အလုပ်တိုးတက်မှုကို စောင့်ကြည့်ရန် နှင့် လိုအပ်သလို ပြန်လည်စီမံရန် စနစ်တစ်ခုကိုလည်း အသုံးပြုသည်။

## ယခင်သင်ခန်းစာ

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## နောက်တစ်ခု သင်ခန်းစာ

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။