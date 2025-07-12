<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:57:00+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hi"
}
-->
. विकिपीडिया के अनुसार, एक अभिनेता _समानांतर गणना की मूलभूत इकाई है। प्राप्त संदेश के जवाब में, एक अभिनेता कर सकता है: स्थानीय निर्णय लेना, अधिक अभिनेता बनाना, अधिक संदेश भेजना, और प्राप्त अगले संदेश का उत्तर कैसे देना है यह निर्धारित करना_।

**उपयोग के मामले**: कोड जनरेशन को स्वचालित करना, डेटा विश्लेषण कार्य, और योजना और अनुसंधान कार्यों के लिए कस्टम एजेंट बनाना।

यहाँ AutoGen के कुछ महत्वपूर्ण मूलभूत अवधारणाएँ हैं:

- **एजेंट्स**। एक एजेंट एक सॉफ़्टवेयर इकाई है जो:
  - **संदेशों के माध्यम से संवाद करता है**, ये संदेश सिंक्रोनस या असिंक्रोनस हो सकते हैं।
  - **अपनी स्थिति बनाए रखता है**, जिसे आने वाले संदेशों द्वारा संशोधित किया जा सकता है।
  - **प्राप्त संदेशों या अपनी स्थिति में बदलाव के जवाब में क्रियाएँ करता है**। ये क्रियाएँ एजेंट की स्थिति को बदल सकती हैं और बाहरी प्रभाव उत्पन्न कर सकती हैं, जैसे संदेश लॉग अपडेट करना, नए संदेश भेजना, कोड निष्पादित करना, या API कॉल करना।
    
  यहाँ एक छोटा कोड स्निपेट है जिसमें आप चैट क्षमताओं के साथ अपना खुद का एजेंट बना सकते हैं:

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
    
    पिछले कोड में, `MyAssistant` बनाया गया है और यह `RoutedAgent` से विरासत में मिला है। इसमें एक संदेश हैंडलर है जो संदेश की सामग्री को प्रिंट करता है और फिर `AssistantAgent` डेलीगेट का उपयोग करके प्रतिक्रिया भेजता है। विशेष रूप से ध्यान दें कि हम `self._delegate` को `AssistantAgent` के एक उदाहरण के रूप में असाइन करते हैं, जो एक पूर्व-निर्मित एजेंट है जो चैट पूर्णताओं को संभाल सकता है।

    अब AutoGen को इस एजेंट प्रकार के बारे में सूचित करें और प्रोग्राम शुरू करें:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    पिछले कोड में एजेंट्स को रनटाइम के साथ पंजीकृत किया गया है और फिर एजेंट को एक संदेश भेजा गया है, जिसके परिणामस्वरूप निम्नलिखित आउटपुट आता है:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **मल्टी एजेंट्स**। AutoGen कई एजेंट्स के निर्माण का समर्थन करता है जो मिलकर जटिल कार्यों को पूरा कर सकते हैं। एजेंट्स संवाद कर सकते हैं, जानकारी साझा कर सकते हैं, और अपने कार्यों का समन्वय कर सकते हैं ताकि समस्याओं को अधिक कुशलता से हल किया जा सके। मल्टी-एजेंट सिस्टम बनाने के लिए, आप विभिन्न प्रकार के एजेंट्स को परिभाषित कर सकते हैं जिनके पास विशिष्ट कार्य और भूमिकाएँ होती हैं, जैसे डेटा पुनःप्राप्ति, विश्लेषण, निर्णय लेना, और उपयोगकर्ता इंटरैक्शन। आइए देखें कि ऐसा निर्माण कैसा दिखता है:

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

    पिछले कोड में हमारे पास एक `GroupChatManager` है जो रनटाइम के साथ पंजीकृत है। यह मैनेजर विभिन्न प्रकार के एजेंट्स के बीच इंटरैक्शन का समन्वय करता है, जैसे लेखक, चित्रकार, संपादक, और उपयोगकर्ता।

- **एजेंट रनटाइम**। यह फ्रेमवर्क एक रनटाइम वातावरण प्रदान करता है, जो एजेंट्स के बीच संचार सक्षम करता है, उनकी पहचान और जीवनचक्र का प्रबंधन करता है, और सुरक्षा और गोपनीयता सीमाओं को लागू करता है। इसका मतलब है कि आप अपने एजेंट्स को एक सुरक्षित और नियंत्रित वातावरण में चला सकते हैं, यह सुनिश्चित करते हुए कि वे सुरक्षित और कुशलता से इंटरैक्ट कर सकें। दो प्रकार के रनटाइम हैं:
  - **स्टैंड-अलोन रनटाइम**। यह एकल-प्रक्रिया अनुप्रयोगों के लिए अच्छा विकल्प है जहाँ सभी एजेंट्स एक ही प्रोग्रामिंग भाषा में लागू होते हैं और एक ही प्रक्रिया में चलते हैं। यह काम कैसे करता है इसका एक चित्रण यहाँ है:

एप्लिकेशन स्टैक

    *एजेंट्स रनटाइम के माध्यम से संदेशों के जरिए संवाद करते हैं, और रनटाइम एजेंट्स के जीवनचक्र का प्रबंधन करता है*

  - **वितरित एजेंट रनटाइम**, यह बहु-प्रक्रिया अनुप्रयोगों के लिए उपयुक्त है जहाँ एजेंट्स विभिन्न प्रोग्रामिंग भाषाओं में लागू हो सकते हैं और विभिन्न मशीनों पर चल रहे होते हैं। यह काम कैसे करता है इसका एक चित्रण यहाँ है:

## Semantic Kernel + Agent Framework

Semantic Kernel एक एंटरप्राइज-तैयार AI ऑर्केस्ट्रेशन SDK है। इसमें AI और मेमोरी कनेक्टर्स के साथ एक एजेंट फ्रेमवर्क शामिल है।

पहले कुछ मुख्य घटकों को कवर करते हैं:

- **AI कनेक्टर्स**: यह बाहरी AI सेवाओं और डेटा स्रोतों के साथ इंटरफ़ेस है, जो Python और C# दोनों में उपयोग के लिए है।

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

    यहाँ एक सरल उदाहरण है कि आप कैसे एक kernel बना सकते हैं और एक चैट पूर्णता सेवा जोड़ सकते हैं। Semantic Kernel एक बाहरी AI सेवा से कनेक्शन बनाता है, इस मामले में Azure OpenAI Chat Completion।

- **प्लगइन्स**: ये उन कार्यों को संलग्न करते हैं जिन्हें एक एप्लिकेशन उपयोग कर सकता है। कुछ रेडीमेड प्लगइन्स होते हैं और कुछ आप खुद बना सकते हैं। एक संबंधित अवधारणा है "प्रॉम्प्ट फंक्शंस"। प्राकृतिक भाषा संकेतों के बजाय, आप मॉडल को कुछ कार्य प्रसारित करते हैं। वर्तमान चैट संदर्भ के आधार पर, मॉडल इन कार्यों में से किसी एक को कॉल कर सकता है ताकि अनुरोध या क्वेरी पूरी हो सके। यहाँ एक उदाहरण है:

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

    यहाँ, आपके पास पहले एक टेम्पलेट प्रॉम्प्ट `skPrompt` है जो उपयोगकर्ता के इनपुट के लिए जगह छोड़ता है, `$userInput`। फिर आप kernel फ़ंक्शन `SummarizeText` बनाते हैं और इसे `SemanticFunctions` नाम के प्लगइन के साथ kernel में आयात करते हैं। उस फ़ंक्शन के नाम पर ध्यान दें जो Semantic Kernel को यह समझने में मदद करता है कि फ़ंक्शन क्या करता है और इसे कब कॉल किया जाना चाहिए।

- **नेटिव फंक्शन**: ऐसे नेटिव फंक्शंस भी होते हैं जिन्हें फ्रेमवर्क सीधे कॉल कर सकता है कार्य पूरा करने के लिए। यहाँ एक उदाहरण है जो फ़ाइल से सामग्री पुनःप्राप्त करता है:

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

- **मेमोरी**: AI ऐप्स के लिए संदर्भ प्रबंधन को अमूर्त और सरल बनाता है। मेमोरी का विचार यह है कि यह कुछ ऐसी जानकारी है जिसे LLM को जानना चाहिए। आप इस जानकारी को वेक्टर स्टोर में संग्रहित कर सकते हैं, जो अंततः एक इन-मेमोरी डेटाबेस या वेक्टर डेटाबेस या समान होता है। यहाँ एक बहुत ही सरल परिदृश्य का उदाहरण है जहाँ *तथ्य* मेमोरी में जोड़े जाते हैं:

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

    ये तथ्य फिर मेमोरी संग्रह `SummarizedAzureDocs` में संग्रहित होते हैं। यह एक बहुत ही सरल उदाहरण है, लेकिन आप देख सकते हैं कि आप LLM के उपयोग के लिए जानकारी मेमोरी में कैसे स्टोर कर सकते हैं।
## पिछला पाठ

[AI एजेंट्स और एजेंट उपयोग मामलों का परिचय](../01-intro-to-ai-agents/README.md)

## अगला पाठ

[एजेंटिक डिज़ाइन पैटर्न को समझना](../03-agentic-design-patterns/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।