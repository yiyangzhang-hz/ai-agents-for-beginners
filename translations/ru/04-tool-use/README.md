<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T12:27:14+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ru"
}
-->
[![Как разработать хороших AI-агентов](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ru.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Шаблон проектирования использования инструментов

Инструменты интересны тем, что они расширяют возможности AI-агентов. Вместо того чтобы агент имел ограниченный набор действий, добавление инструмента позволяет ему выполнять широкий спектр задач. В этой главе мы рассмотрим шаблон проектирования использования инструментов, который описывает, как AI-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое шаблон проектирования использования инструментов?
- Какие случаи его применения существуют?
- Какие элементы/строительные блоки необходимы для реализации этого шаблона?
- Какие особые аспекты нужно учитывать при использовании шаблона проектирования использования инструментов для создания надежных AI-агентов?

## Цели обучения

После завершения этого урока вы сможете:

- Определить, что такое шаблон проектирования использования инструментов и его назначение.
- Выявить случаи, в которых применим этот шаблон.
- Понять ключевые элементы, необходимые для реализации шаблона.
- Осознать аспекты, важные для обеспечения надежности AI-агентов, использующих этот шаблон.

## Что такое шаблон проектирования использования инструментов?

**Шаблон проектирования использования инструментов** сосредоточен на предоставлении LLMs возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который может быть выполнен агентом для выполнения действий. Инструмент может быть простой функцией, например калькулятором, или API-запросом к стороннему сервису, например, для получения данных о ценах на акции или прогнозе погоды. В контексте AI-агентов инструменты предназначены для выполнения агентами в ответ на **вызовы функций, сгенерированные моделью**.

## Какие случаи его применения существуют?

AI-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Шаблон проектирования использования инструментов часто применяется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна для множества различных случаев, включая:

- **Динамическое извлечение информации:** Агенты могут запрашивать внешние API или базы данных для получения актуальных данных (например, запрос данных из SQLite для анализа, получение цен на акции или информации о погоде).
- **Выполнение и интерпретация кода:** Агенты могут выполнять код или скрипты для решения математических задач, создания отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** Автоматизация повторяющихся или многоэтапных рабочих процессов с использованием инструментов, таких как планировщики задач, сервисы электронной почты или конвейеры данных.
- **Поддержка клиентов:** Агенты могут взаимодействовать с CRM-системами, платформами тикетов или базами знаний для решения запросов пользователей.
- **Создание и редактирование контента:** Агенты могут использовать инструменты, такие как проверка грамматики, суммаризация текста или оценка безопасности контента, чтобы помочь в задачах создания контента.

## Какие элементы/строительные блоки необходимы для реализации шаблона проектирования использования инструментов?

Эти строительные блоки позволяют AI-агенту выполнять широкий спектр задач. Давайте рассмотрим ключевые элементы, необходимые для реализации шаблона проектирования использования инструментов:

- **Схемы функций/инструментов:** Подробные описания доступных инструментов, включая имя функции, назначение, требуемые параметры и ожидаемые результаты. Эти схемы позволяют LLM понять, какие инструменты доступны и как формировать корректные запросы.

- **Логика выполнения функций:** Определяет, как и когда инструменты вызываются на основе намерений пользователя и контекста разговора. Это может включать модули планирования, механизмы маршрутизации или условные потоки, которые динамически определяют использование инструментов.

- **Система обработки сообщений:** Компоненты, которые управляют потоком общения между вводом пользователя, ответами LLM, вызовами инструментов и их результатами.

- **Фреймворк интеграции инструментов:** Инфраструктура, которая соединяет агента с различными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и проверка:** Механизмы для обработки сбоев выполнения инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием:** Отслеживает контекст разговора, предыдущие взаимодействия с инструментами и постоянные данные для обеспечения согласованности в многоходовых взаимодействиях.

Далее мы подробнее рассмотрим вызов функций/инструментов.

### Вызов функций/инструментов

Вызов функций — это основной способ, с помощью которого мы даем возможность большим языковым моделям (LLMs) взаимодействовать с инструментами. Часто термины "функция" и "инструмент" используются взаимозаменяемо, поскольку "функции" (блоки повторно используемого кода) являются "инструментами", которые агенты используют для выполнения задач. Чтобы код функции был вызван, LLM должен сравнить запрос пользователя с описанием функции. Для этого схема, содержащая описания всех доступных функций, отправляется в LLM. Затем LLM выбирает наиболее подходящую функцию для задачи и возвращает ее имя и аргументы. Выбранная функция вызывается, ее ответ отправляется обратно в LLM, который использует информацию для ответа на запрос пользователя.

Для реализации вызова функций для агентов разработчикам потребуется:

1. Модель LLM, поддерживающая вызов функций
2. Схема, содержащая описания функций
3. Код для каждой описанной функции

Рассмотрим пример получения текущего времени в городе:

1. **Инициализация LLM, поддерживающего вызов функций:**

    Не все модели поддерживают вызов функций, поэтому важно убедиться, что используемая вами модель LLM это делает. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Создание схемы функции:**

    Далее мы определим JSON-схему, содержащую имя функции, описание того, что она делает, а также имена и описания параметров функции. Затем мы передадим эту схему клиенту, созданному ранее, вместе с запросом пользователя найти время в Сан-Франциско. Важно отметить, что возвращается **вызов инструмента**, а не окончательный ответ на вопрос. Как упоминалось ранее, LLM возвращает имя функции, которую он выбрал для задачи, и аргументы, которые будут переданы ей.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функции, необходимый для выполнения задачи:**

    Теперь, когда LLM выбрал, какую функцию нужно выполнить, необходимо реализовать и выполнить код, который выполняет задачу. Мы можем реализовать код для получения текущего времени на Python. Также потребуется написать код для извлечения имени и аргументов из response_message, чтобы получить окончательный результат.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Вызов функций является основой большинства, если не всех, дизайнов использования инструментов агентами, однако его реализация с нуля может быть сложной. Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентные фреймворки предоставляют нам готовые строительные блоки для реализации использования инструментов.

## Примеры использования инструментов с агентными фреймворками

Вот несколько примеров того, как можно реализовать шаблон проектирования использования инструментов с использованием различных агентных фреймворков:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> — это открытый AI-фреймворк для разработчиков на .NET, Python и Java, работающих с большими языковыми моделями (LLMs). Он упрощает процесс использования вызова функций, автоматически описывая ваши функции и их параметры модели через процесс, называемый <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">сериализацией</a>. Он также управляет обменом данными между моделью и вашим кодом. Еще одно преимущество использования агентного фреймворка, такого как Semantic Kernel, заключается в доступе к готовым инструментам, таким как <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Следующая диаграмма иллюстрирует процесс вызова функций с Semantic Kernel:

![вызов функций](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ru.png)

В Semantic Kernel функции/инструменты называются <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">плагинами</a>. Мы можем преобразовать функцию `get_current_time`, которую видели ранее, в плагин, превратив ее в класс с функцией внутри. Мы также можем импортировать декоратор `kernel_function`, который принимает описание функции. Когда вы создаете ядро с GetCurrentTimePlugin, ядро автоматически сериализует функцию и ее параметры, создавая схему для отправки в LLM в процессе.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — это новый агентный фреймворк, предназначенный для того, чтобы разработчики могли безопасно создавать, развертывать и масштабировать высококачественных и расширяемых AI-агентов без необходимости управлять базовыми вычислительными и хранилищными ресурсами. Он особенно полезен для корпоративных приложений, так как является полностью управляемым сервисом с корпоративным уровнем безопасности.

В сравнении с разработкой напрямую с использованием API LLM, Azure AI Agent Service предоставляет некоторые преимущества, включая:

- Автоматический вызов инструментов — нет необходимости анализировать вызов инструмента, вызывать инструмент и обрабатывать ответ; все это теперь выполняется на стороне сервера.
- Безопасно управляемые данные — вместо управления собственным состоянием разговора можно полагаться на потоки для хранения всей необходимой информации.
- Готовые инструменты — инструменты, которые можно использовать для взаимодействия с вашими источниками данных, такие как Bing, Azure AI Search и Azure Functions.

Инструменты, доступные в Azure AI Agent Service, можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Граундирование с Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определенные OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервис Agent Service позволяет использовать эти инструменты вместе как `toolset`. Он также использует `threads`, которые отслеживают историю сообщений из конкретного разговора.

Представьте, что вы являетесь агентом по продажам в компании Contoso. Вы хотите разработать разговорного агента, который сможет отвечать на вопросы о ваших данных продаж.

Следующее изображение иллюстрирует, как можно использовать Azure AI Agent Service для анализа данных продаж:

![Agentic Service в действии](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ru.jpg)

Чтобы использовать любой из этих инструментов с сервисом, мы можем создать клиент и определить инструмент или набор инструментов. Для практической реализации можно использовать следующий код на Python. LLM сможет посмотреть на набор инструментов и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или готовый Code Interpreter в зависимости от запроса пользователя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особые аспекты нужно учитывать при использовании шаблона проектирования использования инструментов для создания надежных AI-агентов?

Распространенной проблемой с SQL, динамически генерируемым LLM, является безопасность, особенно риск SQL-инъекций или вредоносных действий, таких как удаление или изменение базы данных. Хотя эти проблемы актуальны, их можно эффективно устранить, правильно настроив разрешения доступа к базе данных. Для большинства баз данных это включает настройку базы данных как только для чтения. Для таких сервисов баз данных, как PostgreSQL или Azure SQL, приложению следует назначить роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно повышает защиту. В корпоративных сценариях данные обычно извлекаются и преобразуются из операционных систем в базу данных только для чтения или хранилище данных с удобной для пользователя схемой. Этот подход гарантирует, что данные защищены, оптимизированы для производительности и доступности, а приложение имеет ограниченный доступ только для чтения.

### Остались вопросы о шаблоне проектирования использования инструментов?
Присоединяйтесь к [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), чтобы встретиться с другими учащимися, посетить часы консультаций и получить ответы на ваши вопросы о AI Agents.

## Дополнительные ресурсы

## Предыдущий урок

[Понимание шаблонов агентного дизайна](../03-agentic-design-patterns/README.md)

## Следующий урок

[Agentic RAG](../05-agentic-rag/README.md)

---

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.