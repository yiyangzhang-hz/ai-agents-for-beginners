<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:29+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "he"
}
-->
# מדריך אינטגרציה לשרת MCP

## דרישות מוקדמות
- התקנת Node.js (גרסה 14 ומעלה)
- מנהל החבילות npm
- סביבת Python עם התלויות הנדרשות

## שלבי ההתקנה

1. **התקנת חבילת MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **הפעלת שרת MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   השרת אמור להתחיל ולהציג כתובת URL לחיבור.

3. **אימות החיבור**  
   - חפש את סמל השקע (🔌) בממשק Chainlit שלך  
   - מספר (1) אמור להופיע ליד סמל השקע, מה שמעיד על חיבור מוצלח  
   - הקונסולה תציג: "GitHub plugin setup completed successfully" (יחד עם שורות סטטוס נוספות)

## פתרון בעיות

### בעיות נפוצות

1. **קונפליקט פורט**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   פתרון: שנה את הפורט באמצעות:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **בעיות אימות**  
   - ודא שפרטי ההתחברות ל-GitHub מוגדרים כראוי  
   - בדוק שקובץ .env מכיל את הטוקנים הנדרשים  
   - אמת גישה ל-API של GitHub

3. **החיבור נכשל**  
   - ודא שהשרת רץ על הפורט הצפוי  
   - בדוק את הגדרות חומת האש  
   - אמת שסביבת Python כוללת את החבילות הנדרשות

## אימות החיבור

שרת MCP שלך מחובר כראוי כאשר:  
1. הקונסולה מציגה "GitHub plugin setup completed successfully"  
2. יומני החיבור מציגים "✓ MCP Connection Status: Active"  
3. פקודות GitHub פועלות בממשק הצ'אט

## משתני סביבה

נדרשים בקובץ .env שלך:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## בדיקת חיבור

שלח את הודעת הבדיקה הזו בצ'אט:  
```
Show me the repositories for username: [GitHub Username]
```  
תגובה מוצלחת תציג מידע על המאגר.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.