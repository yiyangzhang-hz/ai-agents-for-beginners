<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:12:35+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sr"
}
-->
. Према Википедији, актер је _основни градивни блок конкурентног израчунавања. Као одговор на поруку коју прими, актер може: доносити локалне одлуке, креирати више актера, слати више порука и одредити како ће одговорити на следећу примљену поруку_.

**Примери употребе**: Аутоматизација генерисања кода, задатака анализе података и изградња прилагођених агената за планирање и истраживачке функције.

Ево неколико важних основних појмова AutoGen-а:

- **Агенти**. Агент је софтверски ентитет који:
  - **Комуницира путем порука**, ове поруке могу бити синхроне или асинхроне.
  - **Одржава своје стање**, које може бити модификовано долазним порукама.
  - **Извршава акције** као одговор на примљене поруке или промене у свом стању. Ове акције могу модификовати стање агента и произвести спољне ефекте, као што су ажурирање дневника порука, слање нових порука, извршавање кода или позиви API-ја.
    
  Ево кратког примера кода у којем креирате свог агента са могућностима ћаскања:

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
    
    У претходном коду, `MyAssistant` је креиран и наслеђује `RoutedAgent`. Има обрађивач порука који исписује садржај поруке, а затим шаље одговор користећи делегата `AssistantAgent`. Посебно обратите пажњу како додељујемо `self._delegate` инстанцу `AssistantAgent`, који је унапред направљен агент способан за руковање завршетком ћаскања.

    Хајде да обавестимо AutoGen о овом типу агента и покренемо програм:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    У претходном коду агенти су регистровани у runtime-у, а затим је послата порука агенту што резултује следећим излазом:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Више агената**. AutoGen подржава креирање више агената који могу заједно радити на постизању сложених задатака. Агенти могу комуницирати, делити информације и координисати своје акције како би ефикасније решавали проблеме. Да бисте креирали систем са више агената, можете дефинисати различите типове агената са специјализованим функцијама и улогама, као што су преузимање података, анализа, доношење одлука и интеракција са корисником. Погледајмо како изгледа таква креирање:

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

    У претходном коду имамо `GroupChatManager` који је регистрован у runtime-у. Овај менаџер је одговоран за координацију интеракција између различитих типова агената, као што су писци, илустратори, уредници и корисници.

- **Agent Runtime**. Овај фрејмворк пружа runtime окружење које омогућава комуникацију између агената, управља њиховим идентитетима и животним циклусима, и спроводи безбедносне и приватносне границе. То значи да можете покретати своје агенте у безбедном и контролисаном окружењу, осигуравајући да могу безбедно и ефикасно комуницирати. Постоје два runtime-а од интереса:
  - **Самостални runtime**. Ово је добар избор за апликације у једном процесу где су сви агенти имплементирани у истом програмском језику и раде у истом процесу. Ево илустрације како то функционише:

Апликациони слој

    *агенти комуницирају путем порука преко runtime-а, а runtime управља животним циклусом агената*

  - **Дистрибуирани агентски runtime**, погодан за апликације са више процеса где агенти могу бити имплементирани у различитим програмским језицима и радити на различитим машинама. Ево илустрације како то функционише:

## Semantic Kernel + Agent Framework

Semantic Kernel је AI Orchestration SDK спреман за предузећа. Састоји се од AI и меморијских конектора, заједно са Agent Framework-ом.

Прво ћемо покрити неке основне компоненте:

- **AI конектори**: Ово је интерфејс са спољним AI сервисима и изворима података за коришћење у Python-у и C#-у.

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

    Ево једноставног примера како можете креирати kernel и додати сервис за завршетак ћаскања. Semantic Kernel успоставља везу са спољним AI сервисом, у овом случају Azure OpenAI Chat Completion.

- **Плугин-и**: Они обухватају функције које апликација може користити. Постоје и спремни плугин-и и прилагођени које можете креирати. Повезани појам су "prompt функције". Уместо да се користе природни језички наговештаји за позив функција, одређене функције се емитују моделу. На основу тренутног контекста ћаскања, модел може изабрати да позове једну од ових функција да заврши захтев или упит. Ево примера:

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

    Овде прво имате шаблонски prompt `skPrompt` који оставља простор за унос текста од стране корисника, `$userInput`. Затим креирате kernel функцију `SummarizeText` и увозите је у kernel са именом плугина `SemanticFunctions`. Обратите пажњу на име функције које помаже Semantic Kernel-у да разуме шта функција ради и када треба да се позове.

- **Нативне функције**: Постоје и нативне функције које фрејмворк може директно позвати да изврши задатак. Ево примера такве функције која преузима садржај из фајла:

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

- **Меморија**: Апстрахује и поједностављује управљање контекстом за AI апликације. Идеја меморије је да је то нешто што LLM треба да зна. Ове информације можете чувати у векторској бази података која функционише као база података у меморији или слично. Ево примера веома поједностављеног сценарија у којем се *чињенице* додају у меморију:

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

    Ове чињенице се затим чувају у меморијској колекцији `SummarizedAzureDocs`. Ово је веома поједностављен пример, али можете видети како можете чувати информације у меморији за коришћење од стране LLM-а.
## Претходна лекција

[Увод у AI агенте и случајеве употребе агената](../01-intro-to-ai-agents/README.md)

## Следећа лекција

[Разумевање агентских дизајн образаца](../03-agentic-design-patterns/README.md)

**Одрицање одговорности**:  
Овај документ је преведен коришћењем AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.