<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:44:50+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ur"
}
-->
# سبق 11: ماڈل کانٹیکسٹ پروٹوکول (MCP) انٹیگریشن

## ماڈل کانٹیکسٹ پروٹوکول (MCP) کا تعارف

ماڈل کانٹیکسٹ پروٹوکول (MCP) ایک جدید فریم ورک ہے جو AI ماڈلز اور کلائنٹ ایپلیکیشنز کے درمیان تعاملات کو معیاری بنانے کے لیے ڈیزائن کیا گیا ہے۔ MCP AI ماڈلز اور ان ایپلیکیشنز کے درمیان ایک پل کا کام دیتا ہے جو انہیں استعمال کرتی ہیں، اور ماڈل کی بنیادی عمل درآمد سے قطع نظر ایک مستقل انٹرفیس فراہم کرتا ہے۔

MCP کے اہم پہلو:

- **معیاری مواصلات**: MCP ایپلیکیشنز کو AI ماڈلز سے بات چیت کرنے کے لیے ایک مشترکہ زبان فراہم کرتا ہے  
- **بہتر کانٹیکسٹ مینجمنٹ**: AI ماڈلز کو سیاق و سباق کی معلومات مؤثر طریقے سے منتقل کرنے کی اجازت دیتا ہے  
- **کراس-پلیٹ فارم مطابقت**: مختلف پروگرامنگ زبانوں جیسے C#, Java, JavaScript, Python، اور TypeScript میں کام کرتا ہے  
- **بغیر رکاوٹ انٹیگریشن**: ڈویلپرز کو مختلف AI ماڈلز کو اپنی ایپلیکیشنز میں آسانی سے شامل کرنے کے قابل بناتا ہے  

MCP خاص طور پر AI ایجنٹ کی ترقی میں قیمتی ہے کیونکہ یہ ایجنٹس کو مختلف نظاموں اور ڈیٹا ذرائع کے ساتھ ایک متحد پروٹوکول کے ذریعے بات چیت کرنے کی اجازت دیتا ہے، جس سے ایجنٹس زیادہ لچکدار اور طاقتور بن جاتے ہیں۔

## سیکھنے کے مقاصد
- MCP کیا ہے اور AI ایجنٹ کی ترقی میں اس کا کردار سمجھنا  
- GitHub انٹیگریشن کے لیے MCP سرور کی ترتیب اور کنفیگریشن  
- MCP ٹولز کا استعمال کرتے ہوئے ملٹی-ایجنٹ سسٹم بنانا  
- Azure Cognitive Search کے ساتھ RAG (Retrieval Augmented Generation) کو نافذ کرنا  

## ضروریات
- Python 3.8+  
- Node.js 14+  
- Azure سبسکرپشن  
- GitHub اکاؤنٹ  
- Semantic Kernel کی بنیادی سمجھ  

## سیٹ اپ کی ہدایات

1. **ماحول کی ترتیب**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure سروسز کی کنفیگریشن**  
   - Azure Cognitive Search ریسورس بنائیں  
   - Azure OpenAI سروس سیٹ اپ کریں  
   - `.env` میں ماحول کے متغیرات ترتیب دیں  

3. **MCP سرور کی ترتیب**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## پروجیکٹ کی ساخت

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

## بنیادی اجزاء

### 1. ملٹی-ایجنٹ سسٹم  
- GitHub ایجنٹ: ریپوزیٹری کا تجزیہ  
- Hackathon ایجنٹ: پروجیکٹ کی سفارشات  
- Events ایجنٹ: ٹیک ایونٹس کی تجاویز  

### 2. Azure انٹیگریشن  
- ایونٹس کی انڈیکسنگ کے لیے Cognitive Search  
- ایجنٹ کی ذہانت کے لیے Azure OpenAI  
- RAG پیٹرن کی نفاذ  

### 3. MCP ٹولز  
- GitHub ریپوزیٹری کا تجزیہ  
- کوڈ کا معائنہ  
- میٹا ڈیٹا نکالنا  

## کوڈ کا جائزہ

نمونہ درج ذیل دکھاتا ہے:  
1. MCP سرور کی انٹیگریشن  
2. ملٹی-ایجنٹ کی ہم آہنگی  
3. Azure Cognitive Search کی انٹیگریشن  
4. RAG پیٹرن کی نفاذ  

اہم خصوصیات:  
- حقیقی وقت میں GitHub ریپوزیٹری کا تجزیہ  
- ذہین پروجیکٹ کی سفارشات  
- Azure Search کے ذریعے ایونٹ میچنگ  
- Chainlit کے ساتھ اسٹریمنگ جوابات  

## نمونہ چلانا

تفصیلی سیٹ اپ ہدایات اور مزید معلومات کے لیے، [Github MCP Server Example README](./code_samples/github-mcp/README.md) ملاحظہ کریں۔

1. MCP سرور شروع کریں:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. ایپلیکیشن لانچ کریں:  
   ```bash
   chainlit run app.py -w
   ```

3. انٹیگریشن کی جانچ کریں:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## مسائل کا حل

عام مسائل اور ان کے حل:  
1. MCP کنکشن کے مسائل  
   - سرور چل رہا ہے اس کی تصدیق کریں  
   - پورٹ کی دستیابی چیک کریں  
   - GitHub ٹوکنز کی تصدیق کریں  

2. Azure Search کے مسائل  
   - کنکشن سٹرنگز کی تصدیق کریں  
   - انڈیکس کی موجودگی چیک کریں  
   - دستاویزات کی اپ لوڈ کی تصدیق کریں  

## اگلے اقدامات
- مزید MCP ٹولز دریافت کریں  
- کسٹم ایجنٹس نافذ کریں  
- RAG صلاحیتوں کو بہتر بنائیں  
- مزید ایونٹ ذرائع شامل کریں  

## وسائل
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔