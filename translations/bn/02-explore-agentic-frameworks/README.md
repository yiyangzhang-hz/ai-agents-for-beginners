<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:57:31+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "bn"
}
-->
. উইকিপিডিয়ার মতে, একটি অভিনেতা হল _সমান্তরাল গণনার মৌলিক নির্মাণ ব্লক। এটি যে বার্তাটি পায় তার প্রতিক্রিয়ায়, একজন অভিনেতা করতে পারে: স্থানীয় সিদ্ধান্ত নেওয়া, আরও অভিনেতা তৈরি করা, আরও বার্তা পাঠানো, এবং পরবর্তী প্রাপ্ত বার্তায় কীভাবে প্রতিক্রিয়া জানানো হবে তা নির্ধারণ করা_।

**ব্যবহার ক্ষেত্র**: কোড জেনারেশন স্বয়ংক্রিয়করণ, ডেটা বিশ্লেষণ কাজ, এবং পরিকল্পনা ও গবেষণা ফাংশনের জন্য কাস্টম এজেন্ট তৈরি করা।

এখানে AutoGen-এর কিছু গুরুত্বপূর্ণ মূল ধারণা রয়েছে:

- **এজেন্টস**। একটি এজেন্ট হল একটি সফটওয়্যার সত্তা যা:
  - **বার্তার মাধ্যমে যোগাযোগ করে**, এই বার্তাগুলি সিঙ্ক্রোনাস বা অ্যাসিঙ্ক্রোনাস হতে পারে।
  - **নিজস্ব অবস্থা বজায় রাখে**, যা আগত বার্তাগুলির দ্বারা পরিবর্তিত হতে পারে।
  - **প্রাপ্ত বার্তা বা অবস্থার পরিবর্তনের প্রতিক্রিয়ায় কাজ করে**। এই কাজগুলি এজেন্টের অবস্থা পরিবর্তন করতে পারে এবং বাহ্যিক প্রভাব সৃষ্টি করতে পারে, যেমন বার্তা লগ আপডেট করা, নতুন বার্তা পাঠানো, কোড চালানো, বা API কল করা।
    
  এখানে একটি ছোট কোড স্নিপেট আছে যেখানে আপনি চ্যাট সক্ষমতা সহ আপনার নিজস্ব এজেন্ট তৈরি করছেন:

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
    
    পূর্বের কোডে, `MyAssistant` তৈরি করা হয়েছে এবং এটি `RoutedAgent` থেকে উত্তরাধিকারসূত্রে প্রাপ্ত। এতে একটি বার্তা হ্যান্ডলার আছে যা বার্তার বিষয়বস্তু প্রিন্ট করে এবং তারপর `AssistantAgent` ডেলিগেট ব্যবহার করে একটি প্রতিক্রিয়া পাঠায়। বিশেষ করে লক্ষ্য করুন কিভাবে আমরা `self._delegate`-কে `AssistantAgent` এর একটি ইনস্ট্যান্স হিসেবে অ্যাসাইন করেছি, যা একটি প্রি-বিল্ট এজেন্ট যা চ্যাট সম্পূর্ণতা পরিচালনা করতে পারে।

    চলুন AutoGen-কে এই এজেন্ট টাইপ সম্পর্কে জানাই এবং প্রোগ্রাম শুরু করি:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    পূর্বের কোডে এজেন্টগুলি রানটাইমে নিবন্ধিত হয় এবং তারপর একটি বার্তা এজেন্টকে পাঠানো হয়, যার ফলে নিম্নলিখিত আউটপুট হয়:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **মাল্টি এজেন্টস**। AutoGen একাধিক এজেন্ট তৈরি করার সমর্থন দেয় যারা একসাথে কাজ করতে পারে জটিল কাজ সম্পাদনের জন্য। এজেন্টরা যোগাযোগ করতে পারে, তথ্য শেয়ার করতে পারে, এবং তাদের কাজ সমন্বয় করতে পারে যাতে সমস্যা আরও দক্ষতার সাথে সমাধান হয়। মাল্টি-এজেন্ট সিস্টেম তৈরি করতে, আপনি বিভিন্ন ধরনের এজেন্ট সংজ্ঞায়িত করতে পারেন যাদের বিশেষায়িত ফাংশন এবং ভূমিকা থাকে, যেমন ডেটা পুনরুদ্ধার, বিশ্লেষণ, সিদ্ধান্ত গ্রহণ, এবং ব্যবহারকারী ইন্টারঅ্যাকশন। চলুন দেখি এরকম একটি সৃষ্টির উদাহরণ:

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

    পূর্বের কোডে একটি `GroupChatManager` আছে যা রানটাইমে নিবন্ধিত। এই ম্যানেজারটি বিভিন্ন ধরনের এজেন্টের মধ্যে ইন্টারঅ্যাকশন সমন্বয় করার জন্য দায়ী, যেমন লেখক, চিত্রশিল্পী, সম্পাদক, এবং ব্যবহারকারী।

- **এজেন্ট রানটাইম**। ফ্রেমওয়ার্ক একটি রানটাইম পরিবেশ প্রদান করে, যা এজেন্টদের মধ্যে যোগাযোগ সক্ষম করে, তাদের পরিচয় এবং জীবনচক্র পরিচালনা করে, এবং নিরাপত্তা ও গোপনীয়তা সীমানা প্রয়োগ করে। এর মানে আপনি আপনার এজেন্টগুলোকে একটি নিরাপদ এবং নিয়ন্ত্রিত পরিবেশে চালাতে পারেন, নিশ্চিত করে যে তারা নিরাপদে এবং দক্ষতার সাথে ইন্টারঅ্যাক্ট করতে পারে। এখানে দুটি রানটাইম রয়েছে:
  - **স্ট্যান্ড-অ্যালোন রানটাইম**। এটি একক-প্রক্রিয়া অ্যাপ্লিকেশনের জন্য ভালো, যেখানে সব এজেন্ট একই প্রোগ্রামিং ভাষায় বাস্তবায়িত এবং একই প্রক্রিয়ায় চলে। এটি কিভাবে কাজ করে তার একটি চিত্র এখানে:

অ্যাপ্লিকেশন স্ট্যাক

    *এজেন্টরা বার্তার মাধ্যমে রানটাইমের মাধ্যমে যোগাযোগ করে, এবং রানটাইম এজেন্টদের জীবনচক্র পরিচালনা করে*

  - **বিতরণকৃত এজেন্ট রানটাইম**, এটি মাল্টি-প্রক্রিয়া অ্যাপ্লিকেশনের জন্য উপযুক্ত যেখানে এজেন্টরা বিভিন্ন প্রোগ্রামিং ভাষায় বাস্তবায়িত হতে পারে এবং বিভিন্ন মেশিনে চলতে পারে। এটি কিভাবে কাজ করে তার একটি চিত্র এখানে:

## Semantic Kernel + Agent Framework

Semantic Kernel হল একটি এন্টারপ্রাইজ-রেডি AI অর্কেস্ট্রেশন SDK। এটি AI এবং মেমরি কানেক্টরসহ একটি এজেন্ট ফ্রেমওয়ার্ক নিয়ে গঠিত।

প্রথমে কিছু মূল উপাদান কভার করি:

- **AI কানেক্টরস**: এটি বাইরের AI সার্ভিস এবং ডেটা সোর্সের সাথে ইন্টারফেস, যা Python এবং C# উভয়ের জন্য ব্যবহৃত হয়।

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

    এখানে একটি সহজ উদাহরণ আছে যেখানে আপনি একটি kernel তৈরি করেন এবং একটি চ্যাট সম্পূর্ণতা সার্ভিস যোগ করেন। Semantic Kernel একটি বাইরের AI সার্ভিসের সাথে সংযোগ তৈরি করে, এই ক্ষেত্রে Azure OpenAI Chat Completion।

- **প্লাগইনস**: এগুলো এমন ফাংশনগুলোকে আবৃত করে যা একটি অ্যাপ্লিকেশন ব্যবহার করতে পারে। এখানে প্রস্তুত-প্লাগইন এবং কাস্টম প্লাগইন উভয়ই থাকতে পারে। একটি সম্পর্কিত ধারণা হল "prompt functions"। ফাংশন কল করার জন্য প্রাকৃতিক ভাষার সংকেত দেওয়ার পরিবর্তে, আপনি মডেলের কাছে নির্দিষ্ট ফাংশনগুলো সম্প্রচার করেন। বর্তমান চ্যাট প্রসঙ্গের ভিত্তিতে, মডেল একটি অনুরোধ বা প্রশ্ন সম্পূর্ণ করার জন্য এই ফাংশনগুলোর মধ্যে একটি কল করতে পারে। উদাহরণ:

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

    এখানে, প্রথমে একটি টেমপ্লেট প্রম্পট `skPrompt` আছে যা ব্যবহারকারীর ইনপুট `$userInput` এর জন্য জায়গা রাখে। তারপর আপনি kernel ফাংশন `SummarizeText` তৈরি করেন এবং এটি `SemanticFunctions` নামে প্লাগইন হিসেবে kernel-এ ইম্পোর্ট করেন। ফাংশনের নাম লক্ষ্য করুন যা Semantic Kernel-কে সাহায্য করে বুঝতে ফাংশনটি কী করে এবং কখন কল করা উচিত।

- **নেটিভ ফাংশন**: ফ্রেমওয়ার্কের এমন নেটিভ ফাংশনও আছে যা সরাসরি কাজ সম্পাদনের জন্য কল করা যায়। এখানে একটি উদাহরণ যেখানে একটি ফাইল থেকে কনটেন্ট রিট্রিভ করা হচ্ছে:

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

- **মেমরি**: AI অ্যাপের জন্য প্রসঙ্গ ব্যবস্থাপনাকে বিমূর্ত এবং সহজ করে তোলে। মেমরির ধারণা হল এটি এমন কিছু যা LLM-কে জানা উচিত। আপনি এই তথ্য একটি ভেক্টর স্টোরে সংরক্ষণ করতে পারেন যা একটি ইন-মেমরি ডাটাবেস, ভেক্টর ডাটাবেস বা অনুরূপ হতে পারে। এখানে একটি খুব সরলীকৃত দৃশ্য যেখানে *তথ্য* মেমরিতে যোগ করা হচ্ছে:

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

    এই তথ্যগুলো মেমরি কালেকশন `SummarizedAzureDocs`-এ সংরক্ষিত হয়। এটি একটি খুব সরল উদাহরণ, তবে আপনি দেখতে পাচ্ছেন কিভাবে তথ্য মেমরিতে সংরক্ষণ করা যায় যাতে LLM এটি ব্যবহার করতে পারে।
## পূর্ববর্তী পাঠ

[AI এজেন্ট এবং এজেন্ট ব্যবহারের পরিচিতি](../01-intro-to-ai-agents/README.md)

## পরবর্তী পাঠ

[এজেন্টিক ডিজাইন প্যাটার্ন বোঝা](../03-agentic-design-patterns/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।