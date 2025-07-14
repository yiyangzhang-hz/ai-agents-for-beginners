<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:53:11+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fa"
}
-->
. طبق ویکی‌پدیا، یک بازیگر _بلاک ساختاری پایه‌ای محاسبات همزمان است. در پاسخ به پیامی که دریافت می‌کند، یک بازیگر می‌تواند: تصمیمات محلی بگیرد، بازیگران بیشتری ایجاد کند، پیام‌های بیشتری ارسال کند و تعیین کند چگونه به پیام بعدی دریافتی پاسخ دهد_.

**موارد استفاده**: خودکارسازی تولید کد، وظایف تحلیل داده و ساخت عوامل سفارشی برای برنامه‌ریزی و عملکردهای تحقیقاتی.

در اینجا برخی مفاهیم کلیدی AutoGen آورده شده است:

- **عوامل**. یک عامل یک موجودیت نرم‌افزاری است که:
  - **از طریق پیام‌ها ارتباط برقرار می‌کند**، این پیام‌ها می‌توانند همزمان یا ناهمزمان باشند.
  - **وضعیت خود را حفظ می‌کند**، که می‌تواند توسط پیام‌های ورودی تغییر یابد.
  - **اقدامات انجام می‌دهد** در پاسخ به پیام‌های دریافتی یا تغییرات در وضعیت خود. این اقدامات ممکن است وضعیت عامل را تغییر داده و اثرات خارجی مانند به‌روزرسانی لاگ پیام‌ها، ارسال پیام‌های جدید، اجرای کد یا فراخوانی API ایجاد کنند.
    
  در اینجا یک قطعه کد کوتاه دارید که در آن عامل خود را با قابلیت‌های چت ایجاد می‌کنید:

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
    
    در کد قبلی، `MyAssistant` ایجاد شده و از `RoutedAgent` ارث‌بری می‌کند. این عامل یک هندلر پیام دارد که محتوای پیام را چاپ می‌کند و سپس با استفاده از نماینده `AssistantAgent` پاسخ می‌فرستد. به‌ویژه توجه کنید که چگونه به `self._delegate` یک نمونه از `AssistantAgent` اختصاص داده‌ایم که یک عامل پیش‌ساخته است و می‌تواند تکمیل‌های چت را مدیریت کند.

    حالا اجازه دهید AutoGen را از این نوع عامل مطلع کنیم و برنامه را اجرا کنیم:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    در کد قبلی، عوامل با زمان اجرا ثبت شده‌اند و سپس پیامی به عامل ارسال می‌شود که منجر به خروجی زیر می‌شود:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **چند عامل**. AutoGen از ایجاد چندین عامل که می‌توانند با هم کار کنند برای انجام وظایف پیچیده پشتیبانی می‌کند. عوامل می‌توانند ارتباط برقرار کنند، اطلاعات را به اشتراک بگذارند و اقدامات خود را هماهنگ کنند تا مشکلات را به شکل موثرتری حل کنند. برای ایجاد یک سیستم چندعاملی، می‌توانید انواع مختلفی از عوامل با عملکردها و نقش‌های تخصصی مانند بازیابی داده، تحلیل، تصمیم‌گیری و تعامل با کاربر تعریف کنید. بیایید ببینیم چنین ساختاری چگونه به نظر می‌رسد:

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

    در کد قبلی، یک `GroupChatManager` داریم که با زمان اجرا ثبت شده است. این مدیر مسئول هماهنگی تعاملات بین انواع مختلف عوامل مانند نویسندگان، تصویرگران، ویراستاران و کاربران است.

- **زمان اجرای عامل**. این فریم‌ورک یک محیط زمان اجرا فراهم می‌کند که ارتباط بین عوامل را ممکن می‌سازد، هویت و چرخه عمر آن‌ها را مدیریت می‌کند و مرزهای امنیتی و حریم خصوصی را اعمال می‌کند. این بدان معناست که می‌توانید عوامل خود را در یک محیط امن و کنترل‌شده اجرا کنید تا اطمینان حاصل شود که آن‌ها می‌توانند به شکل ایمن و کارآمد تعامل داشته باشند. دو نوع زمان اجرا وجود دارد:
  - **زمان اجرای مستقل**. این گزینه خوبی برای برنامه‌های تک‌فرآیندی است که در آن همه عوامل به یک زبان برنامه‌نویسی پیاده‌سازی شده و در همان فرآیند اجرا می‌شوند. در اینجا تصویری از نحوه عملکرد آن آمده است:

پشته برنامه

    *عوامل از طریق پیام‌ها با هم ارتباط برقرار می‌کنند و زمان اجرا چرخه عمر عوامل را مدیریت می‌کند*

  - **زمان اجرای توزیع‌شده عامل**، مناسب برنامه‌های چندفرآیندی است که عوامل ممکن است به زبان‌های برنامه‌نویسی مختلف پیاده‌سازی شده و روی ماشین‌های مختلف اجرا شوند. در اینجا تصویری از نحوه عملکرد آن آمده است:

## Semantic Kernel + چارچوب عامل

Semantic Kernel یک SDK ارکستراسیون هوش مصنوعی آماده سازمانی است. این شامل کانکتورهای هوش مصنوعی و حافظه به همراه یک چارچوب عامل است.

ابتدا برخی اجزای اصلی را بررسی کنیم:

- **کانکتورهای هوش مصنوعی**: این یک رابط با سرویس‌های هوش مصنوعی خارجی و منابع داده برای استفاده در هر دو زبان Python و C# است.

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

    در اینجا یک مثال ساده دارید که چگونه می‌توانید یک کرنل ایجاد کرده و سرویس تکمیل چت را اضافه کنید. Semantic Kernel یک اتصال به سرویس هوش مصنوعی خارجی، در این مورد Azure OpenAI Chat Completion، ایجاد می‌کند.

- **پلاگین‌ها**: این‌ها توابعی را که یک برنامه می‌تواند استفاده کند، در بر می‌گیرند. هم پلاگین‌های آماده و هم پلاگین‌های سفارشی که می‌توانید ایجاد کنید وجود دارد. یک مفهوم مرتبط "توابع پرامپت" است. به جای ارائه نشانه‌های زبان طبیعی برای فراخوانی تابع، شما توابع خاصی را به مدل پخش می‌کنید. بر اساس زمینه چت فعلی، مدل ممکن است یکی از این توابع را برای تکمیل درخواست یا پرس‌وجو انتخاب کند. در اینجا یک مثال آمده است:

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

    در اینجا ابتدا یک قالب پرامپت `skPrompt` دارید که فضایی برای ورودی کاربر، `$userInput`، باقی می‌گذارد. سپس تابع کرنل `SummarizeText` را ایجاد کرده و آن را با نام پلاگین `SemanticFunctions` وارد کرنل می‌کنید. به نام تابع توجه کنید که به Semantic Kernel کمک می‌کند بفهمد این تابع چه کاری انجام می‌دهد و چه زمانی باید فراخوانی شود.

- **تابع بومی**: همچنین توابع بومی وجود دارد که فریم‌ورک می‌تواند مستقیماً برای انجام کار فراخوانی کند. در اینجا مثالی از چنین تابعی که محتوای یک فایل را بازیابی می‌کند آمده است:

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

- **حافظه**: مدیریت زمینه را برای برنامه‌های هوش مصنوعی انتزاعی و ساده می‌کند. ایده حافظه این است که این چیزی است که LLM باید درباره آن بداند. می‌توانید این اطلاعات را در یک فروشگاه برداری ذخیره کنید که در نهایت به یک پایگاه داده در حافظه یا پایگاه داده برداری یا مشابه تبدیل می‌شود. در اینجا مثالی از یک سناریوی بسیار ساده شده که در آن *حقایق* به حافظه اضافه می‌شوند آمده است:

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

    این حقایق سپس در مجموعه حافظه `SummarizedAzureDocs` ذخیره می‌شوند. این یک مثال بسیار ساده است، اما می‌توانید ببینید چگونه می‌توانید اطلاعات را در حافظه ذخیره کنید تا LLM از آن استفاده کند.
## درس قبلی

[مقدمه‌ای بر عوامل هوش مصنوعی و موارد استفاده از عامل‌ها](../01-intro-to-ai-agents/README.md)

## درس بعدی

[درک الگوهای طراحی عاملی](../03-agentic-design-patterns/README.md)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.