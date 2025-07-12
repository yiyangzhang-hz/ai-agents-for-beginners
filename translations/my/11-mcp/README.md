<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:51:34+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "my"
}
-->
# သင်ခန်းစာ ၁၁: Model Context Protocol (MCP) ပေါင်းစည်းခြင်း

## Model Context Protocol (MCP) အကြောင်းအရာမိတ်ဆက်

Model Context Protocol (MCP) သည် AI မော်ဒယ်များနှင့် client application များအကြား ဆက်သွယ်မှုများကို စံပြအတိုင်းအတာဖြင့် သတ်မှတ်ပေးရန် ရည်ရွယ်ထားသော နောက်ဆုံးပေါ် framework တစ်ခုဖြစ်သည်။ MCP သည် AI မော်ဒယ်များနှင့် ထိုမော်ဒယ်များကို အသုံးပြုသော application များအကြား တစ်မျိုးတည်းသော အင်တာဖေ့စ်ကို ပေးဆောင်ခြင်းဖြင့် မော်ဒယ်အမျိုးအစားမရွေး တူညီသော ဆက်သွယ်မှုကို အာမခံပေးသည်။

MCP ၏ အဓိကအချက်များမှာ -

- **စံပြ ဆက်သွယ်မှု** - MCP သည် application များနှင့် AI မော်ဒယ်များအကြား ဆက်သွယ်ရန် ပုံမှန်ဘာသာစကားတစ်ခုကို ဖန်တီးပေးသည်
- **အကြောင်းအရာ စီမံခန့်ခွဲမှု တိုးတက်မှု** - AI မော်ဒယ်များသို့ အကြောင်းအရာဆိုင်ရာ သတင်းအချက်အလက်များကို ထိရောက်စွာ ပေးပို့နိုင်စေသည်
- **Cross-platform ကိုက်ညီမှု** - C#, Java, JavaScript, Python, TypeScript စသည့် programming language များအတွင်း လုပ်ဆောင်နိုင်သည်
- **အဆင်ပြေစွာ ပေါင်းစည်းနိုင်မှု** - developer များအနေဖြင့် မတူညီသော AI မော်ဒယ်များကို လွယ်ကူစွာ application များထဲသို့ ပေါင်းစည်းနိုင်စေသည်

MCP သည် AI agent ဖွံ့ဖြိုးတိုးတက်မှုတွင် အထူးအသုံးဝင်ပြီး၊ agent များကို စနစ်များနှင့် ဒေတာရင်းမြစ်များအကြား တစ်ခုတည်းသော protocol ဖြင့် ဆက်သွယ်နိုင်စေခြင်းအားဖြင့် agent များကို ပိုမိုတိုးတက်ပြီး လွယ်ကူစွာ အသုံးပြုနိုင်စေသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ
- MCP ဆိုတာဘာလဲ၊ AI agent ဖွံ့ဖြိုးတိုးတက်မှုတွင် ၎င်း၏ အခန်းကဏ္ဍကို နားလည်ခြင်း
- GitHub ပေါင်းစည်းမှုအတွက် MCP server ကို တပ်ဆင်ပြင်ဆင်ခြင်း
- MCP tools အသုံးပြု၍ multi-agent စနစ်တည်ဆောက်ခြင်း
- Azure Cognitive Search ဖြင့် RAG (Retrieval Augmented Generation) ကို အကောင်အထည်ဖော်ခြင်း

## လိုအပ်ချက်များ
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub အကောင့်
- Semantic Kernel အခြေခံနားလည်မှု

## တပ်ဆင်ခြင်း လမ်းညွှန်ချက်များ

1. **ပတ်ဝန်းကျင် တပ်ဆင်ခြင်း**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure ဝန်ဆောင်မှုများ ပြင်ဆင်ခြင်း**
   - Azure Cognitive Search resource တည်ဆောက်ခြင်း
   - Azure OpenAI ဝန်ဆောင်မှု တပ်ဆင်ခြင်း
   - `.env` ဖိုင်တွင် ပတ်ဝန်းကျင် အပြောင်းအလဲများ သတ်မှတ်ခြင်း

3. **MCP Server တပ်ဆင်ခြင်း**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## ပရောဂျက် ဖွဲ့စည်းပုံ

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## အဓိက အစိတ်အပိုင်းများ

### ၁။ Multi-Agent စနစ်
- GitHub Agent: Repository စစ်တမ်းခွဲခြမ်းစိတ်ဖြာခြင်း
- Hackathon Agent: ပရောဂျက် အကြံပြုချက်များ
- Events Agent: နည်းပညာ အခမ်းအနား အကြံပြုချက်များ

### ၂။ Azure ပေါင်းစည်းမှု
- Event များ အညွှန်းပြုရန် Cognitive Search အသုံးပြုခြင်း
- Agent အတတ်ပညာအတွက် Azure OpenAI အသုံးပြုခြင်း
- RAG ပုံစံ အကောင်အထည်ဖော်ခြင်း

### ၃။ MCP Tools
- GitHub repository စစ်တမ်းခွဲခြမ်းစိတ်ဖြာခြင်း
- ကုဒ် စစ်ဆေးခြင်း
- Metadata ထုတ်ယူခြင်း

## ကုဒ် လမ်းညွှန်ချက်

ဥပမာတွင် ဖော်ပြထားသည်မှာ -
1. MCP server ပေါင်းစည်းခြင်း
2. Multi-agent စနစ် စီမံခန့်ခွဲခြင်း
3. Azure Cognitive Search ပေါင်းစည်းခြင်း
4. RAG ပုံစံ အကောင်အထည်ဖော်ခြင်း

အဓိက လက္ခဏာများ -
- အချိန်နှင့်တပြေးညီ GitHub repository စစ်တမ်းခွဲခြမ်းစိတ်ဖြာခြင်း
- အတတ်ပညာပြည့်ဝသော ပရောဂျက် အကြံပြုချက်များ
- Azure Search ဖြင့် အခမ်းအနား မျှတမှု
- Chainlit ဖြင့် Streaming တုံ့ပြန်မှုများ

## ဥပမာကို လည်ပတ်ခြင်း

အသေးစိတ် တပ်ဆင်ခြင်း လမ်းညွှန်ချက်များနှင့် အချက်အလက်များအတွက် [Github MCP Server Example README](./code_samples/github-mcp/README.md) ကို ကြည့်ပါ။

1. MCP server ကို စတင်ပါ -
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. အက်ပလီကေးရှင်းကို စတင်ပါ -
   ```bash
   chainlit run app.py -w
   ```

3. ပေါင်းစည်းမှုကို စမ်းသပ်ပါ -
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ပြဿနာဖြေရှင်းခြင်း

ရောဂါများနှင့် ဖြေရှင်းနည်းများ -
1. MCP ဆက်သွယ်မှု ပြဿနာများ
   - server လည်ပတ်နေမှုကို စစ်ဆေးပါ
   - port ရရှိနိုင်မှုကို စစ်ဆေးပါ
   - GitHub token များကို အတည်ပြုပါ

2. Azure Search ပြဿနာများ
   - ဆက်သွယ်မှု string များကို စစ်ဆေးပါ
   - index ရှိမှုကို စစ်ဆေးပါ
   - စာရွက်စာတမ်း တင်သွင်းမှုကို အတည်ပြုပါ

## နောက်တစ်ဆင့်များ
- MCP tools များ ပိုမိုလေ့လာပါ
- ကိုယ်ပိုင် agent များ ဖန်တီးပါ
- RAG စွမ်းဆောင်ရည်များ တိုးတက်စေပါ
- အခမ်းအနား ရင်းမြစ်များ ပိုမိုထည့်သွင်းပါ

## အရင်းအမြစ်များ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။