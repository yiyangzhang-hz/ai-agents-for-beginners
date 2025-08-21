<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-21T14:52:22+00:00",
  "source_file": "11-mcp/code_samples/mcp-agents/README.md",
  "language_code": "hu"
}
-->
# Agent-to-Agent Kommunikációs Rendszerek Építése MCP-vel

> Röviden - Lehet MCP-n Agent2Agent Kommunikációt építeni? Igen!

Az MCP jelentősen túllépett eredeti célján, amely az "LLM-ek kontextusának biztosítása" volt. Az új fejlesztések, mint például a [folytatható streamek](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [kikérdezés](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [mintavétel](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling), és értesítések ([haladás](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) és [erőforrások](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)) révén az MCP most már szilárd alapot nyújt komplex agent-to-agent kommunikációs rendszerek építéséhez.

## Az Agent/Tool Téveszme

Ahogy egyre több fejlesztő fedezi fel az agentikus viselkedésű eszközöket (hosszú ideig futnak, közben további bemenetet igényelhetnek stb.), gyakori tévhit, hogy az MCP nem alkalmas erre, főként azért, mert korai példái az eszközök primitívjeinek egyszerű kérés-válasz mintákra összpontosítottak.

Ez a nézet elavult. Az MCP specifikációt az elmúlt hónapokban jelentősen kibővítették olyan képességekkel, amelyek lehetővé teszik a hosszú távú agentikus viselkedés megvalósítását:

- **Streaming és Részleges Eredmények**: Valós idejű haladás frissítések a végrehajtás során
- **Folytathatóság**: Az ügyfelek újra csatlakozhatnak és folytathatják a megszakítás után
- **Tartósság**: Az eredmények túlélnek szerver újraindításokat (pl. erőforrás linkek révén)
- **Többfordulós**: Interaktív bemenet a végrehajtás közben kikérdezés és mintavétel révén

Ezek a funkciók kombinálhatók komplex agentikus és több agentet magában foglaló alkalmazások létrehozására, mindezt az MCP protokollon belül.

Referenciaként az agentet "eszközként" fogjuk említeni, amely elérhető egy MCP szerveren. Ez magában foglalja egy host alkalmazás létezését, amely megvalósít egy MCP klienst, amely kapcsolatot létesít az MCP szerverrel és hívhatja az agentet.

## Mi Teszi Az MCP Eszközt "Agentikussá"?

Mielőtt belevágnánk a megvalósításba, határozzuk meg, milyen infrastruktúra képességekre van szükség a hosszú távú agentek támogatásához.

> Az agentet olyan entitásként definiáljuk, amely képes önállóan működni hosszabb időn keresztül, komplex feladatokat kezelve, amelyek több interakciót vagy valós idejű visszajelzés alapján történő módosítást igényelhetnek.

### 1. Streaming és Részleges Eredmények

A hagyományos kérés-válasz minták nem működnek hosszú távú feladatok esetén. Az agenteknek biztosítaniuk kell:

- Valós idejű haladás frissítéseket
- Köztes eredményeket

**MCP Támogatás**: Az erőforrás frissítési értesítések lehetővé teszik a részleges eredmények streamelését, bár ez gondos tervezést igényel, hogy elkerüljük az ütközéseket a JSON-RPC 1:1 kérés/válasz modelljével.

| Funkció                    | Használati Példa                                                                                                                                                                       | MCP Támogatás                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Valós idejű Haladás Frissítések | A felhasználó kér egy kódalap migrációs feladatot. Az agent streameli a haladást: "10% - Függőségek elemzése... 25% - TypeScript fájlok konvertálása... 50% - Importok frissítése..." | ✅ Haladás értesítések                                                                  |
| Részleges Eredmények            | "Könyv generálása" feladat streameli a részleges eredményeket, pl. 1) Történetív vázlat, 2) Fejezet lista, 3) Minden fejezet, ahogy elkészül. A host bármelyik szakaszban ellenőrizheti, törölheti vagy átirányíthatja. | ✅ Értesítések "kiterjeszthetők" részleges eredményekkel, lásd javaslatok PR 383, 776 |

### 2. Folytathatóság

Az agenteknek képesnek kell lenniük a hálózati megszakítások kezelésére:

- Újra csatlakozás (ügyfél) megszakítás után
- Folytatás ott, ahol abbahagyták (üzenet újraküldés)

**MCP Támogatás**: Az MCP StreamableHTTP transport ma támogatja a session folytatást és üzenet újraküldést session ID-k és utolsó esemény ID-k segítségével. Fontos megjegyezni, hogy a szervernek implementálnia kell egy EventStore-t, amely lehetővé teszi az események újrajátszását ügyfél újracsatlakozáskor.  
Megjegyzendő, hogy van egy közösségi javaslat (PR #975), amely transport-agnosztikus folytatható streameket vizsgál.

### 3. Tartósság

A hosszú távú agenteknek tartós állapotra van szükségük:

- Az eredmények túlélnek szerver újraindításokat
- Az állapot lekérdezhető külsőleg
- Haladás követése session-ök között

**MCP Támogatás**: Az MCP most támogatja az Erőforrás link visszatérési típust eszköz hívásokhoz. Ma egy lehetséges minta egy olyan eszköz tervezése, amely létrehoz egy erőforrást és azonnal visszaad egy erőforrás linket. Az eszköz a háttérben folytathatja a feladatot, és frissítheti az erőforrást. Az ügyfél választhat, hogy lekérdezi az erőforrás állapotát részleges vagy teljes eredményekért (az alapján, hogy milyen erőforrás frissítéseket biztosít a szerver), vagy feliratkozik az erőforrás frissítésekre.

### 4. Többfordulós Interakciók

Az agentek gyakran igényelnek további bemenetet a végrehajtás közben:

- Emberi pontosítás vagy jóváhagyás
- AI segítség komplex döntésekhez
- Dinamikus paraméter beállítás

**MCP Támogatás**: Teljes mértékben támogatott mintavétel (AI bemenethez) és kikérdezés (emberi bemenethez) révén.

## Hosszú Távú Agentek Megvalósítása MCP-n - Kód Áttekintés

Az MCP Python SDK-val és StreamableHTTP transporttal megvalósított hosszú távú agentek teljes implementációját tartalmazó [kód repository](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents) bemutatja, hogyan lehet az MCP képességeit kombinálni, hogy kifinomult agent-szerű viselkedést érjünk el.

## Következtetés

Az MCP kibővített képességei - erőforrás értesítések, kikérdezés/mintavétel, folytatható streamek és tartós erőforrások - lehetővé teszik a komplex agent-to-agent interakciókat, miközben megőrzik a protokoll egyszerűségét.

## Kezdés

Készen állsz saját agent2agent rendszered építésére? Kövesd az alábbi lépéseket:

### 1. Futtasd a Demót

### 2. Teszteld a Folytathatósági Képességeket

### 3. Fedezd fel és Bővítsd

Ez bemutatja, hogyan teszi lehetővé az MCP az intelligens agent viselkedést, miközben megőrzi az eszköz-alapú egyszerűséget.

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.