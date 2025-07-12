<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:44:42+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "ms"
}
-->
untuk gambaran ringkas.

Petikan Python berikut menunjukkan agen perancangan mudah yang memecahkan matlamat kepada subtugas dan menghasilkan pelan berstruktur:

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

### Agen Perancangan dengan Orkestrasi Multi-Agen

Dalam contoh ini, Semantic Router Agent menerima permintaan pengguna (contohnya, "Saya perlukan pelan hotel untuk perjalanan saya.").

Perancang kemudian:

* Menerima Pelan Hotel: Perancang mengambil mesej pengguna dan, berdasarkan arahan sistem (termasuk butiran agen yang tersedia), menghasilkan pelan perjalanan berstruktur.
* Menyenaraikan Agen dan Alat Mereka: Daftar agen memegang senarai agen (contohnya untuk penerbangan, hotel, sewa kereta, dan aktiviti) bersama fungsi atau alat yang mereka tawarkan.
* Menghantar Pelan kepada Agen Berkaitan: Bergantung pada bilangan subtugas, perancang sama ada menghantar mesej terus kepada agen khusus (untuk senario tugas tunggal) atau mengkoordinasi melalui pengurus sembang kumpulan untuk kerjasama multi-agen.
* Merumuskan Hasil: Akhir sekali, perancang merumuskan pelan yang dihasilkan untuk kejelasan.
Kod Python berikut menggambarkan langkah-langkah ini:

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

Berikut adalah output dari kod sebelumnya dan anda boleh menggunakan output berstruktur ini untuk dihantar ke `assigned_agent` dan merumuskan pelan perjalanan kepada pengguna akhir.

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

Contoh notebook dengan kod sebelumnya boleh didapati [di sini](../../../07-planning-design/07-autogen.ipynb).

### Perancangan Iteratif

Sesetengah tugas memerlukan proses bolak-balik atau perancangan semula, di mana hasil satu subtugas mempengaruhi yang seterusnya. Contohnya, jika agen menemui format data yang tidak dijangka semasa menempah penerbangan, ia mungkin perlu menyesuaikan strateginya sebelum meneruskan tempahan hotel.

Selain itu, maklum balas pengguna (contohnya manusia memutuskan mereka lebih suka penerbangan lebih awal) boleh mencetuskan perancangan semula sebahagian. Pendekatan dinamik dan iteratif ini memastikan penyelesaian akhir selaras dengan kekangan dunia sebenar dan keutamaan pengguna yang berubah.

contoh kod

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

Untuk perancangan yang lebih menyeluruh, sila lihat Magnetic One

untuk menyelesaikan tugas kompleks.

## Ringkasan

Dalam artikel ini, kita telah melihat contoh bagaimana kita boleh mencipta perancang yang boleh memilih agen yang tersedia secara dinamik. Output Perancang memecahkan tugas dan menetapkan agen supaya ia boleh dilaksanakan. Diasumsikan agen mempunyai akses kepada fungsi/alat yang diperlukan untuk melaksanakan tugas. Selain agen, anda boleh memasukkan corak lain seperti refleksi, perumus, dan sembang round robin untuk penyesuaian lanjut.

## Sumber Tambahan

* AutoGen Magnetic One - Sistem multi-agen generalis untuk menyelesaikan tugas kompleks dan telah mencapai keputusan mengagumkan pada beberapa penanda aras agen yang mencabar. Rujukan:

. Dalam pelaksanaan ini, pengorkestra mencipta pelan khusus tugas dan mendelegasikan tugas ini kepada agen yang tersedia. Selain merancang, pengorkestra juga menggunakan mekanisme penjejakan untuk memantau kemajuan tugas dan merancang semula jika perlu.

## Pelajaran Sebelumnya

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

## Pelajaran Seterusnya

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.