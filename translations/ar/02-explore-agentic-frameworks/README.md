<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:52:43+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ar"
}
-->
. وفقًا لويكيبيديا، الممثل هو _اللبنة الأساسية للحوسبة المتزامنة. استجابةً لرسالة يتلقاها، يمكن للممثل: اتخاذ قرارات محلية، إنشاء المزيد من الممثلين، إرسال المزيد من الرسائل، وتحديد كيفية الرد على الرسالة التالية التي يتلقاها_.

**حالات الاستخدام**: أتمتة توليد الشيفرة، مهام تحليل البيانات، وبناء وكلاء مخصصين لوظائف التخطيط والبحث.

إليك بعض المفاهيم الأساسية المهمة في AutoGen:

- **الوكلاء**. الوكيل هو كيان برمجي يقوم بـ:
  - **التواصل عبر الرسائل**، يمكن أن تكون هذه الرسائل متزامنة أو غير متزامنة.
  - **الحفاظ على حالته الخاصة**، والتي يمكن تعديلها بواسطة الرسائل الواردة.
  - **أداء الإجراءات** استجابةً للرسائل المستلمة أو التغيرات في حالته. قد تؤدي هذه الإجراءات إلى تعديل حالة الوكيل وإحداث تأثيرات خارجية، مثل تحديث سجلات الرسائل، إرسال رسائل جديدة، تنفيذ الشيفرة، أو إجراء مكالمات API.
    
  هنا لديك مقتطف شيفرة قصير حيث تقوم بإنشاء وكيل خاص بك بقدرات الدردشة:

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
    
    في الشيفرة السابقة، تم إنشاء `MyAssistant` ويرث من `RoutedAgent`. لديه معالج رسائل يطبع محتوى الرسالة ثم يرسل ردًا باستخدام المندوب `AssistantAgent`. لاحظ بشكل خاص كيف نُسند إلى `self._delegate` نسخة من `AssistantAgent` وهو وكيل مُعد مسبقًا يمكنه التعامل مع إكمالات الدردشة.

    دعونا نُعلم AutoGen عن نوع هذا الوكيل ونبدأ البرنامج بعد ذلك:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    في الشيفرة السابقة، يتم تسجيل الوكلاء مع وقت التشغيل ثم تُرسل رسالة إلى الوكيل مما يؤدي إلى الإخراج التالي:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **الوكلاء المتعددون**. يدعم AutoGen إنشاء عدة وكلاء يمكنهم العمل معًا لتحقيق مهام معقدة. يمكن للوكلاء التواصل، مشاركة المعلومات، وتنسيق أفعالهم لحل المشكلات بكفاءة أكبر. لإنشاء نظام وكلاء متعدد، يمكنك تعريف أنواع مختلفة من الوكلاء بوظائف وأدوار متخصصة، مثل استرجاع البيانات، التحليل، اتخاذ القرار، والتفاعل مع المستخدم. لنرَ كيف يبدو هذا الإنشاء:

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

    في الشيفرة السابقة لدينا `GroupChatManager` مسجل مع وقت التشغيل. هذا المدير مسؤول عن تنسيق التفاعلات بين أنواع مختلفة من الوكلاء، مثل الكتاب، الرسامين، المحررين، والمستخدمين.

- **وقت تشغيل الوكيل**. يوفر الإطار بيئة وقت تشغيل، تمكّن التواصل بين الوكلاء، تدير هوياتهم ودورات حياتهم، وتفرض حدود الأمان والخصوصية. هذا يعني أنه يمكنك تشغيل وكلائك في بيئة آمنة ومتحكم بها، مما يضمن تفاعلهم بأمان وكفاءة. هناك نوعان من أوقات التشغيل ذات الاهتمام:
  - **وقت تشغيل مستقل**. هذا خيار جيد لتطبيقات العملية الواحدة حيث يتم تنفيذ جميع الوكلاء بنفس لغة البرمجة ويعملون في نفس العملية. إليك توضيحًا لكيفية عمله:

مكدس التطبيق

    *يتواصل الوكلاء عبر الرسائل من خلال وقت التشغيل، ويدير وقت التشغيل دورة حياة الوكلاء*

  - **وقت تشغيل الوكلاء الموزع**، مناسب لتطبيقات متعددة العمليات حيث قد يتم تنفيذ الوكلاء بلغات برمجة مختلفة ويعملون على أجهزة مختلفة. إليك توضيحًا لكيفية عمله:

## Semantic Kernel + إطار الوكيل

Semantic Kernel هو SDK تنسيق ذكاء اصطناعي جاهز للمؤسسات. يتكون من موصلات ذكاء اصطناعي وذاكرة، إلى جانب إطار وكيل.

لنبدأ بتغطية بعض المكونات الأساسية:

- **موصلات الذكاء الاصطناعي**: هذه واجهة مع خدمات الذكاء الاصطناعي الخارجية ومصادر البيانات للاستخدام في كل من Python و C#.

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

    هنا لديك مثال بسيط على كيفية إنشاء kernel وإضافة خدمة إكمال الدردشة. يقوم Semantic Kernel بإنشاء اتصال مع خدمة ذكاء اصطناعي خارجية، في هذه الحالة، Azure OpenAI Chat Completion.

- **الإضافات (Plugins)**: تغلف الوظائف التي يمكن للتطبيق استخدامها. هناك إضافات جاهزة وأخرى مخصصة يمكنك إنشاؤها. مفهوم ذو صلة هو "وظائف المطالبة". بدلاً من تقديم تلميحات بلغة طبيعية لاستدعاء الوظائف، تقوم ببث وظائف معينة إلى النموذج. بناءً على سياق الدردشة الحالي، قد يختار النموذج استدعاء إحدى هذه الوظائف لإكمال طلب أو استعلام. إليك مثالًا:

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

    هنا، لديك أولاً قالب مطالبة `skPrompt` يترك مساحة للمستخدم لإدخال نص، `$userInput`. ثم تنشئ دالة kernel `SummarizeText` ثم تستوردها إلى kernel باسم الإضافة `SemanticFunctions`. لاحظ اسم الدالة الذي يساعد Semantic Kernel على فهم وظيفة الدالة ومتى يجب استدعاؤها.

- **الدالة الأصلية**: هناك أيضًا دوال أصلية يمكن للإطار استدعاؤها مباشرة لتنفيذ المهمة. إليك مثالًا على دالة تسترجع المحتوى من ملف:

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

- **الذاكرة**: تجريد وتبسيط إدارة السياق لتطبيقات الذكاء الاصطناعي. الفكرة مع الذاكرة هي أن هذا شيء يجب أن يعرفه LLM. يمكنك تخزين هذه المعلومات في مخزن متجهات والذي ينتهي به الأمر ليكون قاعدة بيانات في الذاكرة أو قاعدة بيانات متجهات أو ما شابه. إليك مثالًا على سيناريو مبسط جدًا حيث تُضاف *حقائق* إلى الذاكرة:

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

    تُخزن هذه الحقائق بعد ذلك في مجموعة الذاكرة `SummarizedAzureDocs`. هذا مثال مبسط جدًا، لكن يمكنك أن ترى كيف يمكنك تخزين المعلومات في الذاكرة ليستخدمها LLM.
## الدرس السابق

[مقدمة في وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

## الدرس التالي

[فهم أنماط التصميم الوكيلية](../03-agentic-design-patterns/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.