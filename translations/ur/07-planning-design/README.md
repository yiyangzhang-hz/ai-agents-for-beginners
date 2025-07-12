<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:36:42+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ur"
}
-->
کے لیے ایک فوری جائزہ۔

مندرجہ ذیل پائتھن کوڈ ایک سادہ پلاننگ ایجنٹ کی مثال پیش کرتا ہے جو ایک مقصد کو ذیلی کاموں میں تقسیم کرتا ہے اور ایک منظم منصوبہ تیار کرتا ہے:

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

### ملٹی ایجنٹ آرکسٹریشن کے ساتھ پلاننگ ایجنٹ

اس مثال میں، ایک سیمانٹک روٹر ایجنٹ صارف کی درخواست وصول کرتا ہے (مثلاً "مجھے اپنی سفر کے لیے ہوٹل کا منصوبہ چاہیے۔")۔

پلانر پھر:

* ہوٹل پلان وصول کرتا ہے: پلانر صارف کا پیغام لیتا ہے اور سسٹم پرامپٹ کی بنیاد پر (جس میں دستیاب ایجنٹس کی تفصیلات شامل ہوتی ہیں) ایک منظم سفر کا منصوبہ تیار کرتا ہے۔
* ایجنٹس اور ان کے ٹولز کی فہرست بناتا ہے: ایجنٹ رجسٹری میں ایجنٹس کی فہرست ہوتی ہے (مثلاً فلائٹ، ہوٹل، کار کرایہ، اور سرگرمیاں) اور وہ فنکشنز یا ٹولز جو وہ فراہم کرتے ہیں۔
* منصوبہ متعلقہ ایجنٹس کو بھیجتا ہے: ذیلی کاموں کی تعداد کے مطابق، پلانر پیغام کو براہ راست مخصوص ایجنٹ کو بھیجتا ہے (اگر صرف ایک کام ہو) یا ملٹی ایجنٹ تعاون کے لیے گروپ چیٹ مینیجر کے ذریعے رابطہ کرتا ہے۔
* نتیجہ کا خلاصہ کرتا ہے: آخر میں، پلانر تیار کردہ منصوبے کا خلاصہ پیش کرتا ہے۔
مندرجہ ذیل پائتھن کوڈ ان مراحل کی وضاحت کرتا ہے:

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

مندرجہ ذیل کوڈ کا آؤٹ پٹ ہے اور آپ اس منظم آؤٹ پٹ کو `assigned_agent` کو بھیجنے اور صارف کو سفر کے منصوبے کا خلاصہ پیش کرنے کے لیے استعمال کر سکتے ہیں۔

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

پچھلے کوڈ کی مثال کے ساتھ ایک نوٹ بک یہاں دستیاب ہے [یہاں](../../../07-planning-design/07-autogen.ipynb)۔

### تکراری منصوبہ بندی

کچھ کاموں کے لیے بار بار بات چیت یا دوبارہ منصوبہ بندی کی ضرورت ہوتی ہے، جہاں ایک ذیلی کام کا نتیجہ اگلے پر اثر انداز ہوتا ہے۔ مثال کے طور پر، اگر ایجنٹ فلائٹ بکنگ کے دوران غیر متوقع ڈیٹا فارمیٹ دریافت کرتا ہے، تو اسے ہوٹل کی بکنگ سے پہلے اپنی حکمت عملی کو ایڈجسٹ کرنا پڑ سکتا ہے۔

مزید برآں، صارف کی رائے (مثلاً کوئی انسان جو پہلے فلائٹ کو ترجیح دیتا ہے) جزوی دوبارہ منصوبہ بندی کا سبب بن سکتی ہے۔ یہ متحرک، تکراری طریقہ کار یقینی بناتا ہے کہ آخری حل حقیقی دنیا کی پابندیوں اور بدلتی ہوئی صارف کی ترجیحات کے مطابق ہو۔

مثال کے طور پر کوڈ

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

مزید جامع منصوبہ بندی کے لیے Magnetic One دیکھیں۔

## خلاصہ

اس مضمون میں ہم نے ایک ایسی مثال دیکھی ہے جس میں ہم ایک ایسا پلانر بنا سکتے ہیں جو دستیاب ایجنٹس کو متحرک طور پر منتخب کرتا ہے۔ پلانر کا آؤٹ پٹ کاموں کو تقسیم کرتا ہے اور ایجنٹس کو تفویض کرتا ہے تاکہ وہ انجام دے سکیں۔ فرض کیا جاتا ہے کہ ایجنٹس کے پاس وہ فنکشنز/ٹولز موجود ہیں جو کام انجام دینے کے لیے ضروری ہیں۔ ایجنٹس کے علاوہ، آپ دیگر پیٹرنز جیسے reflection، summarizer، اور round robin chat بھی شامل کر سکتے ہیں تاکہ مزید تخصیص کی جا سکے۔

## اضافی وسائل

* AutoGen Magnetic One - ایک جنرلسٹ ملٹی ایجنٹ سسٹم جو پیچیدہ کاموں کو حل کرنے کے لیے ہے اور متعدد چیلنجنگ ایجنٹک بینچ مارکس پر شاندار نتائج حاصل کر چکا ہے۔ حوالہ:

۔ اس عمل میں آرکسٹریٹر مخصوص کاموں کا منصوبہ بناتا ہے اور ان کاموں کو دستیاب ایجنٹس کو تفویض کرتا ہے۔ منصوبہ بندی کے علاوہ، آرکسٹریٹر ایک ٹریکنگ میکانزم بھی استعمال کرتا ہے تاکہ کام کی پیش رفت کی نگرانی کی جا سکے اور ضرورت پڑنے پر دوبارہ منصوبہ بندی کی جا سکے۔

## پچھلا سبق

[قابل اعتماد AI ایجنٹس کی تعمیر](../06-building-trustworthy-agents/README.md)

## اگلا سبق

[ملٹی ایجنٹ ڈیزائن پیٹرن](../08-multi-agent/README.md)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔