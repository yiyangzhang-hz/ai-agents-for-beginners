<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:44:07+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "vi"
}
-->
cho một cái nhìn tổng quan nhanh.

Đoạn mã Python dưới đây minh họa một agent lập kế hoạch đơn giản phân tách một mục tiêu thành các nhiệm vụ con và tạo ra một kế hoạch có cấu trúc:

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

### Agent Lập Kế Hoạch với Điều Phối Đa Agent

Trong ví dụ này, một Semantic Router Agent nhận yêu cầu từ người dùng (ví dụ: "Tôi cần một kế hoạch khách sạn cho chuyến đi của mình.").

Người lập kế hoạch sau đó:

* Nhận Kế Hoạch Khách Sạn: Người lập kế hoạch lấy tin nhắn của người dùng và, dựa trên một lời nhắc hệ thống (bao gồm thông tin các agent có sẵn), tạo ra một kế hoạch du lịch có cấu trúc.
* Liệt Kê Các Agent và Công Cụ Của Họ: Đăng ký agent giữ danh sách các agent (ví dụ, cho vé máy bay, khách sạn, thuê xe và hoạt động) cùng với các chức năng hoặc công cụ mà họ cung cấp.
* Chuyển Kế Hoạch Đến Các Agent Tương Ứng: Tùy thuộc vào số lượng nhiệm vụ con, người lập kế hoạch sẽ gửi tin nhắn trực tiếp đến một agent chuyên trách (trong trường hợp nhiệm vụ đơn lẻ) hoặc điều phối qua một quản lý nhóm chat để hợp tác đa agent.
* Tóm Tắt Kết Quả: Cuối cùng, người lập kế hoạch tóm tắt kế hoạch đã tạo để làm rõ.
Đoạn mã Python dưới đây minh họa các bước này:

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

Phần tiếp theo là kết quả từ đoạn mã trên và bạn có thể sử dụng kết quả có cấu trúc này để chuyển đến `assigned_agent` và tóm tắt kế hoạch du lịch cho người dùng cuối.

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

Một notebook ví dụ với đoạn mã trên có sẵn [tại đây](../../../07-planning-design/07-autogen.ipynb).

### Lập Kế Hoạch Lặp Đi Lặp Lại

Một số nhiệm vụ yêu cầu sự trao đổi qua lại hoặc lập kế hoạch lại, trong đó kết quả của một nhiệm vụ con ảnh hưởng đến nhiệm vụ tiếp theo. Ví dụ, nếu agent phát hiện định dạng dữ liệu không mong đợi khi đặt vé máy bay, nó có thể cần điều chỉnh chiến lược trước khi tiếp tục đặt khách sạn.

Ngoài ra, phản hồi từ người dùng (ví dụ: một người dùng quyết định họ muốn chuyến bay sớm hơn) có thể kích hoạt việc lập kế hoạch lại một phần. Cách tiếp cận động và lặp đi lặp lại này đảm bảo giải pháp cuối cùng phù hợp với các ràng buộc thực tế và sở thích thay đổi của người dùng.

ví dụ mã

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

Để lập kế hoạch toàn diện hơn, hãy tham khảo Magnetic One

cho việc giải quyết các nhiệm vụ phức tạp.

## Tóm Tắt

Trong bài viết này, chúng ta đã xem xét một ví dụ về cách tạo ra một người lập kế hoạch có thể chọn động các agent có sẵn được định nghĩa. Kết quả của người lập kế hoạch phân tách các nhiệm vụ và phân công các agent để họ có thể thực hiện. Giả định rằng các agent có quyền truy cập vào các chức năng/công cụ cần thiết để thực hiện nhiệm vụ. Ngoài các agent, bạn có thể bao gồm các mẫu khác như phản chiếu, tóm tắt và chat vòng tròn để tùy chỉnh thêm.

## Tài Nguyên Bổ Sung

* AutoGen Magnetic One - Một hệ thống đa agent tổng quát để giải quyết các nhiệm vụ phức tạp và đã đạt được kết quả ấn tượng trên nhiều bài kiểm tra agentic thách thức. Tham khảo:

. Trong triển khai này, người điều phối tạo kế hoạch cụ thể cho từng nhiệm vụ và phân công các nhiệm vụ này cho các agent có sẵn. Ngoài việc lập kế hoạch, người điều phối còn sử dụng cơ chế theo dõi để giám sát tiến độ nhiệm vụ và lập kế hoạch lại khi cần thiết.

## Bài Học Trước

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Bài Học Tiếp Theo

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.