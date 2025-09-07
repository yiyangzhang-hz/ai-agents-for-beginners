<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T09:00:13+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sw"
}
-->
# Kutumia Itifaki za Wakala (MCP, A2A na NLWeb)

[![Itifaki za Wakala](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sw.png)](https://youtu.be/X-Dh9R3Opn8)

Kadri matumizi ya mawakala wa AI yanavyoongezeka, ndivyo pia hitaji la itifaki zinazohakikisha usanifishaji, usalama, na kuhimiza uvumbuzi wa wazi linavyoongezeka. Katika somo hili, tutajadili itifaki 3 zinazolenga kukidhi hitaji hili - Model Context Protocol (MCP), Agent to Agent (A2A) na Natural Language Web (NLWeb).

## Utangulizi

Katika somo hili, tutajadili:

• Jinsi **MCP** inavyowezesha Mawakala wa AI kufikia zana za nje na data ili kukamilisha kazi za mtumiaji.

• Jinsi **A2A** inavyowezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI.

• Jinsi **NLWeb** inavyowaletea tovuti kiolesura cha lugha asilia, kuwezesha Mawakala wa AI kugundua na kuingiliana na maudhui.

## Malengo ya Kujifunza

• **Tambua** madhumuni ya msingi na faida za MCP, A2A, na NLWeb katika muktadha wa mawakala wa AI.

• **Eleza** jinsi kila itifaki inavyorahisisha mawasiliano na mwingiliano kati ya LLMs, zana, na mawakala wengine.

• **Tambua** majukumu tofauti ya kila itifaki katika kujenga mifumo changamano ya wakala.

## Model Context Protocol

**Model Context Protocol (MCP)** ni kiwango cha wazi kinachotoa njia sanifu kwa programu kutoa muktadha na zana kwa LLMs. Hii inaruhusu "kiunganishi cha ulimwengu wote" kwa vyanzo tofauti vya data na zana ambazo Mawakala wa AI wanaweza kuziunganisha kwa njia thabiti.

Hebu tuangalie vipengele vya MCP, faida zake ikilinganishwa na matumizi ya API moja kwa moja, na mfano wa jinsi mawakala wa AI wanaweza kutumia seva ya MCP.

### Vipengele Muhimu vya MCP

MCP inafanya kazi kwa usanifu wa **mteja-seva**, na vipengele vyake vikuu ni:

• **Wenyeji** ni programu za LLM (kwa mfano, mhariri wa msimbo kama VSCode) zinazozindua miunganisho kwa seva ya MCP.

• **Wateja** ni vipengele ndani ya programu ya mwenyeji vinavyodumisha miunganisho ya moja kwa moja na seva.

• **Seva** ni programu nyepesi zinazofichua uwezo maalum.

Itifaki inajumuisha misingi mitatu muhimu ambayo ni uwezo wa seva ya MCP:

• **Zana**: Hizi ni hatua au kazi maalum ambazo wakala wa AI anaweza kuita ili kutekeleza hatua. Kwa mfano, huduma ya hali ya hewa inaweza kufichua zana ya "pata hali ya hewa," au seva ya biashara mtandaoni inaweza kufichua zana ya "nunua bidhaa." Seva za MCP hutangaza jina la kila zana, maelezo, na mpangilio wa pembejeo/mazao katika orodha yao ya uwezo.

• **Rasilimali**: Hizi ni vitu vya data vya kusomwa tu au nyaraka ambazo seva ya MCP inaweza kutoa, na wateja wanaweza kuzipata wanapohitaji. Mifano ni pamoja na maudhui ya faili, rekodi za hifadhidata, au faili za kumbukumbu. Rasilimali zinaweza kuwa maandishi (kama msimbo au JSON) au binary (kama picha au PDF).

• **Vichochezi**: Hizi ni violezo vilivyotangulia ambavyo vinatoa mapendekezo ya vichochezi, kuruhusu michakato changamano zaidi.

### Faida za MCP

MCP inatoa faida kubwa kwa Mawakala wa AI:

• **Ugunduzi wa Zana kwa Njia ya Nguvu**: Mawakala wanaweza kupokea orodha ya zana zinazopatikana kutoka kwa seva pamoja na maelezo ya kazi zake. Hii ni tofauti na API za jadi, ambazo mara nyingi zinahitaji usimbaji tuli kwa miunganisho, ikimaanisha mabadiliko yoyote ya API yanahitaji masasisho ya msimbo. MCP inatoa njia ya "unganisha mara moja," ikileta uwezo wa kubadilika zaidi.

• **Uingiliano Kati ya LLMs**: MCP inafanya kazi katika LLM tofauti, ikitoa kubadilika kwa kubadilisha mifano ya msingi ili kutathmini utendaji bora.

• **Usalama Sanifu**: MCP inajumuisha njia sanifu ya uthibitishaji, ikiboresha upanuzi wakati wa kuongeza ufikiaji kwa seva za MCP za ziada. Hii ni rahisi kuliko kusimamia funguo tofauti na aina za uthibitishaji kwa API za jadi.

### Mfano wa MCP

![Mchoro wa MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sw.png)

Fikiria mtumiaji anataka kuhifadhi tiketi ya ndege kwa kutumia msaidizi wa AI unaotumia MCP.

1. **Muunganisho**: Msaidizi wa AI (mteja wa MCP) unaunganisha na seva ya MCP inayotolewa na shirika la ndege.

2. **Ugunduzi wa Zana**: Mteja anauliza seva ya MCP ya shirika la ndege, "Una zana gani zinazopatikana?" Seva inajibu na zana kama "tafuta ndege" na "hifadhi ndege."

3. **Kuitisha Zana**: Unamuuliza msaidizi wa AI, "Tafadhali tafuta ndege kutoka Portland kwenda Honolulu." Msaidizi wa AI, akitumia LLM yake, anatambua kuwa inahitaji kuita zana ya "tafuta ndege" na kupitisha vigezo husika (asili, marudio) kwa seva ya MCP.

4. **Utekelezaji na Jibu**: Seva ya MCP, ikifanya kama kifuniko, inafanya wito halisi kwa API ya ndani ya uhifadhi wa shirika la ndege. Kisha inapokea taarifa za ndege (mfano, data ya JSON) na kuirudisha kwa msaidizi wa AI.

5. **Mwingiliano Zaidi**: Msaidizi wa AI anawasilisha chaguo za ndege. Mara unapochagua ndege, msaidizi anaweza kuita zana ya "hifadhi ndege" kwenye seva hiyo hiyo ya MCP, kukamilisha uhifadhi.

## Itifaki ya Wakala kwa Wakala (A2A)

Wakati MCP inalenga kuunganisha LLMs na zana, **Itifaki ya Wakala kwa Wakala (A2A)** inachukua hatua zaidi kwa kuwezesha mawasiliano na ushirikiano kati ya mawakala tofauti wa AI. A2A inaunganisha mawakala wa AI katika mashirika, mazingira, na mifumo tofauti ya teknolojia ili kukamilisha kazi ya pamoja.

Tutachunguza vipengele na faida za A2A, pamoja na mfano wa jinsi inaweza kutumika katika programu yetu ya usafiri.

### Vipengele Muhimu vya A2A

A2A inalenga kuwezesha mawasiliano kati ya mawakala na kuwafanya wafanye kazi pamoja kukamilisha kazi ndogo za mtumiaji. Kila kipengele cha itifaki huchangia hili:

#### Kadi ya Wakala

Kama vile seva ya MCP inavyoshiriki orodha ya zana, Kadi ya Wakala ina:

- Jina la Wakala.  
- **Maelezo ya kazi za jumla** inazokamilisha.  
- **Orodha ya ujuzi maalum** na maelezo kusaidia mawakala wengine (au hata watumiaji wa binadamu) kuelewa wakati na kwa nini wangependa kuita wakala huyo.  
- **URL ya sasa ya Endpoint** ya wakala.  
- **Toleo** na **uwezo** wa wakala kama vile majibu ya mtiririko na arifa za kushinikiza.  

#### Mtekelezaji wa Wakala

Mtekelezaji wa Wakala anawajibika kwa **kupitisha muktadha wa mazungumzo ya mtumiaji kwa wakala wa mbali**, wakala wa mbali unahitaji hili ili kuelewa kazi inayohitaji kukamilishwa. Katika seva ya A2A, wakala hutumia LLM yake mwenyewe kuchanganua maombi yanayoingia na kutekeleza kazi kwa kutumia zana zake za ndani.

#### Kifaa cha Kazi

Mara wakala wa mbali anapokamilisha kazi iliyoombwa, matokeo yake yanaundwa kama kifaa cha kazi. Kifaa cha kazi **kina matokeo ya kazi ya wakala**, **maelezo ya kilichokamilishwa**, na **muktadha wa maandishi** uliotumwa kupitia itifaki. Baada ya kifaa cha kazi kutumwa, muunganisho na wakala wa mbali hufungwa hadi utakapohitajika tena.

#### Foleni ya Matukio

Kipengele hiki kinatumika kwa **kushughulikia masasisho na kupitisha ujumbe**. Hii ni muhimu hasa katika uzalishaji wa mifumo ya wakala ili kuzuia muunganisho kati ya mawakala kufungwa kabla ya kazi kukamilika, hasa wakati wa kukamilisha kazi kunapochukua muda mrefu.

### Faida za A2A

• **Ushirikiano Ulioboreshwa**: Inawawezesha mawakala kutoka kwa wauzaji na majukwaa tofauti kuingiliana, kushiriki muktadha, na kufanya kazi pamoja, kuwezesha otomatiki isiyo na mshono katika mifumo ambayo hapo awali haikuunganishwa.  

• **Kubadilika kwa Uchaguzi wa Mfano**: Kila wakala wa A2A anaweza kuamua ni LLM gani itumie kuhudumia maombi yake, kuruhusu mifano iliyoboreshwa au iliyofanyiwa marekebisho kwa kila wakala, tofauti na muunganisho mmoja wa LLM katika baadhi ya hali za MCP.  

• **Uthibitishaji Uliojengwa Ndani**: Uthibitishaji umejumuishwa moja kwa moja katika itifaki ya A2A, ikitoa mfumo thabiti wa usalama kwa mwingiliano wa wakala.  

### Mfano wa A2A

![Mchoro wa A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sw.png)

Hebu tuendelee na hali yetu ya uhifadhi wa safari, lakini wakati huu tukitumia A2A.

1. **Ombi la Mtumiaji kwa Wakala wa Wakala Wengi**: Mtumiaji anawasiliana na "Wakala wa Usafiri" mteja/wakala wa A2A, labda kwa kusema, "Tafadhali niandalie safari nzima kwenda Honolulu wiki ijayo, ikijumuisha ndege, hoteli, na gari la kukodisha."

2. **Urushaji na Wakala wa Usafiri**: Wakala wa Usafiri anapokea ombi hili changamano. Anatumia LLM yake kufikiria kuhusu kazi hiyo na kuamua kwamba inahitaji kuingiliana na mawakala wengine maalum.

3. **Mawasiliano ya Wakala kwa Wakala**: Wakala wa Usafiri kisha hutumia itifaki ya A2A kuungana na mawakala wa chini, kama vile "Wakala wa Ndege," "Wakala wa Hoteli," na "Wakala wa Kukodisha Gari" ambao wameundwa na kampuni tofauti.

4. **Utekelezaji wa Kazi Uliokabidhiwa**: Wakala wa Usafiri hutuma kazi maalum kwa mawakala hawa maalum (mfano, "Tafuta ndege kwenda Honolulu," "Hifadhi hoteli," "Kukodisha gari"). Kila mmoja wa mawakala hawa maalum, wakitumia LLM zao na zana zao za ndani (ambazo zinaweza kuwa seva za MCP zenyewe), hutekeleza sehemu yake maalum ya uhifadhi.

5. **Jibu Lililounganishwa**: Mara mawakala wote wa chini wanapokamilisha kazi zao, Wakala wa Usafiri hukusanya matokeo (maelezo ya ndege, uthibitisho wa hoteli, uhifadhi wa gari la kukodisha) na kutuma jibu kamili, la mtindo wa mazungumzo, kwa mtumiaji.

## Mtandao wa Lugha Asilia (NLWeb)

Tovuti zimekuwa njia kuu kwa watumiaji kufikia taarifa na data kwenye mtandao.

Hebu tuangalie vipengele tofauti vya NLWeb, faida za NLWeb na mfano wa jinsi NLWeb inavyofanya kazi kwa kuangalia programu yetu ya usafiri.

### Vipengele vya NLWeb

- **Programu ya NLWeb (Msimbo wa Huduma ya Msingi)**: Mfumo unaochakata maswali ya lugha asilia. Inaunganisha sehemu tofauti za jukwaa ili kuunda majibu. Unaweza kuufikiria kama **injini inayowezesha vipengele vya lugha asilia** vya tovuti.

- **Itifaki ya NLWeb**: Hii ni **seti ya msingi ya sheria za mwingiliano wa lugha asilia** na tovuti. Inarudisha majibu katika muundo wa JSON (mara nyingi kwa kutumia Schema.org). Madhumuni yake ni kuunda msingi rahisi kwa “Mtandao wa AI,” kwa njia ile ile ambayo HTML ilifanya iwezekane kushiriki nyaraka mtandaoni.

- **Seva ya MCP (Endpoint ya Model Context Protocol)**: Kila usanidi wa NLWeb pia hufanya kazi kama **seva ya MCP**. Hii inamaanisha inaweza **kushiriki zana (kama njia ya “uliza”) na data** na mifumo mingine ya AI. Kwa vitendo, hii hufanya maudhui na uwezo wa tovuti kupatikana kwa mawakala wa AI, kuruhusu tovuti kuwa sehemu ya “mfumo wa wakala” mpana.

- **Mifano ya Uwekaji wa Vectors**: Mifano hii hutumika **kubadilisha maudhui ya tovuti kuwa uwakilishi wa nambari unaoitwa vectors** (uwekaji wa vectors). Vectors hizi hushika maana kwa njia ambayo kompyuta zinaweza kulinganisha na kutafuta. Zinahifadhiwa kwenye hifadhidata maalum, na watumiaji wanaweza kuchagua ni mfano gani wa uwekaji wa vectors wanataka kutumia.

- **Hifadhidata ya Vectors (Mfumo wa Urejeshaji)**: Hifadhidata hii **huhifadhi uwekaji wa vectors wa maudhui ya tovuti**. Wakati mtu anauliza swali, NLWeb hukagua hifadhidata ya vectors ili kupata haraka taarifa muhimu zaidi. Inatoa orodha ya haraka ya majibu yanayowezekana, yaliyopangwa kwa kufanana. NLWeb hufanya kazi na mifumo tofauti ya hifadhi ya vectors kama Qdrant, Snowflake, Milvus, Azure AI Search, na Elasticsearch.

### NLWeb kwa Mfano

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sw.png)

Fikiria tovuti yetu ya uhifadhi wa safari tena, lakini wakati huu, inaendeshwa na NLWeb.

1. **Uingizaji wa Data**: Katalogi zilizopo za bidhaa za tovuti ya safari (mfano, orodha za ndege, maelezo ya hoteli, vifurushi vya ziara) zimepangwa kwa kutumia Schema.org au kupakiwa kupitia milisho ya RSS. Zana za NLWeb zinachukua data hii iliyopangwa, kuunda uwekaji wa vectors, na kuuhifadhi kwenye hifadhidata ya vectors ya ndani au ya mbali.

2. **Swali la Lugha Asilia (Binadamu)**: Mtumiaji anatembelea tovuti na, badala ya kuvinjari menyu, anaandika kwenye kiolesura cha mazungumzo: "Nipatie hoteli inayofaa kwa familia huko Honolulu yenye bwawa la kuogelea kwa wiki ijayo."

3. **Usindikaji wa NLWeb**: Programu ya NLWeb inapokea swali hili. Inatuma swali kwa LLM kwa uelewa na wakati huo huo inatafuta hifadhidata yake ya vectors kwa orodha za hoteli zinazofaa.

4. **Matokeo Sahihi**: LLM husaidia kutafsiri matokeo ya utafutaji kutoka kwa hifadhidata, kutambua mechi bora kulingana na vigezo vya "inayofaa kwa familia," "bwawa la kuogelea," na "Honolulu," kisha kuunda jibu la lugha asilia. Muhimu, jibu linarejelea hoteli halisi kutoka kwa katalogi ya tovuti, kuepuka taarifa zilizotungwa.

5. **Mwingiliano wa Wakala wa AI**: Kwa sababu NLWeb inafanya kazi kama seva ya MCP, wakala wa nje wa AI wa usafiri pia angeweza kuungana na NLWeb ya tovuti hii. Wakala wa AI angeweza kutumia njia ya `uliza` ya MCP kuuliza tovuti moja kwa moja: `uliza("Je, kuna mikahawa inayofaa kwa wanyama wa mboga katika eneo la Honolulu inayopendekezwa na hoteli?")`. NLWeb ingechakata hili, ikitumia hifadhidata yake ya taarifa za mikahawa (ikiwa imepakiwa), na kurudisha jibu la JSON lililopangwa.

### Una Maswali Zaidi Kuhusu MCP/A2A/NLWeb?

Jiunge na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) ili kukutana na wanafunzi wengine, kuhudhuria saa za ofisi na kupata majibu ya maswali yako kuhusu Mawakala wa AI.

## Rasilimali

- [MCP kwa Anayeanza](https://aka.ms/mcp-for-beginners)  
- [Nyaraka za MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Repo ya NLWeb](https://github.com/nlweb-ai/NLWeb)  
- [Miongozo ya Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)  

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.