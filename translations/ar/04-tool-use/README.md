<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T09:15:02+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ar"
}
-->
[![كيفية تصميم وكلاء ذكاء اصطناعي جيدين](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ar.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اضغط على الصورة أعلاه لمشاهدة فيديو الدرس)_

# نمط تصميم استخدام الأدوات

الأدوات مثيرة للاهتمام لأنها تتيح لوكلاء الذكاء الاصطناعي امتلاك مجموعة أوسع من القدرات. بدلاً من أن يكون لدى الوكيل مجموعة محدودة من الإجراءات التي يمكنه تنفيذها، يمكنه الآن، بإضافة أداة، تنفيذ مجموعة واسعة من الإجراءات. في هذا الفصل، سنلقي نظرة على نمط تصميم استخدام الأدوات، الذي يصف كيفية استخدام وكلاء الذكاء الاصطناعي لأدوات محددة لتحقيق أهدافهم.

## المقدمة

في هذا الدرس، نسعى للإجابة على الأسئلة التالية:

- ما هو نمط تصميم استخدام الأدوات؟
- ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟
- ما هي العناصر/اللبنات الأساسية اللازمة لتنفيذ نمط التصميم؟
- ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- تعريف نمط تصميم استخدام الأدوات والغرض منه.
- تحديد حالات الاستخدام التي يكون فيها نمط تصميم استخدام الأدوات قابلاً للتطبيق.
- فهم العناصر الرئيسية اللازمة لتنفيذ نمط التصميم.
- التعرف على الاعتبارات لضمان الموثوقية في وكلاء الذكاء الاصطناعي باستخدام هذا النمط.

## ما هو نمط تصميم استخدام الأدوات؟

يركز **نمط تصميم استخدام الأدوات** على منح نماذج اللغة الكبيرة (LLMs) القدرة على التفاعل مع أدوات خارجية لتحقيق أهداف محددة. الأدوات هي أكواد يمكن تنفيذها بواسطة الوكيل لتنفيذ إجراءات. يمكن أن تكون الأداة وظيفة بسيطة مثل آلة حاسبة، أو استدعاء API لخدمة طرف ثالث مثل البحث عن أسعار الأسهم أو توقعات الطقس. في سياق وكلاء الذكاء الاصطناعي، يتم تصميم الأدوات ليتم تنفيذها بواسطة الوكلاء استجابةً لـ **استدعاءات الوظائف التي يتم إنشاؤها بواسطة النموذج**.

## ما هي حالات الاستخدام التي يمكن تطبيقه عليها؟

يمكن لوكلاء الذكاء الاصطناعي الاستفادة من الأدوات لإكمال المهام المعقدة، أو استرجاع المعلومات، أو اتخاذ القرارات. غالبًا ما يُستخدم نمط تصميم استخدام الأدوات في السيناريوهات التي تتطلب تفاعلًا ديناميكيًا مع الأنظمة الخارجية، مثل قواعد البيانات، أو خدمات الويب، أو مفسري الأكواد. هذه القدرة مفيدة لعدد من حالات الاستخدام المختلفة، بما في ذلك:

- **استرجاع المعلومات الديناميكي:** يمكن للوكلاء استعلام واجهات برمجة التطبيقات الخارجية أو قواعد البيانات لجلب بيانات محدثة (مثل استعلام قاعدة بيانات SQLite لتحليل البيانات، أو جلب أسعار الأسهم أو معلومات الطقس).
- **تنفيذ الأكواد وتفسيرها:** يمكن للوكلاء تنفيذ الأكواد أو البرامج النصية لحل المشكلات الرياضية، أو إنشاء التقارير، أو إجراء المحاكاة.
- **أتمتة سير العمل:** أتمتة سير العمل المتكرر أو متعدد الخطوات من خلال دمج أدوات مثل جداول المهام، أو خدمات البريد الإلكتروني، أو خطوط البيانات.
- **دعم العملاء:** يمكن للوكلاء التفاعل مع أنظمة إدارة علاقات العملاء (CRM)، أو منصات التذاكر، أو قواعد المعرفة لحل استفسارات المستخدمين.
- **إنشاء المحتوى وتحريره:** يمكن للوكلاء الاستفادة من أدوات مثل مدققي القواعد النحوية، أو ملخصات النصوص، أو مقيمي أمان المحتوى للمساعدة في مهام إنشاء المحتوى.

## ما هي العناصر/اللبنات الأساسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات؟

تتيح هذه اللبنات الأساسية لوكيل الذكاء الاصطناعي تنفيذ مجموعة واسعة من المهام. دعونا نلقي نظرة على العناصر الرئيسية اللازمة لتنفيذ نمط تصميم استخدام الأدوات:

- **مخططات الوظائف/الأدوات:** تعريفات مفصلة للأدوات المتاحة، بما في ذلك اسم الوظيفة، والغرض، والمعلمات المطلوبة، والمخرجات المتوقعة. تُمكّن هذه المخططات نموذج اللغة الكبير من فهم الأدوات المتاحة وكيفية إنشاء طلبات صالحة.
- **منطق تنفيذ الوظائف:** يتحكم في كيفية ووقت استدعاء الأدوات بناءً على نية المستخدم وسياق المحادثة. قد يشمل ذلك وحدات التخطيط، أو آليات التوجيه، أو التدفقات الشرطية التي تحدد استخدام الأدوات ديناميكيًا.
- **نظام إدارة الرسائل:** مكونات تدير تدفق المحادثة بين مدخلات المستخدم، واستجابات نموذج اللغة الكبير، واستدعاءات الأدوات، ومخرجات الأدوات.
- **إطار تكامل الأدوات:** البنية التحتية التي تربط الوكيل بمختلف الأدوات، سواء كانت وظائف بسيطة أو خدمات خارجية معقدة.
- **التعامل مع الأخطاء والتحقق:** آليات للتعامل مع فشل تنفيذ الأدوات، والتحقق من المعلمات، وإدارة الاستجابات غير المتوقعة.
- **إدارة الحالة:** تتبع سياق المحادثة، والتفاعلات السابقة مع الأدوات، والبيانات المستمرة لضمان الاتساق عبر التفاعلات متعددة الأدوار.

بعد ذلك، دعونا نلقي نظرة على استدعاء الوظائف/الأدوات بمزيد من التفصيل.

### استدعاء الوظائف/الأدوات

استدعاء الوظائف هو الطريقة الأساسية التي نُمكّن بها نماذج اللغة الكبيرة (LLMs) من التفاعل مع الأدوات. غالبًا ما ترى "وظيفة" و"أداة" تُستخدمان بالتبادل لأن "الوظائف" (كتل من الأكواد القابلة لإعادة الاستخدام) هي "الأدوات" التي يستخدمها الوكلاء لتنفيذ المهام. لكي يتم استدعاء كود الوظيفة، يجب على نموذج اللغة الكبير مقارنة طلب المستخدم بوصف الوظيفة. للقيام بذلك، يتم إرسال مخطط يحتوي على أوصاف جميع الوظائف المتاحة إلى نموذج اللغة الكبير. ثم يختار النموذج الوظيفة الأنسب للمهمة ويعيد اسمها ومعاملاتها. يتم استدعاء الوظيفة المختارة، ويتم إرسال استجابتها مرة أخرى إلى نموذج اللغة الكبير، الذي يستخدم المعلومات للرد على طلب المستخدم.

لتنفيذ استدعاء الوظائف للوكلاء، ستحتاج إلى:

1. نموذج لغة كبير يدعم استدعاء الوظائف
2. مخطط يحتوي على أوصاف الوظائف
3. الكود الخاص بكل وظيفة موصوفة

دعونا نستخدم مثال الحصول على الوقت الحالي في مدينة لتوضيح ذلك:

1. **تهيئة نموذج لغة كبير يدعم استدعاء الوظائف:**

    ليس كل النماذج تدعم استدعاء الوظائف، لذا من المهم التحقق من أن النموذج الذي تستخدمه يدعم ذلك. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> يدعم استدعاء الوظائف. يمكننا البدء بتهيئة عميل Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **إنشاء مخطط وظيفة:**

    بعد ذلك، سنعرّف مخطط JSON يحتوي على اسم الوظيفة، ووصف لما تفعله الوظيفة، وأسماء ووصف معلمات الوظيفة. 
    سنأخذ هذا المخطط ونمرره إلى العميل الذي تم إنشاؤه سابقًا، مع طلب المستخدم للعثور على الوقت في سان فرانسيسكو. من المهم ملاحظة أن ما يتم إرجاعه هو **استدعاء أداة**، وليس الإجابة النهائية على السؤال. كما ذكرنا سابقًا، يعيد نموذج اللغة الكبير اسم الوظيفة التي اختارها للمهمة، والمعاملات التي سيتم تمريرها إليها.

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
  
1. **الكود المطلوب لتنفيذ المهمة:**

    الآن بعد أن اختار نموذج اللغة الكبير الوظيفة التي يجب تشغيلها، يجب تنفيذ الكود الذي ينفذ المهمة. 
    يمكننا تنفيذ الكود للحصول على الوقت الحالي باستخدام Python. سنحتاج أيضًا إلى كتابة الكود لاستخراج الاسم والمعاملات من response_message للحصول على النتيجة النهائية.

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

استدعاء الوظائف هو جوهر معظم، إن لم يكن كل، تصميم استخدام الأدوات للوكلاء، ومع ذلك فإن تنفيذه من الصفر قد يكون أحيانًا تحديًا. كما تعلمنا في [الدرس 2](../../../02-explore-agentic-frameworks) توفر الأطر الوكيلة لنا لبنات بناء جاهزة لتنفيذ استخدام الأدوات.

## أمثلة على استخدام الأدوات مع الأطر الوكيلة

فيما يلي بعض الأمثلة على كيفية تنفيذ نمط تصميم استخدام الأدوات باستخدام أطر وكيلة مختلفة:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> هو إطار عمل مفتوح المصدر للذكاء الاصطناعي للمطورين الذين يعملون مع نماذج اللغة الكبيرة (LLMs) باستخدام .NET، Python، وJava. يبسط عملية استخدام استدعاء الوظائف من خلال وصف وظائفك ومعاملاتها تلقائيًا للنموذج عبر عملية تُسمى <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">التسلسل</a>. كما يدير التواصل ذهابًا وإيابًا بين النموذج وكودك. ميزة أخرى لاستخدام إطار عمل وكيل مثل Semantic Kernel هي أنه يتيح لك الوصول إلى أدوات جاهزة مثل <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">البحث في الملفات</a> و<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">مفسر الأكواد</a>.

يوضح الرسم البياني التالي عملية استدعاء الوظائف باستخدام Semantic Kernel:

![استدعاء الوظائف](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ar.png)

في Semantic Kernel تُسمى الوظائف/الأدوات <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">الإضافات</a>. يمكننا تحويل وظيفة `get_current_time` التي رأيناها سابقًا إلى إضافة عن طريق تحويلها إلى فئة تحتوي على الوظيفة. يمكننا أيضًا استيراد الزخرفة `kernel_function`، التي تأخذ وصف الوظيفة. عندما تقوم بعد ذلك بإنشاء kernel مع GetCurrentTimePlugin، سيقوم kernel تلقائيًا بتسلسل الوظيفة ومعاملاتها، مما ينشئ المخطط لإرساله إلى نموذج اللغة الكبير في العملية.

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
  
### خدمة Azure AI Agent

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Azure AI Agent</a> هي إطار عمل وكيل جديد مصمم لتمكين المطورين من بناء، ونشر، وتوسيع وكلاء ذكاء اصطناعي عالي الجودة وقابل للتوسيع بأمان دون الحاجة إلى إدارة موارد الحوسبة والتخزين الأساسية. إنها مفيدة بشكل خاص للتطبيقات المؤسسية لأنها خدمة مُدارة بالكامل مع أمان على مستوى المؤسسات.

عند مقارنتها بالتطوير باستخدام واجهة برمجة تطبيقات نموذج اللغة الكبير مباشرةً، توفر خدمة Azure AI Agent بعض المزايا، بما في ذلك:

- استدعاء الأدوات تلقائيًا – لا حاجة لتحليل استدعاء الأداة، أو استدعاء الأداة، أو التعامل مع الاستجابة؛ يتم الآن تنفيذ كل هذا على الخادم.
- إدارة البيانات بأمان – بدلاً من إدارة حالة المحادثة الخاصة بك، يمكنك الاعتماد على المواضيع لتخزين جميع المعلومات التي تحتاجها.
- أدوات جاهزة – أدوات يمكنك استخدامها للتفاعل مع مصادر بياناتك، مثل Bing، Azure AI Search، وAzure Functions.

يمكن تقسيم الأدوات المتاحة في خدمة Azure AI Agent إلى فئتين:

1. أدوات المعرفة:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">التأريض باستخدام بحث Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">البحث في الملفات</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. أدوات الإجراءات:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">استدعاء الوظائف</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">مفسر الأكواد</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">الأدوات المعرفة بواسطة OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">وظائف Azure</a>

تتيح لنا خدمة الوكيل استخدام هذه الأدوات معًا كـ `toolset`. كما أنها تستخدم `threads` التي تتبع تاريخ الرسائل من محادثة معينة.

تخيل أنك وكيل مبيعات في شركة تدعى Contoso. تريد تطوير وكيل محادثة يمكنه الإجابة على الأسئلة حول بيانات مبيعاتك.

توضح الصورة التالية كيف يمكنك استخدام خدمة Azure AI Agent لتحليل بيانات مبيعاتك:

![خدمة الوكيل قيد العمل](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ar.jpg)

لاستخدام أي من هذه الأدوات مع الخدمة، يمكننا إنشاء عميل وتعريف أداة أو مجموعة أدوات. لتنفيذ ذلك عمليًا، يمكننا استخدام كود Python التالي. سيتمكن نموذج اللغة الكبير من النظر إلى مجموعة الأدوات وتحديد ما إذا كان سيستخدم الوظيفة التي أنشأها المستخدم، `fetch_sales_data_using_sqlite_query`، أو مفسر الأكواد الجاهز بناءً على طلب المستخدم.

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

## ما هي الاعتبارات الخاصة باستخدام نمط تصميم استخدام الأدوات لبناء وكلاء ذكاء اصطناعي موثوقين؟

من المخاوف الشائعة مع SQL الذي يتم إنشاؤه ديناميكيًا بواسطة نماذج اللغة الكبيرة هو الأمان، خاصة خطر حقن SQL أو الإجراءات الضارة، مثل حذف أو العبث بقاعدة البيانات. على الرغم من أن هذه المخاوف مشروعة، إلا أنه يمكن التخفيف منها بشكل فعال من خلال تكوين أذونات الوصول إلى قاعدة البيانات بشكل صحيح. بالنسبة لمعظم قواعد البيانات، يتضمن ذلك تكوين قاعدة البيانات كقراءة فقط. بالنسبة لخدمات قواعد البيانات مثل PostgreSQL أو Azure SQL، يجب تعيين التطبيق دور قراءة فقط (SELECT).

تشغيل التطبيق في بيئة آمنة يعزز الحماية بشكل أكبر. في السيناريوهات المؤسسية، يتم عادةً استخراج البيانات وتحويلها من الأنظمة التشغيلية إلى قاعدة بيانات للقراءة فقط أو مستودع بيانات يحتوي على مخطط سهل الاستخدام. يضمن هذا النهج أن البيانات آمنة، ومحسنة للأداء وسهولة الوصول، وأن التطبيق لديه وصول مقيد للقراءة فقط.

### هل لديك المزيد من الأسئلة حول أنماط تصميم استخدام الأدوات؟
انضم إلى [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، وحضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## موارد إضافية

## الدرس السابق

[فهم أنماط التصميم الوكيلية](../03-agentic-design-patterns/README.md)

## الدرس التالي

[Agentic RAG](../05-agentic-rag/README.md)

---

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.