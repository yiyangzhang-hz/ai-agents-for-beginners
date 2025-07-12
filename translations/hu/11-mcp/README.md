<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:50:07+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hu"
}
-->
# 11. Lecke: Model Context Protocol (MCP) Integráció

## Bevezetés a Model Context Protocol (MCP) témakörébe

A Model Context Protocol (MCP) egy korszerű keretrendszer, amely az AI modellek és a kliensalkalmazások közötti interakciók szabványosítására szolgál. Az MCP hidat képez az AI modellek és az azokat használó alkalmazások között, egységes felületet biztosítva a mögöttes modell megvalósításától függetlenül.

Az MCP főbb jellemzői:

- **Szabványosított kommunikáció**: Az MCP közös nyelvet teremt az alkalmazások és az AI modellek közötti kommunikációhoz
- **Fejlett kontextuskezelés**: Hatékony módot kínál a kontextuális információk átadására az AI modelleknek
- **Platformok közötti kompatibilitás**: Több programozási nyelven működik, többek között C#, Java, JavaScript, Python és TypeScript
- **Zökkenőmentes integráció**: Lehetővé teszi a fejlesztők számára, hogy könnyedén integráljanak különböző AI modelleket alkalmazásaikba

Az MCP különösen hasznos az AI ügynökök fejlesztésében, mivel lehetővé teszi, hogy az ügynökök egységes protokollon keresztül kommunikáljanak különböző rendszerekkel és adatforrásokkal, így rugalmasabbá és hatékonyabbá téve őket.

## Tanulási célok
- Megérteni, mi az MCP és milyen szerepet tölt be az AI ügynökök fejlesztésében
- MCP szerver beállítása és konfigurálása GitHub integrációhoz
- Többügynökös rendszer építése MCP eszközökkel
- RAG (Retrieval Augmented Generation) megvalósítása Azure Cognitive Search segítségével

## Előfeltételek
- Python 3.8 vagy újabb
- Node.js 14 vagy újabb
- Azure előfizetés
- GitHub fiók
- Alapvető ismeretek a Semantic Kernelről

## Beállítási útmutató

1. **Környezet beállítása**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure szolgáltatások konfigurálása**  
   - Hozz létre egy Azure Cognitive Search erőforrást  
   - Állítsd be az Azure OpenAI szolgáltatást  
   - Konfiguráld a környezeti változókat a `.env` fájlban

3. **MCP szerver beállítása**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projekt struktúrája

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

## Főbb komponensek

### 1. Többügynökös rendszer
- GitHub Agent: Tárolóelemzés  
- Hackathon Agent: Projektajánlások  
- Events Agent: Technológiai események ajánlása

### 2. Azure integráció
- Cognitive Search az események indexeléséhez  
- Azure OpenAI az ügynök intelligenciájához  
- RAG minta megvalósítása

### 3. MCP eszközök
- GitHub tárolóelemzés  
- Kódellenőrzés  
- Metaadat kinyerés

## Kód bemutató

A példa bemutatja:  
1. MCP szerver integrációját  
2. Többügynökös koordinációt  
3. Azure Cognitive Search integrációt  
4. RAG minta megvalósítását

Főbb jellemzők:  
- Valós idejű GitHub tárolóelemzés  
- Intelligens projektajánlások  
- Események párosítása Azure Search segítségével  
- Streaming válaszok Chainlit használatával

## A minta futtatása

Részletes beállítási útmutatóért és további információkért lásd a [Github MCP Server Example README](./code_samples/github-mcp/README.md) fájlt.

1. Indítsd el az MCP szervert:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Indítsd el az alkalmazást:  
   ```bash
   chainlit run app.py -w
   ```

3. Teszteld az integrációt:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Hibakeresés

Gyakori problémák és megoldások:  
1. MCP kapcsolódási problémák  
   - Ellenőrizd, hogy a szerver fut-e  
   - Nézd meg, hogy a port szabad-e  
   - Ellenőrizd a GitHub tokeneket

2. Azure Search problémák  
   - Érvényesítsd a kapcsolati karakterláncokat  
   - Ellenőrizd, hogy az index létezik-e  
   - Győződj meg a dokumentum feltöltéséről

## Következő lépések
- Fedezd fel az MCP további eszközeit  
- Valósíts meg egyedi ügynököket  
- Fejleszd tovább a RAG képességeket  
- Adj hozzá több eseményforrást

## Források
- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search dokumentáció](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel útmutatók](https://learn.microsoft.com/semantic-kernel/)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.