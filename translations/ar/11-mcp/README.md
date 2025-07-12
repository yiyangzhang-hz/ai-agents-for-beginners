<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:44:28+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ar"
}
-->
# الدرس 11: تكامل بروتوكول سياق النموذج (MCP)

## مقدمة في بروتوكول سياق النموذج (MCP)

بروتوكول سياق النموذج (MCP) هو إطار عمل متطور يهدف إلى توحيد التفاعلات بين نماذج الذكاء الاصطناعي وتطبيقات العملاء. يعمل MCP كجسر بين نماذج الذكاء الاصطناعي والتطبيقات التي تستخدمها، موفراً واجهة موحدة بغض النظر عن طريقة تنفيذ النموذج الأساسي.

الجوانب الرئيسية لـ MCP:

- **التواصل الموحد**: يحدد MCP لغة مشتركة لتواصل التطبيقات مع نماذج الذكاء الاصطناعي  
- **إدارة سياق محسنة**: يتيح تمرير المعلومات السياقية بكفاءة إلى نماذج الذكاء الاصطناعي  
- **التوافق عبر المنصات**: يعمل عبر لغات برمجة متعددة مثل C#، Java، JavaScript، Python، وTypeScript  
- **تكامل سلس**: يمكّن المطورين من دمج نماذج ذكاء اصطناعي مختلفة بسهولة في تطبيقاتهم  

يكتسب MCP أهمية خاصة في تطوير وكلاء الذكاء الاصطناعي حيث يسمح للوكلاء بالتفاعل مع أنظمة ومصادر بيانات متعددة من خلال بروتوكول موحد، مما يجعل الوكلاء أكثر مرونة وقوة.

## أهداف التعلم
- فهم ماهية MCP ودوره في تطوير وكلاء الذكاء الاصطناعي  
- إعداد وتكوين خادم MCP لتكامل GitHub  
- بناء نظام متعدد الوكلاء باستخدام أدوات MCP  
- تنفيذ RAG (التوليد المعزز بالاسترجاع) مع Azure Cognitive Search  

## المتطلبات الأساسية
- Python 3.8+  
- Node.js 14+  
- اشتراك Azure  
- حساب GitHub  
- فهم أساسي لـ Semantic Kernel  

## تعليمات الإعداد

1. **إعداد البيئة**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **تكوين خدمات Azure**  
   - إنشاء مورد Azure Cognitive Search  
   - إعداد خدمة Azure OpenAI  
   - تكوين متغيرات البيئة في `.env`  

3. **إعداد خادم MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## هيكل المشروع

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

## المكونات الأساسية

### 1. نظام متعدد الوكلاء  
- وكيل GitHub: تحليل المستودعات  
- وكيل Hackathon: توصيات المشاريع  
- وكيل الأحداث: اقتراحات فعاليات تقنية  

### 2. تكامل Azure  
- البحث المعرفي لفهرسة الفعاليات  
- Azure OpenAI لذكاء الوكلاء  
- تنفيذ نمط RAG  

### 3. أدوات MCP  
- تحليل مستودعات GitHub  
- فحص الكود  
- استخراج البيانات الوصفية  

## استعراض الكود

يعرض المثال التالي:  
1. تكامل خادم MCP  
2. تنسيق نظام متعدد الوكلاء  
3. تكامل Azure Cognitive Search  
4. تنفيذ نمط RAG  

الميزات الرئيسية:  
- تحليل مستودعات GitHub في الوقت الحقيقي  
- توصيات مشاريع ذكية  
- مطابقة الفعاليات باستخدام Azure Search  
- استجابات متدفقة مع Chainlit  

## تشغيل المثال

للحصول على تعليمات إعداد مفصلة ومزيد من المعلومات، راجع [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. ابدأ خادم MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. شغّل التطبيق:  
   ```bash
   chainlit run app.py -w
   ```

3. اختبر التكامل:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## استكشاف الأخطاء وإصلاحها

المشاكل الشائعة والحلول:  
1. مشاكل اتصال MCP  
   - تحقق من تشغيل الخادم  
   - تحقق من توفر المنفذ  
   - تأكد من صحة رموز GitHub  

2. مشاكل Azure Search  
   - تحقق من صحة سلاسل الاتصال  
   - تحقق من وجود الفهرس  
   - تحقق من رفع المستندات  

## الخطوات التالية
- استكشاف أدوات MCP إضافية  
- تنفيذ وكلاء مخصصين  
- تعزيز قدرات RAG  
- إضافة مصادر فعاليات أكثر  

## الموارد
- [MCP للمبتدئين](https://aka.ms/mcp-for-beginners)  
- [توثيق MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [توثيق Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [أدلة Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.