<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:14:50+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "uk"
}
-->
. Згідно з Вікіпедією, актор — це _основний будівельний блок паралельних обчислень. У відповідь на отримане повідомлення актор може: приймати локальні рішення, створювати нових акторів, надсилати додаткові повідомлення та визначати, як реагувати на наступне отримане повідомлення_.

**Випадки використання**: автоматизація генерації коду, завдань аналізу даних та створення спеціалізованих агентів для планування та дослідницьких функцій.

Ось деякі важливі основні концепції AutoGen:

- **Агенти**. Агент — це програмний об’єкт, який:
  - **Спілкується через повідомлення**, які можуть бути синхронними або асинхронними.
  - **Підтримує власний стан**, який може змінюватися вхідними повідомленнями.
  - **Виконує дії** у відповідь на отримані повідомлення або зміни свого стану. Ці дії можуть змінювати стан агента та створювати зовнішні ефекти, такі як оновлення журналів повідомлень, надсилання нових повідомлень, виконання коду або виклики API.
    
  Ось короткий фрагмент коду, у якому ви створюєте власного агента з можливостями чату:

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
    
    У наведеному коді `MyAssistant` створено як похідний від `RoutedAgent`. Він має обробник повідомлень, який виводить вміст повідомлення, а потім надсилає відповідь за допомогою делегата `AssistantAgent`. Особливо зверніть увагу, як ми присвоюємо `self._delegate` екземпляр `AssistantAgent` — це готовий агент, який може обробляти завершення чату.

    Далі повідомимо AutoGen про цей тип агента і запустимо програму:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    У наведеному коді агенти реєструються у середовищі виконання, після чого агенту надсилається повідомлення, що призводить до такого виводу:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Мультиагенти**. AutoGen підтримує створення кількох агентів, які можуть працювати разом для виконання складних завдань. Агенти можуть спілкуватися, обмінюватися інформацією та координувати свої дії для ефективнішого розв’язання проблем. Щоб створити мультиагентну систему, можна визначити різні типи агентів із спеціалізованими функціями та ролями, такими як отримання даних, аналіз, прийняття рішень і взаємодія з користувачем. Ось як це виглядає на прикладі:

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

    У наведеному коді є `GroupChatManager`, який зареєстрований у середовищі виконання. Цей менеджер відповідає за координацію взаємодії між різними типами агентів, такими як письменники, ілюстратори, редактори та користувачі.

- **Середовище виконання агентів**. Фреймворк надає середовище виконання, яке забезпечує комунікацію між агентами, керує їхніми ідентичностями та життєвим циклом, а також забезпечує безпеку та конфіденційність. Це означає, що ви можете запускати своїх агентів у безпечному та контрольованому середовищі, гарантуючи їхню безпечну та ефективну взаємодію. Існують два типи середовищ виконання:
  - **Автономне середовище виконання**. Це хороший вибір для однопроцесних додатків, де всі агенти реалізовані однією мовою програмування і працюють у одному процесі. Ось ілюстрація того, як це працює:

Стек застосунку

    *агенти спілкуються через повідомлення за допомогою середовища виконання, а середовище керує життєвим циклом агентів*

  - **Розподілене середовище виконання агентів** підходить для багатопроцесних додатків, де агенти можуть бути реалізовані різними мовами програмування і працювати на різних машинах. Ось ілюстрація того, як це працює:

## Semantic Kernel + Agent Framework

Semantic Kernel — це корпоративний SDK для оркестрації AI. Він складається з AI- та memory-конекторів, а також Agent Framework.

Спочатку розглянемо основні компоненти:

- **AI-конектори**: це інтерфейс до зовнішніх AI-сервісів і джерел даних для використання як у Python, так і в C#.

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

    Тут наведено простий приклад створення ядра (kernel) та додавання сервісу завершення чату. Semantic Kernel встановлює з’єднання із зовнішнім AI-сервісом, у цьому випадку Azure OpenAI Chat Completion.

- **Плагіни**: вони інкапсулюють функції, які може використовувати додаток. Існують як готові плагіни, так і можливість створювати власні. Пов’язана концепція — "prompt functions". Замість того, щоб надавати природномовні підказки для виклику функції, ви транслюєте певні функції моделі. В залежності від поточного контексту чату модель може обрати виклик однієї з цих функцій для виконання запиту. Ось приклад:

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

    Тут спочатку є шаблон підказки `skPrompt`, який залишає місце для введення тексту користувачем, `$userInput`. Потім створюється функція ядра `SummarizeText` і імпортується в ядро з ім’ям плагіна `SemanticFunctions`. Зверніть увагу на ім’я функції, яке допомагає Semantic Kernel зрозуміти, що робить функція і коли її слід викликати.

- **Нативна функція**: також є нативні функції, які фреймворк може викликати безпосередньо для виконання завдання. Ось приклад такої функції, що отримує вміст файлу:

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

- **Пам’ять**: абстрагує і спрощує управління контекстом для AI-додатків. Ідея пам’яті полягає в тому, що це інформація, яку LLM має знати. Ви можете зберігати цю інформацію у векторному сховищі, яке фактично є базою даних у пам’яті або векторною базою даних чи подібним. Ось приклад дуже спрощеного сценарію, де *факти* додаються до пам’яті:

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

    Ці факти потім зберігаються у колекції пам’яті `SummarizedAzureDocs`. Це дуже спрощений приклад, але ви можете побачити, як можна зберігати інформацію в пам’яті для використання LLM.
## Попередній урок

[Вступ до AI агентів та випадків їх використання](../01-intro-to-ai-agents/README.md)

## Наступний урок

[Розуміння агентних шаблонів проектування](../03-agentic-design-patterns/README.md)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.