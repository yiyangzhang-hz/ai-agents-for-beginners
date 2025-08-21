<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d24f735b3c326b2e515f049a0330e54",
  "translation_date": "2025-08-21T12:18:13+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ur"
}
-->
[![اے آئی ایجنٹس کو بہتر ڈیزائن کرنے کا طریقہ](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ur.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

# ٹول استعمال کرنے کا ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ یہ اے آئی ایجنٹس کو زیادہ وسیع صلاحیتیں فراہم کرتے ہیں۔ ایجنٹ کے پاس محدود ایکشنز کی بجائے، ٹول شامل کرنے سے وہ اب مختلف قسم کے ایکشنز انجام دے سکتا ہے۔ اس باب میں، ہم ٹول استعمال کرنے کے ڈیزائن پیٹرن پر نظر ڈالیں گے، جو بیان کرتا ہے کہ اے آئی ایجنٹس مخصوص ٹولز کو اپنے مقاصد حاصل کرنے کے لیے کیسے استعمال کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جوابات تلاش کریں گے:

- ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟
- یہ کن استعمال کے کیسز پر لاگو ہو سکتا ہے؟
- اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟
- قابل اعتماد اے آئی ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال کے لیے کون سے خاص پہلوؤں پر غور کرنا ضروری ہے؟

## سیکھنے کے اہداف

اس سبق کو مکمل کرنے کے بعد، آپ قابل ہوں گے:

- ٹول استعمال کرنے کے ڈیزائن پیٹرن اور اس کے مقصد کی وضاحت کریں۔
- ان استعمال کے کیسز کی شناخت کریں جہاں ٹول استعمال کرنے کا ڈیزائن پیٹرن قابل اطلاق ہے۔
- اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے ضروری کلیدی عناصر کو سمجھیں۔
- اس ڈیزائن پیٹرن کے ذریعے اے آئی ایجنٹس میں اعتماد کو یقینی بنانے کے لیے غور و فکر کو پہچانیں۔

## ٹول استعمال کرنے کا ڈیزائن پیٹرن کیا ہے؟

**ٹول استعمال کرنے کا ڈیزائن پیٹرن** ایل ایل ایمز کو بیرونی ٹولز کے ساتھ تعامل کرنے کی صلاحیت فراہم کرنے پر مرکوز ہے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز وہ کوڈ ہیں جو ایجنٹ کے ذریعے ایکشنز انجام دینے کے لیے چلائے جا سکتے ہیں۔ ایک ٹول ایک سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا کسی تھرڈ پارٹی سروس جیسے اسٹاک قیمت کی تلاش یا موسم کی پیش گوئی کے لیے API کال۔ اے آئی ایجنٹس کے تناظر میں، ٹولز کو **ماڈل کے ذریعے پیدا کردہ فنکشن کالز** کے جواب میں ایجنٹس کے ذریعے چلانے کے لیے ڈیزائن کیا گیا ہے۔

## یہ کن استعمال کے کیسز پر لاگو ہو سکتا ہے؟

اے آئی ایجنٹس ٹولز کا استعمال کرکے پیچیدہ کام مکمل کر سکتے ہیں، معلومات حاصل کر سکتے ہیں، یا فیصلے کر سکتے ہیں۔ ٹول استعمال کرنے کا ڈیزائن پیٹرن اکثر ان منظرناموں میں استعمال ہوتا ہے جہاں بیرونی نظاموں جیسے ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز کے ساتھ متحرک تعامل کی ضرورت ہوتی ہے۔ یہ صلاحیت مختلف استعمال کے کیسز کے لیے مفید ہے، جن میں شامل ہیں:

- **متحرک معلومات کی بازیافت:** ایجنٹس بیرونی APIs یا ڈیٹا بیس کو سوالات بھیج کر تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً، SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے سوالات، اسٹاک قیمتوں یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کا نفاذ اور تشریح:** ایجنٹس کوڈ یا اسکرپٹس چلا سکتے ہیں تاکہ ریاضی کے مسائل حل کریں، رپورٹس تیار کریں، یا سیمولیشنز انجام دیں۔
- **ورک فلو آٹومیشن:** ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسے ٹولز کو مربوط کرکے بار بار یا کثیر مرحلہ ورک فلو کو خودکار بنانا۔
- **کسٹمر سپورٹ:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیس کے ساتھ تعامل کرکے صارف کے سوالات حل کر سکتے ہیں۔
- **مواد کی تخلیق اور تدوین:** ایجنٹس گرامر چیکرز، ٹیکسٹ سمریزرز، یا مواد کی حفاظت کے جائزہ لینے والے ٹولز کا استعمال کرکے مواد کی تخلیق کے کاموں میں مدد فراہم کر سکتے ہیں۔

## ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟

یہ بلڈنگ بلاکس اے آئی ایجنٹ کو مختلف قسم کے کام انجام دینے کی اجازت دیتے ہیں۔ آئیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو نافذ کرنے کے لیے ضروری کلیدی عناصر پر نظر ڈالیں:

- **فنکشن/ٹول اسکیمہ:** دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، مطلوبہ پیرامیٹرز، اور متوقع آؤٹ پٹس شامل ہیں۔ یہ اسکیمہ ایل ایل ایم کو سمجھنے میں مدد دیتے ہیں کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔
- **فنکشن نفاذ منطق:** یہ طے کرتا ہے کہ صارف کے ارادے اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے استعمال کیا جائے۔ اس میں پلانر ماڈیولز، روٹنگ میکانزم، یا مشروط فلو شامل ہو سکتے ہیں جو متحرک طور پر ٹول کے استعمال کا تعین کرتے ہیں۔
- **پیغام ہینڈلنگ سسٹم:** وہ اجزاء جو صارف کے ان پٹ، ایل ایل ایم کے جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگو کے بہاؤ کو منظم کرتے ہیں۔
- **ٹول انٹیگریشن فریم ورک:** وہ انفراسٹرکچر جو ایجنٹ کو مختلف ٹولز سے جوڑتا ہے، چاہے وہ سادہ فنکشنز ہوں یا پیچیدہ بیرونی سروسز۔
- **غلطی ہینڈلنگ اور توثیق:** وہ میکانزم جو ٹول کے نفاذ میں ناکامیوں کو سنبھالتے ہیں، پیرامیٹرز کی توثیق کرتے ہیں، اور غیر متوقع جوابات کا انتظام کرتے ہیں۔
- **اسٹیٹ مینجمنٹ:** گفتگو کے سیاق و سباق، پچھلے ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر مرحلہ تعاملات میں مستقل مزاجی کو یقینی بنایا جا سکے۔

اب، آئیے فنکشن/ٹول کالنگ کو مزید تفصیل سے دیکھتے ہیں۔

### فنکشن/ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس کے ذریعے ہم بڑے زبان کے ماڈلز (LLMs) کو ٹولز کے ساتھ تعامل کرنے کے قابل بناتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو ایک دوسرے کے ساتھ استعمال ہوتے دیکھیں گے کیونکہ 'فنکشنز' (دوبارہ استعمال کے قابل کوڈ کے بلاکس) وہ 'ٹولز' ہیں جنہیں ایجنٹس کام انجام دینے کے لیے استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، ایل ایل ایم کو صارف کی درخواست کو فنکشن کی تفصیل کے ساتھ موازنہ کرنا ہوگا۔ ایسا کرنے کے لیے، دستیاب فنکشنز کی تفصیلات پر مشتمل ایک اسکیمہ ایل ایل ایم کو بھیجا جاتا ہے۔ ایل ایل ایم پھر کام کے لیے سب سے موزوں فنکشن کا انتخاب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب کردہ فنکشن کو چلایا جاتا ہے، اس کا جواب ایل ایل ایم کو واپس بھیجا جاتا ہے، جو صارف کی درخواست کا جواب دینے کے لیے معلومات کا استعمال کرتا ہے۔

ڈویلپرز کے لیے ایجنٹس کے لیے فنکشن کالنگ کو نافذ کرنے کے لیے، آپ کو ضرورت ہوگی:

1. ایک ایل ایل ایم ماڈل جو فنکشن کالنگ کو سپورٹ کرتا ہو
2. فنکشن کی تفصیلات پر مشتمل ایک اسکیمہ
3. ہر بیان کردہ فنکشن کے لیے کوڈ

آئیے ایک مثال کے ذریعے وضاحت کریں کہ کسی شہر میں موجودہ وقت حاصل کرنے کے لیے یہ کیسے کام کرتا ہے:

1. **فنکشن کالنگ کو سپورٹ کرنے والے ایل ایل ایم کو شروع کریں:**

    تمام ماڈلز فنکشن کالنگ کو سپورٹ نہیں کرتے، لہذا یہ چیک کرنا ضروری ہے کہ آپ جو ایل ایل ایم استعمال کر رہے ہیں وہ کرتا ہے۔ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کو سپورٹ کرتا ہے۔ ہم Azure OpenAI کلائنٹ کو شروع کرکے آغاز کر سکتے ہیں۔

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **فنکشن اسکیمہ بنائیں:**

    اگلا، ہم ایک JSON اسکیمہ کی وضاحت کریں گے جس میں فنکشن کا نام، فنکشن کیا کرتا ہے اس کی تفصیل، اور فنکشن پیرامیٹرز کے نام اور تفصیلات شامل ہوں گی۔
    ہم اس اسکیمہ کو پہلے سے بنائے گئے کلائنٹ کے ساتھ پاس کریں گے، ساتھ ہی صارف کی درخواست کو بھی تاکہ سان فرانسسکو میں وقت معلوم کیا جا سکے۔ اہم بات یہ ہے کہ **ٹول کال** وہ ہے جو واپس آتی ہے، **سوال کا حتمی جواب نہیں**۔ جیسا کہ پہلے ذکر کیا گیا، ایل ایل ایم اس کام کے لیے منتخب کردہ فنکشن کا نام اور اس کے دلائل واپس کرتا ہے۔

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
  
1. **کام انجام دینے کے لیے مطلوبہ فنکشن کوڈ:**

    اب جب کہ ایل ایل ایم نے فیصلہ کر لیا ہے کہ کون سا فنکشن چلایا جانا چاہیے، کام انجام دینے کے لیے کوڈ کو نافذ اور چلانے کی ضرورت ہے۔
    ہم موجودہ وقت حاصل کرنے کے لیے Python میں کوڈ نافذ کر سکتے ہیں۔ ہمیں response_message سے نام اور دلائل نکالنے کے لیے کوڈ بھی لکھنا ہوگا تاکہ حتمی نتیجہ حاصل کیا جا سکے۔

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

فنکشن کالنگ زیادہ تر، اگر تمام نہیں، ایجنٹ ٹول استعمال کے ڈیزائن کے مرکز میں ہے، تاہم اسے شروع سے نافذ کرنا بعض اوقات چیلنجنگ ہو سکتا ہے۔
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹک فریم ورک ہمیں ٹول استعمال کو نافذ کرنے کے لیے پہلے سے بنے ہوئے بلڈنگ بلاکس فراہم کرتے ہیں۔

## ایجنٹک فریم ورک کے ساتھ ٹول استعمال کی مثالیں

یہاں کچھ مثالیں ہیں کہ آپ مختلف ایجنٹک فریم ورک کا استعمال کرتے ہوئے ٹول استعمال کرنے کے ڈیزائن پیٹرن کو کیسے نافذ کر سکتے ہیں:

### سیمینٹک کرنل

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سیمینٹک کرنل</a> .NET، Python، اور Java ڈویلپرز کے لیے ایک اوپن سورس اے آئی فریم ورک ہے جو بڑے زبان کے ماڈلز (LLMs) کے ساتھ کام کرتے ہیں۔ یہ فنکشن کالنگ کے استعمال کے عمل کو آسان بناتا ہے کیونکہ یہ خود بخود آپ کے فنکشنز اور ان کے پیرامیٹرز کو ماڈل کے لیے بیان کرتا ہے، جسے <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سیریلائزنگ</a> کہا جاتا ہے۔ یہ ماڈل اور آپ کے کوڈ کے درمیان بات چیت کو بھی سنبھالتا ہے۔ ایجنٹک فریم ورک جیسے سیمینٹک کرنل کا ایک اور فائدہ یہ ہے کہ یہ آپ کو پہلے سے بنے ہوئے ٹولز تک رسائی فراہم کرتا ہے جیسے <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">فائل سرچ</a> اور <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">کوڈ انٹرپریٹر</a>۔

مندرجہ ذیل خاکہ سیمینٹک کرنل کے ساتھ فنکشن کالنگ کے عمل کو ظاہر کرتا ہے:

![فنکشن کالنگ](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ur.png)

سیمینٹک کرنل میں فنکشنز/ٹولز کو <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">پلگ انز</a> کہا جاتا ہے۔ ہم پہلے دیکھے گئے `get_current_time` فنکشن کو ایک پلگ ان میں تبدیل کر سکتے ہیں، اسے ایک کلاس میں تبدیل کرکے جس میں فنکشن موجود ہو۔ ہم `kernel_function` ڈیکوریٹر کو بھی درآمد کر سکتے ہیں، جو فنکشن کی تفصیل لیتا ہے۔ جب آپ پھر GetCurrentTimePlugin کے ساتھ ایک کرنل بناتے ہیں، تو کرنل خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کرے گا، ایل ایل ایم کو بھیجنے کے لیے اسکیمہ بناتے ہوئے۔

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
  
### Azure AI ایجنٹ سروس

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ایجنٹ سروس</a> ایک نیا ایجنٹک فریم ورک ہے جو ڈویلپرز کو اعلیٰ معیار کے، اور قابل توسیع اے آئی ایجنٹس کو محفوظ طریقے سے بنانے، تعینات کرنے، اور پیمانے پر لانے کے لیے ڈیزائن کیا گیا ہے، بغیر بنیادی کمپیوٹ اور اسٹوریج وسائل کا انتظام کیے۔ یہ خاص طور پر انٹرپرائز ایپلیکیشنز کے لیے مفید ہے کیونکہ یہ ایک مکمل طور پر منظم سروس ہے جس میں انٹرپرائز گریڈ سیکیورٹی ہے۔

ایل ایل ایم API کے ساتھ براہ راست ترقی کے مقابلے میں، Azure AI ایجنٹ سروس کچھ فوائد فراہم کرتی ہے، جن میں شامل ہیں:

- خودکار ٹول کالنگ – ٹول کال کو پارس کرنے، ٹول کو چلانے، اور جواب کو سنبھالنے کی ضرورت نہیں؛ یہ سب اب سرور سائیڈ پر کیا جاتا ہے۔
- محفوظ طریقے سے منظم ڈیٹا – اپنی گفتگو کی حالت کا انتظام کرنے کے بجائے، آپ تھریڈز پر انحصار کر سکتے ہیں تاکہ آپ کو درکار تمام معلومات کو ذخیرہ کیا جا سکے۔
- پہلے سے بنے ہوئے ٹولز – وہ ٹولز جنہیں آپ اپنے ڈیٹا سورسز کے ساتھ تعامل کے لیے استعمال کر سکتے ہیں، جیسے Bing، Azure AI Search، اور Azure Functions۔

Azure AI ایجنٹ سروس میں دستیاب ٹولز کو دو اقسام میں تقسیم کیا جا سکتا ہے:

1. نالج ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing سرچ کے ساتھ گراؤنڈنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">فائل سرچ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI سرچ</a>

2. ایکشن ٹولز:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">فنکشن کالنگ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">کوڈ انٹرپریٹر</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI کے ذریعے بیان کردہ ٹولز</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure فنکشنز</a>

ایجنٹ سروس ہمیں ان ٹولز کو `toolset` کے طور پر ایک ساتھ استعمال کرنے کی اجازت دیتی ہے۔ یہ `threads` کا بھی استعمال کرتی ہے جو کسی خاص گفتگو سے پیغامات کی تاریخ کو ٹریک کرتے ہیں۔

تصور کریں کہ آپ Contoso نامی کمپنی میں ایک سیلز ایجنٹ ہیں۔ آپ ایک گفتگو ایجنٹ تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جواب دے سکے۔

مندرجہ ذیل تصویر ظاہر کرتی ہے کہ آپ Azure AI ایجنٹ سروس کو اپنے سیلز ڈیٹا کا تجزیہ کرنے کے لیے کیسے استعمال کر سکتے ہیں:

![ایجنٹک سروس ایکشن میں](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ur.jpg)

ان ٹولز کو سروس کے ساتھ استعمال کرنے کے لیے ہم ایک کلائنٹ بنا سکتے ہیں اور ایک ٹول یا ٹول سیٹ کی وضاحت کر سکتے ہیں۔ اسے عملی طور پر نافذ کرنے کے لیے ہم درج ذیل Python کوڈ استعمال کر سکتے ہیں۔ ایل ایل ایم ٹول سیٹ کو دیکھ سکے گا اور صارف کے بنائے گئے فنکشن، `fetch_sales_data_using_sqlite_query`، یا پہلے سے بنے ہوئے کوڈ انٹرپریٹر کو صارف کی درخواست کے مطابق استعمال کرنے کا فیصلہ کرے گا۔

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

## قابل اعتماد اے آئی ایجنٹس بنانے کے لیے ٹول استعمال کرنے کے ڈیزائن پیٹرن کے استعمال کے لیے کون سے خاص پہلوؤں پر غور کرنا ضروری ہے؟

ایل ایل ایمز کے ذریعے متحرک طور پر تیار کردہ SQL کے ساتھ ایک عام تشویش سیکیورٹی ہے، خاص طور پر SQL انجیکشن
<a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">
ایزور اے آئی ایجنٹس سروس ورکشاپ  
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">کنٹوسو کریئیٹو رائٹر ملٹی-ایجنٹ ورکشاپ</a>  
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سیمینٹک کرنل فنکشن کالنگ ٹیوٹوریل</a>  
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">سیمینٹک کرنل کوڈ انٹرپریٹر</a>  
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">آٹو جن ٹولز</a>  

## پچھلا سبق  

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)  

## اگلا سبق  

[ایجنٹک آر اے جی](../05-agentic-rag/README.md)  

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز، جو اس کی اصل زبان میں ہے، کو مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔