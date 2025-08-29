<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T12:14:51+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "bn"
}
-->
[![কীভাবে ভালো AI এজেন্ট ডিজাইন করবেন](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.bn.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_

# টুল ব্যবহারের ডিজাইন প্যাটার্ন

টুলগুলো আকর্ষণীয় কারণ এগুলো AI এজেন্টদের আরও বিস্তৃত ক্ষমতা প্রদান করে। এজেন্টের সীমিত সংখ্যক কাজ করার ক্ষমতার পরিবর্তে, একটি টুল যোগ করার মাধ্যমে এজেন্ট এখন অনেক ধরণের কাজ করতে পারে। এই অধ্যায়ে, আমরা টুল ব্যবহারের ডিজাইন প্যাটার্ন নিয়ে আলোচনা করব, যা বর্ণনা করে কীভাবে AI এজেন্টরা নির্দিষ্ট টুল ব্যবহার করে তাদের লক্ষ্য অর্জন করতে পারে।

## ভূমিকা

এই পাঠে আমরা নিম্নলিখিত প্রশ্নগুলোর উত্তর খুঁজব:

- টুল ব্যবহারের ডিজাইন প্যাটার্ন কী?
- এটি কোন কোন ক্ষেত্রে প্রয়োগ করা যেতে পারে?
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় উপাদান/গঠনমূলক ব্লক কী কী?
- বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ব্যবহারের ডিজাইন প্যাটার্ন ব্যবহার করার ক্ষেত্রে বিশেষ বিবেচনা কী কী?

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পর, আপনি সক্ষম হবেন:

- টুল ব্যবহারের ডিজাইন প্যাটার্ন এবং এর উদ্দেশ্য সংজ্ঞায়িত করতে।
- কোন কোন ক্ষেত্রে টুল ব্যবহারের ডিজাইন প্যাটার্ন প্রযোজ্য তা চিহ্নিত করতে।
- ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো বুঝতে।
- এই ডিজাইন প্যাটার্ন ব্যবহার করে AI এজেন্টের বিশ্বাসযোগ্যতা নিশ্চিত করার জন্য বিবেচনাগুলো চিনতে।

## টুল ব্যবহারের ডিজাইন প্যাটার্ন কী?

**টুল ব্যবহারের ডিজাইন প্যাটার্ন** LLM-কে নির্দিষ্ট লক্ষ্য অর্জনের জন্য বাইরের টুলের সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা প্রদান করার উপর কেন্দ্রীভূত। টুল হলো কোড যা এজেন্ট দ্বারা কার্য সম্পাদনের জন্য চালানো যায়। একটি টুল একটি সাধারণ ফাংশন হতে পারে যেমন একটি ক্যালকুলেটর, অথবা তৃতীয় পক্ষের সার্ভিসে API কল যেমন স্টক প্রাইস বা আবহাওয়ার পূর্বাভাস। AI এজেন্টের ক্ষেত্রে, টুলগুলো **মডেল-জেনারেটেড ফাংশন কল** এর প্রতিক্রিয়ায় চালানোর জন্য ডিজাইন করা হয়।

## এটি কোন কোন ক্ষেত্রে প্রয়োগ করা যেতে পারে?

AI এজেন্টরা টুল ব্যবহার করে জটিল কাজ সম্পন্ন করতে, তথ্য সংগ্রহ করতে, বা সিদ্ধান্ত নিতে পারে। টুল ব্যবহারের ডিজাইন প্যাটার্ন সাধারণত এমন পরিস্থিতিতে ব্যবহৃত হয় যেখানে বাইরের সিস্টেমের সাথে গতিশীল ইন্টারঅ্যাকশন প্রয়োজন, যেমন ডাটাবেস, ওয়েব সার্ভিস, বা কোড ইন্টারপ্রেটার। এই ক্ষমতা বিভিন্ন ক্ষেত্রে কার্যকর, যেমন:

- **গতিশীল তথ্য সংগ্রহ:** এজেন্টরা বাইরের API বা ডাটাবেস থেকে আপডেটেড তথ্য সংগ্রহ করতে পারে (যেমন SQLite ডাটাবেস থেকে ডেটা বিশ্লেষণ, স্টক প্রাইস বা আবহাওয়ার তথ্য সংগ্রহ)।
- **কোড চালানো এবং ব্যাখ্যা করা:** এজেন্টরা কোড বা স্ক্রিপ্ট চালিয়ে গাণিতিক সমস্যা সমাধান, রিপোর্ট তৈরি, বা সিমুলেশন করতে পারে।
- **ওয়ার্কফ্লো অটোমেশন:** টাস্ক শিডিউলার, ইমেইল সার্ভিস, বা ডেটা পাইপলাইন ইন্টিগ্রেট করে পুনরাবৃত্তিমূলক বা বহু-ধাপের ওয়ার্কফ্লো অটোমেট করা।
- **কাস্টমার সাপোর্ট:** এজেন্টরা CRM সিস্টেম, টিকেটিং প্ল্যাটফর্ম, বা নলেজ বেসের সাথে ইন্টারঅ্যাক্ট করে ব্যবহারকারীর প্রশ্নের সমাধান করতে পারে।
- **কন্টেন্ট তৈরি এবং সম্পাদনা:** এজেন্টরা গ্রামার চেকার, টেক্সট সামারাইজার, বা কন্টেন্ট সেফটি ইভ্যালুয়েটরের মতো টুল ব্যবহার করে কন্টেন্ট তৈরির কাজে সহায়তা করতে পারে।

## টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় উপাদান/গঠনমূলক ব্লক কী কী?

এই গঠনমূলক ব্লকগুলো AI এজেন্টকে বিভিন্ন ধরণের কাজ সম্পাদন করতে সক্ষম করে। আসুন টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের জন্য প্রয়োজনীয় মূল উপাদানগুলো দেখি:

- **ফাংশন/টুল স্কিমা:** উপলব্ধ টুলগুলোর বিস্তারিত সংজ্ঞা, যার মধ্যে ফাংশনের নাম, উদ্দেশ্য, প্রয়োজনীয় প্যারামিটার, এবং প্রত্যাশিত আউটপুট অন্তর্ভুক্ত। এই স্কিমাগুলো LLM-কে উপলব্ধ টুলগুলো কী এবং কীভাবে বৈধ অনুরোধ তৈরি করতে হয় তা বুঝতে সাহায্য করে।

- **ফাংশন এক্সিকিউশন লজিক:** ব্যবহারকারীর উদ্দেশ্য এবং কথোপকথনের প্রসঙ্গের উপর ভিত্তি করে টুলগুলো কীভাবে এবং কখন চালানো হবে তা নিয়ন্ত্রণ করে। এতে প্ল্যানার মডিউল, রাউটিং মেকানিজম, বা শর্তাধীন প্রবাহ অন্তর্ভুক্ত থাকতে পারে যা গতিশীলভাবে টুল ব্যবহারের সিদ্ধান্ত নেয়।

- **মেসেজ হ্যান্ডলিং সিস্টেম:** ব্যবহারকারীর ইনপুট, LLM-এর প্রতিক্রিয়া, টুল কল, এবং টুল আউটপুটের মধ্যে কথোপকথনের প্রবাহ পরিচালনা করে।

- **টুল ইন্টিগ্রেশন ফ্রেমওয়ার্ক:** এজেন্টকে বিভিন্ন টুলের সাথে সংযুক্ত করার জন্য অবকাঠামো প্রদান করে, তা সাধারণ ফাংশন হোক বা জটিল বাইরের সার্ভিস।

- **এরর হ্যান্ডলিং এবং ভ্যালিডেশন:** টুল এক্সিকিউশনে ব্যর্থতা, প্যারামিটার যাচাই, এবং অপ্রত্যাশিত প্রতিক্রিয়া পরিচালনা করার জন্য মেকানিজম।

- **স্টেট ম্যানেজমেন্ট:** কথোপকথনের প্রসঙ্গ, পূর্ববর্তী টুল ইন্টারঅ্যাকশন, এবং স্থায়ী ডেটা ট্র্যাক করে যাতে বহু-টার্ন ইন্টারঅ্যাকশনে সামঞ্জস্য বজায় থাকে।

এরপর, আমরা ফাংশন/টুল কলিং সম্পর্কে বিস্তারিত আলোচনা করব।

### ফাংশন/টুল কলিং

ফাংশন কলিং হলো বড় ভাষার মডেলগুলোকে (LLMs) টুলের সাথে ইন্টারঅ্যাক্ট করার ক্ষমতা প্রদান করার প্রধান উপায়। 'ফাংশন' এবং 'টুল' প্রায়ই একে অপরের পরিবর্তে ব্যবহৃত হয় কারণ 'ফাংশন' (পুনরায় ব্যবহারযোগ্য কোডের ব্লক) হলো 'টুল' যা এজেন্টরা কাজ সম্পাদনের জন্য ব্যবহার করে। একটি ফাংশনের কোড চালানোর জন্য, LLM-কে ব্যবহারকারীর অনুরোধের সাথে ফাংশনের বিবরণ তুলনা করতে হয়। এটি করার জন্য, উপলব্ধ ফাংশনের বিবরণসহ একটি স্কিমা LLM-কে পাঠানো হয়। LLM তারপর কাজের জন্য সবচেয়ে উপযুক্ত ফাংশন নির্বাচন করে এবং এর নাম এবং আর্গুমেন্টগুলো ফেরত দেয়। নির্বাচিত ফাংশনটি চালানো হয়, এর প্রতিক্রিয়া LLM-কে ফেরত পাঠানো হয়, যা ব্যবহারকারীর অনুরোধের উত্তর দিতে তথ্য ব্যবহার করে।

ডেভেলপারদের জন্য এজেন্টদের ফাংশন কলিং বাস্তবায়ন করতে প্রয়োজন:

1. একটি LLM মডেল যা ফাংশন কলিং সমর্থন করে
2. একটি স্কিমা যা ফাংশনের বিবরণ ধারণ করে
3. প্রতিটি ফাংশনের জন্য কোড যা স্কিমায় বর্ণিত

চলুন একটি উদাহরণ ব্যবহার করে দেখি কীভাবে একটি শহরের বর্তমান সময় পাওয়া যায়:

1. **ফাংশন কলিং সমর্থন করে এমন একটি LLM ইনিশিয়ালাইজ করুন:**

    সব মডেল ফাংশন কলিং সমর্থন করে না, তাই আপনি যে LLM ব্যবহার করছেন তা নিশ্চিত করা গুরুত্বপূর্ণ। <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ফাংশন কলিং সমর্থন করে। আমরা Azure OpenAI ক্লায়েন্ট ইনিশিয়ালাইজ করে শুরু করতে পারি।

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **একটি ফাংশন স্কিমা তৈরি করুন:**

    এরপর আমরা একটি JSON স্কিমা সংজ্ঞায়িত করব যা ফাংশনের নাম, ফাংশন কী করে তার বিবরণ, এবং ফাংশনের প্যারামিটারগুলোর নাম এবং বিবরণ ধারণ করে। আমরা এই স্কিমা ক্লায়েন্টে পাঠাবো, ব্যবহারকারীর অনুরোধের সাথে সান ফ্রান্সিসকোর সময় খুঁজে বের করার জন্য। গুরুত্বপূর্ণ বিষয় হলো একটি **টুল কল** ফেরত দেওয়া হয়, **চূড়ান্ত উত্তর নয়**। পূর্বে উল্লেখ করা হয়েছে, LLM কাজের জন্য নির্বাচিত ফাংশনের নাম এবং পাস করার জন্য আর্গুমেন্টগুলো ফেরত দেয়।

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
  
1. **কাজ সম্পাদনের জন্য প্রয়োজনীয় ফাংশনের কোড:**

    এখন LLM নির্ধারণ করেছে কোন ফাংশন চালানো প্রয়োজন, কাজ সম্পাদনের জন্য কোড বাস্তবায়ন এবং চালানো প্রয়োজন। আমরা Python-এ বর্তমান সময় পাওয়ার কোড বাস্তবায়ন করতে পারি। আমরা response_message থেকে নাম এবং আর্গুমেন্ট বের করার কোডও লিখতে পারি যাতে চূড়ান্ত ফলাফল পাওয়া যায়।

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

ফাংশন কলিং বেশিরভাগ, যদি না সব, এজেন্ট টুল ব্যবহারের ডিজাইনের কেন্দ্রে থাকে, তবে এটি শূন্য থেকে বাস্তবায়ন করা কখনও কখনও চ্যালেঞ্জিং হতে পারে। [Lesson 2](../../../02-explore-agentic-frameworks) এ আমরা শিখেছি যে এজেন্টিক ফ্রেমওয়ার্কগুলো আমাদের টুল ব্যবহারের জন্য প্রি-বিল্ট গঠনমূলক ব্লক প্রদান করে।

## এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে টুল ব্যবহারের উদাহরণ

এখানে বিভিন্ন এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করে টুল ব্যবহারের ডিজাইন প্যাটার্ন বাস্তবায়নের কিছু উদাহরণ দেওয়া হলো:

### সেমান্টিক কার্নেল

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">সেমান্টিক কার্নেল</a> হলো .NET, Python, এবং Java ডেভেলপারদের জন্য একটি ওপেন-সোর্স AI ফ্রেমওয়ার্ক যারা বড় ভাষার মডেল (LLMs) নিয়ে কাজ করছেন। এটি ফাংশন কলিং ব্যবহারের প্রক্রিয়াকে সহজ করে তোলে কারণ এটি আপনার ফাংশন এবং এর প্যারামিটারগুলোকে মডেলের কাছে স্বয়ংক্রিয়ভাবে বর্ণনা করে <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">সিরিয়ালাইজিং</a> প্রক্রিয়ার মাধ্যমে। এটি মডেল এবং আপনার কোডের মধ্যে কথোপকথন পরিচালনা করে। সেমান্টিক কার্নেলের মতো এজেন্টিক ফ্রেমওয়ার্ক ব্যবহার করার আরেকটি সুবিধা হলো এটি আপনাকে প্রি-বিল্ট টুল যেমন <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">ফাইল সার্চ</a> এবং <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">কোড ইন্টারপ্রেটার</a> অ্যাক্সেস করতে দেয়।

নিম্নলিখিত চিত্রটি সেমান্টিক কার্নেলের সাথে ফাংশন কলিং প্রক্রিয়াকে চিত্রিত করে:

![ফাংশন কলিং](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.bn.png)

সেমান্টিক কার্নেলে ফাংশন/টুলগুলো <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">প্লাগইন</a> নামে পরিচিত। আমরা পূর্বে দেখা `get_current_time` ফাংশনটিকে একটি ক্লাসে পরিণত করে প্লাগইনে রূপান্তর করতে পারি। আমরা `kernel_function` ডেকোরেটরও ইমপোর্ট করতে পারি, যা ফাংশনের বিবরণ গ্রহণ করে। যখন আপনি GetCurrentTimePlugin সহ একটি কার্নেল তৈরি করেন, কার্নেলটি স্বয়ংক্রিয়ভাবে ফাংশন এবং এর প্যারামিটারগুলোকে সিরিয়ালাইজ করে, প্রক্রিয়ায় স্কিমা তৈরি করে যা LLM-কে পাঠানো হয়।

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> হলো একটি নতুন এজেন্টিক ফ্রেমওয়ার্ক যা ডেভেলপারদের উচ্চ-মানের এবং এক্সটেনসিবল AI এজেন্ট তৈরি, ডিপ্লয়, এবং স্কেল করতে সক্ষম করে, এবং এর জন্য আন্ডারলাইন কম্পিউট এবং স্টোরেজ রিসোর্স পরিচালনা করার প্রয়োজন হয় না। এটি বিশেষভাবে এন্টারপ্রাইজ অ্যাপ্লিকেশনের জন্য কার্যকর কারণ এটি একটি সম্পূর্ণ পরিচালিত সার্ভিস যা এন্টারপ্রাইজ গ্রেড সিকিউরিটি প্রদান করে।

LLM API সরাসরি ব্যবহার করার তুলনায় Azure AI Agent Service কিছু সুবিধা প্রদান করে, যার মধ্যে রয়েছে:

- স্বয়ংক্রিয় টুল কলিং – টুল কল পার্স করা, টুল চালানো, এবং প্রতিক্রিয়া পরিচালনা করার প্রয়োজন নেই; এটি এখন সার্ভার-সাইডে সম্পন্ন হয়।
- নিরাপদভাবে পরিচালিত ডেটা – আপনার নিজের কথোপকথনের স্টেট পরিচালনা করার পরিবর্তে, আপনি থ্রেড ব্যবহার করে সমস্ত প্রয়োজনীয় তথ্য সংরক্ষণ করতে পারেন।
- প্রস্তুত-প্রস্তুত টুল – আপনার ডেটা সোর্সের সাথে ইন্টারঅ্যাক্ট করার জন্য টুল ব্যবহার করতে পারেন, যেমন Bing, Azure AI Search, এবং Azure Functions।

Azure AI Agent Service-এ উপলব্ধ টুলগুলোকে দুটি বিভাগে ভাগ করা যায়:

1. নলেজ টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing সার্চ দিয়ে গ্রাউন্ডিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ফাইল সার্চ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI সার্চ</a>

2. অ্যাকশন টুল:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ফাংশন কলিং</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">কোড ইন্টারপ্রেটার</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI নির্ধারিত টুল</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service আমাদের এই টুলগুলোকে একসাথে `toolset` হিসেবে ব্যবহার করার সুযোগ দেয়। এটি `threads` ব্যবহার করে যা একটি নির্দিষ্ট কথোপকথনের বার্তাগুলোর ইতিহাস ট্র্যাক করে।

ধরা যাক আপনি Contoso নামক একটি কোম্পানির সেলস এজেন্ট। আপনি একটি কথোপকথন এজেন্ট তৈরি করতে চান যা আপনার সেলস ডেটা সম্পর্কে প্রশ্নের উত্তর দিতে পারে।

নিম্নলিখিত চিত্রটি দেখায় কীভাবে আপনি Azure AI Agent Service ব্যবহার করে আপনার সেলস ডেটা বিশ্লেষণ করতে পারেন:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.bn.jpg)

এই সার্ভিসের সাথে কোনো টুল ব্যবহার করতে আমরা একটি ক্লায়েন্ট তৈরি করতে পারি এবং একটি টুল বা টুলসেট সংজ্ঞায়িত করতে পারি। এটি ব্যবহারিকভাবে বাস্তবায়ন করতে আমরা নিম্নলিখিত Python কোড ব্যবহার করতে পারি। LLM টুলসেটটি দেখে ব্যবহারকারীর তৈরি ফাংশন `fetch_sales_data_using_sqlite_query` অথবা প্রি-বিল্ট কোড ইন্টারপ্রেটার ব্যবহার করবে, ব্যবহারকারীর অনুরোধের উপর নির্ভর করে।

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

## বিশ্বাসযোগ্য AI এজেন্ট তৈরি করতে টুল ব্যবহারের ডিজাইন প্যাটার্ন ব্যবহার করার ক্ষেত্রে বিশেষ বিবেচনা কী কী?

LLM দ্বারা ডায়নামিকভাবে তৈরি করা SQL-এর ক্ষেত্রে একটি সাধারণ উদ্বেগ হলো নিরাপত্তা, বিশেষ করে SQL ইনজেকশন বা ক্ষতিকারক কার্যক্রমের ঝুঁকি, যেমন ডাটাবেস ড্রপ করা বা পরিবর্তন করা। যদিও এই উদ্বেগগুলো বৈধ, সেগুলো কার্যকরভাবে মোকাবিলা করা যেতে পারে ডাটাবেস অ্যাক্সেস অনুমতিগুলো সঠিকভাবে কনফিগার করে। বেশিরভাগ ডাটাবেসের জন্য এটি ডাটাবেসকে রিড-অনলি হিসেবে কনফিগার
[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন, যেখানে আপনি অন্যান্য শিক্ষার্থীদের সাথে যোগাযোগ করতে পারবেন, অফিস আওয়ারে অংশ নিতে পারবেন এবং আপনার AI Agents সম্পর্কিত প্রশ্নের উত্তর পেতে পারবেন।

## অতিরিক্ত সম্পদসমূহ

## পূর্ববর্তী পাঠ

[Agentic Design Patterns বোঝা](../03-agentic-design-patterns/README.md)

## পরবর্তী পাঠ

[Agentic RAG](../05-agentic-rag/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতা নিশ্চিত করার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।