<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:09:07+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sw"
}
-->
. Kulingana na Wikipedia, muigizaji ni _kifungu cha msingi cha uendeshaji wa hesabu sambamba. Kwa kujibu ujumbe unaopokea, muigizaji anaweza: kufanya maamuzi ya ndani, kuunda waigizaji zaidi, kutuma ujumbe zaidi, na kuamua jinsi ya kujibu ujumbe lijalo litakalopokelewa_.

**Matumizi**: Kuendesha utengenezaji wa msimbo wa programu, kazi za uchambuzi wa data, na kujenga waigizaji maalum kwa ajili ya mipango na kazi za utafiti.

Hapa kuna baadhi ya dhana muhimu za msingi za AutoGen:

- **Waigizaji**. Muigizaji ni kiumbe cha programu ambacho:
  - **Huwasiliana kupitia ujumbe**, ujumbe huu unaweza kuwa wa wakati mmoja au wa baadaye.
  - **Huhifadhi hali yake mwenyewe**, ambayo inaweza kubadilishwa na ujumbe unaoingia.
  - **Hufanya vitendo** kama jibu kwa ujumbe unaopokelewa au mabadiliko katika hali yake. Vitendo hivi vinaweza kubadilisha hali ya muigizaji na kusababisha athari za nje, kama vile kusasisha kumbukumbu za ujumbe, kutuma ujumbe mpya, kutekeleza msimbo, au kuita API.
    
  Hapa kuna kipande kifupi cha msimbo ambapo unaunda muigizaji wako mwenye uwezo wa mazungumzo:

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
    
    Katika msimbo uliotangulia, `MyAssistant` imeundwa na inarithi kutoka `RoutedAgent`. Ina mshughulikiaji wa ujumbe anayechapisha maudhui ya ujumbe na kisha kutuma jibu kwa kutumia mwakilishi `AssistantAgent`. Kumbuka hasa jinsi tunavyompa `self._delegate` mfano wa `AssistantAgent` ambaye ni muigizaji aliyejengwa tayari anayeweza kushughulikia ukamilishaji wa mazungumzo.

    Tufahamishe AutoGen kuhusu aina hii ya muigizaji na kuanzisha programu ifuatayo:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Katika msimbo uliotangulia, waigizaji wamesajiliwa na runtime kisha ujumbe umetumwa kwa muigizaji na kusababisha matokeo yafuatayo:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Waigizaji wengi**. AutoGen inaunga mkono uundaji wa waigizaji wengi wanaoweza kushirikiana kufanikisha kazi ngumu. Waigizaji wanaweza kuwasiliana, kushirikiana taarifa, na kuratibu vitendo vyao kutatua matatizo kwa ufanisi zaidi. Ili kuunda mfumo wa waigizaji wengi, unaweza kufafanua aina tofauti za waigizaji wenye kazi maalum na majukumu, kama vile upokeaji wa data, uchambuzi, kufanya maamuzi, na mwingiliano wa mtumiaji. Tazama jinsi uundaji huo unavyoonekana:

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

    Katika msimbo uliotangulia tuna `GroupChatManager` ambaye amesajiliwa na runtime. Meneja huyu anahusika na kuratibu mwingiliano kati ya aina tofauti za waigizaji, kama waandishi, wachoraji, wahariri, na watumiaji.

- **Runtime ya Muigizaji**. Mfumo huu hutoa mazingira ya runtime, kuruhusu mawasiliano kati ya waigizaji, kusimamia utambulisho na mzunguko wa maisha yao, na kutekeleza mipaka ya usalama na faragha. Hii inamaanisha unaweza kuendesha waigizaji wako katika mazingira salama na yaliyodhibitiwa, kuhakikisha wanaweza kuingiliana kwa usalama na kwa ufanisi. Kuna aina mbili za runtime zinazovutia:
  - **Runtime huru**. Hii ni chaguo nzuri kwa programu za mchakato mmoja ambapo waigizaji wote wameandikwa kwa lugha moja ya programu na kuendeshwa katika mchakato mmoja. Hapa kuna mchoro wa jinsi inavyofanya kazi:

Stack ya programu

    *waigizaji huwasiliana kupitia ujumbe kupitia runtime, na runtime husimamia mzunguko wa maisha ya waigizaji*

  - **Runtime ya waigizaji waliosambazwa**, inafaa kwa programu za mchakato nyingi ambapo waigizaji wanaweza kuandikwa kwa lugha tofauti za programu na kuendeshwa kwenye mashine tofauti. Hapa kuna mchoro wa jinsi inavyofanya kazi:

## Semantic Kernel + Agent Framework

Semantic Kernel ni SDK ya kuandaa AI kwa viwanda. Inajumuisha viunganishi vya AI na kumbukumbu, pamoja na Mfumo wa Waigizaji.

Kwanza tuchambue baadhi ya vipengele vya msingi:

- **Viunganishi vya AI**: Hii ni kiolesura na huduma za AI za nje na vyanzo vya data kwa matumizi katika Python na C#.

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

    Hapa kuna mfano rahisi wa jinsi unavyoweza kuunda kernel na kuongeza huduma ya ukamilishaji wa mazungumzo. Semantic Kernel huunda muunganisho na huduma ya AI ya nje, katika kesi hii, Azure OpenAI Chat Completion.

- **Viendelezi (Plugins)**: Hivi vinajumuisha kazi ambazo programu inaweza kutumia. Kuna viendelezi vilivyotengenezwa tayari na pia unaweza kuunda vya kawaida. Dhana inayohusiana ni "kazi za prompt." Badala ya kutoa ishara za lugha ya asili kwa kuitwa kwa kazi, unatangaza kazi fulani kwa mfano. Kulingana na muktadha wa mazungumzo wa sasa, mfano unaweza kuchagua kuita moja ya kazi hizi kukamilisha ombi au swali. Hapa kuna mfano:

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

    Hapa, kwanza una template ya prompt `skPrompt` inayoruhusu mtumiaji kuingiza maandishi, `$userInput`. Kisha unaunda kazi ya kernel `SummarizeText` na kuileta kwenye kernel kwa jina la plugin `SemanticFunctions`. Kumbuka jina la kazi linalosaidia Semantic Kernel kuelewa kazi hiyo inafanya nini na lini inapaswa kuitwa.

- **Kazi za asili**: Pia kuna kazi za asili ambazo mfumo unaweza kuita moja kwa moja kutekeleza kazi. Hapa kuna mfano wa kazi kama hiyo inayopata maudhui kutoka kwa faili:

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

- **Kumbukumbu**: Inafupisha na kurahisisha usimamizi wa muktadha kwa programu za AI. Wazo la kumbukumbu ni kwamba hii ni kitu ambacho LLM inapaswa kujua. Unaweza kuhifadhi taarifa hii katika hifadhi ya vector ambayo huwa kama hifadhidata ya kumbukumbu ya ndani au hifadhidata ya vector au sawa nayo. Hapa kuna mfano wa hali rahisi sana ambapo *mambo* yanaongezwa kwenye kumbukumbu:

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

    Mambo haya kisha huhifadhiwa katika mkusanyiko wa kumbukumbu `SummarizedAzureDocs`. Huu ni mfano rahisi sana, lakini unaweza kuona jinsi unavyoweza kuhifadhi taarifa katika kumbukumbu kwa ajili ya LLM kuitumia.
## Somo lililopita

[Utangulizi wa Wakala wa AI na Matumizi ya Wakala](../01-intro-to-ai-agents/README.md)

## Somo lijalo

[Kuelewa Mifumo ya Muundo wa Wakala](../03-agentic-design-patterns/README.md)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.