<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "88258b03f2893aa2e69eb8fb24baabbc",
  "translation_date": "2025-07-12T09:47:12+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "my"
}
-->
[![How to Design Good AI Agents](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.my.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ဓာတ်ပုံကိုနှိပ်ပြီး ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရှုနိုင်ပါသည်)_

# ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံ

ကိရိယာများသည် စိတ်ဝင်စားဖွယ်ကောင်းသည်၊ အကြောင်းမှာ AI ကိုယ်စားလှယ်များအတွက် ပိုမိုကျယ်ပြန့်သော စွမ်းရည်များကို ပေးစွမ်းနိုင်စေခြင်းဖြစ်သည်။ ကိုယ်စားလှယ်သည် လုပ်ဆောင်နိုင်သည့် လုပ်ဆောင်ချက်အချို့သာရှိခြင်းမဟုတ်ဘဲ၊ ကိရိယာတစ်ခု ထည့်သွင်းခြင်းဖြင့် ကိုယ်စားလှယ်သည် လုပ်ဆောင်ချက်အမျိုးမျိုးကို ပြုလုပ်နိုင်သည်။ ဤအခန်းတွင် ကျွန်ုပ်တို့သည် AI ကိုယ်စားလှယ်များသည် ၎င်းတို့၏ ရည်မှန်းချက်များကို ပြည့်မှီစေရန် အထူးကိရိယာများကို မည်သို့ အသုံးပြုနိုင်သည်ကို ဖော်ပြသည့် Tool Use Design Pattern ကို လေ့လာမည်ဖြစ်သည်။

## နိဒါန်း

ဤသင်ခန်းစာတွင် ကျွန်ုပ်တို့ မေးခွန်းများကို ဖြေရှင်းရန် ကြိုးစားမည်ဖြစ်သည်-

- Tool Use Design Pattern ဆိုတာဘာလဲ?
- ဘယ်လိုအသုံးပြုမှုများတွင် အသုံးပြုနိုင်သလဲ?
- ဒီဇိုင်းပုံစံကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အစိတ်အပိုင်းများ/အခြေခံအဆောက်အအုံများက ဘာတွေလဲ?
- ယုံကြည်စိတ်ချရသော AI ကိုယ်စားလှယ်များ ဖန်တီးရာတွင် Tool Use Design Pattern ကို အသုံးပြုရာတွင် အထူးသတိပြုရမည့်အချက်များက ဘာတွေလဲ?

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးပြီးနောက် သင်သည်-

- Tool Use Design Pattern နှင့် ၎င်း၏ ရည်ရွယ်ချက်ကို သတ်မှတ်နိုင်မည်။
- Tool Use Design Pattern ကို အသုံးပြုနိုင်သည့် အသုံးပြုမှုများကို ဖော်ထုတ်နိုင်မည်။
- ဒီဇိုင်းပုံစံကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများကို နားလည်နိုင်မည်။
- ဒီဒီဇိုင်းပုံစံကို အသုံးပြုသော AI ကိုယ်စားလှယ်များတွင် ယုံကြည်စိတ်ချရမှုအတွက် သတိပြုရမည့်အချက်များကို သိရှိနိုင်မည်။

## Tool Use Design Pattern ဆိုတာဘာလဲ?

**Tool Use Design Pattern** သည် LLM များအား အထူးကိရိယာများနှင့် ဆက်သွယ်နိုင်စေရန် အာရုံစိုက်ထားသည်။ ကိရိယာများသည် ကိုယ်စားလှယ်တစ်ဦးက လုပ်ဆောင်ချက်များ ပြုလုပ်ရန် အကောင်အထည်ဖော်နိုင်သည့် ကုဒ်များဖြစ်သည်။ ကိရိယာတစ်ခုမှာ ကိန်းဂဏန်းတွက်စက်ကဲ့သို့ ရိုးရှင်းသော function တစ်ခုဖြစ်နိုင်သလို၊ စတော့ရှယ်ယာစျေးနှုန်းရှာဖွေရေး သို့မဟုတ် ရာသီဥတုခန့်မှန်းခြေကဲ့သို့ တတိယပါတီဝန်ဆောင်မှု API ခေါ်ဆိုမှုတစ်ခုဖြစ်နိုင်သည်။ AI ကိုယ်စားလှယ်များ၏ အခြေအနေတွင် ကိရိယာများကို **model-generated function calls** အဖြစ် ကိုယ်စားလှယ်များမှ အကောင်အထည်ဖော်ရန် ဒီဇိုင်းထားသည်။

## ဘယ်လိုအသုံးပြုမှုများတွင် အသုံးပြုနိုင်သလဲ?

AI ကိုယ်စားလှယ်များသည် ကိရိယာများကို အသုံးပြု၍ ရှုပ်ထွေးသော အလုပ်များ ပြီးမြောက်စေခြင်း၊ သတင်းအချက်အလက် ရယူခြင်း သို့မဟုတ် ဆုံးဖြတ်ချက်ချခြင်းများ ပြုလုပ်နိုင်သည်။ Tool Use Design Pattern ကို အပြင်ဘက်စနစ်များနှင့် တုံ့ပြန်ဆက်သွယ်မှုလိုအပ်သည့် အခြေအနေများတွင် အသုံးပြုလေ့ရှိသည်၊ ဥပမာ- ဒေတာဘေ့စ်များ၊ ဝက်ဘ်ဝန်ဆောင်မှုများ သို့မဟုတ် ကုဒ်ဖတ်ရှုသူများ။ ၎င်းစွမ်းရည်သည် အောက်ပါ အသုံးပြုမှုများအတွက် အထူးအသုံးဝင်သည်-

- **ဒိုင်နမစ် သတင်းအချက်အလက် ရယူခြင်း** - ကိုယ်စားလှယ်များသည် အပြင်ဘက် API များ သို့မဟုတ် ဒေတာဘေ့စ်များကို မေးမြန်း၍ နောက်ဆုံးရ သတင်းအချက်အလက်များ ရယူနိုင်သည် (ဥပမာ- SQLite ဒေတာဘေ့စ်ကို မေးမြန်း၍ ဒေတာခွဲခြမ်းစိတ်ဖြာခြင်း၊ စတော့ရှယ်ယာစျေးနှုန်း သို့မဟုတ် ရာသီဥတု သတင်းများ ရယူခြင်း)။
- **ကုဒ် အကောင်အထည်ဖော်ခြင်းနှင့် ဖတ်ရှုခြင်း** - ကိုယ်စားလှယ်များသည် ကုဒ် သို့မဟုတ် စာရိုက်ချက်များကို အကောင်အထည်ဖော်၍ သင်္ချာပြဿနာများ ဖြေရှင်းခြင်း၊ အစီရင်ခံစာများ ထုတ်လုပ်ခြင်း သို့မဟုတ် အတုအယောင်များ ပြုလုပ်နိုင်သည်။
- **အလုပ်စဉ် အလိုအလျောက်လုပ်ခြင်း** - အလုပ်များကို အလိုအလျောက် ပြုလုပ်ရန် task scheduler များ၊ အီးမေးလ်ဝန်ဆောင်မှုများ သို့မဟုတ် ဒေတာလိုင်းများကို ပေါင်းစည်းခြင်း။
- **ဖောက်သည်ပံ့ပိုးမှု** - ကိုယ်စားလှယ်များသည် CRM စနစ်များ၊ တစ်ကတ်စနစ်များ သို့မဟုတ် အသိပညာအခြေများနှင့် ဆက်သွယ်၍ အသုံးပြုသူ မေးခွန်းများ ဖြေရှင်းနိုင်သည်။
- **အကြောင်းအရာ ဖန်တီးခြင်းနှင့် တည်းဖြတ်ခြင်း** - ကိုယ်စားလှယ်များသည် စာလုံးပေါင်းစစ်ဆေးသူများ၊ စာသားအကျဉ်းချုပ်သူများ သို့မဟုတ် အကြောင်းအရာလုံခြုံရေး စစ်ဆေးသူများကဲ့သို့ ကိရိယာများကို အသုံးပြု၍ အကြောင်းအရာ ဖန်တီးမှုများကို ကူညီနိုင်သည်။

## Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အစိတ်အပိုင်းများ/အခြေခံအဆောက်အအုံများ

ဤအခြေခံအဆောက်အအုံများက AI ကိုယ်စားလှယ်အား အမျိုးမျိုးသော လုပ်ငန်းများ ပြုလုပ်နိုင်စေသည်။ Tool Use Design Pattern ကို အကောင်အထည်ဖော်ရန် လိုအပ်သော အဓိကအစိတ်အပိုင်းများမှာ-

- **Function/Tool Schemas**: ရနိုင်သော ကိရိယာများ၏ အသေးစိတ်ဖော်ပြချက်များ၊ function အမည်၊ ရည်ရွယ်ချက်၊ လိုအပ်သော ပါရာမီတာများနှင့် မျှော်မှန်းထားသော ထွက်ရှိမှုများပါဝင်သည်။ ဤ schemas များက LLM ကို ရနိုင်သော ကိရိယာများကို နားလည်စေပြီး တရားဝင်တောင်းဆိုမှုများ ဖန်တီးနိုင်စေသည်။

- **Function Execution Logic**: အသုံးပြုသူ၏ ရည်ရွယ်ချက်နှင့် စကားပြောပတ်ဝန်းကျင်အပေါ် မူတည်၍ ကိရိယာများကို မည်သည့်အချိန်တွင် မည်သို့ ခေါ်ယူမည်ကို ထိန်းချုပ်သည်။ ဤတွင် စီမံကိန်းရေးဆွဲသူ မော်ဂျူးများ၊ လမ်းညွှန်စနစ်များ သို့မဟုတ် အခြေအနေအလိုက် လမ်းကြောင်းများ ပါဝင်နိုင်သည်။

- **Message Handling System**: အသုံးပြုသူ၏ အဝင်များ၊ LLM ၏ တုံ့ပြန်ချက်များ၊ ကိရိယာခေါ်ဆိုမှုများနှင့် ကိရိယာထွက်ရှိမှုများအကြား စကားပြောစီးဆင်းမှုကို စီမံခန့်ခွဲသော အစိတ်အပိုင်းများ။

- **Tool Integration Framework**: ကိုယ်စားလှယ်နှင့် ကိရိယာများကို ချိတ်ဆက်ပေးသည့် အခြေခံအဆောက်အအုံ၊ ရိုးရှင်းသော function များဖြစ်စေ၊ ရှုပ်ထွေးသော အပြင်ဘက်ဝန်ဆောင်မှုများဖြစ်စေ။

- **Error Handling & Validation**: ကိရိယာအကောင်အထည်ဖော်မှုတွင် ဖြစ်ပေါ်နိုင်သည့် အမှားများကို ကိုင်တွယ်ခြင်း၊ ပါရာမီတာများကို စစ်ဆေးခြင်းနှင့် မမျှော်လင့်ထားသော တုံ့ပြန်ချက်များကို စီမံခန့်ခွဲခြင်း။

- **State Management**: စကားပြောပတ်ဝန်းကျင်၊ ယခင်ကိရိယာဆက်သွယ်မှုများနှင့် အမြဲတမ်းရှိသော ဒေတာများကို မှတ်တမ်းတင်ခြင်းဖြင့် မျိုးစုံသော စကားပြောဆက်လက်မှုများတွင် တည်ငြိမ်မှုရှိစေရန်။

နောက်တစ်ခုအနေဖြင့် Function/Tool Calling ကို ပိုမိုအသေးစိတ် လေ့လာကြမည်။

### Function/Tool Calling

Function calling သည် LLM များအား ကိရိယာများနှင့် ဆက်သွယ်နိုင်စေရန် အဓိကနည်းလမ်းဖြစ်သည်။ 'Function' နှင့် 'Tool' ဆိုသော စကားလုံးများကို အတူတူ အသုံးပြုလေ့ရှိသည်၊ အကြောင်းမှာ 'function' များသည် ပြန်လည်အသုံးပြုနိုင်သော ကုဒ်အပိုင်းများဖြစ်ပြီး၊ ၎င်းတို့သည် ကိုယ်စားလှယ်များ၏ လုပ်ငန်းများ ဆောင်ရွက်ရန် အသုံးပြုသော 'tools' ဖြစ်သည်။ function ၏ ကုဒ်ကို ခေါ်ယူရန် LLM သည် အသုံးပြုသူ၏ တောင်းဆိုမှုကို function ဖော်ပြချက်နှင့် နှိုင်းယှဉ်ရမည်။ ၎င်းအတွက် ရနိုင်သော function များအားလုံး၏ ဖော်ပြချက်များပါဝင်သည့် schema တစ်ခုကို LLM သို့ ပို့ပေးသည်။ LLM သည် လုပ်ငန်းအတွက် အကောင်းဆုံး function ကို ရွေးချယ်ပြီး ၎င်း၏ အမည်နှင့် အကြောင်းအရာများကို ပြန်လည်ပေးပို့သည်။ ရွေးချယ်ထားသော function ကို ခေါ်ယူပြီး ၎င်း၏ တုံ့ပြန်ချက်ကို LLM သို့ ပြန်ပို့သည်၊ ထို့နောက် LLM သည် ထိုသတင်းအချက်အလက်များကို အသုံးပြု၍ အသုံးပြုသူ၏ တောင်းဆိုမှုကို ဖြေကြားသည်။

Developer များအနေဖြင့် function calling ကို ကိုယ်စားလှယ်များအတွက် အကောင်အထည်ဖော်ရန် လိုအပ်သည်မှာ-

1. function calling ကို ထောက်ပံ့သော LLM မော်ဒယ်တစ်ခု
2. function ဖော်ပြချက်များပါဝင်သည့် schema တစ်ခု
3. ဖော်ပြထားသော function တစ်ခုချင်းစီအတွက် ကုဒ်

မြို့တစ်မြို့၏ လက်ရှိအချိန်ကို ရယူခြင်းကို ဥပမာအဖြစ် အသုံးပြုကြမည်-

1. **function calling ကို ထောက်ပံ့သော LLM ကို စတင်အသုံးပြုခြင်း**

    မော်ဒယ်အားလုံး function calling ကို ထောက်ပံ့ခြင်းမရှိပါ၊ သင့်အသုံးပြုမည့် LLM သည် ထောက်ပံ့မှုရှိကြောင်း စစ်ဆေးရန် အရေးကြီးသည်။ <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> သည် function calling ကို ထောက်ပံ့သည်။ Azure OpenAI client ကို စတင်ဖန်တီးနိုင်သည်။

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function Schema တစ်ခု ဖန်တီးခြင်း**

    နောက်တစ်ဆင့်တွင် function အမည်၊ function ၏ လုပ်ဆောင်ချက် ဖော်ပြချက်နှင့် function ပါရာမီတာများ၏ အမည်များနှင့် ဖော်ပြချက်များ ပါဝင်သည့် JSON schema တစ်ခုကို သတ်မှတ်မည်။ ထို့နောက် ယင်း schema ကို ယခင်တွင် ဖန်တီးထားသော client သို့ အသုံးပြုသူ၏ တောင်းဆိုမှုနှင့်အတူ ပို့ပေးမည်၊ ဥပမာအားဖြင့် San Francisco ၏ အချိန်ကို ရှာဖွေရန်။ အရေးကြီးသည်မှာ **tool call** ကို ပြန်လည်ရရှိမည်ဖြစ်ပြီး၊ မေးခွန်း၏ နောက်ဆုံးဖြေချက် မဟုတ်ပါ။ ယခင်ကဖော်ပြခဲ့သည့်အတိုင်း LLM သည် လုပ်ငန်းအတွက် ရွေးချယ်ထားသော function အမည်နှင့် ၎င်းသို့ ပေးပို့မည့် အကြောင်းအရာများကို ပြန်လည်ပေးပို့သည်။

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
  
1. **လုပ်ငန်းကို ဆောင်ရွက်ရန် လိုအပ်သော function ကုဒ်**

    LLM သည် မည်သည့် function ကို အကောင်အထည်ဖော်ရမည်ကို ရွေးချယ်ပြီးနောက်၊ လုပ်ငန်းကို ဆောင်ရွက်ရန် ကုဒ်ကို အကောင်အထည်ဖော်၍ အကောင်အထည်ဖော်ရမည်။ Python ဖြင့် လက်ရှိအချိန်ကို ရယူရန် ကုဒ်ရေးသားနိုင်သည်။ ထို့အပြင် response_message မှ function အမည်နှင့် အကြောင်းအရာများကို ထုတ်ယူရန် ကုဒ်ကိုလည်း ရေးသားရမည်။

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

Function Calling သည် ကိုယ်စားလှယ်ကိရိယာအသုံးပြုမှု ဒီဇိုင်းပုံစံများ၏ အဓိကဖြစ်သည်၊ သို့သော် စတင်ကတည်းက အကောင်အထည်ဖော်ခြင်းမှာ အခက်အခဲရှိနိုင်သည်။ [Lesson 2](../../../02-explore-agentic-frameworks) တွင် သင်ယူခဲ့သည့်အတိုင်း agentic frameworks များသည် ကိရိယာအသုံးပြုမှုကို အကောင်အထည်ဖော်ရန် ကြိုတင်ပြင်ဆင်ထားသော အခြေခံအဆောက်အအုံများကို ပေးစွမ်းသည်။

## Agentic Frameworks များဖြင့် Tool Use ဥပမာများ

အောက်တွင် မတူညီသော agentic frameworks များကို အသုံးပြု၍ Tool Use Design Pattern ကို မည်သို့ အကောင်အထည်ဖော်နိုင်သည်ကို ဥပမာများဖြင့် ဖော်ပြထားသည်-

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> သည် .NET၊ Python နှင့် Java developer များအတွက် LLM များနှင့် အလုပ်လုပ်ရာတွင် အသုံးပြုနိုင်သည့် open-source AI framework ဖြစ်သည်။ function calling ကို လွယ်ကူစွာ အသုံးပြုနိုင်ရန် function များနှင့် ၎င်းတို့၏ ပါရာမီတာများကို <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializing</a> လုပ်ခြင်းဖြင့် မော်ဒယ်သို့ အလိုအလျောက် ဖော်ပြပေးသည်။ ထို့အပြင် မော်ဒယ်နှင့် သင့်ကုဒ်အကြား ဆက်သွယ်မှုကိုလည်း စီမံခန့်ခွဲပေးသည်။ Semantic Kernel ကဲ့သို့ agentic framework ကို အသုံးပြုခြင်း၏ အခြားအားသာချက်မှာ <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> နှင့် <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a> ကဲ့သို့ ကြိုတင်ပြင်ဆင်ထားသော ကိရိယ

Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## ယခင်သင်ခန်းစာ

[Agentic Design Patterns ကိုနားလည်ခြင်း](../03-agentic-design-patterns/README.md)

## နောက်တစ်ခုသင်ခန်းစာ

[Agentic RAG](../05-agentic-rag/README.md)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။