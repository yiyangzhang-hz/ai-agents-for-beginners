<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-23T09:04:52+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sw"
}
-->
# Mawakala wa AI Katika Uzalishaji: Ufuatiliaji na Tathmini

Wakati mawakala wa AI wanapohama kutoka kwa prototypes za majaribio hadi matumizi halisi, uwezo wa kuelewa tabia zao, kufuatilia utendaji wao, na kutathmini matokeo yao kwa utaratibu unakuwa muhimu.

## Malengo ya Kujifunza

Baada ya kukamilisha somo hili, utajua jinsi ya/kuelewa:
- Dhana kuu za ufuatiliaji na tathmini ya mawakala
- Mbinu za kuboresha utendaji, gharama, na ufanisi wa mawakala
- Nini na jinsi ya kutathmini mawakala wako wa AI kwa utaratibu
- Jinsi ya kudhibiti gharama wakati wa kupeleka mawakala wa AI katika uzalishaji
- Jinsi ya kuandaa mawakala waliotengenezwa kwa AutoGen

Lengo ni kukupa maarifa ya kubadilisha mawakala wako wa "sanduku jeusi" kuwa mifumo ya uwazi, inayoweza kudhibitiwa, na ya kuaminika.

_**Kumbuka:** Ni muhimu kupeleka Mawakala wa AI ambao ni salama na wa kuaminika. Angalia somo la [Kujenga Mawakala wa AI wa Kuaminika](./06-building-trustworthy-agents/README.md) pia._

## Mfuatano na Vipindi

Zana za ufuatiliaji kama [Langfuse](https://langfuse.com/) au [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) mara nyingi huwakilisha mizunguko ya mawakala kama mfuatano na vipindi.

- **Mfuatano** unawakilisha kazi kamili ya wakala kutoka mwanzo hadi mwisho (kama kushughulikia swali la mtumiaji).
- **Vipindi** ni hatua za kibinafsi ndani ya mfuatano (kama kuita mfano wa lugha au kupata data).

![Mti wa mfuatano katika Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bila ufuatiliaji, wakala wa AI anaweza kuhisi kama "sanduku jeusi" - hali yake ya ndani na mantiki yake ni ngumu kuelewa, na kufanya iwe vigumu kutambua matatizo au kuboresha utendaji. Kwa ufuatiliaji, mawakala wanakuwa "masanduku ya kioo," wakitoa uwazi ambao ni muhimu kwa kujenga uaminifu na kuhakikisha wanafanya kazi kama inavyotarajiwa.

## Kwa Nini Ufuatiliaji Ni Muhimu Katika Mazingira ya Uzalishaji

Kuhamisha mawakala wa AI kwenye mazingira ya uzalishaji huleta changamoto na mahitaji mapya. Ufuatiliaji hauwi tena "mzuri kuwa nao" bali ni uwezo muhimu:

*   **Kutatua Matatizo na Uchambuzi wa Sababu ya Msingi**: Wakati wakala anaposhindwa au kutoa matokeo yasiyotarajiwa, zana za ufuatiliaji hutoa mfuatano unaohitajika kutambua chanzo cha kosa. Hii ni muhimu hasa kwa mawakala wa hali ngumu ambao wanaweza kuhusisha miito mingi ya LLM, mwingiliano wa zana, na mantiki ya masharti.
*   **Usimamizi wa Muda wa Kusubiri na Gharama**: Mawakala wa AI mara nyingi hutegemea LLM na API zingine za nje ambazo hutozwa kwa kila tokeni au kila mwito. Ufuatiliaji huruhusu kufuatilia kwa usahihi miito hii, kusaidia kutambua operesheni ambazo ni polepole sana au ghali. Hii inawawezesha timu kuboresha maelekezo, kuchagua mifano yenye ufanisi zaidi, au kubuni upya mtiririko wa kazi ili kudhibiti gharama za uendeshaji na kuhakikisha uzoefu mzuri wa mtumiaji.
*   **Uaminifu, Usalama, na Uzingatiaji**: Katika matumizi mengi, ni muhimu kuhakikisha kwamba mawakala wanatenda kwa usalama na kimaadili. Ufuatiliaji hutoa rekodi ya hatua na maamuzi ya wakala. Hii inaweza kutumika kugundua na kupunguza masuala kama sindano ya maelekezo, uzalishaji wa maudhui hatari, au utunzaji mbaya wa taarifa za kibinafsi (PII). Kwa mfano, unaweza kukagua mfuatano ili kuelewa kwa nini wakala alitoa jibu fulani au alitumia zana maalum.
*   **Mizunguko ya Kuboresha Kuendelea**: Data ya ufuatiliaji ni msingi wa mchakato wa maendeleo ya kurudia. Kwa kufuatilia jinsi mawakala wanavyofanya kazi katika ulimwengu halisi, timu zinaweza kutambua maeneo ya kuboresha, kukusanya data kwa ajili ya kurekebisha mifano, na kuthibitisha athari za mabadiliko. Hii huunda mzunguko wa maoni ambapo maarifa ya uzalishaji kutoka tathmini ya mtandaoni huarifu majaribio ya nje ya mtandao na uboreshaji, na kusababisha utendaji bora wa wakala kwa hatua.

## Viashiria Muhimu vya Kufuatilia

Ili kufuatilia na kuelewa tabia ya wakala, anuwai ya viashiria na ishara inapaswa kufuatiliwa. Ingawa viashiria maalum vinaweza kutofautiana kulingana na madhumuni ya wakala, baadhi ni muhimu kwa wote.

Hapa kuna baadhi ya viashiria vya kawaida ambavyo zana za ufuatiliaji hufuatilia:

**Muda wa Kusubiri:** Wakala anajibu haraka kiasi gani? Muda mrefu wa kusubiri huathiri uzoefu wa mtumiaji vibaya. Unapaswa kupima muda wa kusubiri kwa kazi na hatua za kibinafsi kwa kufuatilia mizunguko ya wakala. Kwa mfano, wakala anayechukua sekunde 20 kwa miito yote ya mfano anaweza kuharakishwa kwa kutumia mfano wa haraka zaidi au kwa kuendesha miito ya mfano kwa sambamba.

**Gharama:** Gharama kwa kila mzunguko wa wakala ni kiasi gani? Mawakala wa AI hutegemea miito ya LLM inayotozwa kwa kila tokeni au API za nje. Matumizi ya zana mara kwa mara au maelekezo mengi yanaweza kuongeza gharama haraka. Kwa mfano, ikiwa wakala anaita LLM mara tano kwa uboreshaji wa ubora mdogo, lazima upime ikiwa gharama inastahili au ikiwa unaweza kupunguza idadi ya miito au kutumia mfano wa bei nafuu. Ufuatiliaji wa wakati halisi pia unaweza kusaidia kutambua ongezeko lisilotarajiwa (mfano, hitilafu zinazosababisha mizunguko ya API isiyo ya kawaida).

**Hitilafu za Ombi:** Ni ombi ngapi wakala alishindwa? Hii inaweza kujumuisha hitilafu za API au miito ya zana iliyoshindwa. Ili kufanya wakala wako kuwa thabiti zaidi dhidi ya hizi katika uzalishaji, unaweza kuweka upya au kurudia. Mfano, ikiwa mtoa huduma wa LLM A yuko chini, unabadilisha kwenda kwa mtoa huduma wa LLM B kama chelezo.

**Maoni ya Mtumiaji:** Kutekeleza tathmini za moja kwa moja za watumiaji hutoa maarifa muhimu. Hii inaweza kujumuisha ukadiriaji wa moja kwa moja (👍thumbs-up/👎down, ⭐nyota 1-5) au maoni ya maandishi. Maoni hasi ya mara kwa mara yanapaswa kukuonya kwani ni ishara kwamba wakala hafanyi kazi kama inavyotarajiwa.

**Maoni ya Kijanja ya Mtumiaji:** Tabia za watumiaji hutoa maoni ya moja kwa moja hata bila ukadiriaji wa moja kwa moja. Hii inaweza kujumuisha uundaji upya wa swali mara moja, maswali yanayorudiwa au kubonyeza kitufe cha kurudia. Mfano, ikiwa unaona kwamba watumiaji wanauliza swali lile lile mara kwa mara, hii ni ishara kwamba wakala hafanyi kazi kama inavyotarajiwa.

**Usahihi:** Wakala hutoa matokeo sahihi au yanayotarajiwa mara ngapi? Ufafanuzi wa usahihi hutofautiana (mfano, usahihi wa kutatua matatizo, usahihi wa kupata taarifa, kuridhika kwa mtumiaji). Hatua ya kwanza ni kufafanua mafanikio yanavyotazamiwa kwa wakala wako. Unaweza kufuatilia usahihi kupitia ukaguzi wa kiotomatiki, alama za tathmini, au lebo za kukamilisha kazi. Kwa mfano, kuweka mfuatano kama "ulifanikiwa" au "ulishindwa."

**Viashiria vya Tathmini ya Kiotomatiki:** Unaweza pia kuweka tathmini za kiotomatiki. Kwa mfano, unaweza kutumia LLM kupima matokeo ya wakala, mfano ikiwa ni ya msaada, sahihi, au la. Pia kuna maktaba kadhaa za chanzo huria zinazokusaidia kupima vipengele tofauti vya wakala. Mfano, [RAGAS](https://docs.ragas.io/) kwa mawakala wa RAG au [LLM Guard](https://llm-guard.com/) kugundua lugha hatari au sindano ya maelekezo.

Kwa vitendo, mchanganyiko wa viashiria hivi hutoa uelewa bora wa afya ya wakala wa AI. Katika [notebook ya mfano](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) ya sura hii, tutaonyesha jinsi viashiria hivi vinavyoonekana katika mifano halisi lakini kwanza, tutajifunza jinsi mtiririko wa tathmini wa kawaida unavyoonekana.

## Andaa Wakala Wako

Ili kukusanya data ya mfuatano, utahitaji kuandaa msimbo wako. Lengo ni kuandaa msimbo wa wakala ili kutoa mfuatano na viashiria vinavyoweza kukamatwa, kuchakatwa, na kuonyeshwa na jukwaa la ufuatiliaji.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) imeibuka kama kiwango cha tasnia kwa ufuatiliaji wa LLM. Inatoa seti ya API, SDK, na zana za kuzalisha, kukusanya, na kusafirisha data ya telemetry.

Kuna maktaba nyingi za maandalizi zinazofunika mifumo ya wakala iliyopo na kufanya iwe rahisi kusafirisha vipindi vya OpenTelemetry kwa zana ya ufuatiliaji. Hapo chini kuna mfano wa kuandaa wakala wa AutoGen kwa maktaba ya maandalizi ya [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notebook ya mfano](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) katika sura hii itaonyesha jinsi ya kuandaa wakala wako wa AutoGen.

**Uundaji wa Vipindi kwa Mkono:** Ingawa maktaba za maandalizi hutoa msingi mzuri, mara nyingi kuna hali ambapo habari ya kina zaidi au maalum inahitajika. Unaweza kuunda vipindi kwa mkono ili kuongeza mantiki maalum ya programu. Muhimu zaidi, vinaweza kuimarisha vipindi vilivyoundwa kiotomatiki au kwa mkono na sifa maalum (pia zinajulikana kama lebo au metadata). Sifa hizi zinaweza kujumuisha data maalum ya biashara, mahesabu ya kati, au muktadha wowote ambao unaweza kuwa muhimu kwa utatuzi wa matatizo au uchambuzi, kama `user_id`, `session_id`, au `model_version`.

Mfano wa kuunda mfuatano na vipindi kwa mkono kwa kutumia [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Tathmini ya Wakala

Ufuatiliaji hutupa viashiria, lakini tathmini ni mchakato wa kuchambua data hiyo (na kufanya majaribio) ili kuamua jinsi wakala wa AI unavyofanya kazi na jinsi unavyoweza kuboreshwa. Kwa maneno mengine, mara tu unapokuwa na mfuatano na viashiria hivyo, unavitumiaje kuhukumu wakala na kufanya maamuzi?

Tathmini ya mara kwa mara ni muhimu kwa sababu mawakala wa AI mara nyingi si wa kudumu na wanaweza kubadilika (kupitia masasisho au mabadiliko ya tabia ya mfano) – bila tathmini, usingejua ikiwa "wakala wako mwerevu" kweli anafanya kazi yake vizuri au ikiwa umepungua.

Kuna makundi mawili ya tathmini kwa mawakala wa AI: **tathmini ya mtandaoni** na **tathmini ya nje ya mtandao**. Zote ni muhimu, na zinakamilishana. Kwa kawaida tunaanza na tathmini ya nje ya mtandao, kwani hii ni hatua ya chini inayohitajika kabla ya kupeleka wakala yeyote.

### Tathmini ya Nje ya Mtandao

![Vitu vya dataset katika Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Hii inahusisha kutathmini wakala katika mazingira yaliyodhibitiwa, kwa kawaida kwa kutumia seti za majaribio, si maswali ya moja kwa moja ya watumiaji. Unatumia seti za data zilizochaguliwa ambapo unajua matokeo yanayotarajiwa au tabia sahihi, kisha unaendesha wakala wako juu ya hizo.

Kwa mfano, ikiwa umeunda wakala wa matatizo ya maneno ya hesabu, unaweza kuwa na [seti ya majaribio](https://huggingface.co/datasets/gsm8k) ya matatizo 100 yenye majibu yanayojulikana. Tathmini ya nje ya mtandao mara nyingi hufanywa wakati wa maendeleo (na inaweza kuwa sehemu ya mabomba ya CI/CD) ili kuangalia maboresho au kulinda dhidi ya kupungua. Faida ni kwamba ni **inaweza kurudiwa na unaweza kupata viashiria vya usahihi wazi kwa kuwa una ukweli wa msingi**. Unaweza pia kuiga maswali ya watumiaji na kupima majibu ya wakala dhidi ya majibu bora au kutumia viashiria vya kiotomatiki kama ilivyoelezwa hapo juu.

Changamoto kuu na tathmini ya nje ya mtandao ni kuhakikisha seti yako ya majaribio ni ya kina na inabaki kuwa muhimu – wakala anaweza kufanya vizuri kwenye seti ya majaribio iliyowekwa lakini kukutana na maswali tofauti sana katika uzalishaji. Kwa hivyo, unapaswa kuweka seti za majaribio zikiwa zimesasishwa na kesi mpya za ukingo na mifano inayowakilisha hali halisi​. Mchanganyiko wa kesi ndogo za "majaribio ya moshi" na seti kubwa za tathmini ni muhimu: seti ndogo kwa ukaguzi wa haraka na kubwa kwa viashiria vya utendaji mpana​.

### Tathmini ya Mtandaoni

![Muhtasari wa viashiria vya ufuatiliaji](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Hii inahusu kutathmini wakala katika mazingira ya moja kwa moja, ya ulimwengu halisi, yaani, wakati wa matumizi halisi katika uzalishaji. Tathmini ya mtandaoni inahusisha kufuatilia utendaji wa wakala kwenye mwingiliano halisi wa watumiaji na kuchambua matokeo kwa kuendelea.

Kwa mfano, unaweza kufuatilia viwango vya mafanikio, alama za kuridhika kwa watumiaji, au viashiria vingine kwenye trafiki ya moja kwa moja. Faida ya tathmini ya mtandaoni ni kwamba **inakamata mambo ambayo huenda usingetarajia katika mazingira ya maabara** – unaweza kuona mabadiliko ya mfano kwa muda (ikiwa ufanisi wa wakala unashuka kadri mifumo ya pembejeo inavyobadilika) na kugundua maswali au hali zisizotarajiwa ambazo hazikuwa katika data yako ya majaribio​. Inatoa picha ya kweli ya jinsi wakala anavyotenda katika mazingira halisi.

Tathmini ya mtandaoni mara nyingi inahusisha kukusanya maoni ya moja kwa moja na ya kijanja ya watumiaji, kama ilivyojadiliwa, na labda kuendesha majaribio ya kivuli au majaribio ya A/B (ambapo toleo jipya la wakala linaendeshwa sambamba kulinganisha na la zamani). Changamoto ni kwamba inaweza kuwa ngumu kupata lebo au alama za kuaminika kwa mwingiliano wa moja kwa moja – unaweza kutegemea maoni ya watumiaji au viashiria vya chini (kama mtumiaji alibonyeza matokeo).

### Kuchanganya Mbili

Tathmini ya mtandaoni na nje ya mtandao si za kipekee; zinakamilishana sana. Maarifa kutoka kwa ufuatiliaji wa mtandaoni (mfano, aina mpya za maswali ya watumiaji ambapo wakala hufanya vibaya) yanaweza kutumika kuongeza na kuboresha seti za majaribio ya nje ya mtandao. Kinyume chake, mawakala wanaofanya vizuri katika majaribio ya nje ya mtandao wanaweza kupelekwa kwa ujasiri zaidi na kufuatiliwa mtandaoni.

Kwa kweli, timu nyingi zinachukua mzunguko:

_tathmini nje ya mtandao -> peleka -> fuatilia mtandaoni -> kukusanya kesi mpya za kushindwa -> ongeza kwenye seti ya nje ya mtandao -> boresha wakala -> rudia_.

## Masuala ya Kawaida

Unapopeleka mawakala wa AI katika uzalishaji, unaweza kukutana na changamoto mbalimbali. Hapa kuna masuala ya kawaida na suluhisho zao zinazowezekana:

| **Tatizo**    | **Suluhisho Linalowezekana**   |
| ------------- | ------------------ |
| Wakala wa AI hafanyi kazi kwa uthabiti | - Boresha maelekezo yanayotolewa kwa wakala wa AI; kuwa wazi juu ya malengo.<br>- Tambua wapi kugawanya kazi katika kazi ndogo na kushughulikiwa na mawakala

- Rekebisha vigezo vilivyobainishwa, maelezo, na majina ya zana.  |
| Mfumo wa Wakala Wengi hauonyeshi utendaji thabiti | - Rekebisha maelezo yanayotolewa kwa kila wakala ili kuhakikisha kuwa ni maalum na tofauti kati yao.<br>- Jenga mfumo wa kihierarkia kwa kutumia wakala wa "usambazaji" au mdhibiti ili kubaini ni wakala gani anayefaa. |

Masuala mengi kati ya haya yanaweza kutambuliwa kwa ufanisi zaidi ikiwa kuna ufuatiliaji. Ufuatiliaji na vipimo tulivyojadili awali husaidia kubaini hasa ni wapi katika mtiririko wa kazi wa wakala matatizo yanatokea, na kufanya utatuzi wa matatizo na uboreshaji kuwa rahisi zaidi.

## Kusimamia Gharama

Hapa kuna mikakati ya kusimamia gharama za kupeleka mawakala wa AI katika uzalishaji:

**Kutumia Miundo Midogo:** Miundo Midogo ya Lugha (SLMs) inaweza kufanya kazi vizuri katika baadhi ya matumizi ya wakala na kupunguza gharama kwa kiasi kikubwa. Kama ilivyotajwa awali, kujenga mfumo wa tathmini ili kubaini na kulinganisha utendaji dhidi ya miundo mikubwa ni njia bora ya kuelewa jinsi SLM itakavyofanya kazi katika matumizi yako. Fikiria kutumia SLMs kwa kazi rahisi kama uainishaji wa nia au uchimbaji wa vigezo, huku ukihifadhi miundo mikubwa kwa hoja ngumu zaidi.

**Kutumia Mfano wa Usambazaji:** Mkakati sawa ni kutumia utofauti wa miundo na ukubwa. Unaweza kutumia LLM/SLM au kazi isiyo na seva kusambaza maombi kulingana na ugumu kwa miundo inayofaa zaidi. Hii pia itasaidia kupunguza gharama huku ikihakikisha utendaji katika kazi sahihi. Kwa mfano, elekeza maswali rahisi kwa miundo midogo, ya haraka, na tumia tu miundo mikubwa ya gharama kubwa kwa kazi za hoja ngumu.

**Kuhifadhi Majibu:** Kutambua maombi na kazi za kawaida na kutoa majibu kabla ya kupitia mfumo wako wa wakala ni njia nzuri ya kupunguza idadi ya maombi yanayofanana. Unaweza hata kutekeleza mtiririko wa kutambua jinsi ombi lilivyo sawa na maombi yako yaliyohifadhiwa kwa kutumia miundo ya AI ya msingi zaidi. Mkakati huu unaweza kupunguza kwa kiasi kikubwa gharama za maswali yanayoulizwa mara kwa mara au mtiririko wa kazi wa kawaida.

## Hebu tuone jinsi hii inavyofanya kazi kwa vitendo

Katika [notebook ya mfano wa sehemu hii](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), tutaona mifano ya jinsi tunavyoweza kutumia zana za ufuatiliaji kufuatilia na kutathmini wakala wetu.

## Somo Lililopita

[Muundo wa Metakujitambua](../09-metacognition/README.md)

## Somo Lijalo

[MCP](../11-mcp/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.