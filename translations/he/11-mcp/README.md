<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:49:05+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "he"
}
-->
# שיעור 11: אינטגרציה של Model Context Protocol (MCP)

## מבוא ל-Model Context Protocol (MCP)

Model Context Protocol (MCP) הוא מסגרת מתקדמת שנועדה לאחד את האינטראקציות בין מודלים של בינה מלאכותית ליישומים של לקוחות. MCP משמשת כגשר בין מודלים של בינה מלאכותית ליישומים שמשתמשים בהם, ומספקת ממשק אחיד ללא תלות במימוש הבסיסי של המודל.

היבטים מרכזיים של MCP:

- **תקשורת סטנדרטית**: MCP מגדירה שפה משותפת ליישומים לתקשר עם מודלים של בינה מלאכותית  
- **ניהול הקשר משופר**: מאפשרת העברת מידע הקשרי בצורה יעילה למודלים  
- **תאימות בין פלטפורמות**: פועלת בשפות תכנות שונות כולל C#, Java, JavaScript, Python ו-TypeScript  
- **אינטגרציה חלקה**: מאפשרת למפתחים לשלב בקלות מודלים שונים של בינה מלאכותית ביישומיהם  

MCP בעלת ערך מיוחד בפיתוח סוכני בינה מלאכותית, שכן היא מאפשרת לסוכנים לתקשר עם מערכות ומקורות נתונים שונים דרך פרוטוקול אחיד, מה שהופך את הסוכנים לגמישים ועוצמתיים יותר.

## מטרות הלמידה
- להבין מהו MCP ותפקידו בפיתוח סוכני בינה מלאכותית  
- להקים ולהגדיר שרת MCP לאינטגרציה עם GitHub  
- לבנות מערכת רב-סוכנית באמצעות כלי MCP  
- ליישם RAG (Retrieval Augmented Generation) עם Azure Cognitive Search  

## דרישות מוקדמות
- Python 3.8 ומעלה  
- Node.js 14 ומעלה  
- מנוי Azure  
- חשבון GitHub  
- הבנה בסיסית של Semantic Kernel  

## הוראות התקנה

1. **הגדרת הסביבה**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **הגדרת שירותי Azure**  
   - יצירת משאב Azure Cognitive Search  
   - הקמת שירות Azure OpenAI  
   - הגדרת משתני סביבה בקובץ `.env`  

3. **הקמת שרת MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## מבנה הפרויקט

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

## רכיבים מרכזיים

### 1. מערכת רב-סוכנית  
- סוכן GitHub: ניתוח מאגרי קוד  
- סוכן Hackathon: המלצות לפרויקטים  
- סוכן Events: הצעות לאירועי טכנולוגיה  

### 2. אינטגרציה עם Azure  
- Cognitive Search לאינדוקס אירועים  
- Azure OpenAI לאינטליגנציה של הסוכנים  
- יישום דפוס RAG  

### 3. כלי MCP  
- ניתוח מאגרי GitHub  
- בדיקת קוד  
- חילוץ מטא-דאטה  

## סקירת הקוד

הדוגמה ממחישה:  
1. אינטגרציה עם שרת MCP  
2. תיאום בין סוכנים מרובים  
3. אינטגרציה עם Azure Cognitive Search  
4. יישום דפוס RAG  

תכונות מרכזיות:  
- ניתוח בזמן אמת של מאגרי GitHub  
- המלצות חכמות לפרויקטים  
- התאמת אירועים באמצעות Azure Search  
- תגובות בזרם עם Chainlit  

## הפעלת הדוגמה

להוראות התקנה מפורטות ומידע נוסף, עיינו ב-[Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. הפעלת שרת MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. הפעלת היישום:  
   ```bash
   chainlit run app.py -w
   ```

3. בדיקת האינטגרציה:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## פתרון תקלות

בעיות נפוצות ופתרונות:  
1. בעיות חיבור ל-MCP  
   - ודאו שהשרת פועל  
   - בדקו זמינות פורט  
   - אשרו את אסימוני GitHub  

2. בעיות ב-Azure Search  
   - אימות מחרוזות חיבור  
   - בדיקת קיום אינדקס  
   - אימות העלאת מסמכים  

## צעדים הבאים
- חקר כלי MCP נוספים  
- יישום סוכנים מותאמים אישית  
- שיפור יכולות RAG  
- הוספת מקורות אירועים נוספים  

## משאבים
- [MCP למתחילים](https://aka.ms/mcp-for-beginners)  
- [תיעוד MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [תיעוד Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [מדריכי Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.