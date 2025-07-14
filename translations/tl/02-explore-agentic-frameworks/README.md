<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:08:22+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "tl"
}
-->
. Ayon sa Wikipedia, ang actor ay _ang pangunahing yunit ng sabayang komputasyon. Bilang tugon sa isang mensaheng natanggap nito, ang isang actor ay maaaring: gumawa ng lokal na desisyon, lumikha ng mas maraming actor, magpadala ng mas maraming mensahe, at tukuyin kung paano tutugon sa susunod na mensaheng matatanggap_.

**Mga Gamit**: Pag-automate ng pagbuo ng code, mga gawain sa pagsusuri ng datos, at paglikha ng mga custom na ahente para sa pagpaplano at pananaliksik.

Narito ang ilang mahahalagang pangunahing konsepto ng AutoGen:

- **Mga Ahente**. Ang isang ahente ay isang software entity na:
  - **Nakikipag-ugnayan sa pamamagitan ng mga mensahe**, maaaring synchronous o asynchronous ang mga ito.
  - **Pinananatili ang sariling estado**, na maaaring mabago ng mga papasok na mensahe.
  - **Gumagawa ng mga aksyon** bilang tugon sa mga natanggap na mensahe o pagbabago sa estado nito. Ang mga aksyong ito ay maaaring magbago sa estado ng ahente at magdulot ng mga panlabas na epekto, tulad ng pag-update ng mga log ng mensahe, pagpapadala ng bagong mga mensahe, pagpapatupad ng code, o paggawa ng mga tawag sa API.
    
  Narito ang isang maikling snippet ng code kung saan maaari kang gumawa ng sarili mong ahente na may kakayahan sa Chat:

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
    
    Sa naunang code, ang `MyAssistant` ay nilikha at nagmana mula sa `RoutedAgent`. Mayroon itong message handler na nagpi-print ng nilalaman ng mensahe at pagkatapos ay nagpapadala ng tugon gamit ang `AssistantAgent` delegate. Pansinin lalo na kung paano namin iniaassign sa `self._delegate` ang isang instance ng `AssistantAgent` na isang pre-built na ahente na kayang humawak ng chat completions.

    Ipaalam natin sa AutoGen ang tungkol sa uri ng ahenteng ito at simulan ang programa:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Sa naunang code, ang mga ahente ay nirehistro sa runtime at pagkatapos ay isang mensahe ang ipinadala sa ahente na nagreresulta sa sumusunod na output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Maramihang mga ahente**. Sinusuportahan ng AutoGen ang paglikha ng maraming ahente na maaaring magtulungan upang makamit ang mga kumplikadong gawain. Ang mga ahente ay maaaring mag-ugnayan, magbahagi ng impormasyon, at mag-coordinate ng kanilang mga aksyon upang mas epektibong malutas ang mga problema. Upang makagawa ng multi-agent system, maaari kang magtakda ng iba't ibang uri ng mga ahente na may mga espesyalisadong tungkulin at papel, tulad ng pagkuha ng datos, pagsusuri, paggawa ng desisyon, at pakikipag-ugnayan sa gumagamit. Tingnan natin kung paano ito ginagawa:

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

    Sa naunang code, mayroon tayong `GroupChatManager` na narehistro sa runtime. Ang manager na ito ang responsable sa pag-coordinate ng mga interaksyon sa pagitan ng iba't ibang uri ng mga ahente, tulad ng mga manunulat, ilustrador, editor, at mga gumagamit.

- **Agent Runtime**. Nagbibigay ang framework ng runtime environment na nagpapahintulot sa komunikasyon sa pagitan ng mga ahente, pinamamahalaan ang kanilang mga pagkakakilanlan at lifecycle, at nagpapatupad ng mga hangganan sa seguridad at privacy. Ibig sabihin nito, maaari mong patakbuhin ang iyong mga ahente sa isang ligtas at kontroladong kapaligiran, na tinitiyak na maaari silang makipag-ugnayan nang ligtas at epektibo. May dalawang uri ng runtime na mahalaga:
  - **Stand-alone runtime**. Magandang pagpipilian ito para sa mga single-process na aplikasyon kung saan lahat ng ahente ay ipinatupad sa parehong programming language at tumatakbo sa parehong proseso. Narito ang ilustrasyon kung paano ito gumagana:

Application stack

    *nakikipag-ugnayan ang mga ahente sa pamamagitan ng mga mensahe sa runtime, at pinamamahalaan ng runtime ang lifecycle ng mga ahente*

  - **Distributed agent runtime**, angkop ito para sa mga multi-process na aplikasyon kung saan ang mga ahente ay maaaring ipatupad sa iba't ibang programming language at tumatakbo sa iba't ibang makina. Narito ang ilustrasyon kung paano ito gumagana:

## Semantic Kernel + Agent Framework

Ang Semantic Kernel ay isang enterprise-ready AI Orchestration SDK. Binubuo ito ng mga AI at memory connectors, kasama ang isang Agent Framework.

Unahin nating talakayin ang ilang pangunahing bahagi:

- **AI Connectors**: Ito ay isang interface sa mga panlabas na AI services at mga pinagkukunan ng datos para magamit sa parehong Python at C#.

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

    Narito ang isang simpleng halimbawa kung paano ka makakagawa ng kernel at magdagdag ng chat completion service. Gumagawa ang Semantic Kernel ng koneksyon sa isang panlabas na AI service, sa kasong ito, Azure OpenAI Chat Completion.

- **Plugins**: Ito ay naglalaman ng mga function na maaaring gamitin ng isang aplikasyon. Mayroon nang mga handang plugins at maaari ka ring gumawa ng sarili mong custom plugins. Kaugnay nito ang konsepto ng "prompt functions." Sa halip na magbigay ng natural language cues para sa pagtawag ng function, ipinapadala mo ang ilang mga function sa model. Batay sa kasalukuyang konteksto ng chat, maaaring piliin ng model na tawagan ang isa sa mga function na ito upang kumpletuhin ang isang kahilingan o query. Narito ang isang halimbawa:

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

    Dito, mayroon kang template prompt na `skPrompt` na nag-iiwan ng puwang para sa input ng user, `$userInput`. Pagkatapos ay nilikha mo ang kernel function na `SummarizeText` at ini-import ito sa kernel gamit ang plugin name na `SemanticFunctions`. Pansinin ang pangalan ng function na tumutulong sa Semantic Kernel na maunawaan kung ano ang ginagawa ng function at kailan ito dapat tawagin.

- **Native function**: Mayroon ding mga native function na direktang tinatawag ng framework upang isagawa ang gawain. Narito ang isang halimbawa ng function na kumukuha ng nilalaman mula sa isang file:

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

- **Memory**: Pinapasimple at iniaabstract ang pamamahala ng konteksto para sa mga AI app. Ang ideya sa memory ay ito ay isang bagay na dapat malaman ng LLM. Maaari mong itago ang impormasyong ito sa isang vector store na nagiging isang in-memory database o vector database o katulad nito. Narito ang isang halimbawa ng isang napakasimpleng senaryo kung saan ang mga *facts* ay idinadagdag sa memory:

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

    Ang mga fact na ito ay iniimbak sa memory collection na `SummarizedAzureDocs`. Isang napakasimpleng halimbawa ito, ngunit makikita mo kung paano mo maaaring itago ang impormasyon sa memory para magamit ng LLM.
## Nakaraang Aralin

[Panimula sa AI Agents at Mga Gamit ng Agent](../01-intro-to-ai-agents/README.md)

## Susunod na Aralin

[Pag-unawa sa Agentic Design Patterns](../03-agentic-design-patterns/README.md)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.