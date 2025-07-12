<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:41:10+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "tr"
}
-->
hızlı bir genel bakış için.

Aşağıdaki Python kodu, bir hedefi alt görevlere ayıran ve yapılandırılmış bir plan oluşturan basit bir planlama ajanını göstermektedir:

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

### Çoklu Ajan Orkestrasyonlu Planlama Ajanı

Bu örnekte, bir Semantik Yönlendirici Ajan kullanıcı isteği alır (örneğin, "Seyahatim için bir otel planına ihtiyacım var.").

Planlayıcı şu adımları izler:

* Otel Planını Alır: Planlayıcı, kullanıcının mesajını alır ve sistem istemi (mevcut ajan detayları dahil) temelinde yapılandırılmış bir seyahat planı oluşturur.
* Ajanları ve Araçlarını Listeler: Ajan kaydı, işlevleri veya sundukları araçlarla birlikte ajanların (örneğin uçuş, otel, araç kiralama ve aktiviteler için) bir listesini tutar.
* Planı İlgili Ajanlara Yönlendirir: Alt görev sayısına bağlı olarak, planlayıcı mesajı doğrudan ilgili ajana (tek görev senaryoları için) gönderir veya çoklu ajan işbirliği için bir grup sohbet yöneticisi aracılığıyla koordine eder.
* Sonucu Özetler: Son olarak, planlayıcı oluşturulan planı açıklık için özetler.
Aşağıdaki Python kod örneği bu adımları göstermektedir:

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

Aşağıda önceki kodun çıktısı yer almakta olup, bu yapılandırılmış çıktıyı `assigned_agent`'a yönlendirebilir ve seyahat planını son kullanıcıya özetleyebilirsiniz.

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

Önceki kod örneği içeren bir örnek defter [burada](../../../07-planning-design/07-autogen.ipynb) mevcuttur.

### Yinelemeli Planlama

Bazı görevler, bir alt görevin sonucu diğerini etkilediğinde karşılıklı etkileşim veya yeniden planlama gerektirir. Örneğin, ajan uçuş rezervasyonu yaparken beklenmedik bir veri formatı keşfederse, otel rezervasyonlarına geçmeden önce stratejisini uyarlaması gerekebilir.

Ayrıca, kullanıcı geri bildirimi (örneğin, bir insanın daha erken bir uçuşu tercih etmesi) kısmi bir yeniden planlamayı tetikleyebilir. Bu dinamik, yinelemeli yaklaşım, nihai çözümün gerçek dünya kısıtlamalarına ve değişen kullanıcı tercihlerine uyum sağlamasını garanti eder.

örnek kod

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

Daha kapsamlı planlama için Magnetic One'a göz atabilirsiniz.

## Özet

Bu makalede, tanımlı mevcut ajanları dinamik olarak seçebilen bir planlayıcı oluşturma örneğine baktık. Planlayıcının çıktısı görevleri alt görevlere ayırır ve ajanlara atar, böylece görevler yürütülebilir. Ajanların görevi yerine getirmek için gerekli işlevlere/araçlara erişimi olduğu varsayılır. Ajanlara ek olarak, yansıtma, özetleyici ve round robin sohbet gibi diğer desenleri de dahil ederek daha fazla özelleştirme yapabilirsiniz.

## Ek Kaynaklar

* AutoGen Magnetic One - Karmaşık görevleri çözmek için genel amaçlı çoklu ajan sistemi ve birçok zorlu ajanik kıyaslamada etkileyici sonuçlar elde etmiştir. Referans:

. Bu uygulamada orkestratör, görev bazlı plan oluşturur ve bu görevleri mevcut ajanlara devreder. Planlamaya ek olarak orkestratör, görevin ilerlemesini izlemek ve gerektiğinde yeniden planlama yapmak için bir takip mekanizması da kullanır.

## Önceki Ders

[Güvenilir AI Ajanları Oluşturma](../06-building-trustworthy-agents/README.md)

## Sonraki Ders

[Çoklu Ajan Tasarım Deseni](../08-multi-agent/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.