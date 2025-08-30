<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6600bebb86f72f3f62a9163fcce9566",
  "translation_date": "2025-08-30T00:09:36+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "my"
}
-->
# Agentic Protocols (MCP, A2A နှင့် NLWeb) ကို အသုံးပြုခြင်း

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.my.png)](https://youtu.be/X-Dh9R3Opn8)

AI အေးဂျင့်များ အသုံးပြုမှု တိုးလာသည့်အခါ၊ စံသတ်မှတ်မှု၊ လုံခြုံရေးနှင့် ဖွင့်လှစ်ဆန်းသစ်မှုကို ပံ့ပိုးပေးနိုင်သော ပရိုတိုကောများအတွက် လိုအပ်ချက်များလည်း တိုးလာပါသည်။ ဒီသင်ခန်းစာမှာ Model Context Protocol (MCP), Agent to Agent (A2A) နှင့် Natural Language Web (NLWeb) ဆိုတဲ့ လိုအပ်ချက်တွေကို ဖြည့်ဆည်းပေးနိုင်ဖို့ ရည်ရွယ်ထားတဲ့ ပရိုတိုကော ၃ ခုကို လေ့လာပါမယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ လေ့လာမယ့်အရာတွေက:

• **MCP** က AI အေးဂျင့်တွေကို အသုံးပြုသူရဲ့ တာဝန်တွေကို ပြည့်စုံအောင် ပြုလုပ်ဖို့ အပြင်အဆင့် tools နဲ့ data တွေကို ရယူနိုင်အောင် ဘယ်လို အကူအညီပေးနိုင်တယ်ဆိုတာ။

• **A2A** က AI အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်မှုနဲ့ ပူးပေါင်းလုပ်ဆောင်မှုကို ဘယ်လို အကူအညီပေးနိုင်တယ်ဆိုတာ။

• **NLWeb** က ဘယ်လို website မဆိုမှာ သဘာဝဘာသာစကား interface တွေကို ပေးစွမ်းပြီး AI အေးဂျင့်တွေ website content ကို ရှာဖွေပြီး အပြန်အလှန်လုပ်ဆောင်နိုင်အောင် ဘယ်လို အကူအညီပေးနိုင်တယ်ဆိုတာ။

## သင်ယူရမယ့် ရည်မှန်းချက်များ

• **MCP, A2A, NLWeb** ရဲ့ အဓိက ရည်ရွယ်ချက်နဲ့ အကျိုးကျေးဇူးတွေကို AI အေးဂျင့်တွေရဲ့ အနေအထားမှာ **သိရှိနိုင်ရန်**။

• **ပရိုတိုကောတစ်ခုစီ** က LLMs, tools, နဲ့ အခြားအေးဂျင့်တွေရဲ့ ဆက်သွယ်မှုနဲ့ အပြန်အလှန်လုပ်ဆောင်မှုကို ဘယ်လို အကူအညီပေးနိုင်တယ်ဆိုတာ **ရှင်းပြနိုင်ရန်**။

• **Agentic systems** တွေ တည်ဆောက်ရာမှာ ပရိုတိုကောတစ်ခုစီရဲ့ သီးခြား အခန်းကဏ္ဍတွေကို **သိရှိနိုင်ရန်**။

## Model Context Protocol

**Model Context Protocol (MCP)** က application တွေကို LLMs ကို context နဲ့ tools တွေ ပေးနိုင်အောင် စံပြနည်းလမ်းတစ်ခုကို ပံ့ပိုးပေးတဲ့ open standard တစ်ခုဖြစ်ပါတယ်။ ဒါက AI အေးဂျင့်တွေကို data sources နဲ့ tools တွေကို တစ်မျိုးတည်းသော နည်းလမ်းနဲ့ ဆက်သွယ်နိုင်အောင် "universal adaptor" တစ်ခုအဖြစ် အကူအညီပေးပါတယ်။

MCP ရဲ့ components, direct API အသုံးပြုမှုနဲ့ နှိုင်းယှဉ်တဲ့ အကျိုးကျေးဇူးတွေ၊ AI အေးဂျင့်တွေ MCP server ကို ဘယ်လို အသုံးပြုနိုင်တယ်ဆိုတာကို လေ့လာကြမယ်။

### MCP ရဲ့ အဓိက Components

MCP က **client-server architecture** ပေါ်မှာ အခြေခံပြီး အဓိက components တွေက:

• **Hosts**: MCP Server နဲ့ ဆက်သွယ်မှုကို စတင်တဲ့ LLM application တွေ (ဥပမာ VSCode ကဲ့သို့ code editor တစ်ခု) ဖြစ်ပါတယ်။

• **Clients**: Host application အတွင်းမှာ MCP Server တွေနဲ့ တစ်ဦးချင်းဆက်သွယ်မှုကို ထိန်းသိမ်းတဲ့ components တွေ ဖြစ်ပါတယ်။

• **Servers**: သတ်မှတ်ထားတဲ့ စွမ်းရည်တွေကို ဖော်ပြပေးတဲ့ lightweight programs တွေ ဖြစ်ပါတယ်။

Protocol အတွင်းမှာ MCP Server ရဲ့ စွမ်းရည်တွေဖြစ်တဲ့ core primitives သုံးခု ပါဝင်ပါတယ်:

• **Tools**: AI အေးဂျင့်တစ်ခုက တစ်ခုခုလုပ်ဆောင်ဖို့ ခေါ်ယူနိုင်တဲ့ discrete actions သို့မဟုတ် functions တွေ ဖြစ်ပါတယ်။ ဥပမာအားဖြင့် မိုးလေဝသဝန်ဆောင်မှုက "get weather" tool ကို ဖော်ပြနိုင်သလို၊ e-commerce server က "purchase product" tool ကို ဖော်ပြနိုင်ပါတယ်။ MCP servers တွေက tool တစ်ခုစီရဲ့ နာမည်၊ ဖော်ပြချက်၊ input/output schema ကို capabilities listing မှာ ဖော်ပြပေးပါတယ်။

• **Resources**: MCP server က ပေးနိုင်တဲ့ read-only data items သို့မဟုတ် documents တွေ ဖြစ်ပြီး clients တွေက လိုအပ်တဲ့အခါ retrieve လုပ်နိုင်ပါတယ်။ ဥပမာအားဖြင့် ဖိုင်အကြောင်းအရာတွေ၊ database records တွေ၊ log files တွေ ပါဝင်ပါတယ်။ Resources တွေက text (code သို့မဟုတ် JSON) သို့မဟုတ် binary (images သို့မဟုတ် PDFs) ဖြစ်နိုင်ပါတယ်။

• **Prompts**: ပိုမိုရှုပ်ထွေးတဲ့ workflows တွေကို အကူအညီပေးနိုင်တဲ့ suggested prompts တွေကို ဖော်ပြပေးတဲ့ predefined templates တွေ ဖြစ်ပါတယ်။

### MCP ရဲ့ အကျိုးကျေးဇူးများ

MCP က AI အေးဂျင့်တွေအတွက် အရေးကြီးတဲ့ အကျိုးကျေးဇူးတွေ ပေးစွမ်းပါတယ်:

• **Dynamic Tool Discovery**: Agents တွေ MCP server ကနေ ရရှိနိုင်တဲ့ tools တွေကို dynamic အနေနဲ့ ရယူနိုင်ပြီး tools တွေ ဘာလုပ်ဆောင်နိုင်တယ်ဆိုတာ ဖော်ပြချက်နဲ့အတူ ရရှိနိုင်ပါတယ်။ ဒါက static coding လိုအပ်တဲ့ traditional APIs တွေနဲ့ နှိုင်းယှဉ်ပြီး ပိုမိုအဆင်ပြေပါတယ်။ MCP က "တစ်ခါ integrate လုပ်ပြီး" နည်းလမ်းကို ပံ့ပိုးပေးပြီး ပိုမိုအလွယ်တကူ ပြောင်းလဲနိုင်စေပါတယ်။

• **Interoperability Across LLMs**: MCP က LLMs မျိုးစုံမှာ အလုပ်လုပ်နိုင်ပြီး အဓိက models တွေကို performance ပိုမိုကောင်းမွန်အောင် စမ်းသပ်ပြောင်းလဲနိုင်စေပါတယ်။

• **Standardized Security**: MCP က standard authentication နည်းလမ်းကို ပံ့ပိုးပေးပြီး MCP servers အသစ်တွေကို ထည့်သွင်းရာမှာ scalability ကို တိုးတက်စေပါတယ်။ ဒါက traditional APIs တွေရဲ့ authentication နည်းလမ်းမျိုးစုံကို စီမံရတာထက် ပိုမိုရိုးရှင်းပါတယ်။

### MCP ရဲ့ ဥပမာ

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.my.png)

ဥပမာအားဖြင့် အသုံးပြုသူတစ်ဦးက MCP အသုံးပြုတဲ့ AI assistant ကို အသုံးပြုပြီး လေယာဉ်ခရီးစဉ်တစ်ခုကို ရှာဖွေပြီး booking လုပ်ချင်တယ်ဆိုပါစို့။

1. **Connection**: AI assistant (MCP client) က လေကြောင်းလိုင်းရဲ့ MCP server နဲ့ ဆက်သွယ်ပါတယ်။

2. **Tool Discovery**: Client က လေကြောင်းလိုင်းရဲ့ MCP server ကို "သင့်မှာ ဘယ် tools တွေ ရှိပါသလဲ?" လို့ မေးပါတယ်။ Server က "search flights" နဲ့ "book flights" tools တွေကို ပြန်လည်ဖြေကြားပါတယ်။

3. **Tool Invocation**: အသုံးပြုသူက AI assistant ကို "Portland ကနေ Honolulu ကို လေယာဉ်ခရီးစဉ် ရှာပေးပါ" လို့ မေးပါတယ်။ AI assistant က LLM ကို အသုံးပြုပြီး "search flights" tool ကို ခေါ်ယူဖို့လိုအပ်တယ်ဆိုတာ သိရှိပြီး MCP server ကို origin နဲ့ destination parameters တွေ ပေးပို့ပါတယ်။

4. **Execution and Response**: MCP server က လေကြောင်းလိုင်းရဲ့ internal booking API ကို ခေါ်ယူပြီး flight information (ဥပမာ JSON data) ကို AI assistant ကို ပြန်ပေးပါတယ်။

5. **Further Interaction**: AI assistant က flight options တွေကို အသုံးပြုသူကို ဖော်ပြပါတယ်။ အသုံးပြုသူက flight တစ်ခုကို ရွေးချယ်ပြီးနောက် assistant က "book flight" tool ကို MCP server မှာ ခေါ်ယူပြီး booking ကို ပြီးစီးစေပါတယ်။

## Agent-to-Agent Protocol (A2A)

MCP က LLMs နဲ့ tools တွေကို ဆက်သွယ်ပေးတာကို အဓိကထားပြီး **Agent-to-Agent (A2A) protocol** က AI အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်ပြီး ပူးပေါင်းလုပ်ဆောင်နိုင်အောင် ပိုမိုတိုးတက်စေပါတယ်။ A2A က အဖွဲ့အစည်း၊ ပတ်ဝန်းကျင်နဲ့ နည်းပညာ stack မျိုးစုံမှာ AI အေးဂျင့်တွေကို ဆက်သွယ်ပေးပြီး shared task တစ်ခုကို ပြီးစီးအောင် လုပ်ဆောင်နိုင်စေပါတယ်။

A2A ရဲ့ components, အကျိုးကျေးဇူးများနဲ့ travel application မှာ ဘယ်လို အသုံးချနိုင်တယ်ဆိုတာကို လေ့လာကြမယ်။

### A2A ရဲ့ အဓိက Components

A2A က အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်ပြီး အသုံးပြုသူရဲ့ subtask တစ်ခုကို ပြီးစီးအောင် လုပ်ဆောင်နိုင်စေပါတယ်။ Protocol ရဲ့ components တစ်ခုစီက ဒီအရာကို အကူအညီပေးပါတယ်:

#### Agent Card

MCP server က tools တွေကို ဖော်ပြသလို Agent Card က:

    ◦ အေးဂျင့်ရဲ့ နာမည်  
    ◦ **အေးဂျင့်ရဲ့ အထွေထွေ တာဝန်များ** ရဲ့ ဖော်ပြချက်  
    ◦ **သတ်မှတ်ထားတဲ့ ကျွမ်းကျင်မှုများ** ရဲ့ ဖော်ပြချက်  
    ◦ အေးဂျင့်ရဲ့ **current Endpoint URL**  
    ◦ အေးဂျင့်ရဲ့ **version** နဲ့ **capabilities** (ဥပမာ streaming responses နဲ့ push notifications)  

#### Agent Executor

Agent Executor က **အသုံးပြုသူရဲ့ chat context ကို remote agent** ကို ပေးပို့တာကို တာဝန်ယူပါတယ်။ Remote agent က ဒီ context ကို အသုံးပြုပြီး လုပ်ဆောင်ရမယ့် task ကို နားလည်နိုင်ဖို့ လိုအပ်ပါတယ်။ A2A server မှာ agent တစ်ခုက LLM ကို အသုံးပြုပြီး request တွေကို parse လုပ်ပြီး internal tools တွေကို အသုံးပြုပြီး task ကို ပြီးစီးစေပါတယ်။

#### Artifact

Remote agent က တောင်းဆိုထားတဲ့ task ကို ပြီးစီးပြီးနောက်၊ artifact တစ်ခုကို ဖန်တီးပါတယ်။ Artifact က **agent ရဲ့ လုပ်ဆောင်မှုရလဒ်**၊ **ပြီးစီးခဲ့တဲ့အရာရဲ့ ဖော်ပြချက်**၊ **protocol မှတဆင့် ပေးပို့ခဲ့တဲ့ text context** ကို ပါဝင်ပါတယ်။ Artifact ကို ပေးပို့ပြီးနောက် remote agent နဲ့ ဆက်သွယ်မှုကို လိုအပ်တဲ့အခါအထိ ပိတ်ထားပါတယ်။

#### Event Queue

ဒီ component က **updates တွေကို စီမံပြီး message တွေကို ပေးပို့** ဖို့ အသုံးပြုပါတယ်။ Agentic systems တွေမှာ task ပြီးစီးဖို့ အချိန်ကြာနိုင်တဲ့အခြေအနေတွေမှာ agents တွေ အချင်းချင်း ဆက်သွယ်မှုကို task ပြီးစီးတဲ့အထိ ပိတ်မသွားစေဖို့ အရေးကြီးပါတယ်။

### A2A ရဲ့ အကျိုးကျေးဇူးများ

• **Collaboration တိုးတက်မှု**: Vendors နဲ့ platforms မျိုးစုံကနေ အေးဂျင့်တွေကို ဆက်သွယ်ပြီး context တွေကို မျှဝေပြီး ပူးပေါင်းလုပ်ဆောင်နိုင်စေပါတယ်။ ဒါက ယခင် disconnected systems တွေကို seamless automation လုပ်ဆောင်နိုင်စေပါတယ်။

• **Model Selection Flexibility**: A2A agent တစ်ခုစီက သူ့ရဲ့ requests တွေကို service ပေးဖို့ ဘယ် LLM ကို အသုံးပြုမယ်ဆိုတာ ဆုံးဖြတ်နိုင်ပါတယ်။ MCP scenarios တစ်ချို့မှာ LLM တစ်ခုတည်းကို အသုံးပြုရတဲ့အခြေအနေနဲ့ မတူဘဲ optimized သို့မဟုတ် fine-tuned models တွေကို agent တစ်ခုစီမှာ အသုံးပြုနိုင်ပါတယ်။

• **Authentication ပေါင်းစည်းထားမှု**: Authentication ကို A2A protocol အတွင်းမှာ တိုက်ရိုက် ပေါင်းစည်းထားပြီး agent interactions တွေမှာ လုံခြုံရေး framework တစ်ခုကို ပံ့ပိုးပေးပါတယ်။

### A2A ရဲ့ ဥပမာ

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.my.png)

Travel booking scenario ကို A2A အသုံးပြုပြီး ပိုမိုတိုးတက်အောင် လေ့လာကြမယ်။

1. **User Request to Multi-Agent**: အသုံးပြုသူက "Travel Agent" A2A client/agent ကို "နောက်တစ်ပတ် Honolulu ကို လေယာဉ်ခရီးစဉ်၊ ဟိုတယ်နဲ့ ကားငှားမှု အားလုံးကို စီစဉ်ပေးပါ" လို့ မေးပါတယ်။

2. **Orchestration by Travel Agent**: Travel Agent က ဒီ request ကို ရရှိပြီး LLM ကို အသုံးပြုပြီး task ကို reasoning လုပ်ပြီး အခြား specialized agents တွေနဲ့ ဆက်သွယ်ဖို့ လိုအပ်တယ်ဆိုတာ ဆုံးဖြတ်ပါတယ်။

3. **Inter-Agent Communication**: Travel Agent က A2A protocol ကို အသုံးပြုပြီး Airline Agent, Hotel Agent, Car Rental Agent တို့လို specialized agents တွေနဲ့ ဆက်သွယ်ပါတယ်။

4. **Delegated Task Execution**: Travel Agent က ဒီ specialized agents တွေကို သတ်မှတ်ထားတဲ့ task တွေ (ဥပမာ "Find flights to Honolulu," "Book a hotel," "Rent a car") ကို ပေးပို့ပါတယ်။ Specialized agents တစ်ခုစီက သူ့ရဲ့ LLMs နဲ့ tools တွေကို အသုံးပြုပြီး task ကို ပြီးစီးစေပါတယ်။

5. **Consolidated Response**: Downstream agents တွေ task တွေကို ပြီးစီးပြီးနောက် Travel Agent က result တွေ (flight details, hotel confirmation, car rental booking) ကို စုစည်းပြီး အသုံးပြုသူကို ပြန်လည်ဖြေကြားပါတယ်။

## Natural Language Web (NLWeb)

Website တွေဟာ အင်တာနက်ပေါ်မှာ အချက်အလက်နဲ့ data တွေကို ရယူဖို့ အသုံးပြုသူတွေရဲ့ အဓိကနည်းလမ်းဖြစ်လာခဲ့ပါတယ်။

NLWeb ရဲ့ components, အကျိုးကျေးဇူးများနဲ့ travel application မှာ NLWeb ကို ဘယ်လို အသုံးချနိုင်တယ်ဆိုတာကို လေ့လာကြမယ်။

### NLWeb ရဲ့ Components

- **NLWeb Application (Core Service Code)**: သဘာဝဘာသာစကားမေးခွန်းတွေကို အလုပ်လုပ်စေတဲ့ စနစ်။ Platform ရဲ့ အစိတ်အပိုင်းတွေကို ဆက်သွယ်ပြီး အဖြေတွေ ဖန်တီးပေးပါတယ်။ Website ရဲ့ natural language features တွေကို အလုပ်လုပ်စေတဲ့ **engine** အဖြစ် တွေးနိုင်ပါတယ်။

- **NLWeb Protocol**: Website နဲ့ သဘာဝဘာသာစကား interaction အတွက် **အခြေခံစည်းမျဉ်းများ** ဖြစ်ပါတယ်။ JSON format (Schema.org ကို အသုံးပြု) နဲ့ အဖြေတွေကို ပြန်ပေးပါတယ်။ HTML က အွန်လိုင်းမှာ စာရွက်စာတမ်းတွေကို မျှဝေဖို့ အခြေခံအဆောက်အအုံပေးသလို၊ NLWeb က "AI Web" အတွက် အခြေခံအဆောက်အအုံကို ဖန်တီးပေးပါတယ်။

- **MCP Server (Model Context Protocol Endpoint)**: NLWeb setup တစ်ခုစီက MCP server အနေနဲ့လည်း အလုပ်လုပ်ပါတယ်။ ဒါက tools (ဥပမာ "ask" method) နဲ့ data တွေကို အခြား AI systems တွေနဲ့ မျှဝေနိုင်စေပါတယ်။ Website ရဲ့ content နဲ့ စွမ်းရည်တွေကို AI အေးဂျင့် ecosystem ရဲ့ အစိတ်အပိုင်းတစ်ခုအဖြစ် အသုံးချနိုင်စေပါတယ်။

- **Embedding Models**: Website content ကို **vectors** (embeddings) အဖြစ် ပြောင်းလဲဖို့ အသုံးပြုတဲ့ models တွေ။ Vectors တွေက အဓိပ္ပာယ်ကို capture လုပ်ပြီး computer တွေက နှိုင်းယှဉ်ပြီး ရှာဖွေနိုင်အောင် အကူအညီပေးပါတယ်။ Vectors တွေကို database တစ်ခုမှာ သိမ်းဆည်းပြီး အသုံးပြုသူတွေက ဘယ် embedding model ကို အသုံးပြုမယ်ဆိုတာ ရွေးချယ်နိုင်ပါတယ်။

- **Vector Database (Retrieval Mechanism)**: Website content ရဲ့ embeddings တွေကို သိမ်းဆည်းတဲ့ database။ မေးခွန်းတစ်ခုကို NLWeb က vector database ကို ရှာဖွေပြီး အရေးပါဆုံး အချက်

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။