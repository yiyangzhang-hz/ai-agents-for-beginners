<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T20:10:35+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "hu"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.hu.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

# Agentic RAG

Ez a lecke átfogó áttekintést nyújt az Agentic Retrieval-Augmented Generation (Agentic RAG) nevű új AI-paradigmáról, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg következő lépéseiket, miközben külső forrásokból gyűjtenek információt. A statikus "keresés-és-olvasás" mintákkal ellentétben az Agentic RAG iteratív hívásokat végez az LLM-re, amelyeket eszköz- vagy funkcióhívások és strukturált kimenetek szakítanak meg. A rendszer értékeli az eredményeket, finomítja a lekérdezéseket, szükség esetén további eszközöket hív meg, és folytatja ezt a ciklust, amíg kielégítő megoldást nem ér el.

## Bevezetés

Ez a lecke az alábbiakat tartalmazza:

- **Az Agentic RAG megértése:** Ismerd meg az AI egy új paradigmáját, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg következő lépéseiket, miközben külső adatforrásokból gyűjtenek információt.
- **Iteratív Maker-Checker stílus elsajátítása:** Értsd meg az iteratív LLM-hívások ciklusát, amelyeket eszköz- vagy funkcióhívások és strukturált kimenetek szakítanak meg, a helyesség javítása és a hibás lekérdezések kezelése érdekében.
- **Gyakorlati alkalmazások felfedezése:** Azonosítsd azokat a helyzeteket, ahol az Agentic RAG kiemelkedően teljesít, például helyesség-központú környezetekben, összetett adatbázis-interakciókban és kiterjesztett munkafolyamatokban.

## Tanulási célok

A lecke elvégzése után képes leszel:

- **Az Agentic RAG megértése:** Ismerd meg az AI egy új paradigmáját, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg következő lépéseiket, miközben külső adatforrásokból gyűjtenek információt.
- **Iteratív Maker-Checker stílus:** Értsd meg az iteratív LLM-hívások ciklusának koncepcióját, amelyeket eszköz- vagy funkcióhívások és strukturált kimenetek szakítanak meg, a helyesség javítása és a hibás lekérdezések kezelése érdekében.
- **A gondolkodási folyamat irányítása:** Értsd meg a rendszer képességét arra, hogy önállóan irányítsa a gondolkodási folyamatát, és döntsön arról, hogyan közelítse meg a problémákat előre meghatározott utak nélkül.
- **Munkafolyamat:** Értsd meg, hogyan dönt egy agentikus modell önállóan arról, hogy piaci trendjelentéseket szerezzen be, azonosítsa a versenytársak adatait, összekapcsolja a belső értékesítési mutatókat, szintetizálja az eredményeket, és értékelje a stratégiát.
- **Iteratív ciklusok, eszközintegráció és memória:** Ismerd meg a rendszer interakciós mintáját, amely fenntartja az állapotot és a memóriát a lépések között, hogy elkerülje az ismétlődő ciklusokat, és megalapozott döntéseket hozzon.
- **Hibakezelési módok és önkorrekció:** Fedezd fel a rendszer robusztus önkorrekciós mechanizmusait, beleértve az iterációt és az újraleérdezést, diagnosztikai eszközök használatát, valamint az emberi felügyeletre való támaszkodást.
- **Az ügynökség határai:** Értsd meg az Agentic RAG korlátait, különös tekintettel a domain-specifikus autonómiára, az infrastruktúra-függőségre és a korlátok tiszteletben tartására.
- **Gyakorlati felhasználási esetek és érték:** Azonosítsd azokat a helyzeteket, ahol az Agentic RAG kiemelkedően teljesít, például helyesség-központú környezetekben, összetett adatbázis-interakciókban és kiterjesztett munkafolyamatokban.
- **Irányítás, átláthatóság és bizalom:** Ismerd meg az irányítás és az átláthatóság fontosságát, beleértve a magyarázható érvelést, az elfogultság ellenőrzését és az emberi felügyeletet.

## Mi az az Agentic RAG?

Az Agentic Retrieval-Augmented Generation (Agentic RAG) egy új AI-paradigma, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg következő lépéseiket, miközben külső forrásokból gyűjtenek információt. A statikus "keresés-és-olvasás" mintákkal ellentétben az Agentic RAG iteratív hívásokat végez az LLM-re, amelyeket eszköz- vagy funkcióhívások és strukturált kimenetek szakítanak meg. A rendszer értékeli az eredményeket, finomítja a lekérdezéseket, szükség esetén további eszközöket hív meg, és folytatja ezt a ciklust, amíg kielégítő megoldást nem ér el. Ez az iteratív „maker-checker” stílus javítja a helyességet, kezeli a hibás lekérdezéseket, és biztosítja a magas színvonalú eredményeket.

A rendszer aktívan irányítja a gondolkodási folyamatát, újraírja a sikertelen lekérdezéseket, különböző lekérdezési módszereket választ, és több eszközt integrál—például vektorkeresést az Azure AI Search-ben, SQL adatbázisokat vagy egyedi API-kat—mielőtt véglegesítené a válaszát. Az agentikus rendszer megkülönböztető jellemzője, hogy képes önállóan irányítani a gondolkodási folyamatát. A hagyományos RAG-megvalósítások előre meghatározott utakon alapulnak, de egy agentikus rendszer autonóm módon határozza meg a lépések sorrendjét az általa talált információk minősége alapján.

## Az Agentic Retrieval-Augmented Generation (Agentic RAG) meghatározása

Az Agentic Retrieval-Augmented Generation (Agentic RAG) egy új AI-fejlesztési paradigma, amelyben az LLM-ek nemcsak külső adatforrásokból gyűjtenek információt, hanem önállóan tervezik meg következő lépéseiket. A statikus "keresés-és-olvasás" mintákkal vagy gondosan szkriptelt prompt-szekvenciákkal ellentétben az Agentic RAG egy iteratív hívási ciklust alkalmaz az LLM-re, amelyet eszköz- vagy funkcióhívások és strukturált kimenetek szakítanak meg. Minden lépésnél a rendszer értékeli az elért eredményeket, eldönti, hogy finomítja-e a lekérdezéseket, szükség esetén további eszközöket hív meg, és folytatja ezt a ciklust, amíg kielégítő megoldást nem ér el.

Ez az iteratív „maker-checker” működési stílus a helyesség javítására, a strukturált adatbázisokhoz (pl. NL2SQL) kapcsolódó hibás lekérdezések kezelésére és kiegyensúlyozott, magas színvonalú eredmények biztosítására szolgál. A gondosan megtervezett prompt-láncokra való támaszkodás helyett a rendszer aktívan irányítja a gondolkodási folyamatát. Újraírhatja a sikertelen lekérdezéseket, különböző lekérdezési módszereket választhat, és több eszközt integrálhat—például vektorkeresést az Azure AI Search-ben, SQL adatbázisokat vagy egyedi API-kat—mielőtt véglegesítené a válaszát. Ez megszünteti a túlzottan bonyolult orkesztrációs keretrendszerek szükségességét. Ehelyett egy viszonylag egyszerű „LLM-hívás → eszközhasználat → LLM-hívás → …” ciklus is kifinomult és jól megalapozott kimeneteket eredményezhet.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.hu.png)

## A gondolkodási folyamat irányítása

Az a megkülönböztető tulajdonság, amely „agentikussá” tesz egy rendszert, az a képessége, hogy irányítsa a gondolkodási folyamatát. A hagyományos RAG-megvalósítások gyakran az emberek által előre meghatározott útra támaszkodnak: egy gondolatmenetre, amely meghatározza, mit és mikor kell lekérdezni.  
De amikor egy rendszer valóban agentikus, belsőleg dönti el, hogyan közelítse meg a problémát. Nem csak egy szkriptet hajt végre; autonóm módon határozza meg a lépések sorrendjét az általa talált információk minősége alapján.  
Például, ha egy termékbevezetési stratégiát kell létrehoznia, nem támaszkodik kizárólag egy olyan promptra, amely részletezi az egész kutatási és döntéshozatali munkafolyamatot. Ehelyett az agentikus modell önállóan dönt arról, hogy:

1. Piaci trendjelentéseket szerezzen be a Bing Web Grounding segítségével.
2. Releváns versenytársi adatokat azonosítson az Azure AI Search használatával.
3. Történelmi belső értékesítési mutatókat kapcsoljon össze az Azure SQL Database segítségével.
4. Az eredményeket egy koherens stratégiává szintetizálja az Azure OpenAI Service segítségével.
5. Értékelje a stratégiát hiányosságok vagy ellentmondások szempontjából, és szükség esetén újabb lekérdezési kört indítson.

Mindezeket a lépéseket—a lekérdezések finomítása, források kiválasztása, iteráció addig, amíg „elégedett” a válasszal—a modell dönti el, nem egy ember által előre szkriptelt folyamat.

## Iteratív ciklusok, eszközintegráció és memória

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.hu.png)

Egy agentikus rendszer egy iteratív interakciós mintára támaszkodik:

- **Kezdeti hívás:** A felhasználó célja (azaz a felhasználói prompt) bemutatásra kerül az LLM-nek.
- **Eszközhasználat:** Ha a modell hiányzó információt vagy kétértelmű utasításokat azonosít, kiválaszt egy eszközt vagy lekérdezési módszert—például egy vektoralapú adatbázis-lekérdezést (pl. Azure AI Search hibrid keresés privát adatokon) vagy egy strukturált SQL-hívást—, hogy több kontextust gyűjtsön.
- **Értékelés és finomítás:** Az adatok áttekintése után a modell eldönti, hogy az információ elegendő-e. Ha nem, finomítja a lekérdezést, másik eszközt próbál ki, vagy módosítja a megközelítést.
- **Ismétlés, amíg elégedett:** Ez a ciklus addig folytatódik, amíg a modell úgy nem érzi, hogy elegendő tisztasággal és bizonyítékkal rendelkezik egy végleges, jól megalapozott válasz megadásához.
- **Memória és állapot:** Mivel a rendszer fenntartja az állapotot és a memóriát a lépések között, emlékezni tud a korábbi próbálkozásokra és azok eredményeire, elkerülve az ismétlődő ciklusokat, és megalapozottabb döntéseket hozva a folyamat során.

Idővel ez egy fejlődő megértés érzetét kelti, lehetővé téve a modell számára, hogy összetett, több lépésből álló feladatokat hajtson végre anélkül, hogy az embernek folyamatosan be kellene avatkoznia vagy újra kellene formálnia a promptot.

## Hibakezelési módok és önkorrekció

Az Agentic RAG autonómiája robusztus önkorrekciós mechanizmusokat is magában foglal. Amikor a rendszer zsákutcába jut—például irreleváns dokumentumokat szerez be, vagy hibás lekérdezésekkel találkozik—, képes:

- **Iterálni és újraleérdezni:** Alacsony értékű válaszok visszaadása helyett a modell új keresési stratégiákat próbál ki, újraírja az adatbázis-lekérdezéseket, vagy alternatív adatforrásokat keres.
- **Diagnosztikai eszközöket használni:** A rendszer további funkciókat hívhat meg, amelyek segítenek a gondolkodási lépések hibakeresésében vagy az adatvisszakeresés helyességének megerősítésében. Az olyan eszközök, mint az Azure AI Tracing, fontosak lesznek a robusztus megfigyelhetőség és monitorozás érdekében.
- **Emberi felügyeletre támaszkodni:** Magas kockázatú vagy ismétlődően sikertelen helyzetekben a modell bizonytalanságot jelezhet, és emberi iránymutatást kérhet. Miután az ember helyesbítő visszajelzést ad, a modell beépítheti azt a tanulságot a továbbiakban.

Ez az iteratív és dinamikus megközelítés lehetővé teszi a modell számára, hogy folyamatosan fejlődjön, biztosítva, hogy ne csak egy egyszeri rendszer legyen, hanem olyan, amely tanul a hibáiból egy adott munkamenet során.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.hu.png)

## Az ügynökség határai

Annak ellenére, hogy egy feladaton belül autonóm, az Agentic RAG nem azonos a mesterséges általános intelligenciával. Az „agentikus” képességei az emberi fejlesztők által biztosított eszközökre, adatforrásokra és irányelvekre korlátozódnak. Nem képes saját eszközöket kitalálni vagy túllépni az előre meghatározott domain-határokon. Ehelyett a rendelkezésre álló erőforrások dinamikus összehangolásában jeleskedik.  
A fejlettebb AI-formáktól való kulcsfontosságú különbségek a következők:

1. **Domain-specifikus autonómia:** Az Agentic RAG rendszerek a felhasználó által meghatározott célok elérésére összpontosítanak egy ismert domainen belül, olyan stratégiákat alkalmazva, mint a lekérdezések újraírása vagy eszközválasztás az eredmények javítása érdekében.
2. **Infrastruktúra-függőség:** A rendszer képességei a fejlesztők által integrált eszközöktől és adatoktól függenek. Emberi beavatkozás nélkül nem lépheti túl ezeket a határokat.
3. **Korlátok tiszteletben tartása:** Az etikai irányelvek, megfelelőségi szabályok és üzleti politikák továbbra is nagyon fontosak. Az ügynök szabadsága mindig biztonsági intézkedések és felügyeleti mechanizmusok által korlátozott (remélhetőleg?).

## Gyakorlati felhasználási esetek és érték

Az Agentic RAG kiemelkedően teljesít olyan helyzetekben, amelyek iteratív finomítást és precizitást igényelnek:

1. **Helyesség-központú környezetek:** Megfelelőségi ellenőrzések, szabályozási elemzések vagy jogi kutatások során az agentikus modell ismételten ellenőrizheti a tényeket, több forrást konzultálhat, és újraírhatja
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementálja a Retrieval Augmented Generation (RAG) technológiát az Azure OpenAI Service segítségével: Ismerje meg, hogyan használhatja saját adatait az Azure OpenAI Service-ben. Ez a Microsoft Learn modul átfogó útmutatót nyújt a RAG megvalósításához.
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatív AI alkalmazások értékelése az Azure AI Foundry segítségével: Ez a cikk bemutatja a modellek értékelését és összehasonlítását nyilvánosan elérhető adathalmazokon, beleértve az Agentic AI alkalmazásokat és a RAG architektúrákat</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mi az az Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Teljes útmutató az ügynök-alapú Retrieval Augmented Generation-hez – Hírek a RAG világából</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbózza fel RAG-ját lekérdezés-átalakítással és önálló lekérdezéssel! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentic rétegek hozzáadása a RAG-hoz</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">A tudásasszisztensek jövője: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hogyan építsünk Agentic RAG rendszereket</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Az Azure AI Foundry Agent Service használata AI ügynökök skálázásához</a>

### Tudományos cikkek

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratív finomítás önvisszacsatolással</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Nyelvi ügynökök verbális megerősítéses tanulással</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Nagy nyelvi modellek önkorrekcióra képesek eszköz-interaktív kritika segítségével</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Felmérés az Agentic RAG-ról</a>

## Előző lecke

[Eszközhasználati tervezési minta](../04-tool-use/README.md)

## Következő lecke

[Megbízható AI ügynökök építése](../06-building-trustworthy-agents/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.