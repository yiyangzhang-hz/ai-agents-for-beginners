<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:43:49+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "he"
}
-->
לעיון מהיר.

קטע הקוד הבא בפייתון מדגים סוכן תכנון פשוט שמפרק מטרה לתת-משימות ומייצר תוכנית מובנית:

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

### סוכן תכנון עם תיאום רב-סוכני

בדוגמה זו, סוכן Semantic Router מקבל בקשת משתמש (למשל, "אני צריך תוכנית מלון לטיול שלי.").

התכניתן מבצע את הפעולות הבאות:

* מקבל את תוכנית המלון: התכניתן לוקח את הודעת המשתמש ומבוסס על הנחיית מערכת (כולל פרטי סוכנים זמינים), מייצר תוכנית טיול מובנית.
* מציג את הסוכנים וכלי העבודה שלהם: רישום הסוכנים מחזיק רשימה של סוכנים (למשל לטיסות, מלונות, השכרת רכב ופעילויות) יחד עם הפונקציות או הכלים שהם מציעים.
* מנתב את התוכנית לסוכנים המתאימים: בהתאם למספר תת-המשימות, התכניתן שולח את ההודעה ישירות לסוכן ייעודי (למקרים של משימה אחת) או מתאם דרך מנהל צ'אט קבוצתי לשיתוף פעולה רב-סוכני.
* מסכם את התוצאה: לבסוף, התכניתן מסכם את התוכנית שנוצרה להבהרה.
קטע הקוד הבא בפייתון ממחיש את השלבים הללו:

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

מה שמוצג לאחר מכן הוא הפלט מהקוד הקודם, ואתה יכול להשתמש בפלט המובנה הזה כדי לנתב ל-`assigned_agent` ולסכם את תוכנית הטיול למשתמש הקצה.

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

מחברת דוגמה עם קוד זה זמינה [כאן](../../../07-planning-design/07-autogen.ipynb).

### תכנון איטרטיבי

חלק מהמשימות דורשות תהליך של הלוך ושוב או תכנון מחדש, שבו תוצאת תת-משימה אחת משפיעה על הבאה. לדוגמה, אם הסוכן מגלה פורמט נתונים בלתי צפוי בעת הזמנת טיסות, ייתכן שיצטרך להתאים את האסטרטגיה שלו לפני המעבר להזמנת מלונות.

בנוסף, משוב משתמש (למשל אדם שמחליט שהוא מעדיף טיסה מוקדמת יותר) יכול להפעיל תכנון מחדש חלקי. גישה דינמית ואיטרטיבית זו מבטיחה שהפתרון הסופי יתאים למגבלות העולם האמיתי ולהעדפות המשתמש המשתנות.

לדוגמה, קוד:

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

לתכנון מקיף יותר מומלץ לבדוק את Magnetic One

לפתרון משימות מורכבות.

## סיכום

במאמר זה בחנו דוגמה לאופן שבו ניתן ליצור מתכנן שיכול לבחור באופן דינמי את הסוכנים הזמינים שהוגדרו. הפלט של המתכנן מפרק את המשימות ומקצה את הסוכנים כך שיוכלו להתבצע. מניחים שלסוכנים יש גישה לפונקציות/כלים הדרושים לביצוע המשימה. בנוסף לסוכנים ניתן לכלול דפוסים נוספים כמו רפלקציה, מסכם וצ'אט בסגנון round robin להתאמה אישית נוספת.

## משאבים נוספים

* AutoGen Magnetic One - מערכת רב-סוכנית כללית לפתרון משימות מורכבות שהשיגה תוצאות מרשימות במגוון מבחני סוכנים מאתגרים. הפניה:

במימוש זה, המתאם יוצר תוכנית ספציפית למשימה ומאציל את המשימות הללו לסוכנים הזמינים. בנוסף לתכנון, המתאם מפעיל גם מנגנון מעקב למעקב אחר התקדמות המשימה ומתכנן מחדש לפי הצורך.

## שיעור קודם

[בניית סוכני AI אמינים](../06-building-trustworthy-agents/README.md)

## שיעור הבא

[דפוס עיצוב רב-סוכני](../08-multi-agent/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.