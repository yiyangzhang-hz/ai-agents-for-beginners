<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:58:05+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "mr"
}
-->
. विकिपीडियानुसार, एक अभिनेता हा _सामयिक संगणनाचा मूलभूत घटक आहे. त्याला प्राप्त झालेल्या संदेशाच्या प्रतिसादात, अभिनेता: स्थानिक निर्णय घेऊ शकतो, अधिक अभिनेते तयार करू शकतो, अधिक संदेश पाठवू शकतो, आणि पुढील प्राप्त होणाऱ्या संदेशाला कसे प्रतिसाद द्यायचे हे ठरवू शकतो_.

**वापर प्रकरणे**: कोड निर्मितीचे स्वयंचलन, डेटा विश्लेषण कार्ये, आणि नियोजन व संशोधन कार्यांसाठी सानुकूल अभिनेते तयार करणे.

AutoGen चे काही महत्त्वाचे मूलभूत संकल्पना येथे आहेत:

- **अभिनेते**. एक अभिनेता हा सॉफ्टवेअर घटक आहे जो:
  - **संदेशांद्वारे संवाद साधतो**, हे संदेश समकालीन किंवा असमकालीन असू शकतात.
  - **त्याची स्वतःची स्थिती राखतो**, जी येणाऱ्या संदेशांद्वारे बदलू शकते.
  - **प्राप्त संदेशांवर किंवा स्थितीतील बदलांवर क्रिया करतो**. या क्रिया अभिनेतेची स्थिती बदलू शकतात आणि बाह्य परिणाम निर्माण करू शकतात, जसे की संदेश लॉग अद्ययावत करणे, नवीन संदेश पाठवणे, कोड चालवणे, किंवा API कॉल करणे.
    
  येथे एक लहान कोड स्निपेट आहे ज्यात तुम्ही Chat क्षमतांसह तुमचा स्वतःचा अभिनेता तयार करता:

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
    
    मागील कोडमध्ये, `MyAssistant` तयार केला गेला आहे आणि `RoutedAgent` कडून वारसा घेतो. त्यात एक संदेश हँडलर आहे जो संदेशाचा मजकूर छापतो आणि नंतर `AssistantAgent` प्रतिनिधी वापरून प्रतिसाद पाठवतो. विशेषतः लक्षात घ्या की आपण `self._delegate` ला `AssistantAgent` चा एक उदाहरण देतो, जो एक पूर्वनिर्मित अभिनेता आहे जो चॅट पूर्णता हाताळू शकतो.

    AutoGen ला या अभिनेता प्रकाराबद्दल कळवू आणि पुढील प्रोग्राम सुरू करूया:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    मागील कोडमध्ये अभिनेते रनटाइमसह नोंदणीकृत केले जातात आणि नंतर अभिनेतेला संदेश पाठवला जातो ज्यामुळे खालील आउटपुट मिळते:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **अनेक अभिनेते**. AutoGen अनेक अभिनेते तयार करण्यास समर्थन देते जे एकत्र काम करू शकतात आणि जटिल कार्ये साध्य करू शकतात. अभिनेते संवाद साधू शकतात, माहिती शेअर करू शकतात, आणि त्यांच्या क्रिया समन्वयित करू शकतात ज्यामुळे समस्या अधिक कार्यक्षमतेने सोडवता येतात. बहु-अभिनेते प्रणाली तयार करण्यासाठी, तुम्ही वेगवेगळ्या प्रकारचे अभिनेते परिभाषित करू शकता ज्यांना विशिष्ट कार्ये आणि भूमिका असतात, जसे की डेटा पुनर्प्राप्ती, विश्लेषण, निर्णय घेणे, आणि वापरकर्ता संवाद. अशा निर्मितीचा एक दृष्टांत पाहूया:

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

    मागील कोडमध्ये `GroupChatManager` आहे जो रनटाइमसह नोंदणीकृत आहे. हा व्यवस्थापक वेगवेगळ्या प्रकारच्या अभिनेते जसे की लेखक, चित्रकार, संपादक, आणि वापरकर्त्यांमधील संवाद समन्वयित करण्यासाठी जबाबदार आहे.

- **अभिनेते रनटाइम**. हा फ्रेमवर्क एक रनटाइम वातावरण प्रदान करतो, जे अभिनेते यांच्यातील संवाद सक्षम करते, त्यांची ओळख आणि जीवनचक्र व्यवस्थापित करते, आणि सुरक्षा व गोपनीयता सीमा लागू करते. याचा अर्थ असा की तुम्ही तुमचे अभिनेते सुरक्षित आणि नियंत्रित वातावरणात चालवू शकता, जेणेकरून ते सुरक्षित आणि कार्यक्षमपणे संवाद साधू शकतील. दोन प्रकारचे रनटाइम आहेत:
  - **स्वतंत्र रनटाइम**. हे एकच प्रक्रिया असलेल्या अनुप्रयोगांसाठी चांगला पर्याय आहे जिथे सर्व अभिनेते एकाच प्रोग्रामिंग भाषेत अंमलात आणले जातात आणि एकाच प्रक्रियेत चालतात. हे कसे कार्य करते याचे एक चित्रण येथे आहे:

अ‍ॅप्लिकेशन स्टॅक

    *अभिनेते संदेशांद्वारे रनटाइमशी संवाद साधतात, आणि रनटाइम अभिनेतेच्या जीवनचक्राचे व्यवस्थापन करतो*

  - **वितरित अभिनेते रनटाइम**, हे बहु-प्रक्रिया अनुप्रयोगांसाठी योग्य आहे जिथे अभिनेते वेगवेगळ्या प्रोग्रामिंग भाषांमध्ये अंमलात आणले जाऊ शकतात आणि वेगवेगळ्या संगणकांवर चालू शकतात. हे कसे कार्य करते याचे एक चित्रण येथे आहे:

## Semantic Kernel + Agent Framework

Semantic Kernel हा एंटरप्राइझ-तयार AI ऑर्केस्ट्रेशन SDK आहे. यात AI आणि मेमरी कनेक्टर्स तसेच एक अभिनेते फ्रेमवर्क आहे.

आता काही मूलभूत घटक पाहूया:

- **AI कनेक्टर्स**: हे बाह्य AI सेवा आणि डेटा स्रोतांसाठी एक इंटरफेस आहे, जे Python आणि C# दोन्हीमध्ये वापरता येते.

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

    येथे एक सोपा उदाहरण आहे ज्यात तुम्ही एक कर्नेल तयार करता आणि चॅट पूर्णता सेवा जोडता. Semantic Kernel बाह्य AI सेवेशी कनेक्शन तयार करतो, या प्रकरणात Azure OpenAI Chat Completion शी.

- **प्लगइन्स**: हे अशा फंक्शन्सला समाविष्ट करतात जे अनुप्रयोग वापरू शकतो. तयार केलेले प्लगइन्स तसेच तुम्ही स्वतः तयार करू शकता असे कस्टम प्लगइन्स आहेत. एक संबंधित संकल्पना म्हणजे "प्रॉम्प्ट फंक्शन्स." फंक्शन कॉलसाठी नैसर्गिक भाषा संकेत देण्याऐवजी, तुम्ही काही फंक्शन्स मॉडेलला प्रसारित करता. चालू चॅट संदर्भानुसार, मॉडेल या फंक्शन्सपैकी एक कॉल करण्याचा निर्णय घेऊ शकते जेणेकरून विनंती किंवा चौकशी पूर्ण करता येईल. येथे एक उदाहरण आहे:

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

    येथे, प्रथम तुम्हाला एक टेम्पलेट प्रॉम्प्ट `skPrompt` आहे ज्यात वापरकर्त्याला मजकूर इनपुट करण्यासाठी जागा दिली आहे, `$userInput`. नंतर तुम्ही कर्नेल फंक्शन `SummarizeText` तयार करता आणि नंतर ते `SemanticFunctions` नावाच्या प्लगइनसह कर्नेलमध्ये आयात करता. फंक्शनचे नाव लक्षात ठेवा जे Semantic Kernel ला समजण्यास मदत करते की फंक्शन काय करते आणि कधी कॉल करावे.

- **नेटिव्ह फंक्शन**: असेही नेटिव्ह फंक्शन्स आहेत जे फ्रेमवर्क थेट कॉल करू शकते कार्य पार पाडण्यासाठी. येथे एक उदाहरण आहे जे फाइलमधून सामग्री प्राप्त करते:

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

- **मेमरी**: AI अनुप्रयोगांसाठी संदर्भ व्यवस्थापन सुलभ करते आणि संक्षिप्त करते. मेमरीचा विचार असा आहे की LLM ला ही माहिती माहित असावी. तुम्ही ही माहिती व्हेक्टर स्टोअरमध्ये साठवू शकता, जी अंततः एक इन-मेमरी डेटाबेस किंवा व्हेक्टर डेटाबेस किंवा तत्सम असू शकते. येथे एक अतिशय सोपा उदाहरण आहे जिथे *तथ्ये* मेमरीमध्ये जोडली जातात:

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

    ही तथ्ये नंतर `SummarizedAzureDocs` मेमरी संग्रहात साठवली जातात. हे एक अतिशय सोपे उदाहरण आहे, पण तुम्ही पाहू शकता की कसे तुम्ही LLM साठी वापरण्यासाठी माहिती मेमरीमध्ये साठवू शकता.
## मागील धडा

[AI एजंट्स आणि एजंट वापर प्रकरणांची ओळख](../01-intro-to-ai-agents/README.md)

## पुढील धडा

[एजंटिक डिझाइन पॅटर्न समजून घेणे](../03-agentic-design-patterns/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.