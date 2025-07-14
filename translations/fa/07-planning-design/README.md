<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:36:22+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "fa"
}
-->
برای مرور سریع.

قطعه کد پایتون زیر یک عامل برنامه‌ریز ساده را نشان می‌دهد که یک هدف را به زیرکارها تقسیم می‌کند و یک برنامه ساختاریافته تولید می‌کند:

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

### عامل برنامه‌ریز با هماهنگی چندعاملی

در این مثال، یک عامل مسیریاب معنایی درخواست کاربر را دریافت می‌کند (مثلاً «من به یک برنامه هتل برای سفرم نیاز دارم.»).

سپس برنامه‌ریز:

* دریافت برنامه هتل: برنامه‌ریز پیام کاربر را گرفته و بر اساس یک پرامپت سیستمی (شامل جزئیات عوامل موجود)، یک برنامه سفر ساختاریافته تولید می‌کند.
* فهرست عوامل و ابزارهای آن‌ها: ثبت‌نام عوامل شامل فهرستی از عوامل (مثلاً برای پرواز، هتل، اجاره خودرو و فعالیت‌ها) به همراه توابع یا ابزارهایی است که ارائه می‌دهند.
* ارسال برنامه به عوامل مربوطه: بسته به تعداد زیرکارها، برنامه‌ریز یا پیام را مستقیماً به یک عامل اختصاصی می‌فرستد (برای سناریوهای تک‌کار) یا از طریق مدیر چت گروهی برای همکاری چندعاملی هماهنگ می‌کند.
* خلاصه‌سازی نتیجه: در نهایت، برنامه‌ریز برنامه تولید شده را برای وضوح خلاصه می‌کند.
نمونه کد پایتون زیر این مراحل را نشان می‌دهد:

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

خروجی کد قبلی در ادامه آمده است و شما می‌توانید از این خروجی ساختاریافته برای ارسال به `assigned_agent` و خلاصه‌سازی برنامه سفر برای کاربر نهایی استفاده کنید.

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

یک دفترچه نمونه با کد قبلی در این [لینک](../../../07-planning-design/07-autogen.ipynb) موجود است.

### برنامه‌ریزی تکراری

برخی وظایف نیاز به رفت و برگشت یا برنامه‌ریزی مجدد دارند، جایی که نتیجه یک زیرکار بر زیرکار بعدی تأثیر می‌گذارد. برای مثال، اگر عامل هنگام رزرو پروازها با فرمت داده غیرمنتظره‌ای مواجه شود، ممکن است نیاز باشد استراتژی خود را قبل از ادامه به رزرو هتل تغییر دهد.

علاوه بر این، بازخورد کاربر (مثلاً تصمیم یک انسان برای پرواز زودتر) می‌تواند باعث برنامه‌ریزی مجدد جزئی شود. این رویکرد پویا و تکراری تضمین می‌کند که راه‌حل نهایی با محدودیت‌های دنیای واقعی و ترجیحات در حال تغییر کاربر هماهنگ باشد.

مثال کد

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

برای برنامه‌ریزی جامع‌تر، Magnetic One را بررسی کنید.

برای حل وظایف پیچیده.

## خلاصه

در این مقاله نمونه‌ای از چگونگی ایجاد یک برنامه‌ریز که بتواند به صورت پویا عوامل موجود را انتخاب کند، بررسی کردیم. خروجی برنامه‌ریز وظایف را تجزیه کرده و عوامل را اختصاص می‌دهد تا بتوانند اجرا شوند. فرض بر این است که عوامل به توابع/ابزارهای لازم برای انجام وظیفه دسترسی دارند. علاوه بر عوامل، می‌توانید الگوهای دیگری مانند بازتاب، خلاصه‌ساز و چت راند رابین را برای سفارشی‌سازی بیشتر اضافه کنید.

## منابع اضافی

* AutoGen Magnetic One - یک سیستم چندعاملی عمومی برای حل وظایف پیچیده که نتایج چشمگیری در چندین معیار چالشی عامل‌محور کسب کرده است. مرجع:

. در این پیاده‌سازی، هماهنگ‌کننده برنامه‌های خاص وظیفه را ایجاد کرده و این وظایف را به عوامل موجود واگذار می‌کند. علاوه بر برنامه‌ریزی، هماهنگ‌کننده مکانیزم پیگیری برای نظارت بر پیشرفت وظیفه و برنامه‌ریزی مجدد در صورت نیاز به کار می‌گیرد.

## درس قبلی

[ساخت عوامل هوش مصنوعی قابل اعتماد](../06-building-trustworthy-agents/README.md)

## درس بعدی

[الگوی طراحی چندعاملی](../08-multi-agent/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.