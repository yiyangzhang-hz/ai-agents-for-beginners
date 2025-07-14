<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:14:12+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "my"
}
-->
Wikipedia အရ actor ဆိုတာက _အချိန်တပြေးညီတွက်ချက်မှုရဲ့ အခြေခံတည်ဆောက်ပုံတစ်ခုဖြစ်ပါတယ်။ actor တစ်ခုက ရရှိတဲ့ message ကို တုံ့ပြန်ရာမှာ - ဒေသခံဆုံးဖြတ်ချက်တွေချနိုင်တယ်၊ actor အသစ်တွေဖန်တီးနိုင်တယ်၊ message တွေ ပိုပို့နိုင်တယ်၊ နောက်ထပ်ရရှိမယ့် message ကို ဘယ်လိုတုံ့ပြန်မလဲ ဆုံးဖြတ်နိုင်တယ်_ ဆိုတာပါ။

**အသုံးပြုမှုများ**: ကုဒ်ဖန်တီးခြင်းကို အလိုအလျောက်လုပ်ဆောင်ခြင်း၊ ဒေတာခွဲခြမ်းစိတ်ဖြာမှုလုပ်ငန်းများ၊ စီမံကိန်းရေးဆွဲခြင်းနှင့် သုတေသနလုပ်ငန်းများအတွက် စိတ်ကြိုက် agent များ ဖန်တီးခြင်း။

AutoGen ရဲ့ အရေးကြီးသော အခြေခံအယူအဆများမှာ -

- **Agents**။ Agent ဆိုတာက software အဖွဲ့အစည်းတစ်ခုဖြစ်ပြီး -
  - **Message များဖြင့် ဆက်သွယ်တယ်**၊ ဒီ message တွေက synchronous သို့မဟုတ် asynchronous ဖြစ်နိုင်တယ်။
  - **ကိုယ်ပိုင်အခြေအနေကို ထိန်းသိမ်းထားတယ်**၊ ရောက်ရှိလာတဲ့ message များဖြင့် အခြေအနေကို ပြောင်းလဲနိုင်တယ်။
  - **ရရှိတဲ့ message များ သို့မဟုတ် အခြေအနေပြောင်းလဲမှုများအပေါ် တုံ့ပြန်မှုလုပ်ဆောင်တယ်**။ ဒီလုပ်ဆောင်ချက်တွေက agent ရဲ့ အခြေအနေကို ပြောင်းလဲနိုင်ပြီး message မှတ်တမ်းများ update လုပ်ခြင်း၊ message အသစ်ပို့ခြင်း၊ ကုဒ်အကောင်အထည်ဖော်ခြင်း သို့မဟုတ် API ခေါ်ဆိုခြင်း စသည့် ပြင်ပအကျိုးသက်ရောက်မှုများ ဖြစ်စေတတ်သည်။

  ဒီမှာ Chat စွမ်းရည်ပါဝင်တဲ့ ကိုယ်ပိုင် agent တစ်ခု ဖန်တီးထားတဲ့ အတိုချုံးကုဒ်နမူနာရှိပါတယ်-

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
    
    အထက်ပါကုဒ်မှာ `MyAssistant` ကို `RoutedAgent` မှ ဆက်ခံပြီး ဖန်တီးထားပါတယ်။ message handler က message ရဲ့ အကြောင်းအရာကို ပုံနှိပ်ပြီး `AssistantAgent` delegate ကို အသုံးပြုပြီး တုံ့ပြန်ချက်ပို့ပါတယ်။ အထူးသဖြင့် `self._delegate` ကို `AssistantAgent` instance တစ်ခု assign လုပ်ထားတာကို သတိထားပါ၊ ဒါက chat completion ကို ကိုင်တွယ်နိုင်တဲ့ pre-built agent တစ်ခုဖြစ်ပါတယ်။

    AutoGen ကို ဒီ agent အမျိုးအစားအကြောင်း သိရှိစေပြီး အစီအစဉ်ကို စတင်လိုက်ပါ-

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    အထက်ပါကုဒ်မှာ agents တွေကို runtime နဲ့ မှတ်ပုံတင်ပြီး message တစ်ခု ပို့လိုက်တဲ့အခါ အောက်ပါ output ရရှိပါသည်-

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**။ AutoGen က အဆင့်မြင့် လုပ်ငန်းများကို ဖြေရှင်းနိုင်ဖို့ အတူတကွ လုပ်ဆောင်နိုင်တဲ့ agent များစွာ ဖန်တီးနိုင်စေပါတယ်။ Agents တွေက ဆက်သွယ်၊ သတင်းအချက်အလက်မျှဝေ၊ လုပ်ဆောင်ချက်များကို ညှိနှိုင်းပြီး ပိုမိုထိရောက်စွာ ပြဿနာများကို ဖြေရှင်းနိုင်ပါတယ်။ Multi-agent system တစ်ခု ဖန်တီးဖို့အတွက် အထူးပြုလုပ်ငန်းများနှင့် တာဝန်များရှိတဲ့ agent အမျိုးအစားများကို သတ်မှတ်နိုင်ပါတယ်၊ ဥပမာ - ဒေတာ ရယူခြင်း၊ ခွဲခြမ်းစိတ်ဖြာခြင်း၊ ဆုံးဖြတ်ချက်ချခြင်း၊ အသုံးပြုသူနှင့် ဆက်သွယ်ခြင်း စသဖြင့်။ ဒီလို ဖန်တီးမှုတစ်ခု ဘယ်လိုပုံစံရှိတယ်ဆိုတာ ကြည့်ကြရအောင်-

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

    အထက်ပါကုဒ်မှာ `GroupChatManager` ကို runtime နဲ့ မှတ်ပုံတင်ထားပြီး ဒီ manager က စာရေးသူများ၊ ပုံဆွဲသူများ၊ တည်းဖြတ်သူများ၊ အသုံးပြုသူများလို အမျိုးအစား agent များအကြား ဆက်သွယ်မှုကို ညှိနှိုင်းတာကို တာဝန်ယူပါတယ်။

- **Agent Runtime**။ Framework က agent များအကြား ဆက်သွယ်မှုကို အထောက်အပံ့ပေးတဲ့ runtime ပတ်ဝန်းကျင်ကို ပံ့ပိုးပေးပြီး agent များ၏ အတည်ပြုချက်နှင့် အသက်တာကာလကို စီမံခန့်ခွဲပေးပါတယ်၊ လုံခြုံရေးနှင့် ကိုယ်ရေးကိုယ်တာ အကာအကွယ်များကိုလည်း ထိန်းသိမ်းပေးပါတယ်။ ဒါက သင့် agent များကို လုံခြုံပြီး ထိန်းချုပ်ထားတဲ့ ပတ်ဝန်းကျင်မှာ လည်ပတ်နိုင်စေပါတယ်။ စိတ်ဝင်စားစရာ runtime နှစ်မျိုးရှိပါတယ်-
  - **Stand-alone runtime**။ ဒီဟာက တစ်ခုတည်းသော process အတွက် သင့်တော်ပြီး agent အားလုံးကို တူညီတဲ့ programming language နဲ့ တူညီတဲ့ process ထဲမှာ လည်ပတ်စေချင်တဲ့အခါ အသုံးပြုနိုင်ပါတယ်။ အလုပ်လုပ်ပုံကို အောက်ပါပုံစံနဲ့ ဖော်ပြထားပါတယ်-

Application stack

    *agents တွေက runtime မှတဆင့် message များဖြင့် ဆက်သွယ်ပြီး runtime က agent များ၏ အသက်တာကာလကို စီမံခန့်ခွဲတယ်*

  - **Distributed agent runtime** ကတော့ multi-process application များအတွက် သင့်တော်ပြီး agent များကို programming language မတူညီတဲ့ အခြားစက်များပေါ်မှာ လည်ပတ်စေချင်တဲ့အခါ အသုံးပြုနိုင်ပါတယ်။ အလုပ်လုပ်ပုံကို အောက်ပါပုံစံနဲ့ ဖော်ပြထားပါတယ်-

## Semantic Kernel + Agent Framework

Semantic Kernel ဆိုတာ ကုမ္ပဏီအသုံးပြုရန် အသင့်ပြင် AI Orchestration SDK တစ်ခုဖြစ်ပါတယ်။ AI နှင့် memory connectors တွေနဲ့ Agent Framework ပါဝင်ပါတယ်။

အရင်ဆုံး အခြေခံအစိတ်အပိုင်းများကို ဖော်ပြပါမယ်-

- **AI Connectors**: Python နဲ့ C# နှစ်ခုလုံးမှာ အသုံးပြုနိုင်တဲ့ ပြင်ပ AI ဝန်ဆောင်မှုများနှင့် ဒေတာရင်းမြစ်များကို ဆက်သွယ်ဖို့ အင်တာဖေ့စ်ဖြစ်ပါတယ်။

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

    ဒီမှာ kernel တစ်ခု ဖန်တီးပြီး chat completion ဝန်ဆောင်မှုကို ထည့်သွင်းထားတဲ့ ရိုးရှင်းတဲ့ နမူနာကို တွေ့ရမှာဖြစ်ပါတယ်။ Semantic Kernel က Azure OpenAI Chat Completion ဆိုတဲ့ ပြင်ပ AI ဝန်ဆောင်မှုနဲ့ ချိတ်ဆက်ထားပါတယ်။

- **Plugins**: Application က အသုံးပြုနိုင်တဲ့ function များကို ထုပ်ပိုးထားတာဖြစ်ပြီး၊ ရှိပြီးသား plugins တွေနဲ့ ကိုယ်တိုင် ဖန်တီးနိုင်တဲ့ plugins နှစ်မျိုးရှိပါတယ်။ "prompt functions" ဆိုတဲ့ အယူအဆလည်း ရှိပြီး၊ function ကို ခေါ်ရန် သဘာဝဘာသာစကား အညွှန်းများ ပေးခြင်းမဟုတ်ဘဲ၊ function တချို့ကို မော်ဒယ်ထံ ပေးပို့ထားပါတယ်။ လက်ရှိ chat context အပေါ် မူတည်ပြီး မော်ဒယ်က ဒီ function တွေထဲမှ တစ်ခုကို ရွေးချယ်ခေါ်နိုင်ပါတယ်။ ဥပမာ-

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

    ဒီမှာ `skPrompt` ဆိုတဲ့ template prompt ရှိပြီး အသုံးပြုသူရဲ့ input `$userInput` အတွက် နေရာထားပေးထားပါတယ်။ ပြီးတော့ `SummarizeText` ဆိုတဲ့ kernel function ကို ဖန်တီးပြီး `SemanticFunctions` ဆိုတဲ့ plugin နာမည်နဲ့ kernel ထဲသို့ import လုပ်ထားပါတယ်။ function နာမည်က Semantic Kernel ကို function ရဲ့ အလုပ်လုပ်ပုံနဲ့ ဘယ်အချိန်ခေါ်သင့်တယ်ဆိုတာ နားလည်စေပါတယ်။

- **Native function**: Framework က တိုက်ရိုက်ခေါ်နိုင်တဲ့ native function တွေပါရှိပြီး၊ ဥပမာ ဖိုင်ထဲက အကြောင်းအရာကို ရယူတဲ့ function တစ်ခု-

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

- **Memory**: AI app များအတွက် context စီမံခန့်ခွဲမှုကို ရိုးရှင်းပြီး abstraction ပေးပါတယ်။ Memory ဆိုတာ LLM က သိထားသင့်တဲ့ အချက်အလက်တွေကို သိမ်းဆည်းထားတာဖြစ်ပါတယ်။ ဒီအချက်အလက်တွေကို vector store တစ်ခုမှာ သိမ်းဆည်းနိုင်ပြီး၊ ဒါက in-memory database သို့မဟုတ် vector database တစ်ခုလို ဖြစ်ပါတယ်။ အောက်မှာ *facts* တွေကို memory ထဲ ထည့်သွင်းထားတဲ့ ရိုးရှင်းတဲ့ နမူနာတစ်ခုရှိပါတယ်-

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

    ဒီ facts တွေကို `SummarizedAzureDocs` ဆိုတဲ့ memory collection ထဲ သိမ်းဆည်းထားပါတယ်။ ဒီဟာက ရိုးရှင်းတဲ့ နမူနာတစ်ခုဖြစ်ပေမယ့် LLM အတွက် အသုံးပြုဖို့ အချက်အလက်တွေကို memory ထဲ သိမ်းဆည်းနိုင်တာကို မြင်တွေ့နိုင်ပါတယ်။
## ယခင်သင်ခန်းစာ

[AI Agent များနှင့် Agent အသုံးပြုမှုများအကြောင်းအကျဉ်း](../01-intro-to-ai-agents/README.md)

## နောက်တစ်ခုသင်ခန်းစာ

[Agentic ဒီဇိုင်းပုံစံများကိုနားလည်ခြင်း](../03-agentic-design-patterns/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းသည် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။