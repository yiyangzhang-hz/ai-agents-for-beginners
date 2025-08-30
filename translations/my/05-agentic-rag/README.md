<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-30T00:01:08+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "my"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.my.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(အပေါ်ရှိပုံကိုနှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ပါ)_

# Agentic RAG

ဒီသင်ခန်းစာမှာ Agentic Retrieval-Augmented Generation (Agentic RAG) ဆိုတဲ့ AI နည်းပညာအသစ်တစ်ခုကို အကျယ်အဝန်း ရှင်းလင်းပြသထားပါတယ်။ ဒီနည်းပညာမှာ အကြီးစားဘာသာစကားမော်ဒယ်များ (LLMs) က အပြင်ပအရင်းအမြစ်များမှ အချက်အလက်များကို ရယူရင်း၊ ကိုယ်တိုင်အဆင့်ဆင့် အစီအစဉ်ချပြီး ဆက်လက်လုပ်ဆောင်နိုင်ပါတယ်။ ရိုးရိုး static retrieval-then-read ပုံစံနဲ့ မတူဘဲ Agentic RAG မှာ LLM ကို အဆင့်ဆင့် ခေါ်ယူပြီး tool သို့မဟုတ် function calls နဲ့ structured outputs တွေကို ပေါင်းစပ်အသုံးပြုပါတယ်။ စနစ်က ရလဒ်တွေကို အကဲဖြတ်ပြီး၊ query တွေကို ပြန်လည်တိုးတက်အောင်လုပ်ဆောင်၊ လိုအပ်ပါက tool တွေကို ထပ်ခေါ်ပြီး၊ လိုက်လျောညီထွေဖြေရှင်းမှုရရှိတဲ့အထိ ဒီစက်ဝိုင်းကို ဆက်လက်လုပ်ဆောင်ပါတယ်။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ အောက်ပါအကြောင်းအရာများကို လေ့လာပါမည်-

- **Agentic RAG ကို နားလည်ခြင်း:** အကြီးစားဘာသာစကားမော်ဒယ်များ (LLMs) က အပြင်ပအရင်းအမြစ်များမှ အချက်အလက်များကို ရယူရင်း၊ ကိုယ်တိုင်အဆင့်ဆင့် အစီအစဉ်ချပြီး ဆက်လက်လုပ်ဆောင်နိုင်တဲ့ AI နည်းပညာအသစ်ကို လေ့လာပါ။
- **Iterative Maker-Checker ပုံစံကို နားလည်ခြင်း:** LLM ကို အဆင့်ဆင့် ခေါ်ယူပြီး tool သို့မဟုတ် function calls နဲ့ structured outputs တွေကို ပေါင်းစပ်အသုံးပြုတဲ့ loop ကို နားလည်ပါ။
- **အကောင်းဆုံးအသုံးချမှုများကို ရှာဖွေခြင်း:** Agentic RAG က ထူးချွန်တဲ့နေရာများကို ရှာဖွေပါ၊ ဥပမာ- အမှန်တကယ်ဖြစ်စဉ်များ၊ ရှုပ်ထွေးတဲ့ database အပြန်အလှန်လုပ်ဆောင်မှုများ၊ နှင့် တိုးတက်တဲ့ workflow များ။

## သင်ယူရမည့်ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးပြီးနောက်မှာ သင်သည် အောက်ပါအရာများကို နားလည်နိုင်ပါမည်-

- **Agentic RAG ကို နားလည်ခြင်း:** AI နည်းပညာအသစ်တစ်ခုဖြစ်တဲ့ Agentic RAG ကို နားလည်ပါ။
- **Iterative Maker-Checker ပုံစံ:** LLM ကို အဆင့်ဆင့် ခေါ်ယူပြီး tool သို့မဟုတ် function calls နဲ့ structured outputs တွေကို ပေါင်းစပ်အသုံးပြုတဲ့ loop ကို နားလည်ပါ။
- **Reasoning Process ကို ကိုယ်တိုင်ပိုင်ဆိုင်ခြင်း:** စနစ်က ကိုယ်တိုင် reasoning process ကို ပိုင်ဆိုင်နိုင်ပြီး၊ ပြဿနာကို ဖြေရှင်းဖို့ အကွေ့အကောက်များကို ဆုံးဖြတ်နိုင်သည်။
- **Workflow:** Agentic မော်ဒယ်က ကိုယ်တိုင် market trend reports ကို ရယူခြင်း၊ ပြိုင်ဘက်အချက်အလက်များကို ရှာဖွေခြင်း၊ internal sales metrics ကို correlation လုပ်ခြင်း၊ အချက်အလက်များကို စနစ်တကျ စုစည်းခြင်း၊ နှင့် strategy ကို အကဲဖြတ်ခြင်း စသည်တို့ကို ဆောင်ရွက်နိုင်သည်။
- **Iterative Loops, Tool Integration, နှင့် Memory:** Loop interaction pattern ကို အသုံးပြုပြီး၊ state နှင့် memory ကို ထိန်းသိမ်းထားခြင်း၊ ပြန်လည်ထပ်ခါတလဲလဲဖြစ်မှုကို ရှောင်ရှားခြင်း၊ နှင့် informed decisions လုပ်ဆောင်ခြင်း။
- **Failure Modes ကို ကိုင်တွယ်ခြင်းနှင့် Self-Correction:** Iterating နှင့် re-querying, diagnostic tools အသုံးပြုခြင်း၊ နှင့် လူ့အကူအညီကို fallback လုပ်ခြင်း စသည်တို့ကို လေ့လာပါ။
- **Boundaries of Agency:** Agentic RAG ရဲ့ အကန့်အသတ်များကို နားလည်ပါ၊ domain-specific autonomy, infrastructure dependence, နှင့် guardrails များကို လေးစားခြင်း။
- **Practical Use Cases နှင့် Value:** Agentic RAG ရဲ့ ထူးချွန်တဲ့နေရာများကို ရှာဖွေပါ၊ correctness-first environments, ရှုပ်ထွေးတဲ့ database interactions, နှင့် extended workflows စသည်တို့။
- **Governance, Transparency, နှင့် Trust:** Governance နှင့် transparency ရဲ့ အရေးပါမှုကို လေ့လာပါ၊ reasoning ကို ရှင်းလင်းပြနိုင်ခြင်း၊ bias control, နှင့် လူ့အကူအညီ။

## Agentic RAG ဆိုတာဘာလဲ?

Agentic Retrieval-Augmented Generation (Agentic RAG) ဆိုတာ AI နည်းပညာအသစ်တစ်ခုဖြစ်ပြီး၊ အကြီးစားဘာသာစကားမော်ဒယ်များ (LLMs) က အပြင်ပအရင်းအမြစ်များမှ အချက်အလက်များကို ရယူရင်း၊ ကိုယ်တိုင်အဆင့်ဆင့် အစီအစဉ်ချပြီး ဆက်လက်လုပ်ဆောင်နိုင်သည်။ Static retrieval-then-read ပုံစံနဲ့ မတူဘဲ Agentic RAG မှာ LLM ကို အဆင့်ဆင့် ခေါ်ယူပြီး tool သို့မဟုတ် function calls နဲ့ structured outputs တွေကို ပေါင်းစပ်အသုံးပြုသည်။ စနစ်က ရလဒ်တွေကို အကဲဖြတ်ပြီး၊ query တွေကို ပြန်လည်တိုးတက်အောင်လုပ်ဆောင်၊ လိုအပ်ပါက tool တွေကို ထပ်ခေါ်ပြီး၊ လိုက်လျောညီထွေဖြေရှင်းမှုရရှိတဲ့အထိ ဒီစက်ဝိုင်းကို ဆက်လက်လုပ်ဆောင်သည်။

ဒီ iterative “maker-checker” ပုံစံက အမှန်တကယ်ဖြစ်စဉ်များကို တိုးတက်အောင်လုပ်ဆောင်ပြီး၊ malformed queries များကို ကိုင်တွယ်နိုင်စွမ်းရှိစေသည်။ Structured databases (ဥပမာ- NL2SQL) တွေမှာ query များကို ပြန်လည်ရေးသားခြင်း၊ retrieval methods များကို ရွေးချယ်ခြင်း၊ နှင့် tools များကို ပေါင်းစပ်အသုံးပြုခြင်း စသည်တို့ကို စနစ်က ကိုယ်တိုင် ဆောင်ရွက်နိုင်သည်။

## Agentic Retrieval-Augmented Generation (Agentic RAG) ကို အဓိပ္ပါယ်ဖွင့်ဆိုခြင်း

Agentic Retrieval-Augmented Generation (Agentic RAG) ဆိုတာ AI နည်းပညာအသစ်တစ်ခုဖြစ်ပြီး၊ LLMs တွေက အပြင်ပအရင်းအမြစ်များမှ အချက်အလက်များကို ရယူရင်း၊ ကိုယ်တိုင်အဆင့်ဆင့် အစီအစဉ်ချပြီး ဆက်လက်လုပ်ဆောင်နိုင်သည်။ Static retrieval-then-read patterns သို့မဟုတ် scripted prompt sequences များနဲ့ မတူဘဲ Agentic RAG မှာ LLM ကို အဆင့်ဆင့် ခေါ်ယူပြီး tool သို့မဟုတ် function calls နဲ့ structured outputs တွေကို ပေါင်းစပ်အသုံးပြုသည်။ 

## Reasoning Process ကို ကိုယ်တိုင်ပိုင်ဆိုင်ခြင်း

Agentic RAG ရဲ့ ထူးခြားတဲ့အချက်က reasoning process ကို ကိုယ်တိုင်ပိုင်ဆိုင်နိုင်ခြင်းဖြစ်သည်။ Traditional RAG implementations တွေက လူတွေက pre-define လုပ်ထားတဲ့ path ကို model က အလွယ်တကူ လိုက်နာရုံသာဖြစ်သည်။ 

## Iterative Loops, Tool Integration, နှင့် Memory

Agentic RAG စနစ်က looped interaction pattern ကို အခြေခံထားသည်-

- **Initial Call:** User prompt ကို LLM မှာ တင်ပြသည်။
- **Tool Invocation:** Model က မရှိသေးတဲ့ အချက်အလက်များ သို့မဟုတ် မရှင်းလင်းတဲ့ အညွှန်းများကို တွေ့ရှိပါက tool သို့မဟုတ် retrieval method ကို ရွေးချယ်သည်။
- **Assessment & Refinement:** Returned data ကို ပြန်လည်သုံးသပ်ပြီး၊ model က အချက်အလက်များလုံလောက်မှုရှိ/မရှိကို ဆုံးဖြတ်သည်။
- **Repeat Until Satisfied:** Model က လုံလောက်တဲ့ ဖြေရှင်းမှုရရှိတဲ့အထိ ဒီစက်ဝိုင်းကို ဆက်လက်လုပ်ဆောင်သည်။
- **Memory & State:** စနစ်က state နှင့် memory ကို ထိန်းသိမ်းထားပြီး၊ ပြန်လည်ထပ်ခါတလဲလဲဖြစ်မှုကို ရှောင်ရှားသည်။

## Failure Modes ကို ကိုင်တွယ်ခြင်းနှင့် Self-Correction

Agentic RAG ရဲ့ autonomy က robust self-correction mechanisms ပါဝင်သည်။ 

## Boundaries of Agency

Agentic RAG ရဲ့ “agentic” စွမ်းရည်များသည် လူသား developer များက ပေးထားသော tools, data sources, နှင့် policies များအတွင်းသာ အကျုံးဝင်သည်။

## Practical Use Cases နှင့် Value

Agentic RAG က အောက်ပါနေရာများတွင် ထူးချွန်သည်-

1. **Correctness-First Environments:** Compliance checks, regulatory analysis, သို့မဟုတ် legal research စသည်တို့တွင် အမှန်တကယ်ဖြစ်စဉ်များကို အကြိမ်ကြိမ် စစ်ဆေးနိုင်သည်။
2. **Complex Database Interactions:** Structured data တွေကို ကိုင်တွယ်ရာတွင် query များကို ပြန်လည်ရေးသားနိုင်သည်။
3. **Extended Workflows:** အချိန်ကြာမြင့်တဲ့ session များတွင် Agentic RAG က အချက်အလက်အသစ်များကို ဆက်လက်ထည့်သွင်းနိုင်သည်။

## Governance, Transparency, နှင့် Trust

Agentic RAG စနစ်များမှာ reasoning ကို ရှင်းလင်းပြနိုင်မှု၊ bias control, နှင့် လူ့အကူအညီကို အရေးပါစွာ ထိန်းသိမ်းထားသည်။

## နိဂုံး

Agentic RAG က AI စနစ်များအတွက် data-intensive tasks များကို handle လုပ်ရာတွင် တိုးတက်မှုတစ်ခုဖြစ်သည်။ Static prompt-following ကို ကျော်လွန်ပြီး adaptive, context-aware decision-making ကို ဆောင်ရွက်နိုင်သည်။ 

### Agentic RAG အကြောင်း မေးမြန်းလိုပါသလား?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ကို ဝင်ရောက်ပြီး အခြားသော သင်ယူသူများနှင့် တွေ့ဆုံပါ၊ office hours တွေကို တက်ရောက်ပါ၊ နှင့် AI Agents အကြောင်း မေးမြန်းပါ။

## အပိုဆောင်းအရင်းအမြစ်များ

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Azure OpenAI Service ကို အသုံးပြု၍ Retrieval Augmented Generation (RAG) ကို အကောင်အထည်ဖော်ခြင်း: Azure OpenAI Service ကို သင့်ရဲ့ ကိုယ်ပိုင်ဒေတာနဲ့ ဘယ်လိုအသုံးပြုရမယ်ဆိုတာကို လေ့လာပါ။ ဒီ Microsoft Learn module က RAG ကို အကောင်အထည်ဖော်ဖို့ လမ်းညွှန်ချက်အပြည့်အစုံပေးထားပါတယ်  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Azure AI Foundry နဲ့ Generative AI အက်ပလီကေးရှင်းများကို အကဲဖြတ်ခြင်း: ဒီဆောင်းပါးမှာ Agentic AI အက်ပလီကေးရှင်းနဲ့ RAG အဆောက်အအုံများအပါအဝင်၊ အများပြည်သူရရှိနိုင်တဲ့ ဒေတာများပေါ်မှာ မော်ဒယ်များကို အကဲဖြတ်ခြင်းနဲ့ နှိုင်းယှဉ်ခြင်းကို ဖော်ပြထားပါတယ်</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Agentic RAG ဆိုတာဘာလဲ | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Agent-Based Retrieval Augmented Generation အတွက် လမ်းညွှန်ချက်အပြည့်အစုံ – News from generation RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: Query Reformulation နဲ့ Self-Query နဲ့အတူ RAG ကို အရှိန်မြှင့်ပါ! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">RAG အတွက် Agentic Layers ထည့်သွင်းခြင်း</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Knowledge Assistants ရဲ့ အနာဂတ်: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Agentic RAG Systems ဘယ်လိုတည်ဆောက်မလဲ</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Azure AI Foundry Agent Service ကို အသုံးပြုပြီး သင့် AI Agents ကို အရွယ်အစားကြီးစေခြင်း</a>  

### သုတေသနစာတမ်းများ  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Agentic RAG အပေါ် စစ်တမ်းတစ်ခု</a>  

## ယခင်သင်ခန်းစာ  

[Tool Use Design Pattern](../04-tool-use/README.md)  

## နောက်သင်ခန်းစာ  

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)  

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာပိုင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲအနားမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။