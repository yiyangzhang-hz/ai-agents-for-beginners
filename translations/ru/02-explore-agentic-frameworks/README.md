<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:52:16+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ru"
}
-->
. Согласно Википедии, актор — это _основной строительный блок параллельных вычислений. В ответ на полученное сообщение актор может: принимать локальные решения, создавать новых акторов, отправлять дополнительные сообщения и определять, как реагировать на следующее полученное сообщение_.

**Сценарии использования**: автоматизация генерации кода, задачи анализа данных и создание пользовательских агентов для функций планирования и исследований.

Вот несколько важных основных концепций AutoGen:

- **Агенты**. Агент — это программный объект, который:
  - **Обменивается сообщениями**, которые могут быть синхронными или асинхронными.
  - **Поддерживает собственное состояние**, которое может изменяться в ответ на входящие сообщения.
  - **Выполняет действия** в ответ на полученные сообщения или изменения состояния. Эти действия могут изменять состояние агента и вызывать внешние эффекты, такие как обновление журналов сообщений, отправка новых сообщений, выполнение кода или вызов API.
    
  Ниже приведён короткий пример кода, в котором создаётся собственный агент с возможностями чата:

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
    
    В предыдущем коде `MyAssistant` создан и наследуется от `RoutedAgent`. У него есть обработчик сообщений, который выводит содержимое сообщения, а затем отправляет ответ с помощью делегата `AssistantAgent`. Обратите особое внимание, как мы присваиваем `self._delegate` экземпляр `AssistantAgent` — это готовый агент, который умеет обрабатывать завершения чата.

    Давайте зарегистрируем этот тип агента в AutoGen и запустим программу:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    В предыдущем коде агенты регистрируются в среде выполнения, после чего агенту отправляется сообщение, что приводит к следующему выводу:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Мультиагенты**. AutoGen поддерживает создание нескольких агентов, которые могут работать совместно для решения сложных задач. Агенты могут общаться, обмениваться информацией и координировать свои действия для более эффективного решения проблем. Чтобы создать мультиагентную систему, можно определить разные типы агентов с специализированными функциями и ролями, такими как получение данных, анализ, принятие решений и взаимодействие с пользователем. Посмотрим, как это выглядит на практике:

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

    В предыдущем коде у нас есть `GroupChatManager`, зарегистрированный в среде выполнения. Этот менеджер отвечает за координацию взаимодействия между разными типами агентов, такими как писатели, иллюстраторы, редакторы и пользователи.

- **Среда выполнения агентов**. Фреймворк предоставляет среду выполнения, которая обеспечивает коммуникацию между агентами, управляет их идентичностями и жизненным циклом, а также поддерживает границы безопасности и конфиденциальности. Это значит, что вы можете запускать своих агентов в безопасной и контролируемой среде, гарантируя их безопасное и эффективное взаимодействие. Существует два варианта среды выполнения:
  - **Автономная среда выполнения**. Хороший выбор для однопроцессных приложений, где все агенты реализованы на одном языке программирования и работают в одном процессе. Вот иллюстрация того, как это работает:

Стек приложения

    *агенты обмениваются сообщениями через среду выполнения, которая управляет жизненным циклом агентов*

  - **Распределённая среда выполнения** подходит для многопроцессных приложений, где агенты могут быть реализованы на разных языках программирования и запускаться на разных машинах. Вот иллюстрация того, как это работает:

## Semantic Kernel + Agent Framework

Semantic Kernel — это корпоративный SDK для оркестрации ИИ. Он включает AI и memory коннекторы, а также Agent Framework.

Сначала рассмотрим основные компоненты:

- **AI коннекторы**: интерфейс для взаимодействия с внешними AI-сервисами и источниками данных, доступный как для Python, так и для C#.

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

    Здесь простой пример создания ядра и добавления сервиса завершения чата. Semantic Kernel устанавливает соединение с внешним AI-сервисом, в данном случае Azure OpenAI Chat Completion.

- **Плагины**: инкапсулируют функции, которые может использовать приложение. Есть готовые плагины и возможность создавать свои. Связанная концепция — "prompt functions". Вместо того чтобы давать естественно-языковые подсказки для вызова функций, вы транслируете определённые функции модели. В зависимости от текущего контекста чата модель может выбрать вызов одной из этих функций для выполнения запроса. Вот пример:

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

    Здесь сначала создаётся шаблон подсказки `skPrompt`, оставляющий место для ввода пользователя `$userInput`. Затем создаётся функция ядра `SummarizeText`, которая импортируется в ядро с именем плагина `SemanticFunctions`. Обратите внимание на имя функции, которое помогает Semantic Kernel понять, что делает функция и когда её следует вызывать.

- **Нативные функции**: также есть нативные функции, которые фреймворк может вызывать напрямую для выполнения задачи. Вот пример такой функции, которая получает содержимое файла:

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

- **Память**: абстрагирует и упрощает управление контекстом для AI-приложений. Идея памяти в том, что это информация, которую LLM должен знать. Вы можете хранить эти данные в векторном хранилище, которое может быть in-memory базой данных, векторной базой данных или чем-то подобным. Вот пример очень упрощённого сценария, где *факты* добавляются в память:

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

    Эти факты затем сохраняются в коллекции памяти `SummarizedAzureDocs`. Это очень упрощённый пример, но вы можете видеть, как можно хранить информацию в памяти для использования LLM.
## Предыдущее занятие

[Введение в AI-агентов и сценарии их использования](../01-intro-to-ai-agents/README.md)

## Следующее занятие

[Понимание агентных шаблонов проектирования](../03-agentic-design-patterns/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.