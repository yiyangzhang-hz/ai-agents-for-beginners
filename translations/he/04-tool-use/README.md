<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T17:38:50+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "he"
}
-->
[![איך לעצב סוכני AI טובים](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.he.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

# תבנית עיצוב לשימוש בכלים

כלים הם מעניינים מכיוון שהם מאפשרים לסוכני AI להרחיב את טווח היכולות שלהם. במקום שסוכן יהיה מוגבל למספר פעולות מצומצם, הוספת כלי מאפשרת לו לבצע מגוון רחב של פעולות. בפרק זה נבחן את תבנית העיצוב לשימוש בכלים, שמתארת כיצד סוכני AI יכולים להשתמש בכלים ספציפיים כדי להשיג את מטרותיהם.

## מבוא

בשיעור זה ננסה לענות על השאלות הבאות:

- מהי תבנית העיצוב לשימוש בכלים?
- לאילו מקרים ניתן ליישם אותה?
- מהם האלמנטים/אבני הבניין הנדרשים ליישום תבנית העיצוב?
- מהם השיקולים המיוחדים לשימוש בתבנית העיצוב לשימוש בכלים כדי לבנות סוכני AI אמינים?

## מטרות למידה

לאחר השלמת השיעור, תוכלו:

- להגדיר את תבנית העיצוב לשימוש בכלים ואת מטרתה.
- לזהות מקרים שבהם תבנית העיצוב לשימוש בכלים רלוונטית.
- להבין את האלמנטים המרכזיים הנדרשים ליישום תבנית העיצוב.
- לזהות שיקולים להבטחת אמינות סוכני AI המשתמשים בתבנית עיצוב זו.

## מהי תבנית העיצוב לשימוש בכלים?

**תבנית העיצוב לשימוש בכלים** מתמקדת במתן יכולת ל-LLMs (מודלים לשפה גדולה) לתקשר עם כלים חיצוניים כדי להשיג מטרות ספציפיות. כלים הם קוד שניתן להריץ על ידי סוכן כדי לבצע פעולות. כלי יכול להיות פונקציה פשוטה כמו מחשבון, או קריאה ל-API של שירות צד שלישי כמו בדיקת מחירי מניות או תחזית מזג אוויר. בהקשר של סוכני AI, כלים מתוכננים להיות מופעלים על ידי סוכנים בתגובה ל**קריאות פונקציה שנוצרו על ידי המודל**.

## לאילו מקרים ניתן ליישם אותה?

סוכני AI יכולים לנצל כלים כדי להשלים משימות מורכבות, לאחזר מידע או לקבל החלטות. תבנית העיצוב לשימוש בכלים משמשת לעיתים קרובות בתרחישים הדורשים אינטראקציה דינמית עם מערכות חיצוניות, כמו מסדי נתונים, שירותי רשת או מפרשי קוד. יכולת זו שימושית למגוון מקרים, כולל:

- **אחזור מידע דינמי:** סוכנים יכולים לשאול APIs חיצוניים או מסדי נתונים כדי לאחזר נתונים עדכניים (לדוגמה, שאילת מסד נתונים SQLite לניתוח נתונים, אחזור מחירי מניות או מידע על מזג האוויר).
- **הרצת קוד ופירושו:** סוכנים יכולים להריץ קוד או סקריפטים כדי לפתור בעיות מתמטיות, ליצור דוחות או לבצע סימולציות.
- **אוטומציה של תהליכים:** אוטומציה של תהליכים חוזרים או מרובי שלבים על ידי שילוב כלים כמו מתזמני משימות, שירותי דוא"ל או צינורות נתונים.
- **תמיכה בלקוחות:** סוכנים יכולים לתקשר עם מערכות CRM, פלטפורמות כרטיסים או מאגרי ידע כדי לפתור שאילתות משתמשים.
- **יצירה ועריכת תוכן:** סוכנים יכולים להשתמש בכלים כמו בודקי דקדוק, מסכמי טקסט או מעריכי בטיחות תוכן כדי לסייע במשימות יצירת תוכן.

## מהם האלמנטים/אבני הבניין הנדרשים ליישום תבנית העיצוב לשימוש בכלים?

אבני בניין אלו מאפשרות לסוכן AI לבצע מגוון רחב של משימות. בואו נבחן את האלמנטים המרכזיים הנדרשים ליישום תבנית העיצוב לשימוש בכלים:

- **סכמות פונקציה/כלי:** הגדרות מפורטות של הכלים הזמינים, כולל שם הפונקציה, מטרתה, הפרמטרים הנדרשים והתוצאות הצפויות. סכמות אלו מאפשרות ל-LLM להבין אילו כלים זמינים וכיצד לבנות בקשות תקפות.
- **לוגיקת ביצוע פונקציות:** מגדירה כיצד ומתי כלים מופעלים בהתבסס על כוונת המשתמש והקשר השיחה. זה עשוי לכלול מודולי תכנון, מנגנוני ניתוב או זרימות מותנות שקובעות את השימוש בכלים באופן דינמי.
- **מערכת ניהול הודעות:** רכיבים שמנהלים את זרימת השיחה בין קלטי המשתמש, תגובות ה-LLM, קריאות הכלים ותוצאות הכלים.
- **מסגרת אינטגרציה לכלים:** תשתית שמחברת את הסוכן לכלים שונים, בין אם הם פונקציות פשוטות או שירותים חיצוניים מורכבים.
- **ניהול שגיאות ואימות:** מנגנונים לטיפול בכשלים בביצוע כלים, אימות פרמטרים וניהול תגובות בלתי צפויות.
- **ניהול מצב:** מעקב אחר הקשר השיחה, אינטראקציות קודמות עם כלים ונתונים מתמשכים כדי להבטיח עקביות באינטראקציות מרובות שלבים.

כעת, נבחן את נושא קריאות הפונקציות/כלים בפירוט.

### קריאות פונקציות/כלים

קריאות פונקציות הן הדרך המרכזית שבה אנו מאפשרים ל-LLMs לתקשר עם כלים. לעיתים קרובות תראו את המונחים 'פונקציה' ו'כלי' משמשים לסירוגין, מכיוון ש'פונקציות' (בלוקים של קוד לשימוש חוזר) הן ה'כלים' שבהם סוכנים משתמשים לביצוע משימות. כדי להפעיל את קוד הפונקציה, ה-LLM משווה את בקשת המשתמש לתיאור הפונקציה. לשם כך, סכימה המכילה את תיאורי כל הפונקציות הזמינות נשלחת ל-LLM. ה-LLM בוחר את הפונקציה המתאימה ביותר למשימה ומחזיר את שמה ואת הפרמטרים שלה. הפונקציה הנבחרת מופעלת, תגובתה נשלחת חזרה ל-LLM, שמשתמש במידע כדי להגיב לבקשת המשתמש.

כדי שמפתחים יוכלו ליישם קריאות פונקציות עבור סוכנים, תצטרכו:

1. מודל LLM שתומך בקריאות פונקציות
2. סכימה המכילה תיאורי פונקציות
3. הקוד של כל פונקציה המתוארת

בואו נשתמש בדוגמה של קבלת השעה הנוכחית בעיר כדי להמחיש:

1. **אתחול LLM שתומך בקריאות פונקציות:**

    לא כל המודלים תומכים בקריאות פונקציות, ולכן חשוב לבדוק שה-LLM שבו אתם משתמשים תומך בכך.  
    <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> תומך בקריאות פונקציות. נוכל להתחיל על ידי אתחול לקוח Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **יצירת סכמת פונקציה:**

    לאחר מכן נגדיר סכמת JSON המכילה את שם הפונקציה, תיאור של מה שהפונקציה עושה, ושמות ותיאורים של פרמטרי הפונקציה.  
    ניקח את הסכימה הזו ונעביר אותה ללקוח שיצרנו קודם, יחד עם בקשת המשתמש למצוא את השעה בסן פרנסיסקו. חשוב לציין שמה שמוחזר הוא **קריאת כלי**, **לא** התשובה הסופית לשאלה. כפי שצוין קודם, ה-LLM מחזיר את שם הפונקציה שבחר למשימה ואת הפרמטרים שיועברו אליה.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **הקוד של הפונקציה הנדרש לביצוע המשימה:**

    כעת, לאחר שה-LLM בחר איזו פונקציה יש להריץ, יש ליישם ולהריץ את הקוד שמבצע את המשימה.  
    נוכל ליישם את הקוד לקבלת השעה הנוכחית ב-Python. נצטרך גם לכתוב את הקוד שמוציא את שם הפונקציה והפרמטרים מתגובת ההודעה כדי לקבל את התוצאה הסופית.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

    ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

    ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

קריאות פונקציות הן בלב רוב, אם לא כל, עיצובי השימוש בכלים של סוכנים, אך יישומן מאפס עשוי להיות מאתגר לעיתים.  
כפי שלמדנו ב-[שיעור 2](../../../02-explore-agentic-frameworks), מסגרות סוכנים מספקות לנו אבני בניין מוכנות מראש ליישום שימוש בכלים.

## דוגמאות לשימוש בכלים עם מסגרות סוכנים

להלן כמה דוגמאות ליישום תבנית העיצוב לשימוש בכלים באמצעות מסגרות סוכנים שונות:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> היא מסגרת AI בקוד פתוח למפתחים ב-.NET, Python ו-Java העובדים עם LLMs. היא מפשטת את תהליך השימוש בקריאות פונקציות על ידי תיאור אוטומטי של הפונקציות והפרמטרים שלהן למודל בתהליך שנקרא <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a>. היא גם מנהלת את התקשורת בין המודל לקוד שלכם. יתרון נוסף של שימוש במסגרת סוכנים כמו Semantic Kernel הוא שהיא מאפשרת גישה לכלים מוכנים מראש כמו <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">חיפוש קבצים</a> ו-<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">מפרש קוד</a>.

התרשים הבא ממחיש את תהליך קריאות הפונקציות עם Semantic Kernel:

![קריאות פונקציות](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.he.png)

ב-Semantic Kernel פונקציות/כלים נקראים <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. נוכל להמיר את הפונקציה `get_current_time` שראינו קודם לפלאגין על ידי הפיכתה למחלקה עם הפונקציה בתוכה. נוכל גם לייבא את הדקורטור `kernel_function`, שמקבל את תיאור הפונקציה. כאשר תיצרו Kernel עם ה-GetCurrentTimePlugin, ה-Kernel יתאר אוטומטית את הפונקציה והפרמטרים שלה, וייצור את הסכימה לשליחה ל-LLM בתהליך.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> היא מסגרת סוכנים חדשה יותר שנועדה לאפשר למפתחים לבנות, לפרוס ולהרחיב סוכני AI איכותיים ומותאמים אישית בצורה מאובטחת, מבלי לנהל את משאבי המחשוב והאחסון הבסיסיים. היא שימושית במיוחד ליישומים ארגוניים מכיוון שהיא שירות מנוהל לחלוטין עם אבטחה ברמה ארגונית.

בהשוואה לפיתוח ישיר עם API של LLM, Azure AI Agent Service מספקת כמה יתרונות, כולל:

- קריאות כלים אוטומטיות – אין צורך לנתח קריאת כלי, להפעיל את הכלי ולטפל בתגובה; כל זה נעשה בצד השרת.
- ניהול נתונים מאובטח – במקום לנהל את מצב השיחה בעצמכם, תוכלו להסתמך על threads לאחסון כל המידע הדרוש.
- כלים מוכנים לשימוש – כלים שניתן להשתמש בהם כדי לתקשר עם מקורות הנתונים שלכם, כמו Bing, Azure AI Search ו-Azure Functions.

הכלים הזמינים ב-Azure AI Agent Service מחולקים לשתי קטגוריות:

1. כלים לידע:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">חיפוש Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">חיפוש קבצים</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. כלים לפעולה:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">קריאות פונקציות</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">מפרש קוד</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">כלים שהוגדרו על ידי OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

שירות הסוכנים מאפשר לנו להשתמש בכלים אלו יחד כ-`toolset`. הוא גם משתמש ב-`threads` שעוקבים אחר היסטוריית ההודעות משיחה מסוימת.

דמיינו שאתם סוכני מכירות בחברה בשם Contoso. אתם רוצים לפתח סוכן שיחה שיכול לענות על שאלות בנוגע לנתוני המכירות שלכם.

התמונה הבאה ממחישה כיצד תוכלו להשתמש ב-Azure AI Agent Service לניתוח נתוני המכירות שלכם:

![שירות סוכנים בפעולה](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.he.jpg)

כדי להשתמש בכלים אלו עם השירות, נוכל ליצור לקוח ולהגדיר כלי או סט כלים. כדי ליישם זאת בפועל, נוכל להשתמש בקוד Python הבא. ה-LLM יוכל להסתכל על ה-toolset ולהחליט אם להשתמש בפונקציה שיצר המשתמש, `fetch_sales_data_using_sqlite_query`, או במפרש הקוד המובנה, בהתאם לבקשת המשתמש.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## מהם השיקולים המיוחדים לשימוש בתבנית העיצוב לשימוש בכלים כדי לבנות סוכני AI אמינים?

דאגה נפוצה עם SQL שנוצר באופן דינמי על ידי LLMs היא אבטחה, במיוחד הסיכון להזרקת SQL או פעולות זדוניות, כמו מחיקת מסד הנתונים או שינויו. למרות שחששות אלו תקפים, ניתן להתמודד איתם ביעילות על ידי הגדרת הרשאות גישה למסד הנתונים בצורה נכונה. עבור רוב מסדי הנתונים, זה כולל הגדרת מסד הנתונים כקריאה בלבד. עבור שירותי מסדי נתונים כמו PostgreSQL או Azure SQL, יש להקצות לאפליקציה תפקיד קריאה בלבד (SELECT).

הרצת האפליקציה בסביבה מאובטחת משפרת עוד יותר את ההגנה. בתרחישים ארגוניים, נתונים בדרך כלל מופקים ומועברים ממערכות תפעוליות למסד נתונים לקריאה בלבד או למחסן נתונים עם סכימה ידידותית למשתמש. גישה זו מבטיחה שהנתונים מאובטחים, מותאמים לביצועים ונגישות, ושלאפליקציה יש גישה מוגבלת לקריאה בלבד.

### יש לכם עוד שאלות על תבניות העיצוב לשימוש בכלים?
הצטרפו ל-[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות משרד ולקבל תשובות לשאלות שלכם על סוכני AI.

## משאבים נוספים

## שיעור קודם

[הבנת תבניות עיצוב סוכנים](../03-agentic-design-patterns/README.md)

## שיעור הבא

[Agentic RAG](../05-agentic-rag/README.md)

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.