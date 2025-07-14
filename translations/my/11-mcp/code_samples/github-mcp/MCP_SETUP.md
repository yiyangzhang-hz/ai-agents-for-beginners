<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:19:08+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "my"
}
-->
# MCP Server ပေါင်းစည်းခြင်းလမ်းညွှန်

## မလိုအပ်သောအချက်များ  
- Node.js တပ်ဆင်ထားပြီး (ဗားရှင်း 14 သို့မဟုတ်အထက်)  
- npm package manager  
- လိုအပ်သော dependencies များပါဝင်သော Python ပတ်ဝန်းကျင်  

## တပ်ဆင်ခြင်းအဆင့်များ  

1. **MCP Server Package ကို တပ်ဆင်ပါ**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```  

2. **MCP Server ကို စတင်ပါ**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   ဆာဗာသည် စတင်ပြီး ချိတ်ဆက်ရန် URL ကို ပြသသင့်သည်။  

3. **ချိတ်ဆက်မှုကို စစ်ဆေးပါ**  
   - Chainlit အင်တာဖေ့စ်တွင် plug icon (🔌) ကို ရှာပါ  
   - plug icon အနားတွင် (1) ဆိုသော နံပါတ်တစ်ခု ပေါ်လာရမည်၊ ချိတ်ဆက်မှုအောင်မြင်ကြောင်းပြသည်  
   - console တွင် "GitHub plugin setup completed successfully" (အခြား status များနှင့်အတူ) ပြသသင့်သည်  

## ပြဿနာဖြေရှင်းခြင်း  

### ပုံမှန်ပြဿနာများ  

1. **Port တစ်ခုတည်းသုံးနေခြင်း**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   ဖြေရှင်းနည်း - port ကို အောက်ပါအတိုင်း ပြောင်းပါ။  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```  

2. **အတည်ပြုမှု ပြဿနာများ**  
   - GitHub အချက်အလက်များကို မှန်ကန်စွာ ပြင်ဆင်ထားပါ  
   - .env ဖိုင်တွင် လိုအပ်သော token များပါဝင်မှုကို စစ်ဆေးပါ  
   - GitHub API သို့ ဝင်ရောက်ခွင့်ရှိမှုကို အတည်ပြုပါ  

3. **ချိတ်ဆက်မှု မအောင်မြင်ခြင်း**  
   - ဆာဗာသည် မျှော်မှန်းထားသော port တွင် လည်ပတ်နေမှုကို အတည်ပြုပါ  
   - firewall ဆက်တင်များကို စစ်ဆေးပါ  
   - Python ပတ်ဝန်းကျင်တွင် လိုအပ်သော package များ ရှိမှုကို အတည်ပြုပါ  

## ချိတ်ဆက်မှု အတည်ပြုခြင်း  

သင့် MCP server သည် အောက်ပါအတိုင်း ချိတ်ဆက်မှုမှန်ကန်သည်။  
1. Console တွင် "GitHub plugin setup completed successfully" ပြသသည်  
2. ချိတ်ဆက်မှု မှတ်တမ်းများတွင် "✓ MCP Connection Status: Active" ပြသသည်  
3. GitHub command များကို chat interface တွင် အသုံးပြုနိုင်သည်  

## ပတ်ဝန်းကျင် အပြောင်းအလဲများ  

သင့် .env ဖိုင်တွင် လိုအပ်သည်။  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```  

## ချိတ်ဆက်မှု စမ်းသပ်ခြင်း  

chat တွင် စမ်းသပ်မက်ဆေ့ခ်ျကို ပို့ပါ။  
```
Show me the repositories for username: [GitHub Username]
```  
အောင်မြင်သော တုံ့ပြန်ချက်တွင် repository အချက်အလက်များ ပြသမည်ဖြစ်သည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။