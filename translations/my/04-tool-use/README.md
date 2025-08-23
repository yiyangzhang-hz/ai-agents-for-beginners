<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d24f735b3c326b2e515f049a0330e54",
  "translation_date": "2025-08-21T14:07:45+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "my"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.my.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဤရုပ်ပုံကိုနှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ပါ)_

# Tool Use Design Pattern

Tools တွေက စိတ်ဝင်စားစရာကောင်းပါတယ်၊ အကြောင်းကတော့ AI အေးဂျင့်တွေကို ပိုမိုကျယ်ပြန့်တဲ့ စွမ်းရည်တွေ ပေးနိုင်လို့ပါ။ အေးဂျင့်တစ်ခုမှာ လုပ်ဆောင်နိုင်တဲ့ လှုပ်ရှားမှု အကန့်အသတ်ရှိတဲ့အစား tool တစ်ခု ထည့်သွင်းလိုက်တာနဲ့ အေးဂျင့်ဟာ အမျိုးမျိုးသော လှုပ်ရှားမှုတွေ လုပ်ဆောင်နိုင်ပါပြီ။ ဒီအခန်းမှာတော့ AI အေးဂျင့်တွေက သူတို့ရဲ့ ရည်မှန်းချက်တွေကို ရောက်ရှိအောင် အထူး tools တွေကို ဘယ်လိုအသုံးပြုနိုင်မလဲဆိုတာ ဖော်ပြတဲ့ Tool Use Design Pattern ကို လေ့လာပါမယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ ကျွန်တော်တို့ လေ့လာမယ့်မေးခွန်းတွေကတော့ -

- Tool Use Design Pattern ဆိုတာဘာလဲ?
- ဘယ်လိုအခြေအနေတွေမှာ အသုံးချနိုင်မလဲ?
- ဒီ design pattern ကို အကောင်အထည်ဖော်ဖို့ လိုအပ်တဲ့ အစိတ်အပိုင်း/အခြေခံအဆောက်အအုံတွေက ဘာတွေလဲ?
- Tool Use Design Pattern ကို အသုံးပြုပြီး ယုံကြည်ရတဲ့ AI အေးဂျင့်တွေ တည်ဆောက်ဖို့ အထူးစဉ်းစားရမယ့်အချက်တွေက ဘာတွေလဲ?

## သင်ယူရမယ့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးတဲ့အခါမှာ သင်တစ်ဦးဦး -

- Tool Use Design Pattern ရဲ့ အဓိပ္ပါယ်နဲ့ ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မယ်။
- Tool Use Design Pattern ကို အသုံးချနိုင်တဲ့ အခြေအနေတွေကို ဖော်ထုတ်နိုင်မယ်။
- ဒီ design pattern ကို အကောင်အထည်ဖော်ဖို့ လိုအပ်တဲ့ အဓိကအစိတ်အပိုင်းတွေကို နားလည်နိုင်မယ်။
- Tool Use Design Pattern ကို အသုံးပြုတဲ့ AI အေးဂျင့်တွေမှာ ယုံကြည်မှုရှိစေရန် စဉ်းစားရမယ့်အချက်တွေကို သိရှိနိုင်မယ်။

## Tool Use Design Pattern ဆိုတာဘာလဲ?

**Tool Use Design Pattern** ဟာ LLMs တွေကို အပြင်ပန်း tools တွေနဲ့ အပြန်အလှန်ဆက်သွယ်နိုင်စေဖို့ အခြေခံထားတဲ့ ပုံစံတစ်ခုဖြစ်ပါတယ်။ Tools တွေဟာ အေးဂျင့်က လှုပ်ရှားမှုတွေ လုပ်ဆောင်ဖို့ ရေးသားထားတဲ့ code တွေဖြစ်ပါတယ်။ Tool တစ်ခုဟာ calculator လို ရိုးရှင်းတဲ့ function တစ်ခုဖြစ်နိုင်သလို၊ stock price ရှာဖွေခြင်း၊ သတိရဖွယ်ရာ API call တစ်ခုလို third-party service တစ်ခုဖြစ်နိုင်ပါတယ်။ AI အေးဂျင့်တွေရဲ့ context မှာတော့ tools တွေဟာ **model-generated function calls** တွေကို အဖြစ်အပျက်အရ လုပ်ဆောင်ဖို့ ရည်ရွယ်ထားပါတယ်။

## ဘယ်လိုအခြေအနေတွေမှာ အသုံးချနိုင်မလဲ?

AI အေးဂျင့်တွေဟာ tools တွေကို အသုံးပြုပြီး ရှုပ်ထွေးတဲ့အလုပ်တွေကို ပြီးမြောက်စေခြင်း၊ အချက်အလက်တွေ ရယူခြင်း၊ သို့မဟုတ် ဆုံးဖြတ်ချက်ချခြင်းတို့ကို လုပ်ဆောင်နိုင်ပါတယ်။ Tool Use Design Pattern ကို အပြင်ပန်းစနစ်တွေ (databases, web services, code interpreters) နဲ့ အပြန်အလှန်ဆက်သွယ်ဖို့ လိုအပ်တဲ့ အခြေအနေတွေမှာ အသုံးပြုပါတယ်။ ဒီစွမ်းရည်ဟာ အမျိုးမျိုးသော အသုံးချမှုအခြေအနေများအတွက် အသုံးဝင်ပါတယ်၊ အထူးသဖြင့် -

- **Dynamic Information Retrieval:** Agents တွေဟာ external APIs သို့မဟုတ် databases တွေကို query လုပ်ပြီး နောက်ဆုံးရရှိတဲ့ အချက်အလက်တွေ ရယူနိုင်ပါတယ် (ဥပမာ- SQLite database ကို query လုပ်ပြီး data analysis လုပ်ခြင်း၊ stock price သို့မဟုတ် ရာသီဥတုအချက်အလက် ရယူခြင်း)။
- **Code Execution and Interpretation:** Agents တွေဟာ code သို့မဟုတ် scripts တွေကို run လုပ်ပြီး သင်္ချာပြဿနာတွေ ဖြေရှင်းခြင်း၊ report တွေ ဖန်တီးခြင်း၊ သို့မဟုတ် simulation တွေ လုပ်ဆောင်နိုင်ပါတယ်။
- **Workflow Automation:** Task schedulers, email services, data pipelines လို tools တွေကို ပေါင်းစပ်ပြီး အလုပ်အကိုင်များကို အလိုအလျောက်လုပ်ဆောင်ခြင်း။
- **Customer Support:** CRM systems, ticketing platforms, knowledge bases တွေနဲ့ ဆက်သွယ်ပြီး အသုံးပြုသူရဲ့ မေးခွန်းတွေကို ဖြေရှင်းခြင်း။
- **Content Generation and Editing:** Grammar checkers, text summarizers, content safety evaluators လို tools တွေကို အသုံးပြုပြီး အကြောင်းအရာဖန်တီးမှုအလုပ်တွေကို ကူညီဆောင်ရွက်ခြင်း။

## Tool Use Design Pattern ကို အကောင်အထည်ဖော်ဖို့ လိုအပ်တဲ့ အစိတ်အပိုင်း/အခြေခံအဆောက်အအုံတွေက ဘာတွေလဲ?

AI အေးဂျင့်တွေကို အမျိုးမျိုးသော အလုပ်တွေ လုပ်ဆောင်နိုင်စေဖို့ ဒီအစိတ်အပိုင်းတွေ လိုအပ်ပါတယ်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ဖို့ လိုအပ်တဲ့ အဓိကအစိတ်အပိုင်းတွေကို ကြည့်ကြမယ် -

- **Function/Tool Schemas**: အသုံးပြုနိုင်တဲ့ tools တွေကို ဖော်ပြထားတဲ့ အသေးစိတ်အချက်အလက်များ (function name, ရည်ရွယ်ချက်, လိုအပ်တဲ့ parameters, မျှော်မှန်းထားတဲ့ output)။
- **Function Execution Logic**: အသုံးပြုသူရဲ့ ရည်ရွယ်ချက်နဲ့ စကားဝိုင်းအကြောင်းအရာအပေါ်မူတည်ပြီး tools တွေကို ဘယ်လိုနှင့် ဘယ်အချိန်မှာ invoke လုပ်မလဲဆိုတာကို စီမံခြင်း။
- **Message Handling System**: အသုံးပြုသူရဲ့ input, LLM response, tool call, tool output တို့အကြား စကားဝိုင်းလှုပ်ရှားမှုကို စီမံခြင်း။
- **Tool Integration Framework**: ရိုးရှင်းတဲ့ functions တွေဖြစ်စေ၊ ရှုပ်ထွေးတဲ့ external services တွေဖြစ်စေ အေးဂျင့်ကို tools တွေနဲ့ ချိတ်ဆက်ပေးတဲ့ အဆောက်အအုံ။
- **Error Handling & Validation**: Tool execution မှာဖြစ်ပေါ်တဲ့ အမှားတွေကို ကိုင်တွယ်ခြင်း၊ parameters တွေကို validate လုပ်ခြင်း၊ မမျှော်လင့်ထားတဲ့ response တွေကို စီမံခြင်း။
- **State Management**: စကားဝိုင်းအကြောင်းအရာ, အရင် tool interaction တွေ, multi-turn interaction တွေမှာ တိကျမှုရှိစေရန် persistent data တွေကို ထိန်းသိမ်းခြင်း။

## Function/Tool Calling

Function calling ဟာ Large Language Models (LLMs) တွေကို tools တွေနဲ့ ဆက်သွယ်စေဖို့ အဓိကနည်းလမ်းဖြစ်ပါတယ်။ 'Function' နဲ့ 'Tool' ဆိုတာ အတူတူအသုံးပြုတာတွေ တွေ့ရတတ်ပါတယ်၊ အကြောင်းကတော့ 'functions' (ပြန်လည်အသုံးပြုနိုင်တဲ့ code blocks) တွေဟာ အေးဂျင့်တွေ task တွေကို လုပ်ဆောင်ဖို့ အသုံးပြုတဲ့ 'tools' တွေဖြစ်လို့ပါ။ Function code ကို invoke လုပ်ဖို့ LLM ဟာ အသုံးပြုသူရဲ့ တောင်းဆိုမှုကို function description နဲ့ နှိုင်းယှဉ်ရပါမယ်။ Function တွေရဲ့ description တွေပါဝင်တဲ့ schema ကို LLM ကို ပေးပို့ပြီး LLM ဟာ task အတွက် အကောင်းဆုံး function ကို ရွေးချယ်ပြီး function name နဲ့ arguments ကို ပြန်ပေးပါမယ်။ ရွေးချယ်ထားတဲ့ function ကို invoke လုပ်ပြီး response ကို LLM ကို ပြန်ပေးပြီး အသုံးပြုသူရဲ့ တောင်းဆိုမှုကို ဖြေရှင်းပေးပါမယ်။

Function calling ကို အကောင်အထည်ဖော်ဖို့ developer တွေလိုအပ်တာတွေကတော့ -

1. Function calling ကို support လုပ်တဲ့ LLM model
2. Function description တွေပါဝင်တဲ့ schema
3. Function description တွေမှာ ဖော်ပြထားတဲ့ code

ဥပမာ - မြို့တစ်မြို့ရဲ့ လက်ရှိအချိန်ကို ရယူဖို့ function calling ကို အသုံးပြုခြင်း -

1. **Function calling ကို support လုပ်တဲ့ LLM ကို initialize လုပ်ပါ:**

    Function calling ကို support မလုပ်တဲ့ models တွေရှိတတ်ပါတယ်၊ ဒါကြောင့် သုံးမယ့် model ကို စစ်ဆေးဖို့ အရေးကြီးပါတယ်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ဟာ function calling ကို support လုပ်ပါတယ်။ Azure OpenAI client ကို initialize လုပ်နိုင်ပါတယ်။

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခု ဖန်တီးပါ:**

    JSON schema တစ်ခုကို ဖန်တီးပြီး function name, function ရဲ့ ရည်ရွယ်ချက်, function parameters တွေရဲ့ အမည်နဲ့ ဖော်ပြချက်တွေကို ထည့်သွင်းပါ။ Schema ကို client နဲ့ user request ကို ပေးပို့ပါ။ Tool call ကို return လုပ်ပါမယ်၊ **မဟုတ်** final answer ကို return မလုပ်ပါဘူး။ အဆိုပါ tool call ဟာ function name နဲ့ arguments ကို return လုပ်ပါမယ်။

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
  
1. **Task ကို လုပ်ဆောင်ဖို့ လိုအပ်တဲ့ function code:**

    LLM က ရွေးချယ်ထားတဲ့ function ကို run လုပ်ဖို့ လိုအပ်တဲ့ code ကို ရေးသားပြီး execute လုပ်ပါ။ Python ကို အသုံးပြုပြီး လက်ရှိအချိန်ကို ရယူဖို့ code ကို ရေးနိုင်ပါတယ်။ response_message ကနေ function name နဲ့ arguments ကို extract လုပ်ဖို့ code ကို ရေးသားပါ။

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

Function Calling ဟာ agent tool use design ရဲ့ အဓိကအချက်ဖြစ်ပါတယ်၊ သို့သော် အစမှ implementation လုပ်ရတာ ခက်ခဲတတ်ပါတယ်။ [Lesson 2](../../../02-explore-agentic-frameworks) မှာ လေ့လာခဲ့သလို agentic frameworks တွေက pre-built building blocks တွေကို ပေးပြီး tool use ကို အကောင်အထည်ဖော်နိုင်ပါတယ်။

## Agentic Frameworks နဲ့ Tool Use Examples

Agentic frameworks တွေကို အသုံးပြုပြီး Tool Use Design Pattern ကို အကောင်အထည်ဖော်နိုင်တဲ့ ဥပမာတွေကို ကြည့်ကြမယ် -

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> ဟာ .NET, Python, Java developer တွေအတွက် LLMs တွေနဲ့ အလုပ်လုပ်ဖို့ open-source AI framework ဖြစ်ပါတယ်။ Function calling ကို အသုံးပြုတဲ့ process ကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> လုပ်ပြီး model ကို functions နဲ့ parameters တွေကို အလိုအလျောက် ဖော်ပြပေးပါတယ်။ Model နဲ့ code အကြား communication ကို handle လုပ်ပေးပါတယ်။ Semantic Kernel ကို အသုံးပြုပြီး pre-built tools တွေကို access လုပ်နိုင်ပါတယ်၊ ဥပမာ - <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a>, <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>။

Semantic Kernel နဲ့ function calling process ကို အောက်ပါ diagram မှာ ဖော်ပြထားပါတယ် -

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.my.png)

Semantic Kernel မှာ functions/tools တွေကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> လို့ ခေါ်ပါတယ်။ `get_current_time` function ကို plugin အဖြစ် ပြောင်းလဲနိုင်ပါတယ်၊ class အဖြစ် ပြောင်းပြီး function ကို ထည့်သွင်းပါ။ `kernel_function` decorator ကို import လုပ်ပြီး function ရဲ့ description ကို ထည့်သွင်းပါ။ Kernel ကို GetCurrentTimePlugin နဲ့ ဖန်တီးပြီး function နဲ့ parameters တွေကို serialize လုပ်ပါ။

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ဟာ developer တွေကို compute နဲ့ storage resources ကို စီမံစရာမလိုဘဲ AI agents တွေကို securely build, deploy, scale လုပ်နိုင်စေဖို့ agentic framework အသစ်ဖြစ်ပါတယ်။ Enterprise applications တွေအတွက် အထူးအသုံးဝင်ပါတယ်၊ အကြောင်းကတော့ fully managed service ဖြစ်ပြီး enterprise grade security ရှိလို့ပါ။

LLM API ကို တိုက်ရိုက် အသုံးပြုတာနဲ့ နှိုင်းယှဉ်ကြည့်မယ်ဆိုရင် Azure AI Agent Service ရဲ့ အကျိုးကျေးဇူးတွေက -

- Automatic tool calling – tool call ကို parse လုပ်စရာမလိုဘဲ tool ကို invoke လုပ်ပြီး response ကို handle လုပ်ပေးပါတယ်။
- Securely managed data – conversation state ကို ကိုယ်တိုင် စီမံစရာမလိုဘဲ threads ကို အသုံးပြုပြီး အချက်အလက်တွေကို သိမ်းဆည်းနိုင်ပါတယ်။
- Out-of-the-box tools – Bing, Azure AI Search, Azure Functions လို data sources တွေနဲ့ ဆက်သွယ်ဖို့ tools တွေကို အသုံးပြုနိုင်ပါတယ်။

Azure AI Agent Service မှာ tools တွေကို `toolset` အဖြစ် အသုံးပြုနိုင်ပါတယ်။ `threads` တွေကို အသုံးပြုပြီး စကားဝိုင်း message history ကို track လုပ်နိုင်ပါတယ်။

ဥပမာ - Contoso ဆိုတဲ့ ကုမ္ပဏီရဲ့ sales agent အဖြစ် သင်လုပ်နေတယ်လို့ ဆိုပါစို့။ သင်ရဲ့ sales data ကို အဖြေထုတ်ပေးနိုင်တဲ့ conversational agent တစ်ခု ဖန်တီးချင်တယ်။

အောက်ပါပုံမှာ Azure AI Agent Service ကို အသုံးပြုပြီး sales data ကို analysis လုပ်တဲ့ နည်းလမ်းကို ဖော်ပြထားပါတယ် -

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.my.jpg)

Service ကို အသုံးပြုဖို့ client တစ်ခု ဖန်တီးပြီး tool သို့မဟုတ် toolset ကို သတ်မှတ်နိုင်ပါတယ်။ Python code ကို အသုံးပြုပြီး user created function `fetch_sales_data_using_sqlite_query` နဲ့ pre-built Code Interpreter ကို user request အပေါ်မူတည်ပြီး LLM က ရွေးချယ်နိုင်ပါတယ်။

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

## Tool Use Design Pattern ကို အသုံးပြုပြီး ယုံကြည်ရတဲ့ AI အေးဂျင့်တွေ တည်ဆောက်ဖို့ အထူးစဉ်းစားရမယ့်အချက်တွေက ဘာတွေလဲ?

LLMs တွေက dynamically generate လုပ်တဲ့ SQL တွေမှာ security ဆိုင်ရာ စိုးရိမ်ရမယ့်အချက်တွေ ရှိတတ်ပါတယ်၊ အထူးသဖြင့် SQL injection သို့မဟုတ် malicious actions (ဥပမာ- database ကို drop လုပ်ခြင်း၊ tamper လုပ်ခြင်း) စတဲ့အန္တရာယ်တွေ ဖြစ်နိုင်ပါတယ်။ ဒီစိုးရိမ်ရမယ့်အချက်တွေဟာ database access permissions ကို သေချာစီမံခြင်းနဲ့ အကျိုးသက်သာရှိစေပါတယ်။ Database အများစုမှာ read-only အဖြစ် configure လုပ်နိုင်ပါတယ်။ PostgreSQL သို့မဟုတ် Azure SQL လို database services တွေမှာ app ကို read-only (SELECT) role assign လုပ်နိုင်ပါတယ်။

App ကို secure environment မှာ run လုပ်ခြင်းကလည်း အကောင်းဆုံးကာကွယ်မှုကို ပေးနိုင်ပါတယ်။ Enterprise scenarios တွေမှာ operational systems ကနေ data ကို extract လုပ်ပြီး read-only database သို့မဟုတ် data warehouse ကို transform လုပ်ပြီး user-friendly schema နဲ့ တင်သွင်းတတ်ပါတယ်။ ဒီနည်းလမ်းက data ကို secure ဖြစ်စေပြီး performance နဲ့ accessibility ကို optimize လုပ်ပေးပါတယ်၊ app ရဲ့ access ကို read-only အဖြစ် အကန့်အသတ်ထားပါတယ်။

## အပိုဆောင်းအရင်းအမြစ်များ

-

Azure AI Agents Service Workshop  
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>  
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>  
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>  
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>  

## ယခင် သင်ခန်းစာ  

[Agentic Design Patterns ကို နားလည်ခြင်း](../03-agentic-design-patterns/README.md)  

## နောက်ထပ် သင်ခန်းစာ  

[Agentic RAG](../05-agentic-rag/README.md)  

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူသားပညာရှင်များမှ ပြုလုပ်သည့် ပရော်ဖက်ရှင်နယ်ဘာသာပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ဆိုမှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသည့် နားလည်မှုမှားမှုများ သို့မဟုတ် အဓိပ္ပာယ်မှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။ 