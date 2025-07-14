<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:20:19+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "ur"
}
-->
# Github MCP سرور کی مثال

## وضاحت

یہ ایک ڈیمو تھا جو Microsoft Reactor کے ذریعے منعقدہ AI Agents Hackathon کے لیے بنایا گیا تھا۔

یہ ٹول صارف کے Github ریپوز کی بنیاد پر ہیکاتھون پروجیکٹس کی سفارش کرنے کے لیے استعمال ہوتا ہے۔  
یہ کام درج ذیل طریقے سے کیا جاتا ہے:

1. **Github Agent** - Github MCP سرور کا استعمال کرتے ہوئے ریپوز اور ان ریپوز کی معلومات حاصل کرنا۔  
2. **Hackathon Agent** - Github Agent سے حاصل کردہ ڈیٹا کو لے کر صارف کے پروجیکٹس، استعمال شدہ زبانوں اور AI Agents ہیکاتھون کے پروجیکٹ ٹریکس کی بنیاد پر تخلیقی ہیکاتھون پروجیکٹ آئیڈیاز پیش کرنا۔  
3. **Events Agent** - ہیکاتھون ایجنٹس کی تجاویز کی بنیاد پر، Events Agent AI Agent Hackathon سیریز کے متعلقہ ایونٹس کی سفارش کرے گا۔  

## کوڈ چلانا

### ماحول کے متغیرات

یہ ڈیمو Azure Open AI Service، Semantic Kernel، Github MCP Server اور Azure AI Search استعمال کرتا ہے۔

ان ٹولز کو استعمال کرنے کے لیے یقینی بنائیں کہ آپ کے پاس مناسب ماحول کے متغیرات سیٹ ہیں:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Chainlit سرور چلانا

MCP سرور سے جڑنے کے لیے، یہ ڈیمو Chainlit کو چیٹ انٹرفیس کے طور پر استعمال کرتا ہے۔

سرور چلانے کے لیے، اپنے ٹرمینل میں درج ذیل کمانڈ استعمال کریں:

```bash
chainlit run app.py -w
```

اس سے آپ کا Chainlit سرور `localhost:8000` پر شروع ہو جائے گا اور ساتھ ہی آپ کے Azure AI Search انڈیکس میں `event-descriptions.md` کا مواد شامل ہو جائے گا۔

## MCP سرور سے کنیکٹ ہونا

Github MCP سرور سے جڑنے کے لیے، "Type your message here.." چیٹ باکس کے نیچے موجود "plug" آئیکن کو منتخب کریں:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.ur.png)

وہاں سے آپ "Connect an MCP" پر کلک کر کے Github MCP سرور سے جڑنے کا کمانڈ شامل کر سکتے ہیں:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" کو اپنے اصل Personal Access Token سے تبدیل کریں۔

کنیکٹ ہونے کے بعد، آپ کو plug آئیکن کے ساتھ (1) نظر آئے گا جو کنکشن کی تصدیق کرے گا۔ اگر ایسا نہ ہو تو، `chainlit run app.py -w` کے ساتھ chainlit سرور کو دوبارہ شروع کرنے کی کوشش کریں۔

## ڈیمو کا استعمال

ہیکاتھون پروجیکٹس کی سفارش کے ایجنٹ ورک فلو کو شروع کرنے کے لیے، آپ اس طرح کا پیغام لکھ سکتے ہیں:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent آپ کی درخواست کا تجزیہ کرے گا اور فیصلہ کرے گا کہ کون سے ایجنٹس (GitHub، Hackathon، اور Events) کا مجموعہ آپ کی درخواست کو سنبھالنے کے لیے سب سے مناسب ہے۔ ایجنٹس مل کر GitHub ریپوزٹری کے تجزیے، پروجیکٹ آئیڈیاز، اور متعلقہ ٹیک ایونٹس کی بنیاد پر جامع سفارشات فراہم کرتے ہیں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔