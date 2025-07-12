<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:53:42+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ur"
}
-->
۔ ویکیپیڈیا کے مطابق، ایک اداکار _ہم عصر کمپیوٹیشن کی بنیادی تعمیراتی اکائی ہے۔ موصول ہونے والے پیغام کے جواب میں، ایک اداکار کر سکتا ہے: مقامی فیصلے کرنا، مزید اداکار بنانا، مزید پیغامات بھیجنا، اور اگلے موصول ہونے والے پیغام کا جواب دینے کا طریقہ طے کرنا_۔

**استعمال کے کیسز**: کوڈ جنریشن کو خودکار بنانا، ڈیٹا تجزیہ کے کام، اور منصوبہ بندی اور تحقیق کے افعال کے لیے کسٹم ایجنٹس بنانا۔

یہاں AutoGen کے کچھ اہم بنیادی تصورات ہیں:

- **ایجنٹس**۔ ایک ایجنٹ ایک سافٹ ویئر ہستی ہے جو:
  - **پیغامات کے ذریعے بات چیت کرتی ہے**، یہ پیغامات ہم وقت یا غیر ہم وقت ہو سکتے ہیں۔
  - **اپنی حالت برقرار رکھتی ہے**، جسے آنے والے پیغامات کے ذریعے تبدیل کیا جا سکتا ہے۔
  - **موصولہ پیغامات یا اپنی حالت میں تبدیلیوں کے جواب میں کارروائیاں انجام دیتی ہے**۔ یہ کارروائیاں ایجنٹ کی حالت کو تبدیل کر سکتی ہیں اور بیرونی اثرات پیدا کر سکتی ہیں، جیسے کہ پیغام کے لاگز کو اپ ڈیٹ کرنا، نئے پیغامات بھیجنا، کوڈ چلانا، یا API کالز کرنا۔
    
  یہاں ایک مختصر کوڈ کا ٹکڑا ہے جس میں آپ چیٹ کی صلاحیتوں کے ساتھ اپنا ایجنٹ بنا سکتے ہیں:

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
    
    پچھلے کوڈ میں، `MyAssistant` بنایا گیا ہے اور `RoutedAgent` سے وراثت میں لیا گیا ہے۔ اس میں ایک پیغام ہینڈلر ہے جو پیغام کے مواد کو پرنٹ کرتا ہے اور پھر `AssistantAgent` ڈیلیگیٹ کا استعمال کرتے ہوئے جواب بھیجتا ہے۔ خاص طور پر نوٹ کریں کہ ہم `self._delegate` کو `AssistantAgent` کی ایک مثال تفویض کرتے ہیں جو ایک پہلے سے تیار شدہ ایجنٹ ہے جو چیٹ مکمل کرنے کو سنبھال سکتا ہے۔

    آئیے AutoGen کو اس ایجنٹ کی قسم کے بارے میں بتائیں اور پروگرام شروع کریں:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    پچھلے کوڈ میں ایجنٹس کو رن ٹائم کے ساتھ رجسٹر کیا گیا ہے اور پھر ایجنٹ کو ایک پیغام بھیجا جاتا ہے جس کے نتیجے میں درج ذیل آؤٹ پٹ آتا ہے:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **کئی ایجنٹس**۔ AutoGen متعدد ایجنٹس کی تخلیق کی حمایت کرتا ہے جو مل کر پیچیدہ کام انجام دے سکتے ہیں۔ ایجنٹس بات چیت کر سکتے ہیں، معلومات کا اشتراک کر سکتے ہیں، اور اپنے اعمال کو مربوط کر کے مسائل کو زیادہ مؤثر طریقے سے حل کر سکتے ہیں۔ ایک کثیر ایجنٹ نظام بنانے کے لیے، آپ مختلف قسم کے ایجنٹس کو مخصوص افعال اور کرداروں کے ساتھ تعریف کر سکتے ہیں، جیسے کہ ڈیٹا بازیافت، تجزیہ، فیصلہ سازی، اور صارف کے ساتھ تعامل۔ آئیے دیکھتے ہیں کہ ایسی تخلیق کیسی لگتی ہے تاکہ ہمیں اس کا اندازہ ہو:

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

    پچھلے کوڈ میں ہمارے پاس ایک `GroupChatManager` ہے جو رن ٹائم کے ساتھ رجسٹر ہے۔ یہ مینیجر مختلف قسم کے ایجنٹس جیسے کہ لکھاری، مصور، مدیر، اور صارفین کے درمیان تعاملات کو مربوط کرنے کا ذمہ دار ہے۔

- **ایجنٹ رن ٹائم**۔ یہ فریم ورک ایک رن ٹائم ماحول فراہم کرتا ہے جو ایجنٹس کے درمیان بات چیت کو ممکن بناتا ہے، ان کی شناخت اور زندگی کے چکر کا انتظام کرتا ہے، اور سیکیورٹی اور پرائیویسی کی حدود کو نافذ کرتا ہے۔ اس کا مطلب ہے کہ آپ اپنے ایجنٹس کو ایک محفوظ اور کنٹرول شدہ ماحول میں چلا سکتے ہیں، اس بات کو یقینی بناتے ہوئے کہ وہ محفوظ اور مؤثر طریقے سے بات چیت کر سکیں۔ دلچسپی کے دو رن ٹائم ہیں:
  - **اسٹینڈ الون رن ٹائم**۔ یہ واحد عمل کی ایپلیکیشنز کے لیے اچھا انتخاب ہے جہاں تمام ایجنٹس ایک ہی پروگرامنگ زبان میں نافذ کیے گئے ہوں اور ایک ہی عمل میں چل رہے ہوں۔ یہاں ایک مثال ہے کہ یہ کیسے کام کرتا ہے:

ایپلیکیشن اسٹیک

    *ایجنٹس رن ٹائم کے ذریعے پیغامات کے ذریعے بات چیت کرتے ہیں، اور رن ٹائم ایجنٹس کی زندگی کے چکر کا انتظام کرتا ہے*

  - **تقسیم شدہ ایجنٹ رن ٹائم**، یہ کثیر عمل کی ایپلیکیشنز کے لیے موزوں ہے جہاں ایجنٹس مختلف پروگرامنگ زبانوں میں نافذ کیے جا سکتے ہیں اور مختلف مشینوں پر چل رہے ہوتے ہیں۔ یہاں ایک مثال ہے کہ یہ کیسے کام کرتا ہے:

## Semantic Kernel + Agent Framework

Semantic Kernel ایک انٹرپرائز کے لیے تیار کردہ AI آرکسٹریشن SDK ہے۔ یہ AI اور میموری کنیکٹرز پر مشتمل ہے، ساتھ ہی ایک ایجنٹ فریم ورک بھی ہے۔

آئیے پہلے کچھ بنیادی اجزاء کا احاطہ کرتے ہیں:

- **AI کنیکٹرز**: یہ بیرونی AI خدمات اور ڈیٹا ذرائع کے ساتھ انٹرفیس ہے جو Python اور C# دونوں میں استعمال کے لیے دستیاب ہے۔

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

    یہاں ایک سادہ مثال ہے کہ آپ کیسے ایک کرنل بنا سکتے ہیں اور چیٹ مکمل کرنے کی سروس شامل کر سکتے ہیں۔ Semantic Kernel ایک بیرونی AI سروس سے کنکشن بناتا ہے، اس صورت میں Azure OpenAI Chat Completion۔

- **پلگ انز**: یہ فنکشنز کو انکیپسولیٹ کرتے ہیں جنہیں ایک ایپلیکیشن استعمال کر سکتی ہے۔ یہاں تیار شدہ پلگ انز اور آپ کے بنائے ہوئے کسٹم پلگ انز دونوں موجود ہیں۔ ایک متعلقہ تصور "پرومپٹ فنکشنز" ہے۔ قدرتی زبان کے اشارے فراہم کرنے کے بجائے، آپ ماڈل کو مخصوص فنکشنز نشر کرتے ہیں۔ موجودہ چیٹ کے سیاق و سباق کی بنیاد پر، ماڈل ان میں سے کسی فنکشن کو کال کر سکتا ہے تاکہ درخواست یا سوال مکمل کیا جا سکے۔ یہاں ایک مثال ہے:

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

    یہاں، آپ کے پاس پہلے ایک ٹیمپلیٹ پرومپٹ `skPrompt` ہے جو صارف کے متن `$userInput` کے لیے جگہ چھوڑتا ہے۔ پھر آپ کرنل فنکشن `SummarizeText` بناتے ہیں اور اسے پلگ ان کے نام `SemanticFunctions` کے ساتھ کرنل میں درآمد کرتے ہیں۔ فنکشن کے نام پر غور کریں جو Semantic Kernel کو سمجھنے میں مدد دیتا ہے کہ فنکشن کیا کرتا ہے اور کب اسے کال کرنا چاہیے۔

- **نیٹیو فنکشن**: فریم ورک کے پاس نیٹیو فنکشنز بھی ہیں جنہیں وہ براہ راست کال کر سکتا ہے تاکہ کام انجام دے۔ یہاں ایک مثال ہے جو فائل سے مواد حاصل کرتی ہے:

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

- **میموری**: AI ایپس کے لیے سیاق و سباق کے انتظام کو آسان اور خلاصہ کرتی ہے۔ میموری کا خیال یہ ہے کہ یہ وہ معلومات ہے جو LLM کو معلوم ہونی چاہیے۔ آپ اس معلومات کو ویکٹر اسٹور میں محفوظ کر سکتے ہیں جو ایک ان میموری ڈیٹا بیس یا ویکٹر ڈیٹا بیس یا اس جیسا کچھ ہوتا ہے۔ یہاں ایک بہت سادہ منظر نامہ ہے جہاں *حقائق* میموری میں شامل کیے جاتے ہیں:

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

    یہ حقائق پھر میموری کلیکشن `SummarizedAzureDocs` میں محفوظ کیے جاتے ہیں۔ یہ ایک بہت سادہ مثال ہے، لیکن آپ دیکھ سکتے ہیں کہ آپ کس طرح معلومات کو میموری میں ذخیرہ کر سکتے ہیں تاکہ LLM اسے استعمال کر سکے۔
## پچھلا سبق

[AI ایجنٹس اور ایجنٹ کے استعمال کے کیسز کا تعارف](../01-intro-to-ai-agents/README.md)

## اگلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔