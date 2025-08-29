<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T09:31:43+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ur"
}
-->
[![اچھے AI ایجنٹس ڈیزائن کرنے کا طریقہ](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.ur.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(اوپر دی گئی تصویر پر کلک کریں تاکہ اس سبق کی ویڈیو دیکھ سکیں)_

# ٹول یوز ڈیزائن پیٹرن

ٹولز دلچسپ ہیں کیونکہ یہ AI ایجنٹس کو زیادہ وسیع صلاحیتیں فراہم کرتے ہیں۔ ایجنٹ کے محدود اعمال کے بجائے، ایک ٹول شامل کرنے سے ایجنٹ اب مختلف قسم کے اعمال انجام دے سکتا ہے۔ اس باب میں، ہم ٹول یوز ڈیزائن پیٹرن پر غور کریں گے، جو بیان کرتا ہے کہ AI ایجنٹس مخصوص ٹولز کو اپنے مقاصد حاصل کرنے کے لیے کیسے استعمال کر سکتے ہیں۔

## تعارف

اس سبق میں، ہم درج ذیل سوالات کے جوابات تلاش کریں گے:

- ٹول یوز ڈیزائن پیٹرن کیا ہے؟
- یہ کن استعمالات کے لیے لاگو ہو سکتا ہے؟
- اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟
- قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول یوز ڈیزائن پیٹرن استعمال کرنے کے لیے کون سے خاص پہلوؤں پر غور کرنا چاہیے؟

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ قابل ہوں گے:

- ٹول یوز ڈیزائن پیٹرن اور اس کے مقصد کی وضاحت کریں۔
- وہ استعمالات شناخت کریں جہاں ٹول یوز ڈیزائن پیٹرن لاگو ہو سکتا ہے۔
- ان اہم عناصر کو سمجھیں جو اس ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار ہیں۔
- AI ایجنٹس میں اس ڈیزائن پیٹرن کے استعمال کے دوران اعتماد کو یقینی بنانے کے پہلوؤں کو پہچانیں۔

## ٹول یوز ڈیزائن پیٹرن کیا ہے؟

**ٹول یوز ڈیزائن پیٹرن** LLMs کو بیرونی ٹولز کے ساتھ تعامل کرنے کی صلاحیت فراہم کرنے پر مرکوز ہے تاکہ مخصوص مقاصد حاصل کیے جا سکیں۔ ٹولز وہ کوڈ ہیں جو ایجنٹ کے ذریعے اعمال انجام دینے کے لیے چلائے جا سکتے ہیں۔ ایک ٹول ایک سادہ فنکشن ہو سکتا ہے جیسے کیلکولیٹر، یا کسی تیسرے فریق کی سروس جیسے اسٹاک پرائس لوک اپ یا موسم کی پیش گوئی کے لیے API کال۔ AI ایجنٹس کے سیاق و سباق میں، ٹولز کو **ماڈل کے ذریعے پیدا کردہ فنکشن کالز** کے جواب میں ایجنٹس کے ذریعے چلانے کے لیے ڈیزائن کیا گیا ہے۔

## یہ کن استعمالات کے لیے لاگو ہو سکتا ہے؟

AI ایجنٹس ٹولز کا فائدہ اٹھا کر پیچیدہ کام مکمل کر سکتے ہیں، معلومات حاصل کر سکتے ہیں، یا فیصلے کر سکتے ہیں۔ ٹول یوز ڈیزائن پیٹرن اکثر ان منظرناموں میں استعمال ہوتا ہے جن میں بیرونی نظاموں جیسے ڈیٹا بیس، ویب سروسز، یا کوڈ انٹرپریٹرز کے ساتھ متحرک تعامل کی ضرورت ہوتی ہے۔ یہ صلاحیت مختلف استعمالات کے لیے مفید ہے، جن میں شامل ہیں:

- **متحرک معلومات کی بازیافت:** ایجنٹس بیرونی APIs یا ڈیٹا بیس کو استفسار کر کے تازہ ترین ڈیٹا حاصل کر سکتے ہیں (مثلاً، SQLite ڈیٹا بیس سے ڈیٹا تجزیہ کے لیے استفسار کرنا، اسٹاک کی قیمتیں یا موسم کی معلومات حاصل کرنا)۔
- **کوڈ کا نفاذ اور تشریح:** ایجنٹس کوڈ یا اسکرپٹس چلا سکتے ہیں تاکہ ریاضی کے مسائل حل کریں، رپورٹس تیار کریں، یا تخروپن انجام دیں۔
- **ورک فلو آٹومیشن:** ٹاسک شیڈولرز، ای میل سروسز، یا ڈیٹا پائپ لائنز جیسے ٹولز کو مربوط کر کے بار بار یا کثیر مرحلہ ورک فلو کو خودکار بنانا۔
- **کسٹمر سپورٹ:** ایجنٹس CRM سسٹمز، ٹکٹنگ پلیٹ فارمز، یا نالج بیسز کے ساتھ تعامل کر کے صارف کے سوالات حل کر سکتے ہیں۔
- **مواد کی تخلیق اور تدوین:** ایجنٹس گرامر چیکرز، ٹیکسٹ سمریزرز، یا مواد کی حفاظت کے جائزہ لینے والے ٹولز کا فائدہ اٹھا کر مواد تخلیق کے کاموں میں مدد کر سکتے ہیں۔

## ٹول یوز ڈیزائن پیٹرن کو نافذ کرنے کے لیے کون سے عناصر/بلڈنگ بلاکس درکار ہیں؟

یہ بلڈنگ بلاکس AI ایجنٹ کو مختلف قسم کے کام انجام دینے کی اجازت دیتے ہیں۔ آئیے ان اہم عناصر پر نظر ڈالیں جو ٹول یوز ڈیزائن پیٹرن کو نافذ کرنے کے لیے درکار ہیں:

- **فنکشن/ٹول اسکیمے:** دستیاب ٹولز کی تفصیلی تعریفیں، جن میں فنکشن کا نام، مقصد، مطلوبہ پیرامیٹرز، اور متوقع آؤٹ پٹس شامل ہیں۔ یہ اسکیمے LLM کو یہ سمجھنے کے قابل بناتے ہیں کہ کون سے ٹولز دستیاب ہیں اور درست درخواستیں کیسے بنائی جائیں۔
- **فنکشن نفاذ منطق:** یہ طے کرتا ہے کہ صارف کے ارادے اور گفتگو کے سیاق و سباق کی بنیاد پر ٹولز کو کب اور کیسے استعمال کیا جائے۔ اس میں پلانر ماڈیولز، روٹنگ میکانزم، یا مشروط فلو شامل ہو سکتے ہیں جو متحرک طور پر ٹول کے استعمال کا تعین کرتے ہیں۔
- **پیغام ہینڈلنگ سسٹم:** وہ اجزاء جو صارف کے ان پٹ، LLM کے جوابات، ٹول کالز، اور ٹول آؤٹ پٹس کے درمیان گفتگو کے بہاؤ کو منظم کرتے ہیں۔
- **ٹول انضمام فریم ورک:** وہ انفراسٹرکچر جو ایجنٹ کو مختلف ٹولز سے جوڑتا ہے، چاہے وہ سادہ فنکشنز ہوں یا پیچیدہ بیرونی خدمات۔
- **خرابی ہینڈلنگ اور توثیق:** ٹول کے نفاذ میں ناکامیوں کو سنبھالنے، پیرامیٹرز کی توثیق کرنے، اور غیر متوقع جوابات کا انتظام کرنے کے طریقہ کار۔
- **اسٹیٹ مینجمنٹ:** گفتگو کے سیاق و سباق، پچھلے ٹول تعاملات، اور مستقل ڈیٹا کو ٹریک کرتا ہے تاکہ کثیر موڑ تعاملات میں مستقل مزاجی کو یقینی بنایا جا سکے۔

اب، آئیے فنکشن/ٹول کالنگ کو مزید تفصیل سے دیکھتے ہیں۔

### فنکشن/ٹول کالنگ

فنکشن کالنگ وہ بنیادی طریقہ ہے جس کے ذریعے ہم بڑے لینگویج ماڈلز (LLMs) کو ٹولز کے ساتھ تعامل کرنے کے قابل بناتے ہیں۔ آپ اکثر 'فنکشن' اور 'ٹول' کو ایک دوسرے کے متبادل کے طور پر دیکھیں گے کیونکہ 'فنکشنز' (دوبارہ استعمال کے قابل کوڈ کے بلاکس) وہ 'ٹولز' ہیں جنہیں ایجنٹس کام انجام دینے کے لیے استعمال کرتے ہیں۔ کسی فنکشن کے کوڈ کو چلانے کے لیے، LLM کو صارف کی درخواست کا موازنہ فنکشن کی تفصیل سے کرنا ہوتا ہے۔ ایسا کرنے کے لیے، تمام دستیاب فنکشنز کی تفصیلات پر مشتمل ایک اسکیمہ LLM کو بھیجا جاتا ہے۔ پھر LLM اس کام کے لیے سب سے موزوں فنکشن کا انتخاب کرتا ہے اور اس کا نام اور دلائل واپس کرتا ہے۔ منتخب کردہ فنکشن کو چلایا جاتا ہے، اس کا جواب LLM کو واپس بھیجا جاتا ہے، جو اس معلومات کو صارف کی درخواست کا جواب دینے کے لیے استعمال کرتا ہے۔

ایجنٹس کے لیے فنکشن کالنگ کو نافذ کرنے کے لیے، آپ کو ضرورت ہوگی:

1. ایک LLM ماڈل جو فنکشن کالنگ کو سپورٹ کرتا ہو
2. ایک اسکیمہ جس میں فنکشن کی تفصیلات ہوں
3. ہر بیان کردہ فنکشن کے لیے کوڈ

آئیے ایک مثال کے ذریعے وضاحت کریں کہ کسی شہر میں موجودہ وقت معلوم کرنے کے لیے یہ کیسے کام کرتا ہے:

1. **ایک LLM شروع کریں جو فنکشن کالنگ کو سپورٹ کرتا ہو:**

    تمام ماڈلز فنکشن کالنگ کو سپورٹ نہیں کرتے، اس لیے یہ چیک کرنا ضروری ہے کہ آپ جو LLM استعمال کر رہے ہیں وہ کرتا ہے یا نہیں۔ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> فنکشن کالنگ کو سپورٹ کرتا ہے۔ ہم Azure OpenAI کلائنٹ کو شروع کر کے شروعات کر سکتے ہیں۔

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **فنکشن اسکیمہ بنائیں:**

    اس کے بعد ہم ایک JSON اسکیمہ کی وضاحت کریں گے جس میں فنکشن کا نام، فنکشن کے کام کی وضاحت، اور فنکشن کے پیرامیٹرز کے نام اور وضاحت شامل ہوں۔  
    ہم اس اسکیمہ کو پہلے سے بنائے گئے کلائنٹ کے ساتھ ساتھ صارف کی درخواست کے ساتھ پاس کریں گے تاکہ سان فرانسسکو میں وقت معلوم کیا جا سکے۔ اہم بات یہ ہے کہ ایک **ٹول کال** واپس کی جاتی ہے، **سوال کا حتمی جواب نہیں**۔ جیسا کہ پہلے ذکر کیا گیا، LLM اس کام کے لیے منتخب کردہ فنکشن کا نام اور اس کے دلائل واپس کرتا ہے۔

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
  
1. **کام انجام دینے کے لیے درکار فنکشن کوڈ:**

    اب جب کہ LLM نے منتخب کر لیا ہے کہ کون سا فنکشن چلایا جانا چاہیے، اس کام کو انجام دینے کے لیے کوڈ کو نافذ اور چلانے کی ضرورت ہے۔  
    ہم Python میں موجودہ وقت حاصل کرنے کے لیے کوڈ نافذ کر سکتے ہیں۔ ہمیں response_message سے نام اور دلائل نکالنے کے لیے کوڈ بھی لکھنا ہوگا تاکہ حتمی نتیجہ حاصل کیا جا سکے۔

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

فنکشن کالنگ زیادہ تر، اگر تمام نہیں، ایجنٹ ٹول یوز ڈیزائن کے مرکز میں ہے، تاہم اسے شروع سے نافذ کرنا بعض اوقات چیلنجنگ ہو سکتا ہے۔  
جیسا کہ ہم نے [سبق 2](../../../02-explore-agentic-frameworks) میں سیکھا، ایجنٹک فریم ورک ہمیں ٹول یوز کو نافذ کرنے کے لیے پہلے سے بنے ہوئے بلڈنگ بلاکس فراہم کرتے ہیں۔

## ایجنٹک فریم ورک کے ساتھ ٹول یوز کی مثالیں

یہاں کچھ مثالیں ہیں کہ آپ مختلف ایجنٹک فریم ورک کا استعمال کرتے ہوئے ٹول یوز ڈیزائن پیٹرن کو کیسے نافذ کر سکتے ہیں:

### سیمینٹک کرنل

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">سیمینٹک کرنل</a> .NET، Python، اور Java ڈویلپرز کے لیے ایک اوپن سورس AI فریم ورک ہے جو بڑے لینگویج ماڈلز (LLMs) کے ساتھ کام کرتے ہیں۔ یہ فنکشن کالنگ کے عمل کو آسان بناتا ہے کیونکہ یہ آپ کے فنکشنز اور ان کے پیرامیٹرز کو ماڈل کے لیے خود بخود بیان کرتا ہے، جسے <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">سیریلائزنگ</a> کہا جاتا ہے۔ یہ ماڈل اور آپ کے کوڈ کے درمیان بات چیت کو بھی سنبھالتا ہے۔ سیمینٹک کرنل جیسے ایجنٹک فریم ورک کا ایک اور فائدہ یہ ہے کہ یہ آپ کو پہلے سے بنے ہوئے ٹولز تک رسائی فراہم کرتا ہے جیسے <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">فائل سرچ</a> اور <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">کوڈ انٹرپریٹر</a>۔

مندرجہ ذیل ڈایاگرام سیمینٹک کرنل کے ساتھ فنکشن کالنگ کے عمل کو واضح کرتا ہے:

![فنکشن کالنگ](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.ur.png)

سیمینٹک کرنل میں فنکشنز/ٹولز کو <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">پلگ انز</a> کہا جاتا ہے۔ ہم `get_current_time` فنکشن کو، جو ہم نے پہلے دیکھا، ایک پلگ ان میں تبدیل کر سکتے ہیں، اسے ایک کلاس میں تبدیل کر کے جس میں یہ فنکشن موجود ہو۔ ہم `kernel_function` ڈیکوریٹر بھی درآمد کر سکتے ہیں، جو فنکشن کی وضاحت لیتا ہے۔ جب آپ GetCurrentTimePlugin کے ساتھ ایک کرنل بناتے ہیں، تو کرنل خود بخود فنکشن اور اس کے پیرامیٹرز کو سیریلائز کر دے گا، اس عمل میں اسکیمہ بنا کر LLM کو بھیج دے گا۔

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ایجنٹ سروس</a> ایک نیا ایجنٹک فریم ورک ہے جو ڈویلپرز کو اعلیٰ معیار کے، قابل توسیع AI ایجنٹس کو محفوظ طریقے سے بنانے، تعینات کرنے، اور اسکیل کرنے کے قابل بناتا ہے، بغیر بنیادی کمپیوٹ اور اسٹوریج وسائل کو منظم کرنے کی ضرورت کے۔ یہ خاص طور پر انٹرپرائز ایپلیکیشنز کے لیے مفید ہے کیونکہ یہ ایک مکمل طور پر منظم سروس ہے جس میں انٹرپرائز گریڈ سیکیورٹی ہے۔

LLM API کے ساتھ براہ راست ترقی کرنے کے مقابلے میں، Azure AI ایجنٹ سروس کچھ فوائد فراہم کرتی ہے، جن میں شامل ہیں:

- خودکار ٹول کالنگ – ٹول کال کو پارس کرنے، ٹول کو چلانے، اور جواب کو ہینڈل کرنے کی ضرورت نہیں؛ یہ سب اب سرور سائیڈ پر کیا جاتا ہے۔
- محفوظ طریقے سے منظم ڈیٹا – اپنی گفتگو کی حالت کو منظم کرنے کے بجائے، آپ تھریڈز پر انحصار کر سکتے ہیں تاکہ آپ کو درکار تمام معلومات کو اسٹور کیا جا سکے۔
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

ایجنٹ سروس ہمیں ان ٹولز کو `ٹول سیٹ` کے طور پر ایک ساتھ استعمال کرنے کی اجازت دیتی ہے۔ یہ `تھریڈز` کا بھی استعمال کرتی ہے جو کسی خاص گفتگو سے پیغامات کی تاریخ کو ٹریک کرتے ہیں۔

تصور کریں کہ آپ Contoso نامی کمپنی میں ایک سیلز ایجنٹ ہیں۔ آپ ایک ایسا گفتگو کرنے والا ایجنٹ تیار کرنا چاہتے ہیں جو آپ کے سیلز ڈیٹا کے بارے میں سوالات کے جوابات دے سکے۔

مندرجہ ذیل تصویر یہ واضح کرتی ہے کہ آپ Azure AI ایجنٹ سروس کو اپنے سیلز ڈیٹا کا تجزیہ کرنے کے لیے کیسے استعمال کر سکتے ہیں:

![ایجنٹک سروس ایکشن میں](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.ur.jpg)

اس سروس کے ساتھ کسی بھی ٹول کو استعمال کرنے کے لیے ہم ایک کلائنٹ بنا سکتے ہیں اور ایک ٹول یا ٹول سیٹ کی وضاحت کر سکتے ہیں۔ اسے عملی طور پر نافذ کرنے کے لیے ہم درج ذیل Python کوڈ استعمال کر سکتے ہیں۔ LLM ٹول سیٹ کو دیکھ سکے گا اور صارف کے بنائے گئے فنکشن `fetch_sales_data_using_sqlite_query` یا پہلے سے بنے ہوئے کوڈ انٹرپریٹر کو صارف کی درخواست کے مطابق استعمال کرنے کا فیصلہ کرے گا۔

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

## قابل اعتماد AI ایجنٹس بنانے کے لیے ٹول یوز ڈیزائن پیٹرن استعمال کرنے کے لیے کون سے خاص پہلوؤں پر غور کرنا چاہیے؟

LLMs کے ذریعے متحرک طور پر تیار کردہ SQL کے ساتھ ایک عام تشویش سیکیورٹی ہے، خاص طور پر SQL انجیکشن یا بدنیتی پر مبنی اعمال جیسے ڈیٹا بیس کو حذف
Azure AI Foundry Discord میں شامل ہوں [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) تاکہ دوسرے سیکھنے والوں سے ملاقات کریں، آفس آورز میں شرکت کریں اور اپنے AI Agents کے سوالات کے جوابات حاصل کریں۔

## اضافی وسائل

## پچھلا سبق

[ایجنٹک ڈیزائن پیٹرنز کو سمجھنا](../03-agentic-design-patterns/README.md)

## اگلا سبق

[ایجنٹک RAG](../05-agentic-rag/README.md)

---

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔