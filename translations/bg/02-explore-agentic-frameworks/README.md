<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:12:02+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "bg"
}
-->
. Според Wikipedia, актьорът е _основната градивна единица на конкурентното изчисление. В отговор на получено съобщение, актьорът може: да взема локални решения, да създава повече актьори, да изпраща повече съобщения и да определи как да отговори на следващото получено съобщение_.

**Приложения**: Автоматизиране на генериране на код, задачи за анализ на данни и създаване на персонализирани агенти за планиране и изследователски функции.

Ето някои важни основни концепции на AutoGen:

- **Агенти**. Агентът е софтуерна единица, която:
  - **Комуникира чрез съобщения**, които могат да бъдат синхронни или асинхронни.
  - **Поддържа собствено състояние**, което може да бъде променяно от входящи съобщения.
  - **Изпълнява действия** в отговор на получени съобщения или промени в състоянието си. Тези действия могат да променят състоянието на агента и да предизвикат външни ефекти, като актуализиране на логове на съобщения, изпращане на нови съобщения, изпълнение на код или извършване на API повиквания.
    
  Ето кратък кодов фрагмент, в който създавате собствен агент с чат възможности:

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
    
    В предишния код `MyAssistant` е създаден и наследява от `RoutedAgent`. Той има обработчик на съобщения, който отпечатва съдържанието на съобщението и след това изпраща отговор чрез делегата `AssistantAgent`. Особено обърнете внимание как присвояваме на `self._delegate` инстанция на `AssistantAgent`, който е предварително създаден агент, способен да обработва чат завършвания.


    Нека уведомим AutoGen за този тип агент и стартираме програмата:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    В предишния код агентите са регистрирани в runtime средата и след това се изпраща съобщение към агента, което води до следния изход:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Множество агенти**. AutoGen поддържа създаването на множество агенти, които могат да работят заедно за постигане на сложни задачи. Агентите могат да комуникират, да споделят информация и да координират действията си за по-ефективно решаване на проблеми. За да създадете мултиагентна система, можете да дефинирате различни типове агенти с специализирани функции и роли, като извличане на данни, анализ, вземане на решения и взаимодействие с потребителя. Нека видим как изглежда такова създаване, за да добием представа:

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

    В предишния код имаме `GroupChatManager`, който е регистриран в runtime средата. Този мениджър отговаря за координиране на взаимодействията между различни типове агенти, като писатели, илюстратори, редактори и потребители.

- **Agent Runtime**. Фреймуъркът предоставя runtime среда, която позволява комуникация между агентите, управлява техните идентичности и жизнен цикъл и налага граници за сигурност и поверителност. Това означава, че можете да изпълнявате агентите си в сигурна и контролирана среда, гарантирайки, че те могат да взаимодействат безопасно и ефективно. Има два runtime-а, които представляват интерес:
  - **Самостоятелен runtime**. Това е добър избор за приложения с един процес, където всички агенти са реализирани на един и същ програмен език и работят в един и същ процес. Ето илюстрация как работи:  

Application stack

    *агентите комуникират чрез съобщения през runtime, а runtime управлява жизнения цикъл на агентите*

  - **Разпределен агентен runtime**, подходящ за мулти-процесни приложения, където агентите могат да са реализирани на различни програмни езици и да работят на различни машини. Ето илюстрация как работи:  

## Semantic Kernel + Agent Framework

Semantic Kernel е корпоративен AI Orchestration SDK. Той се състои от AI и memory конектори, заедно с Agent Framework.

Нека първо разгледаме някои основни компоненти:

- **AI Connectors**: Това е интерфейс към външни AI услуги и източници на данни за използване както в Python, така и в C#.

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

    Тук имате прост пример как да създадете kernel и да добавите услуга за чат завършване. Semantic Kernel създава връзка с външна AI услуга, в този случай Azure OpenAI Chat Completion.

- **Plugins**: Те капсулират функции, които приложението може да използва. Има както готови плъгини, така и такива, които можете да създадете сами. Свързана концепция са "prompt functions". Вместо да предоставяте естествени езикови подсказки за извикване на функция, вие излъчвате определени функции към модела. Въз основа на текущия контекст на чата, моделът може да избере да извика една от тези функции, за да изпълни заявка или въпрос. Ето пример:

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

    Тук първо имате шаблонен prompt `skPrompt`, който оставя място за въвеждане на текст от потребителя, `$userInput`. След това създавате kernel функцията `SummarizeText` и я импортирате в kernel с името на плъгина `SemanticFunctions`. Обърнете внимание на името на функцията, което помага на Semantic Kernel да разбере какво прави функцията и кога трябва да бъде извикана.

- **Native function**: Има и native функции, които фреймуъркът може да извика директно, за да изпълни задачата. Ето пример за такава функция, която извлича съдържание от файл:

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

- **Memory**: Абстрахира и опростява управлението на контекста за AI приложения. Идеята с паметта е, че това е нещо, което LLM трябва да знае. Можете да съхранявате тази информация във векторно хранилище, което в крайна сметка представлява in-memory база данни или векторна база данни или подобно. Ето пример за много опростен сценарий, в който *факти* се добавят в паметта:

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

    Тези факти след това се съхраняват в колекцията памет `SummarizedAzureDocs`. Това е много опростен пример, но можете да видите как можете да съхранявате информация в паметта за използване от LLM.
## Предишен урок

[Въведение в AI агентите и техните приложения](../01-intro-to-ai-agents/README.md)

## Следващ урок

[Разбиране на агентните дизайн модели](../03-agentic-design-patterns/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.