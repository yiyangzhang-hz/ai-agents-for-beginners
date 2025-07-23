<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-23T09:06:51+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "hu"
}
-->
# AI-ügynökök a gyakorlatban: Megfigyelhetőség és értékelés

Ahogy az AI-ügynökök kísérleti prototípusokból valós alkalmazásokba lépnek, egyre fontosabbá válik viselkedésük megértése, teljesítményük nyomon követése és kimeneteik rendszerszintű értékelése.

## Tanulási célok

A leckét követően képes leszel:
- Az ügynökök megfigyelhetőségének és értékelésének alapfogalmainak megértésére
- Az ügynökök teljesítményének, költségeinek és hatékonyságának javítására szolgáló technikák alkalmazására
- Az AI-ügynökök rendszerszintű értékelésére: mit és hogyan kell értékelni
- Az AI-ügynökök gyakorlatba való telepítésekor a költségek kontrollálására
- Az AutoGen-nel épített ügynökök instrumentálására

A cél az, hogy olyan tudással ruházzunk fel, amely lehetővé teszi, hogy a "fekete doboz" ügynököket átlátható, kezelhető és megbízható rendszerekké alakítsd.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI-ügynököket telepítsünk. Nézd meg a [Megbízható AI-ügynökök építése](./06-building-trustworthy-agents/README.md) című leckét is._

## Nyomvonalak és szakaszok

A megfigyelhetőségi eszközök, mint például a [Langfuse](https://langfuse.com/) vagy az [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), általában az ügynök futtatásait nyomvonalakként és szakaszokként ábrázolják.

- **Nyomvonal**: Egy teljes ügynökfeladatot képvisel a kezdetektől a végéig (például egy felhasználói kérdés kezelése).
- **Szakaszok**: A nyomvonalon belüli egyedi lépések (például egy nyelvi modell hívása vagy adatlekérés).

![Nyomvonalfa a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Megfigyelhetőség nélkül egy AI-ügynök "fekete doboznak" tűnhet – belső állapota és érvelése átláthatatlan, ami megnehezíti a problémák diagnosztizálását vagy a teljesítmény optimalizálását. Megfigyelhetőséggel az ügynökök "üveg dobozokká" válnak, átláthatóságot biztosítva, amely elengedhetetlen a bizalom kiépítéséhez és annak biztosításához, hogy az ügynökök a kívánt módon működjenek.

## Miért fontos a megfigyelhetőség a gyakorlatban?

Az AI-ügynökök gyakorlatba való telepítése új kihívásokat és követelményeket hoz magával. A megfigyelhetőség már nem "jó, ha van", hanem kritikus képesség:

*   **Hibakeresés és okfeltárás**: Ha egy ügynök hibázik vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök nyomvonalakat biztosítanak a hiba forrásának azonosításához. Ez különösen fontos összetett ügynököknél, amelyek több LLM-hívást, eszközinterakciót és feltételes logikát tartalmazhatnak.
*   **Késleltetés és költségkezelés**: Az AI-ügynökök gyakran támaszkodnak LLM-ekre és más külső API-kra, amelyek tokenenként vagy hívásonként kerülnek számlázásra. A megfigyelhetőség lehetővé teszi ezeknek a hívásoknak a pontos nyomon követését, segítve a túl lassú vagy drága műveletek azonosítását. Ezáltal a csapatok optimalizálhatják a promptokat, hatékonyabb modelleket választhatnak, vagy áttervezhetik a munkafolyamatokat az üzemeltetési költségek kezelésére és a jó felhasználói élmény biztosítására.
*   **Bizalom, biztonság és megfelelőség**: Számos alkalmazásban fontos, hogy az ügynökök biztonságosan és etikusan viselkedjenek. A megfigyelhetőség auditnyomvonalat biztosít az ügynökök cselekedeteiről és döntéseiről. Ez felhasználható olyan problémák észlelésére és enyhítésére, mint a prompt injekció, káros tartalom generálása vagy személyes azonosításra alkalmas információk (PII) helytelen kezelése. Például nyomvonalakat vizsgálhatsz, hogy megértsd, miért adott az ügynök egy adott választ vagy miért használt egy adott eszközt.
*   **Folyamatos fejlesztési ciklusok**: A megfigyelhetőségi adatok az iteratív fejlesztési folyamat alapját képezik. Az ügynökök valós teljesítményének nyomon követésével a csapatok azonosíthatják a fejlesztési területeket, adatokat gyűjthetnek a modellek finomhangolásához, és ellenőrizhetik a változtatások hatását. Ez egy visszacsatolási hurkot hoz létre, ahol az online értékelésből származó gyártási betekintések informálják az offline kísérletezést és finomítást, ami fokozatosan jobb ügynökteljesítményhez vezet.

## Kulcsfontosságú mérőszámok nyomon követése

Az ügynökök viselkedésének nyomon követéséhez és megértéséhez számos mérőszámot és jelet kell figyelni. Bár a konkrét mérőszámok az ügynök céljától függően változhatnak, néhány univerzálisan fontos.

Íme néhány a leggyakoribb mérőszámok közül, amelyeket a megfigyelhetőségi eszközök monitoroznak:

**Késleltetés:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. A késleltetést a feladatok és az egyes lépések szintjén kell mérni az ügynök futtatásainak nyomon követésével. Például egy ügynök, amely 20 másodpercet vesz igénybe az összes modellhívásra, gyorsítható egy gyorsabb modell használatával vagy a modellhívások párhuzamos futtatásával.

**Költségek:** Mennyibe kerül egy ügynök futtatása? Az AI-ügynökök LLM-hívásokra támaszkodnak, amelyek tokenenként vagy külső API-ként kerülnek számlázásra. A gyakori eszközhasználat vagy több prompt gyorsan növelheti a költségeket. Például, ha egy ügynök ötször hív egy LLM-et marginális minőségjavítás érdekében, értékelni kell, hogy a költség indokolt-e, vagy csökkenteni lehet-e a hívások számát, illetve olcsóbb modellt használni. A valós idejű monitorozás segíthet az előre nem látható kiugrások azonosításában is (például hibák, amelyek túlzott API-hurkokat okoznak).

**Kérés hibák:** Hány kérést nem sikerült teljesítenie az ügynöknek? Ez magában foglalhatja az API-hibákat vagy a sikertelen eszközhívásokat. Az ügynököt robusztusabbá teheted ezekkel szemben a gyakorlatban, ha visszaállításokat vagy újrapróbálkozásokat állítasz be. Például, ha az A LLM-szolgáltató nem elérhető, válthatsz a B LLM-szolgáltatóra tartalékként.

**Felhasználói visszajelzés:** A közvetlen felhasználói értékelések értékes betekintést nyújtanak. Ez magában foglalhatja az explicit értékeléseket (👍fel/👎le, ⭐1-5 csillag) vagy szöveges megjegyzéseket. A következetesen negatív visszajelzések figyelmeztető jelzésként szolgálnak, hogy az ügynök nem működik megfelelően.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedések közvetett visszajelzést nyújtanak, még explicit értékelések nélkül is. Ez magában foglalhatja az azonnali kérdésátfogalmazást, ismételt lekérdezéseket vagy egy újrapróbálkozás gomb megnyomását. Például, ha azt látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, ez annak a jele, hogy az ügynök nem működik megfelelően.

**Pontosság:** Milyen gyakran produkál az ügynök helyes vagy kívánatos kimeneteket? A pontosság definíciói változhatnak (például problémamegoldási helyesség, információkeresési pontosság, felhasználói elégedettség). Az első lépés az, hogy meghatározd, mit jelent a siker az ügynököd számára. A pontosságot automatizált ellenőrzésekkel, értékelési pontszámokkal vagy feladat teljesítési címkékkel követheted. Például a nyomvonalakat "sikeres" vagy "sikertelen" címkével láthatod el.

**Automatizált értékelési mérőszámok:** Automatizált értékeléseket is beállíthatsz. Például használhatsz egy LLM-et az ügynök kimenetének pontozására, például hogy az hasznos, pontos vagy sem. Számos nyílt forráskódú könyvtár is segít az ügynök különböző aspektusainak pontozásában. Például [RAGAS](https://docs.ragas.io/) RAG-ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt injekció észlelésére.

A gyakorlatban ezeknek a mérőszámoknak a kombinációja nyújtja a legjobb lefedettséget az AI-ügynök egészségi állapotáról. Ebben a fejezetben [példa jegyzetfüzetben](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) bemutatjuk, hogyan néznek ki ezek a mérőszámok valós példákban, de először megtanuljuk, hogyan néz ki egy tipikus értékelési munkafolyamat.

## Instrumentáld az ügynöködet

A nyomvonaladatok gyűjtéséhez instrumentálnod kell a kódodat. A cél az, hogy az ügynökkódot úgy instrumentáld, hogy nyomvonalakat és mérőszámokat bocsásson ki, amelyeket egy megfigyelhetőségi platform rögzíthet, feldolgozhat és megjeleníthet.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) az LLM-megfigyelhetőség iparági szabványává vált. API-k, SDK-k és eszközök készletét biztosítja a telemetriai adatok generálásához, gyűjtéséhez és exportálásához.

Számos instrumentációs könyvtár létezik, amelyek meglévő ügynökkeretrendszereket csomagolnak, és megkönnyítik az OpenTelemetry szakaszok exportálását egy megfigyelhetőségi eszközbe. Az alábbiakban egy példa látható az AutoGen ügynök instrumentálására az [OpenLit instrumentációs könyvtárral](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

A fejezet [példa jegyzetfüzete](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) bemutatja, hogyan instrumentálhatod az AutoGen ügynöködet.

**Manuális szakasz létrehozása:** Bár az instrumentációs könyvtárak jó alapot biztosítanak, gyakran előfordulnak olyan esetek, amikor részletesebb vagy egyedi információkra van szükség. Manuálisan hozhatsz létre szakaszokat, hogy egyedi alkalmazáslogikát adj hozzá. Ennél is fontosabb, hogy gazdagíthatod az automatikusan vagy manuálisan létrehozott szakaszokat egyedi attribútumokkal (más néven címkékkel vagy metaadatokkal). Ezek az attribútumok tartalmazhatnak üzleti specifikus adatokat, köztes számításokat vagy bármilyen kontextust, amely hasznos lehet a hibakereséshez vagy elemzéshez, például `user_id`, `session_id` vagy `model_version`.

Példa nyomvonalak és szakaszok manuális létrehozására a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) segítségével:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelése

A megfigyelhetőség mérőszámokat biztosít, de az értékelés az adatok elemzésének (és tesztek elvégzésének) folyamata annak meghatározására, hogy az AI-ügynök mennyire teljesít jól, és hogyan lehetne javítani. Más szavakkal, ha már megvannak a nyomvonalak és mérőszámok, hogyan használhatod ezeket az ügynök megítélésére és döntések meghozatalára?

A rendszeres értékelés fontos, mert az AI-ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy modellek viselkedésének eltolódása révén) – értékelés nélkül nem tudnád, hogy az "okos ügynököd" valóban jól végzi-e a munkáját, vagy visszafejlődött.

Az AI-ügynökök értékelésének két kategóriája van: **offline értékelés** és **online értékelés**. Mindkettő értékes, és kiegészítik egymást. Általában offline értékeléssel kezdünk, mivel ez a minimálisan szükséges lépés bármely ügynök telepítése előtt.

### Offline értékelés

![Adatkészlet elemei a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az ügynök értékelését jelenti kontrollált környezetben, általában tesztadatkészletek használatával, nem élő felhasználói lekérdezésekkel. Olyan gondosan összeállított adatkészleteket használsz, ahol tudod, mi a várható kimenet vagy helyes viselkedés, majd futtatod az ügynököt ezeken.

Például, ha egy matematikai szöveges problémák megoldására szolgáló ügynököt építettél, lehet, hogy van egy [tesztadatkészleted](https://huggingface.co/datasets/gsm8k) 100 problémával, amelyeknek ismert a megoldása. Az offline értékelést gyakran a fejlesztés során végzik (és része lehet a CI/CD folyamatoknak), hogy ellenőrizzék a fejlesztéseket vagy megakadályozzák a visszafejlődést. Az előnye, hogy **ismételhető, és egyértelmű pontossági mérőszámokat kaphatsz, mivel van alapigazságod**. Szimulálhatod a felhasználói lekérdezéseket is, és mérheted az ügynök válaszait az ideális válaszokhoz képest, vagy használhatsz automatizált mérőszámokat, ahogy fentebb leírtuk.

Az offline értékelés kulcsfontosságú kihívása annak biztosítása, hogy a tesztadatkészlet átfogó és releváns maradjon – az ügynök jól teljesíthet egy fix tesztkészleten, de nagyon eltérő lekérdezésekkel találkozhat a gyakorlatban. Ezért a tesztkészleteket frissíteni kell új szélsőséges esetekkel és példákkal, amelyek tükrözik a valós forgatókönyveket​. Egy kis "füstteszt" esetek és nagyobb értékelési készletek keveréke hasznos

- Finomítsd a meghatározott paramétereket, utasításokat és az eszközök elnevezését.  |
| A többügynökös rendszer nem működik következetesen | - Finomítsd az egyes ügynököknek adott utasításokat, hogy specifikusak és egymástól jól elkülöníthetők legyenek.<br>- Építs hierarchikus rendszert egy "irányító" vagy vezérlő ügynök segítségével, amely meghatározza, melyik ügynök a megfelelő. |

Sok ilyen probléma hatékonyabban azonosítható, ha megfigyelhetőség van beépítve. Azok a nyomok és metrikák, amelyeket korábban tárgyaltunk, pontosan segítenek meghatározni, hogy az ügynök munkafolyamatának melyik részén jelentkeznek problémák, így a hibakeresés és az optimalizálás sokkal hatékonyabbá válik.

## Költségek kezelése

Íme néhány stratégia az AI ügynökök éles környezetbe történő telepítésének költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (SLM-ek) bizonyos ügynöki felhasználási esetekben jól teljesíthetnek, és jelentősen csökkenthetik a költségeket. Ahogy korábban említettük, egy értékelési rendszer kiépítése, amely összehasonlítja a teljesítményt a nagyobb modellekkel, a legjobb módja annak, hogy megértsük, mennyire jól teljesít egy SLM az adott felhasználási esetben. Fontold meg SLM-ek használatát egyszerűbb feladatokhoz, például szándékosztályozáshoz vagy paraméterek kinyeréséhez, míg a nagyobb modelleket tartogasd az összetettebb érvelési feladatokra.

**Irányító modell használata:** Egy hasonló stratégia a különböző méretű és típusú modellek használata. Használhatsz egy LLM/SLM modellt vagy szerver nélküli funkciót arra, hogy az összetettség alapján irányítsd a kéréseket a legmegfelelőbb modellekhez. Ez nemcsak a költségeket csökkenti, hanem biztosítja a megfelelő teljesítményt is a megfelelő feladatokon. Például az egyszerű lekérdezéseket irányítsd kisebb, gyorsabb modellekhez, és csak az összetett érvelési feladatokhoz használd a drágább, nagy modelleket.

**Válaszok gyorsítótárazása:** Az ismétlődő kérések és feladatok azonosítása, valamint a válaszok előzetes biztosítása az ügynöki rendszerbe való belépés előtt jó módja a hasonló kérések mennyiségének csökkentésére. Akár egy olyan folyamatot is bevezethetsz, amely azonosítja, hogy egy kérés mennyire hasonlít a gyorsítótárban lévő kérésekhez, egyszerűbb AI modellek használatával. Ez a stratégia jelentősen csökkentheti a költségeket a gyakran ismétlődő kérdések vagy megszokott munkafolyamatok esetén.

## Nézzük, hogyan működik ez a gyakorlatban

A [szakasz példafüzetében](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) példákat láthatunk arra, hogyan használhatunk megfigyelési eszközöket az ügynökök monitorozására és értékelésére.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[MCP](../11-mcp/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.