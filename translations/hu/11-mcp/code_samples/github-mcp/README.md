<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:24:15+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "hu"
}
-->
# Github MCP Server példa

## Leírás

Ez egy demó volt, amelyet az AI Agents Hackathonra készítettek a Microsoft Reactor keretében.

Az eszköz arra szolgál, hogy hackathon projektek ajánlását végezze egy felhasználó Github tárolói alapján.  
Ez a következőképpen történik:

1. **Github Agent** – A Github MCP Server segítségével lekéri a tárolókat és azok adatait.  
2. **Hackathon Agent** – A Github Agent által szolgáltatott adatokból kreatív hackathon projektötleteket generál a felhasználó projektjei, használt programozási nyelvei és az AI Agents hackathon projektkategóriái alapján.  
3. **Events Agent** – A hackathon agent javaslatai alapján az events agent releváns eseményeket ajánl az AI Agent Hackathon sorozatból.

## A kód futtatása

### Környezeti változók

Ez a demó az Azure Open AI Service-t, a Semantic Kernel-t, a Github MCP Servert és az Azure AI Search-t használja.

Győződj meg róla, hogy a megfelelő környezeti változók be vannak állítva ezekhez az eszközökhöz:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## A Chainlit Server indítása

Az MCP szerverhez való kapcsolódáshoz ez a demó a Chainlit-et használja chat felületként.

A szerver indításához futtasd a következő parancsot a terminálban:

```bash
chainlit run app.py -w
```

Ez elindítja a Chainlit szerveredet a `localhost:8000` címen, valamint feltölti az Azure AI Search indexet az `event-descriptions.md` tartalmával.

## Kapcsolódás az MCP Serverhez

A Github MCP Serverhez való kapcsolódáshoz válaszd ki a "dugasz" ikont a "Type your message here.." chat mező alatt:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.hu.png)

Innen kattints a "Connect an MCP" gombra, hogy hozzáadd a parancsot a Github MCP Serverhez való kapcsolódáshoz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Cseréld le a "[YOUR PERSONAL ACCESS TOKEN]" részt a saját személyes hozzáférési tokenedre.

A kapcsolódás után a dugasz ikon mellett meg kell jelennie egy (1)-es számnak, ami megerősíti a kapcsolatot. Ha nem, próbáld meg újraindítani a chainlit szervert a `chainlit run app.py -w` paranccsal.

## A demó használata

A hackathon projektek ajánlási folyamatának elindításához írj be egy üzenetet, például:

"Recommend hackathon projects for the Github user koreyspace"

A Router Agent elemzi a kérésedet, és eldönti, hogy melyik agent kombináció (GitHub, Hackathon és Events) a legalkalmasabb a lekérdezésed kezelésére. Az ügynökök együttműködve nyújtanak átfogó ajánlásokat a GitHub tárolók elemzése, projektötlet generálás és releváns technológiai események alapján.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.