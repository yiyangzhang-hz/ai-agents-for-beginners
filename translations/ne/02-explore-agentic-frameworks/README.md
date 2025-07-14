<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:58:38+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ne"
}
-->
। विकिपिडियाका अनुसार, एक अभिनेता _समानान्तर गणनाको आधारभूत निर्माण ब्लक हो। प्राप्त सन्देशको प्रतिक्रियामा, एक अभिनेता गर्न सक्छ: स्थानीय निर्णयहरू लिन, थप अभिनेता सिर्जना गर्न, थप सन्देशहरू पठाउन, र प्राप्त हुने अर्को सन्देशमा कसरी प्रतिक्रिया दिने निर्धारण गर्न_।

**प्रयोगका केसहरू**: कोड उत्पादन स्वचालन, डाटा विश्लेषण कार्यहरू, र योजना तथा अनुसन्धान कार्यहरूको लागि अनुकूलित एजेन्टहरू निर्माण।

यहाँ AutoGen का केही महत्वपूर्ण मूल अवधारणाहरू छन्:

- **एजेन्टहरू**। एक एजेन्ट सफ्टवेयर इकाई हो जुन:
  - **सन्देशहरू मार्फत सञ्चार गर्छ**, यी सन्देशहरू समकालीन वा असमकालीन हुन सक्छन्।
  - **आफ्नो अवस्था कायम राख्छ**, जुन आउने सन्देशहरूले परिवर्तन गर्न सक्छन्।
  - **प्राप्त सन्देशहरू वा आफ्नो अवस्थाको परिवर्तनमा प्रतिक्रिया स्वरूप कार्यहरू गर्छ**। यी कार्यहरूले एजेन्टको अवस्था परिवर्तन गर्न सक्छन् र बाह्य प्रभावहरू उत्पन्न गर्न सक्छन्, जस्तै सन्देश लग अपडेट गर्नु, नयाँ सन्देश पठाउनु, कोड कार्यान्वयन गर्नु, वा API कलहरू गर्नु।
    
  यहाँ एउटा सानो कोड स्निपेट छ जसमा तपाईंले आफ्नै च्याट क्षमतासहितको एजेन्ट सिर्जना गर्न सक्नुहुन्छ:

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
    
    माथिको कोडमा, `MyAssistant` सिर्जना गरिएको छ र `RoutedAgent` बाट उत्तराधिकार प्राप्त गरेको छ। यसमा एउटा सन्देश ह्यान्डलर छ जसले सन्देशको सामग्री प्रिन्ट गर्छ र त्यसपछि `AssistantAgent` डेलिगेट प्रयोग गरी प्रतिक्रिया पठाउँछ। विशेष गरी ध्यान दिनुहोस् कि हामीले `self._delegate` लाई `AssistantAgent` को एउटा उदाहरणमा असाइन गरेका छौं जुन पूर्वनिर्मित एजेन्ट हो र च्याट पूर्णताहरू ह्यान्डल गर्न सक्छ।

    अब AutoGen लाई यस एजेन्ट प्रकारको बारेमा जानकारी दिऔं र कार्यक्रम सुरु गरौं:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    माथिको कोडमा एजेन्टहरू रनटाइमसँग दर्ता गरिएका छन् र त्यसपछि एजेन्टलाई सन्देश पठाइन्छ जसको परिणामस्वरूप निम्न आउटपुट प्राप्त हुन्छ:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **बहु एजेन्टहरू**। AutoGen ले धेरै एजेन्टहरू सिर्जना गर्न समर्थन गर्दछ जसले सँगै काम गरेर जटिल कार्यहरू पूरा गर्न सक्छन्। एजेन्टहरूले सञ्चार गर्न, जानकारी साझा गर्न, र आफ्नो कार्यहरू समन्वय गर्न सक्छन् जसले समस्याहरूलाई बढी प्रभावकारी रूपमा समाधान गर्छ। बहु-एजेन्ट प्रणाली सिर्जना गर्न, तपाईंले विभिन्न प्रकारका एजेन्टहरू परिभाषित गर्न सक्नुहुन्छ जसका विशेष कार्यहरू र भूमिकाहरू हुन्छन्, जस्तै डाटा पुनःप्राप्ति, विश्लेषण, निर्णय-निर्माण, र प्रयोगकर्ता अन्तरक्रिया। यस्तो सिर्जना कस्तो देखिन्छ हेर्नुहोस्:

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

    माथिको कोडमा `GroupChatManager` छ जुन रनटाइमसँग दर्ता गरिएको छ। यो प्रबन्धक विभिन्न प्रकारका एजेन्टहरू बीच अन्तरक्रियालाई समन्वय गर्ने जिम्मेवार छ, जस्तै लेखकहरू, चित्रकारहरू, सम्पादकहरू, र प्रयोगकर्ताहरू।

- **एजेन्ट रनटाइम**। फ्रेमवर्कले एक रनटाइम वातावरण प्रदान गर्दछ जसले एजेन्टहरू बीच सञ्चार सक्षम पार्छ, तिनीहरूको पहिचान र जीवनचक्र व्यवस्थापन गर्छ, र सुरक्षा तथा गोपनीयता सीमाहरू लागू गर्छ। यसको अर्थ तपाईंले आफ्नो एजेन्टहरूलाई सुरक्षित र नियन्त्रण गरिएको वातावरणमा चलाउन सक्नुहुन्छ, जसले तिनीहरूलाई सुरक्षित र प्रभावकारी रूपमा अन्तरक्रिया गर्न सक्षम बनाउँछ। यहाँ दुई प्रकारका रनटाइमहरू छन्:
  - **स्ट्यान्ड-अलोन रनटाइम**। यो एकल-प्रक्रिया अनुप्रयोगहरूको लागि राम्रो विकल्प हो जहाँ सबै एजेन्टहरू एउटै प्रोग्रामिङ भाषा प्रयोग गरेर एउटै प्रक्रियामा चलाइन्छन्। यसले कसरी काम गर्छ भन्ने एउटा चित्रण यहाँ छ:

एप्लिकेसन स्ट्याक

    *एजेन्टहरूले रनटाइम मार्फत सन्देशहरू पठाउँछन्, र रनटाइमले एजेन्टहरूको जीवनचक्र व्यवस्थापन गर्छ*

  - **वितरित एजेन्ट रनटाइम**, यो बहु-प्रक्रिया अनुप्रयोगहरूको लागि उपयुक्त छ जहाँ एजेन्टहरू विभिन्न प्रोग्रामिङ भाषाहरूमा कार्यान्वयन हुन सक्छन् र विभिन्न मेसिनहरूमा चलिरहेका हुन्छन्। यसले कसरी काम गर्छ भन्ने एउटा चित्रण यहाँ छ:

## Semantic Kernel + Agent Framework

Semantic Kernel एक उद्यम-तयार AI ऑर्केस्ट्रेशन SDK हो। यसमा AI र मेमोरी कनेक्टर्स छन्, साथै एक एजेन्ट फ्रेमवर्क पनि छ।

पहिले केही मुख्य कम्पोनेन्टहरू कभर गरौं:

- **AI कनेक्टर्स**: यो बाह्य AI सेवाहरू र डाटा स्रोतहरूसँगको इन्टरफेस हो जुन Python र C# दुवैमा प्रयोग गर्न सकिन्छ।

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

    यहाँ एउटा सरल उदाहरण छ जहाँ तपाईंले कर्नेल सिर्जना गरेर च्याट पूर्णता सेवा थप्न सक्नुहुन्छ। Semantic Kernel ले बाह्य AI सेवासँग जडान बनाउँछ, यस अवस्थामा Azure OpenAI Chat Completion।

- **प्लगइन्स**: यीले ती कार्यहरू समेट्छन् जुन अनुप्रयोगले प्रयोग गर्न सक्छ। त्यहाँ तयार प्लगइन्स र तपाईंले सिर्जना गर्न सक्ने अनुकूलित प्लगइन्स दुवै छन्। सम्बन्धित अवधारणा "प्रॉम्प्ट फंक्शन्स" हो। प्राकृतिक भाषा संकेतहरू प्रदान गर्ने सट्टा, तपाईंले मोडेललाई केही कार्यहरू प्रसारण गर्नुहुन्छ। वर्तमान च्याट सन्दर्भको आधारमा, मोडेलले यी कार्यहरू मध्ये कुनै एकलाई कल गर्न सक्छ अनुरोध वा सोधपुछ पूरा गर्न। यहाँ एउटा उदाहरण छ:

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

    यहाँ, तपाईंले पहिले एउटा टेम्प्लेट प्रॉम्प्ट `skPrompt` छ जसले प्रयोगकर्तालाई टेक्स्ट इनपुट गर्न ठाउँ दिन्छ, `$userInput`। त्यसपछि तपाईंले कर्नेल फंक्शन `SummarizeText` सिर्जना गर्नुहुन्छ र त्यसलाई `SemanticFunctions` नामक प्लगइनसँग कर्नेलमा आयात गर्नुहुन्छ। फंक्शनको नामले Semantic Kernel लाई बुझ्न मद्दत गर्छ कि फंक्शनले के गर्छ र कहिले कल गर्नुपर्छ।

- **नेटिभ फंक्शन**: त्यस्ता नेटिभ फंक्शनहरू पनि छन् जुन फ्रेमवर्कले सिधै कल गर्न सक्छ कार्य सम्पन्न गर्न। यहाँ एउटा उदाहरण छ जसले फाइलबाट सामग्री प्राप्त गर्छ:

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

- **मेमोरी**: AI अनुप्रयोगहरूको लागि सन्दर्भ व्यवस्थापनलाई सारांशित र सरल बनाउँछ। मेमोरीको विचार यो हो कि LLM ले यसबारे जान्नुपर्छ। तपाईं यस जानकारीलाई भेक्टर स्टोरमा भण्डारण गर्न सक्नुहुन्छ जुन अन्ततः इन-मेमोरी डाटाबेस वा भेक्टर डाटाबेस वा यस्तै केही हुन्छ। यहाँ एउटा धेरै सरल परिदृश्य छ जहाँ *तथ्यहरू* मेमोरीमा थपिन्छन्:

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

    यी तथ्यहरू पछि मेमोरी संग्रह `SummarizedAzureDocs` मा भण्डारण गरिन्छ। यो एकदम सरल उदाहरण हो, तर तपाईंले देख्न सक्नुहुन्छ कि कसरी तपाईंले LLM को प्रयोगका लागि जानकारी मेमोरीमा भण्डारण गर्न सक्नुहुन्छ।
## अघिल्लो पाठ

[AI एजेन्टहरू र एजेन्ट प्रयोग केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

## अर्को पाठ

[एजेन्टिक डिजाइन ढाँचाहरूको बुझाइ](../03-agentic-design-patterns/README.md)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।