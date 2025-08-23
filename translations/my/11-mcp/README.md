<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T14:07:24+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "my"
}
-->
# အခန်း ၁၁: Model Context Protocol (MCP) ပေါင်းစည်းမှု

## Model Context Protocol (MCP) ကိုမိတ်ဆက်ခြင်း

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client အက်ပလီကေးရှင်းများအကြား အပြန်အလှန်ဆက်သွယ်မှုများကို စံပြုလုပ်ရန် ရည်ရွယ်ထားသော နောက်ဆုံးပေါ် framework တစ်ခုဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် အက်ပလီကေးရှင်းများအကြား တစ်ခုတည်းသော interface ကို ပေးစွမ်းပြီး မော်ဒယ်အကောင်အထည်မည်သည့်ပုံစံဖြစ်စေ မျှတစွာ ဆက်သွယ်နိုင်စေသည်။

MCP ၏ အဓိကအချက်များ:

- **စံပြုဆက်သွယ်မှု**: MCP သည် AI မော်ဒယ်များနှင့် အက်ပလီကေးရှင်းများအကြား ဆက်သွယ်ရန် တစ်ခုတည်းသော ဘာသာစကားကို ဖန်တီးပေးသည်
- **အကြောင်းအရာစီမံခန့်ခွဲမှုတိုးတက်မှု**: AI မော်ဒယ်များသို့ အကြောင်းအရာဆိုင်ရာ အချက်အလက်များကို ထိရောက်စွာ ပေးပို့နိုင်စေသည်
- **Cross-platform ကိုက်ညီမှု**: C#, Java, JavaScript, Python, TypeScript စသည်တို့အပါအဝင် အမျိုးမျိုးသော programming language များတွင် အသုံးပြုနိုင်သည်
- **ရိုးရှင်းသောပေါင်းစည်းမှု**: Developer များအတွက် မတူကွဲပြားသော AI မော်ဒယ်များကို အက်ပလီကေးရှင်းများတွင် လွယ်ကူစွာ ပေါင်းစည်းနိုင်စေသည်

MCP သည် အထူးသဖြင့် AI agent ဖွံ့ဖြိုးတိုးတက်မှုတွင် အထူးတန်ဖိုးရှိပြီး agent များကို စနစ်များနှင့် ဒေတာအရင်းအမြစ်များနှင့် တစ်ခုတည်းသော protocol မှတစ်ဆင့် ဆက်သွယ်နိုင်စေသည်။ ဒါက agent များကို ပိုမိုတက်ကြွပြီး အင်အားကြီးစေသည်။

## သင်ယူရမည့်အချက်များ
- MCP ဆိုတာဘာလဲ၊ AI agent ဖွံ့ဖြိုးတိုးတက်မှုတွင် ၎င်း၏บทบาทကိုနားလည်ခြင်း
- GitHub ပေါင်းစည်းမှုအတွက် MCP server ကို စတင်ပြီး configuration ပြုလုပ်ခြင်း
- MCP tools အသုံးပြု၍ multi-agent system တစ်ခုတည်ဆောက်ခြင်း
- Azure Cognitive Search ဖြင့် RAG (Retrieval Augmented Generation) ကို အကောင်အထည်ဖော်ခြင်း

## လိုအပ်ချက်များ
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Semantic Kernel အခြေခံနားလည်မှု

## Setup လုပ်နည်းများ

1. **ပတ်ဝန်းကျင် Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure Services ကို Configure လုပ်ခြင်း**
   - Azure Cognitive Search resource တစ်ခုဖန်တီးပါ
   - Azure OpenAI service ကို setup လုပ်ပါ
   - `.env` တွင် environment variables များကို configure လုပ်ပါ

3. **MCP Server Setup**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project ဖွဲ့စည်းပုံ

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## အဓိကအစိတ်အပိုင်းများ

### ၁. Multi-Agent System
- GitHub Agent: Repository ကိုခွဲခြမ်းစိတ်ဖြာခြင်း
- Hackathon Agent: Project အကြံပြုချက်များ
- Events Agent: နည်းပညာဆိုင်ရာ event အကြံပြုချက်များ

### ၂. Azure Integration
- Event indexing အတွက် Cognitive Search
- Agent intelligence အတွက် Azure OpenAI
- RAG pattern အကောင်အထည်ဖော်ခြင်း

### ၃. MCP Tools
- GitHub repository ခွဲခြမ်းစိတ်ဖြာခြင်း
- Code inspection
- Metadata extraction

## Code Walkthrough

ဒီနမူနာမှာ ဖော်ပြထားတာတွေက:
1. MCP server integration
2. Multi-agent orchestration
3. Azure Cognitive Search integration
4. RAG pattern အကောင်အထည်ဖော်ခြင်း

အဓိက features:
- GitHub repository ကို အချိန်နှင့်တပြေးညီ ခွဲခြမ်းစိတ်ဖြာခြင်း
- Project အကြံပြုချက်များ
- Azure Search ကို အသုံးပြု၍ Event ကို ကိုက်ညီစေခြင်း
- Chainlit ဖြင့် Streaming responses

## နမူနာကို Run လုပ်ခြင်း

Setup လုပ်နည်းများနှင့် အခြားအချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ရှုပါ။

1. MCP server ကို စတင်ပါ:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Application ကို စတင်ပါ:
   ```bash
   chainlit run app.py -w
   ```

3. Integration ကို စမ်းသပ်ပါ:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Troubleshooting

အများဆုံးဖြစ်နိုင်သောပြဿနာများနှင့် ဖြေရှင်းနည်းများ:
1. MCP Connection Issues
   - Server ရှိ/မရှိ စစ်ဆေးပါ
   - Port ရရှိနိုင်မှု စစ်ဆေးပါ
   - GitHub tokens ကို အတည်ပြုပါ

2. Azure Search Issues
   - Connection strings ကို စစ်ဆေးပါ
   - Index ရှိ/မရှိ စစ်ဆေးပါ
   - Document upload ကို အတည်ပြုပါ

## နောက်တစ်ဆင့်
- MCP tools များကို ထပ်မံလေ့လာပါ
- Custom agents များကို အကောင်အထည်ဖော်ပါ
- RAG စွမ်းဆောင်ရည်များကို တိုးတက်စေပါ
- Event sources များကို ထပ်မံထည့်သွင်းပါ
- **အဆင့်မြင့်**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) တွင် agent-to-agent ဆက်သွယ်မှုနမူနာများကို ကြည့်ပါ

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။