<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:06:26+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "he"
}
-->
. לפי ויקיפדיה, שחקן הוא _היחידה הבסיסית של חישוב מקבילי. בתגובה להודעה שהוא מקבל, שחקן יכול: לקבל החלטות מקומיות, ליצור שחקנים נוספים, לשלוח הודעות נוספות, ולקבוע כיצד להגיב להודעה הבאה שיתקבלו_.

**מקרי שימוש**: אוטומציה של יצירת קוד, משימות ניתוח נתונים, ובניית סוכנים מותאמים אישית לתכנון ולפונקציות מחקר.

הנה כמה מושגים מרכזיים חשובים ב-AutoGen:

- **סוכנים**. סוכן הוא ישות תוכנה ש:
  - **מתקשרת באמצעות הודעות**, הודעות אלו יכולות להיות סינכרוניות או אסינכרוניות.
  - **שומרת על המצב שלה**, שניתן לשנותו על ידי הודעות נכנסות.
  - **מבצעת פעולות** בתגובה להודעות שהתקבלו או לשינויים במצבה. פעולות אלו עשויות לשנות את מצב הסוכן וליצור השפעות חיצוניות, כמו עדכון יומני הודעות, שליחת הודעות חדשות, ביצוע קוד, או קריאות API.
    
  כאן יש קטע קוד קצר שבו יוצרים סוכן עם יכולות שיחה:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    בקוד הקודם, `MyAssistant` נוצר ויורש מ-`RoutedAgent`. יש לו מטפל הודעות שמדפיס את תוכן ההודעה ואז שולח תגובה באמצעות המשלח `AssistantAgent`. שימו לב במיוחד כיצד אנו מייחסים ל-`self._delegate` מופע של `AssistantAgent` שהוא סוכן מוכן מראש שיכול לטפל בהשלמות שיחה.


    בואו נודיע ל-AutoGen על סוג סוכן זה ונפעיל את התוכנית:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    בקוד הקודם הסוכנים נרשמים בסביבת הריצה ואז נשלחת הודעה לסוכן, מה שמניב את הפלט הבא:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **ריבוי סוכנים**. AutoGen תומך ביצירת מספר סוכנים שיכולים לעבוד יחד כדי להשיג משימות מורכבות. סוכנים יכולים לתקשר, לשתף מידע, ולתאם את פעולותיהם כדי לפתור בעיות בצורה יעילה יותר. כדי ליצור מערכת רב-סוכנית, ניתן להגדיר סוגים שונים של סוכנים עם פונקציות ותפקידים מיוחדים, כמו אחזור נתונים, ניתוח, קבלת החלטות, ואינטראקציה עם משתמש. בואו נראה איך יצירה כזו נראית:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    בקוד הקודם יש לנו `GroupChatManager` שנרשם בסביבת הריצה. מנהל זה אחראי לתיאום האינטראקציות בין סוגים שונים של סוכנים, כמו כותבים, מאיירים, עורכים, ומשתמשים.

- **סביבת ריצה לסוכנים**. המסגרת מספקת סביבת ריצה, שמאפשרת תקשורת בין סוכנים, מנהלת את הזהויות והמחזור חיים שלהם, ואוכפת גבולות אבטחה ופרטיות. משמעות הדבר היא שניתן להריץ את הסוכנים בסביבה בטוחה ומבוקרת, שמבטיחה שהם יוכלו לפעול בבטחה וביעילות. קיימות שתי סביבות ריצה עיקריות:
  - **סביבת ריצה עצמאית**. זו בחירה טובה לאפליקציות חד-תהליכיות שבהן כל הסוכנים מיושמים באותה שפת תכנות ומופעלים באותו תהליך. הנה המחשה של אופן הפעולה:  

מערך היישום

    *הסוכנים מתקשרים באמצעות הודעות דרך סביבת הריצה, וסביבת הריצה מנהלת את מחזור החיים של הסוכנים*

  - **סביבת ריצה מבוזרת**, מתאימה לאפליקציות רב-תהליכיות שבהן סוכנים עשויים להיות מיושמים בשפות תכנות שונות ולהריץ על מכונות שונות. הנה המחשה של אופן הפעולה:  

## Semantic Kernel + Agent Framework

Semantic Kernel הוא SDK לאורקסטרציה של AI המיועד לארגונים. הוא כולל מחברים ל-AI ולזיכרון, יחד עם מסגרת סוכנים.

נתחיל בכמה רכיבים מרכזיים:

- **מחברי AI**: זוהי ממשק עם שירותי AI חיצוניים ומקורות נתונים לשימוש ב-Python וב-C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    כאן יש דוגמה פשוטה כיצד ליצור kernel ולהוסיף שירות השלמת שיחה. Semantic Kernel יוצר חיבור לשירות AI חיצוני, במקרה זה, Azure OpenAI Chat Completion.

- **תוספים (Plugins)**: אלו מכילים פונקציות שהאפליקציה יכולה להשתמש בהן. קיימים תוספים מוכנים מראש ותוספים מותאמים אישית שניתן ליצור. מושג קשור הוא "פונקציות פרומפט". במקום לספק רמזים בשפה טבעית להפעלת פונקציה, משדרים פונקציות מסוימות למודל. בהתבסס על הקשר השיחה הנוכחי, המודל עשוי לבחור לקרוא לאחת מהפונקציות הללו כדי להשלים בקשה או שאילתה. הנה דוגמה:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    כאן, יש תחילה תבנית פרומפט `skPrompt` שמשאירה מקום למשתמש להזין טקסט, `$userInput`. לאחר מכן יוצרים את פונקציית ה-kernel `SummarizeText` ומייבאים אותה ל-kernel בשם התוסף `SemanticFunctions`. שימו לב לשם הפונקציה שעוזר ל-Semantic Kernel להבין מה הפונקציה עושה ומתי יש לקרוא לה.

- **פונקציה מקומית**: קיימות גם פונקציות מקומיות שהמסגרת יכולה לקרוא להן ישירות לביצוע המשימה. הנה דוגמה לפונקציה כזו שמחזירה תוכן מקובץ:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **זיכרון**: מפשט ומופשט את ניהול ההקשר לאפליקציות AI. הרעיון בזיכרון הוא שזה משהו שה-LLM צריך לדעת עליו. ניתן לאחסן מידע זה במאגר וקטורים, שהוא בעצם מסד נתונים בזיכרון או מסד וקטורי או דומה. הנה דוגמה לתרחיש פשוט מאוד שבו *עובדות* מתווספות לזיכרון:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    העובדות הללו נשמרות באוסף הזיכרון `SummarizedAzureDocs`. זו דוגמה מאוד פשוטה, אבל ניתן לראות כיצד ניתן לאחסן מידע בזיכרון לשימוש ה-LLM.
## השיעור הקודם

[מבוא לסוכני AI ומקרי שימוש בסוכנים](../01-intro-to-ai-agents/README.md)

## השיעור הבא

[הבנת תבניות עיצוב סוכניות](../03-agentic-design-patterns/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.