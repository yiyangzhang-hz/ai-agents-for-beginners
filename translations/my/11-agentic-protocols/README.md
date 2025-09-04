<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T09:25:31+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "my"
}
-->
# Agentic Protocols (MCP, A2A နှင့် NLWeb) ကို အသုံးပြုခြင်း

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.my.png)](https://youtu.be/X-Dh9R3Opn8)

AI အေးဂျင့်များ အသုံးပြုမှု တိုးလာသည့်အခါ၊ စံနှုန်းချမှတ်ခြင်း၊ လုံခြုံရေးနှင့် ဖွင့်လှစ်နည်းပညာဆန်းသစ်မှုများကို ပံ့ပိုးပေးနိုင်သော ပရိုတိုကောများအတွက် လိုအပ်ချက်များလည်း တိုးလာပါသည်။ ဒီသင်ခန်းစာမှာတော့ Model Context Protocol (MCP), Agent to Agent (A2A) နှင့် Natural Language Web (NLWeb) ဆိုတဲ့ လိုအပ်ချက်တွေကို ဖြည့်ဆည်းပေးနိုင်မယ့် ပရိုတိုကော ၃ ခုကို လေ့လာသွားမှာ ဖြစ်ပါတယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ လေ့လာမယ့်အရာတွေကတော့ -

• **MCP** က AI အေးဂျင့်တွေကို အသုံးပြုသူရဲ့ တာဝန်တွေကို ပြည့်စုံအောင် လုပ်ဆောင်နိုင်ဖို့ အပြင်ပရိုဂရမ်တွေ၊ အချက်အလက်တွေကို ရယူနိုင်အောင် ဘယ်လို အကူအညီပေးသလဲ။

• **A2A** က AI အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်ပြီး ပူးပေါင်းလုပ်ဆောင်နိုင်ဖို့ ဘယ်လို အကူအညီပေးသလဲ။

• **NLWeb** က AI အေးဂျင့်တွေကို ဝက်ဘ်ဆိုဒ်တွေမှာ အကြောင်းအရာတွေကို ရှာဖွေပြီး အပြန်အလှန် ဆက်သွယ်နိုင်အောင် ဘယ်လို အကူအညီပေးသလဲ။

## သင်ယူရမည့် ရည်မှန်းချက်များ

• **MCP, A2A, NLWeb** ရဲ့ အဓိကရည်ရွယ်ချက်နဲ့ အကျိုးကျေးဇူးတွေကို AI အေးဂျင့်တွေရဲ့ အခြေအနေမှာ **သိရှိနိုင်ရန်**။

• **ပရိုတိုကောတစ်ခုချင်းစီ** က LLMs, tools, နဲ့ အခြားအေးဂျင့်တွေအကြား ဆက်သွယ်မှုနဲ့ အပြန်အလှန်လုပ်ဆောင်မှုကို ဘယ်လို အကူအညီပေးသလဲဆိုတာ **ရှင်းပြနိုင်ရန်**။

• **ပရိုတိုကောတစ်ခုချင်းစီ** က အေးဂျင့်စနစ်တွေကို ဖွဲ့စည်းရာမှာ ဘယ်လို အခန်းကဏ္ဍတွေ ပါဝင်သလဲဆိုတာ **သိရှိနိုင်ရန်**။

## Model Context Protocol

**Model Context Protocol (MCP)** က AI အေးဂျင့်တွေကို အခြား application တွေက context နဲ့ tools တွေကို စံနှုန်းချမှတ်ထားတဲ့ နည်းလမ်းတစ်ခုဖြင့် ပေးပို့နိုင်အောင် ဖွင့်လှစ်ထားတဲ့ စံနှုန်းတစ်ခု ဖြစ်ပါတယ်။ ဒါဟာ AI အေးဂျင့်တွေကို အမျိုးမျိုးသော အချက်အလက်ရင်းမြစ်များနဲ့ tools တွေကို တစ်စည်းတစ်လုံးနဲ့ ဆက်သွယ်နိုင်အောင် Universal Adaptor တစ်ခုအဖြစ် အကူအညီပေးပါတယ်။

MCP ရဲ့ အစိတ်အပိုင်းတွေ၊ API ကို တိုက်ရိုက်အသုံးပြုခြင်းနဲ့ နှိုင်းယှဉ်တဲ့ အကျိုးကျေးဇူးတွေ၊ AI အေးဂျင့်တွေ MCP server ကို ဘယ်လို အသုံးပြုနိုင်မလဲဆိုတာကို လေ့လာကြမယ်။

### MCP ရဲ့ အဓိကအစိတ်အပိုင်းများ

MCP က **client-server architecture** ပေါ်မှာ အခြေခံထားပြီး အဓိကအစိတ်အပိုင်းတွေက -

• **Hosts**: MCP Server နဲ့ ဆက်သွယ်မှုကို စတင်တဲ့ LLM application (ဥပမာ - VSCode ကဲ့သို့သော code editor) တွေ။

• **Clients**: Host application အတွင်းရှိ အစိတ်အပိုင်းတွေဖြစ်ပြီး server တွေနဲ့ တစ်ဦးချင်းဆက်သွယ်မှုကို ထိန်းသိမ်းထားပါတယ်။

• **Servers**: အထူးစွမ်းဆောင်ရည်တွေကို ဖော်ပြပေးတဲ့ အလွယ်တကူ အသုံးပြုနိုင်တဲ့ ပရိုဂရမ်တွေ။

MCP Server ရဲ့ စွမ်းဆောင်ရည်တွေမှာ အဓိက primitive ၃ ခု ပါဝင်ပါတယ် -

• **Tools**: AI အေးဂျင့်တွေ action တစ်ခုကို လုပ်ဆောင်ဖို့ ခေါ်ယူနိုင်တဲ့ discrete actions သို့မဟုတ် functions တွေ။ ဥပမာ - မိုးလေဝသဝန်ဆောင်မှုက "get weather" tool ကို ဖော်ပြနိုင်သလို၊ e-commerce server က "purchase product" tool ကို ဖော်ပြနိုင်ပါတယ်။ MCP servers က tool တစ်ခုချင်းစီရဲ့ နာမည်၊ ဖော်ပြချက်နဲ့ input/output schema ကို capabilities listing မှာ ဖော်ပြပေးပါတယ်။

• **Resources**: MCP server က ပေးနိုင်တဲ့ ဖတ်ရှုနိုင်တဲ့ အချက်အလက် item တွေ သို့မဟုတ် စာရွက်စာတမ်းတွေဖြစ်ပြီး clients တွေက တောင်းဆိုမှုအရ ရယူနိုင်ပါတယ်။ ဥပမာ - ဖိုင်အကြောင်းအရာတွေ၊ ဒေတာဘေ့စ်မှတ်တမ်းတွေ သို့မဟုတ် log ဖိုင်တွေ။ Resources တွေက text (ဥပမာ - code သို့မဟုတ် JSON) သို့မဟုတ် binary (ဥပမာ - images သို့မဟုတ် PDFs) ဖြစ်နိုင်ပါတယ်။

• **Prompts**: Predefined templates တွေဖြစ်ပြီး ပိုမိုရှုပ်ထွေးတဲ့ workflows တွေကို အကူအညီပေးနိုင်ပါတယ်။

### MCP ရဲ့ အကျိုးကျေးဇူးများ

MCP က AI အေးဂျင့်တွေ အတွက် အရေးကြီးတဲ့ အကျိုးကျေးဇူးတွေ ပေးပါတယ် -

• **Dynamic Tool Discovery**: Agents တွေ MCP server က tool တွေကို dynamic အနေနဲ့ ရယူနိုင်ပြီး tool တွေ ဘာလုပ်ဆောင်နိုင်သလဲဆိုတာ ဖော်ပြချက်နဲ့အတူ ရရှိနိုင်ပါတယ်။ ဒါဟာ traditional APIs တွေလို static coding လိုအပ်မှုမရှိဘဲ "တစ်ခါပေါင်းစည်းပြီး အမြဲအသုံးပြုနိုင်" approach ကို ပေးပါတယ်။

• **Interoperability Across LLMs**: MCP က အမျိုးမျိုးသော LLMs တွေမှာ အလုပ်လုပ်နိုင်ပြီး အဓိက models တွေကို ပြောင်းလဲသုံးစွဲနိုင်တဲ့ flexibility ကို ပေးပါတယ်။

• **Standardized Security**: MCP မှာ စံနှုန်း authentication နည်းလမ်း ပါဝင်ပြီး MCP servers အသစ်တွေကို ထည့်သွင်းရာမှာ scalability ကို တိုးတက်စေပါတယ်။

### MCP နမူနာ

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.my.png)

ဥပမာ - အသုံးပြုသူတစ်ဦးက MCP အသုံးပြုတဲ့ AI အကူအညီကို သုံးပြီး လေယာဉ်ခရီးစဉ်တစ်ခုကို ရှာဖွေချင်တယ်ဆိုပါစို့။

1. **Connection**: AI အကူအညီ (MCP client) က လေကြောင်းလိုင်းရဲ့ MCP server နဲ့ ဆက်သွယ်ပါတယ်။

2. **Tool Discovery**: Client က လေကြောင်းလိုင်းရဲ့ MCP server ကို "သင့်မှာ ဘယ် tool တွေ ရှိပါသလဲ?" လို့ မေးပါတယ်။ Server က "search flights" နဲ့ "book flights" tools တွေကို ပြန်လည်ဖြေကြားပါတယ်။

3. **Tool Invocation**: အသုံးပြုသူက AI အကူအညီကို "Portland ကနေ Honolulu ကို လေယာဉ်ခရီးစဉ် ရှာပေးပါ" လို့ မေးပါတယ်။ AI အကူအညီက "search flights" tool ကို ခေါ်ယူပြီး သက်ဆိုင်တဲ့ parameters (origin, destination) တွေ MCP server ကို ပေးပို့ပါတယ်။

4. **Execution and Response**: MCP server က လေကြောင်းလိုင်းရဲ့ internal booking API ကို ခေါ်ယူပြီး flight information (ဥပမာ - JSON data) ကို AI အကူအညီဆီ ပြန်ပေးပါတယ်။

5. **Further Interaction**: AI အကူအညီက flight options တွေကို အသုံးပြုသူဆီ ပြန်လည်ဖော်ပြပါတယ်။ အသုံးပြုသူက flight တစ်ခုကို ရွေးချယ်ပြီးနောက် AI အကူအညီက "book flight" tool ကို MCP server မှာ ခေါ်ယူပြီး booking ကို ပြီးစီးစေပါတယ်။

## Agent-to-Agent Protocol (A2A)

MCP က LLMs နဲ့ tools တွေကို ဆက်သွယ်ပေးတာကို အဓိကထားပြီး **Agent-to-Agent (A2A) protocol** က AI အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်ပြီး ပူးပေါင်းလုပ်ဆောင်နိုင်ဖို့ အကူအညီပေးပါတယ်။ A2A က အဖွဲ့အစည်းတွေ၊ ပတ်ဝန်းကျင်တွေ၊ နည်းပညာစနစ်တွေ အကြား AI အေးဂျင့်တွေကို ဆက်သွယ်ပေးပြီး တစ်ဦးချင်း subtask တွေကို ပြည့်စုံအောင် လုပ်ဆောင်နိုင်စေပါတယ်။

A2A ရဲ့ အစိတ်အပိုင်းတွေ၊ အကျိုးကျေးဇူးတွေ၊ နမူနာ travel application မှာ ဘယ်လို အသုံးပြုနိုင်မလဲဆိုတာကို လေ့လာကြမယ်။

### A2A ရဲ့ အဓိကအစိတ်အပိုင်းများ

A2A က အေးဂျင့်တွေ အချင်းချင်း ဆက်သွယ်ပြီး အသုံးပြုသူရဲ့ subtask တစ်ခုကို ပြည့်စုံအောင် လုပ်ဆောင်နိုင်ဖို့ အကူအညီပေးပါတယ်။ Protocol ရဲ့ အစိတ်အပိုင်းတစ်ခုချင်းစီက ဒီအရာကို အကူအညီပေးပါတယ် -

#### Agent Card

MCP server က tool list ကို ဖော်ပြသလို Agent Card က -

- အေးဂျင့်ရဲ့ နာမည်  
- **အေးဂျင့်ရဲ့ အထွေထွေလုပ်ဆောင်နိုင်မှု**  
- **အထူးကျွမ်းကျင်မှုများ** ရဲ့ ဖော်ပြချက်  
- အေးဂျင့်ရဲ့ **Endpoint URL**  
- အေးဂျင့်ရဲ့ **version** နဲ့ **capabilities** (ဥပမာ - streaming responses, push notifications)  

#### Agent Executor

Agent Executor က **အသုံးပြုသူရဲ့ context ကို remote agent ဆီ ပေးပို့တာ** အတွက် တာဝန်ရှိပါတယ်။ Remote agent က user request ကို နားလည်ပြီး task ကို လုပ်ဆောင်ဖို့ context လိုအပ်ပါတယ်။

#### Artifact

Remote agent က တောင်းဆိုမှုကို ပြီးစီးတဲ့အခါ artifact ကို ဖန်တီးပါတယ်။ Artifact က **အေးဂျင့်ရဲ့ လုပ်ဆောင်မှုရလဒ်**၊ **လုပ်ဆောင်ခဲ့တာရဲ့ ဖော်ပြချက်**၊ **text context** ကို protocol မှတစ်ဆင့် ပေးပို့ပါတယ်။

#### Event Queue

ဒီအစိတ်အပိုင်းက **updates တွေကို ထိန်းသိမ်းပြီး message တွေကို ပေးပို့တာ** အတွက် အသုံးပြုပါတယ်။ အေးဂျင့်စနစ်တွေမှာ task ပြီးစီးမှုအချိန်ကြာနိုင်တဲ့အခြေအနေမှာ connection မပျက်စီးအောင် အရေးကြီးပါတယ်။

### A2A ရဲ့ အကျိုးကျေးဇူးများ

• **Collaboration တိုးတက်မှု**: Vendor နဲ့ platform မတူတဲ့ အေးဂျင့်တွေ context တွေကို မျှဝေပြီး ပူးပေါင်းလုပ်ဆောင်နိုင်စေပါတယ်။

• **Model Selection Flexibility**: A2A agent တစ်ခုချင်းစီက သူ့ရဲ့ request ကို ဆောင်ရွက်ဖို့ LLM ကို ရွေးချယ်နိုင်ပါတယ်။

• **Authentication ပါဝင်မှု**: Authentication ကို A2A protocol မှာ တိုက်ရိုက် ထည့်သွင်းထားပြီး အေးဂျင့်အကြား လုံခြုံရေး framework တစ်ခုကို ပေးပါတယ်။

### A2A နမူနာ

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.my.png)

Travel booking scenario ကို A2A အသုံးပြုမှုနဲ့ တိုးချဲ့ကြည့်ရအောင်။

1. **User Request to Multi-Agent**: အသုံးပြုသူက "Travel Agent" A2A client/agent ကို "နောက်တစ်ပတ် Honolulu ကို လေယာဉ်ခရီးစဉ်၊ ဟိုတယ်နဲ့ ကားငှားမှု အားလုံးကို စီစဉ်ပေးပါ" လို့ မေးပါတယ်။

2. **Orchestration by Travel Agent**: Travel Agent က request ကို ရရှိပြီး LLM ကို အသုံးပြုကာ task ကို reasoning လုပ်ပြီး အခြား specialized agents တွေနဲ့ ဆက်သွယ်ဖို့ ဆုံးဖြတ်ပါတယ်။

3. **Inter-Agent Communication**: Travel Agent က A2A protocol ကို အသုံးပြုကာ Airline Agent, Hotel Agent, Car Rental Agent တို့နဲ့ ဆက်သွယ်ပါတယ်။

4. **Delegated Task Execution**: Travel Agent က specialized agents တွေကို task တွေ ပေးပို့ပါတယ် (ဥပမာ - "Find flights to Honolulu," "Book a hotel," "Rent a car")။ Specialized agents တစ်ခုချင်းစီက သူ့ရဲ့ tools တွေ MCP servers တွေကို အသုံးပြုကာ task ကို ဆောင်ရွက်ပါတယ်။

5. **Consolidated Response**: Downstream agents အားလုံး task တွေ ပြီးစီးတဲ့အခါ Travel Agent က result တွေကို စုစည်းပြီး အသုံးပြုသူဆီ ပြန်လည်ပေးပို့ပါတယ်။

## Natural Language Web (NLWeb)

ဝက်ဘ်ဆိုဒ်တွေဟာ အင်တာနက်ပေါ်မှာ အချက်အလက်နဲ့ ဒေတာတွေကို ရယူဖို့ အသုံးပြုသူတွေရဲ့ အဓိကနည်းလမ်းဖြစ်ပါတယ်။

NLWeb ရဲ့ အစိတ်အပိုင်းတွေ၊ အကျိုးကျေးဇူးတွေ၊ Travel application မှာ NLWeb ဘယ်လို အလုပ်လုပ်သလဲဆိုတာကို လေ့လာကြမယ်။

### NLWeb ရဲ့ အစိတ်အပိုင်းများ

- **NLWeb Application (Core Service Code)**: Natural language questions တွေကို ဆောင်ရွက်တဲ့ စနစ်။ Platform ရဲ့ အစိတ်အပိုင်းတွေကို ဆက်သွယ်ပြီး response တွေ ဖန်တီးပါတယ်။ ဒါကို ဝက်ဘ်ဆိုဒ်ရဲ့ natural language features တွေကို အင်ဂျင်တစ်ခုအဖြစ် တွေးနိုင်ပါတယ်။

- **NLWeb Protocol**: Natural language interaction အတွက် အခြေခံစည်းမျဉ်းများ။ JSON format (Schema.org အသုံးပြု) ဖြင့် response တွေကို ပြန်ပေးပါတယ်။

- **MCP Server (Model Context Protocol Endpoint)**: NLWeb setup တစ်ခု MCP server အဖြစ်လည်း အလုပ်လုပ်ပါတယ်။ Tools နဲ့ data တွေကို AI systems တွေနဲ့ မျှဝေနိုင်ပါတယ်။

- **Embedding Models**: Website content ကို vectors (embeddings) အဖြစ် ပြောင်းလဲပေးတဲ့ models တွေ။

- **Vector Database (Retrieval Mechanism)**: Website content ရဲ့ embeddings တွေကို သိမ်းဆည်းထားတဲ့ database။

### NLWeb နမူနာ

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.my.png)

Travel booking website ကို NLWeb နဲ့ အလုပ်လုပ်ပုံကို ကြည့်ရအောင်။

1. **Data Ingestion**: Travel website ရဲ့ product catalogs (ဥပမာ - flight listings, hotel descriptions, tour packages) တွေကို Schema.org သို့မဟုတ် RSS feeds အသုံးပြုကာ NLWeb tools တွေ ingest လုပ်ပြီး embeddings ဖန်တီးကာ vector database မှာ သိမ်းဆည်းပါတယ်။

2. **Natural Language Query (Human)**: အသုံးပြုသူက website ကို ဝင်ရောက်ပြီး menu တွေ browse မလုပ်ဘဲ chat interface မှာ "Find me a family-friendly hotel in Honolulu with a pool for next week" လို့ ရေးထည့်ပါတယ်။

3. **NLWeb Processing**: NLWeb application က query ကို ရရှိပြီး LLM ကို အသုံးပြုကာ vector database ကို ရှာဖွေပါတယ်။

4. **Accurate Results**: LLM က search results တွေကို နားလည်ကာ "family-friendly," "pool," "Honolulu" criteria တွေကို အခြေခံပြီး natural language response တစ်ခုကို ဖန်တီးပါတယ်။

5. **AI Agent Interaction**: NLWeb က MCP server အဖြစ်လည်း အလုပ်လုပ်တဲ့အတွက် AI travel agent တစ်ခုက website ရဲ့ NLWeb instance ကို ဆက်သွယ်နိုင်ပါတယ်။

### MCP/A2A/NLWeb အကြောင်း မေးမြန်းလိုပါသလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပြီး အခြားလေ့လာသူတွေနဲ့ တွေ့ဆုံပါ၊ office hours တွေကို တက်ရောက်ပါ၊ AI Agents အကြောင်း မေးမြန်းပါ။

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)  
- [Semantic Kernel Guides

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်ကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပာယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။