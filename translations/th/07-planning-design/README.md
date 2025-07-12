<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:41:53+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "th"
}
-->
สำหรับภาพรวมอย่างรวดเร็ว

ตัวอย่างโค้ด Python ด้านล่างแสดงให้เห็นถึงตัวแทนวางแผนที่แยกเป้าหมายออกเป็นงานย่อยและสร้างแผนที่มีโครงสร้าง:

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

### ตัวแทนวางแผนพร้อมการประสานงานหลายตัวแทน

ในตัวอย่างนี้ ตัวแทน Semantic Router จะรับคำขอจากผู้ใช้ (เช่น "ฉันต้องการแผนที่พักสำหรับทริปของฉัน")

จากนั้นตัววางแผนจะ:

* รับแผนที่พัก: ตัววางแผนจะรับข้อความจากผู้ใช้และอิงจากคำสั่งระบบ (รวมถึงรายละเอียดของตัวแทนที่มีอยู่) เพื่อสร้างแผนการเดินทางที่มีโครงสร้าง
* แสดงรายการตัวแทนและเครื่องมือของพวกเขา: รายการตัวแทนจะเก็บรายชื่อตัวแทน (เช่น สำหรับเที่ยวบิน ที่พัก รถเช่า และกิจกรรม) พร้อมกับฟังก์ชันหรือเครื่องมือที่พวกเขามี
* ส่งแผนไปยังตัวแทนที่เกี่ยวข้อง: ขึ้นอยู่กับจำนวนงานย่อย ตัววางแผนจะส่งข้อความโดยตรงไปยังตัวแทนเฉพาะ (สำหรับกรณีงานเดียว) หรือประสานงานผ่านผู้จัดการแชทกลุ่มสำหรับการทำงานร่วมกันของหลายตัวแทน
* สรุปผลลัพธ์: สุดท้าย ตัววางแผนจะสรุปแผนที่สร้างขึ้นเพื่อความชัดเจน
ตัวอย่างโค้ด Python ด้านล่างแสดงขั้นตอนเหล่านี้:

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

ต่อไปนี้เป็นผลลัพธ์จากโค้ดก่อนหน้า และคุณสามารถใช้ผลลัพธ์ที่มีโครงสร้างนี้เพื่อส่งต่อไปยัง `assigned_agent` และสรุปแผนการเดินทางให้กับผู้ใช้ปลายทาง

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

ตัวอย่างโน้ตบุ๊กที่มีโค้ดตัวอย่างก่อนหน้านี้สามารถดูได้ที่ [นี่](../../../07-planning-design/07-autogen.ipynb)

### การวางแผนแบบวนซ้ำ

บางงานต้องการการทำงานแบบไป-กลับหรือการวางแผนใหม่ โดยที่ผลลัพธ์ของงานย่อยหนึ่งมีผลต่อขั้นตอนถัดไป เช่น หากตัวแทนพบรูปแบบข้อมูลที่ไม่คาดคิดขณะจองเที่ยวบิน อาจจำเป็นต้องปรับกลยุทธ์ก่อนดำเนินการจองที่พัก

นอกจากนี้ ข้อเสนอแนะจากผู้ใช้ (เช่น ผู้ใช้ตัดสินใจว่าต้องการเที่ยวบินที่ออกก่อนเวลา) สามารถกระตุ้นให้มีการวางแผนใหม่บางส่วน วิธีการแบบไดนามิกและวนซ้ำนี้ช่วยให้แน่ใจว่าวิธีแก้ปัญหาสุดท้ายสอดคล้องกับข้อจำกัดในโลกจริงและความชอบที่เปลี่ยนแปลงของผู้ใช้

เช่น ตัวอย่างโค้ด

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

สำหรับการวางแผนที่ครอบคลุมมากขึ้น ลองดู Magnetic One

สำหรับการแก้ไขงานที่ซับซ้อน

## สรุป

ในบทความนี้เราได้ดูตัวอย่างวิธีการสร้างตัววางแผนที่สามารถเลือกตัวแทนที่มีอยู่ได้อย่างไดนามิก ผลลัพธ์ของตัววางแผนจะแยกงานออกเป็นส่วนย่อยและมอบหมายตัวแทนเพื่อให้สามารถดำเนินการได้ โดยสมมติว่าตัวแทนเหล่านั้นสามารถเข้าถึงฟังก์ชัน/เครื่องมือที่จำเป็นสำหรับการทำงานได้ นอกจากตัวแทนแล้ว คุณยังสามารถรวมรูปแบบอื่นๆ เช่น การสะท้อนความคิด การสรุป และการแชทแบบวนรอบ เพื่อปรับแต่งเพิ่มเติม

## แหล่งข้อมูลเพิ่มเติม

* AutoGen Magnetic One - ระบบตัวแทนหลายตัวแบบทั่วไปสำหรับแก้ไขงานที่ซับซ้อนและได้ผลลัพธ์ที่น่าประทับใจในหลายเกณฑ์ท้าทายของตัวแทน อ้างอิง:

. ในการใช้งานนี้ ตัวประสานงานจะสร้างแผนงานเฉพาะและมอบหมายงานเหล่านี้ให้กับตัวแทนที่มีอยู่ นอกจากการวางแผนแล้ว ตัวประสานงานยังใช้กลไกติดตามเพื่อตรวจสอบความคืบหน้าของงานและวางแผนใหม่ตามความจำเป็น

## บทเรียนก่อนหน้า

[การสร้างตัวแทน AI ที่น่าเชื่อถือ](../06-building-trustworthy-agents/README.md)

## บทเรียนถัดไป

[รูปแบบการออกแบบหลายตัวแทน](../08-multi-agent/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้