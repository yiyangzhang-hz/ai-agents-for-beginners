<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-23T09:10:24+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "sk"
}
-->
# AI agenti v produkcii: Pozorovateľnosť a hodnotenie

Keď sa AI agenti presúvajú z experimentálnych prototypov do reálnych aplikácií, schopnosť porozumieť ich správaniu, monitorovať ich výkon a systematicky hodnotiť ich výstupy sa stáva kľúčovou.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť/rozumieť:
- Základné koncepty pozorovateľnosti a hodnotenia agentov
- Techniky na zlepšenie výkonu, nákladov a efektívnosti agentov
- Čo a ako systematicky hodnotiť u vašich AI agentov
- Ako kontrolovať náklady pri nasadzovaní AI agentov do produkcie
- Ako implementovať pozorovateľnosť u agentov vytvorených pomocou AutoGen

Cieľom je vybaviť vás vedomosťami, ktoré transformujú vašich "čiernych skrinkových" agentov na transparentné, spravovateľné a spoľahlivé systémy.

_**Poznámka:** Je dôležité nasadzovať AI agentov, ktorí sú bezpeční a dôveryhodní. Pozrite si lekciu [Budovanie dôveryhodných AI agentov](./06-building-trustworthy-agents/README.md)._

## Trasy a úseky

Nástroje na pozorovateľnosť, ako napríklad [Langfuse](https://langfuse.com/) alebo [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zvyčajne reprezentujú behy agentov ako trasy a úseky.

- **Trasa** predstavuje kompletnú úlohu agenta od začiatku do konca (napríklad spracovanie používateľského dotazu).
- **Úseky** sú jednotlivé kroky v rámci trasy (napríklad volanie jazykového modelu alebo získavanie údajov).

![Strom trás v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bez pozorovateľnosti môže AI agent pôsobiť ako "čierna skrinka" – jeho vnútorný stav a uvažovanie sú nejasné, čo sťažuje diagnostiku problémov alebo optimalizáciu výkonu. S pozorovateľnosťou sa agenti stávajú "sklenenými skrinkami", poskytujúcimi transparentnosť, ktorá je nevyhnutná na budovanie dôvery a zabezpečenie správneho fungovania.

## Prečo je pozorovateľnosť dôležitá v produkčnom prostredí

Presun AI agentov do produkčného prostredia prináša nové výzvy a požiadavky. Pozorovateľnosť už nie je len "pekný doplnok", ale kritická schopnosť:

*   **Ladenie a analýza príčin problémov**: Keď agent zlyhá alebo poskytne neočakávaný výstup, nástroje na pozorovateľnosť poskytujú trasy potrebné na identifikáciu zdroja chyby. To je obzvlášť dôležité pri komplexných agentoch, ktoré môžu zahŕňať viacero volaní LLM, interakcie s nástrojmi a podmienenú logiku.
*   **Riadenie latencie a nákladov**: AI agenti často využívajú LLM a iné externé API, ktoré sú účtované za token alebo volanie. Pozorovateľnosť umožňuje presné sledovanie týchto volaní, čo pomáha identifikovať operácie, ktoré sú príliš pomalé alebo drahé. To umožňuje tímom optimalizovať výzvy, vybrať efektívnejšie modely alebo prepracovať pracovné postupy na riadenie prevádzkových nákladov a zabezpečenie dobrého používateľského zážitku.
*   **Dôvera, bezpečnosť a súlad**: V mnohých aplikáciách je dôležité zabezpečiť, aby agenti konali bezpečne a eticky. Pozorovateľnosť poskytuje auditnú stopu akcií a rozhodnutí agenta. To môže byť použité na detekciu a zmiernenie problémov, ako je injekcia výziev, generovanie škodlivého obsahu alebo nesprávne nakladanie s osobne identifikovateľnými informáciami (PII). Napríklad môžete preskúmať trasy, aby ste pochopili, prečo agent poskytol určitú odpoveď alebo použil konkrétny nástroj.
*   **Kontinuálne zlepšovanie**: Dáta z pozorovateľnosti sú základom iteratívneho vývojového procesu. Monitorovaním výkonu agentov v reálnom svete môžu tímy identifikovať oblasti na zlepšenie, zhromažďovať údaje na doladenie modelov a overovať dopad zmien. To vytvára spätnú väzbu, kde produkčné poznatky z online hodnotenia informujú offline experimentovanie a zdokonaľovanie, čo vedie k postupne lepšiemu výkonu agentov.

## Kľúčové metriky na sledovanie

Na monitorovanie a pochopenie správania agenta by sa mal sledovať rad metrík a signálov. Hoci konkrétne metriky sa môžu líšiť v závislosti od účelu agenta, niektoré sú univerzálne dôležité.

Tu sú niektoré z najbežnejších metrík, ktoré nástroje na pozorovateľnosť monitorujú:

**Latencia:** Ako rýchlo agent reaguje? Dlhé čakacie doby negatívne ovplyvňujú používateľský zážitok. Mali by ste merať latenciu úloh a jednotlivých krokov sledovaním behov agenta. Napríklad agent, ktorý potrebuje 20 sekúnd na všetky volania modelu, by mohol byť zrýchlený použitím rýchlejšieho modelu alebo paralelným spustením volaní modelu.

**Náklady:** Aké sú náklady na jeden beh agenta? AI agenti sa spoliehajú na volania LLM účtované za token alebo externé API. Časté používanie nástrojov alebo viacero výziev môže rýchlo zvýšiť náklady. Napríklad, ak agent volá LLM päťkrát pre marginálne zlepšenie kvality, musíte posúdiť, či sú náklady opodstatnené, alebo či by ste mohli znížiť počet volaní alebo použiť lacnejší model. Monitorovanie v reálnom čase môže tiež pomôcť identifikovať neočakávané výkyvy (napr. chyby spôsobujúce nadmerné slučky API).

**Chyby požiadaviek:** Koľko požiadaviek agent zlyhal? To môže zahŕňať chyby API alebo zlyhané volania nástrojov. Aby bol váš agent v produkcii robustnejší voči týmto chybám, môžete nastaviť záložné riešenia alebo opakovania. Napríklad, ak je poskytovateľ LLM A nedostupný, prepnete na poskytovateľa LLM B ako zálohu.

**Spätná väzba od používateľov:** Implementácia priameho hodnotenia používateľmi poskytuje cenné poznatky. To môže zahŕňať explicitné hodnotenia (👍palec hore/👎dole, ⭐1-5 hviezdičiek) alebo textové komentáre. Konzistentná negatívna spätná väzba by vás mala upozorniť, pretože to je znak, že agent nefunguje podľa očakávania.

**Implicitná spätná väzba od používateľov:** Správanie používateľov poskytuje nepriame hodnotenie aj bez explicitných hodnotení. To môže zahŕňať okamžité preformulovanie otázky, opakované dotazy alebo kliknutie na tlačidlo opakovania. Napríklad, ak vidíte, že používatelia opakovane kladú tú istú otázku, je to znak, že agent nefunguje podľa očakávania.

**Presnosť:** Ako často agent produkuje správne alebo žiaduce výstupy? Definície presnosti sa líšia (napr. správnosť riešenia problémov, presnosť získavania informácií, spokojnosť používateľov). Prvým krokom je definovať, čo pre vášho agenta znamená úspech. Presnosť môžete sledovať prostredníctvom automatizovaných kontrol, hodnotiacich skóre alebo označení dokončenia úloh. Napríklad označením trás ako "úspešné" alebo "neúspešné".

**Automatizované hodnotiace metriky:** Môžete tiež nastaviť automatizované hodnotenia. Napríklad môžete použiť LLM na hodnotenie výstupu agenta, napr. či je užitočný, presný alebo nie. Existuje tiež niekoľko open source knižníc, ktoré vám pomôžu hodnotiť rôzne aspekty agenta. Napr. [RAGAS](https://docs.ragas.io/) pre RAG agentov alebo [LLM Guard](https://llm-guard.com/) na detekciu škodlivého jazyka alebo injekcie výziev.

V praxi kombinácia týchto metrík poskytuje najlepšie pokrytie zdravia AI agenta. V [príkladovom notebooku](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) tejto kapitoly vám ukážeme, ako tieto metriky vyzerajú v reálnych príkladoch, ale najprv sa naučíme, ako vyzerá typický hodnotiaci pracovný postup.

## Implementácia pozorovateľnosti agenta

Na zhromažďovanie údajov o trasách budete musieť implementovať pozorovateľnosť do vášho kódu. Cieľom je upraviť kód agenta tak, aby emitoval trasy a metriky, ktoré môžu byť zachytené, spracované a vizualizované platformou na pozorovateľnosť.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) sa stalo priemyselným štandardom pre pozorovateľnosť LLM. Poskytuje sadu API, SDK a nástrojov na generovanie, zhromažďovanie a export telemetrických údajov.

Existuje mnoho knižníc na implementáciu pozorovateľnosti, ktoré obalujú existujúce rámce agentov a uľahčujú export úsekov OpenTelemetry do nástroja na pozorovateľnosť. Nižšie je príklad implementácie agenta AutoGen pomocou knižnice [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Príkladový notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) v tejto kapitole ukáže, ako implementovať pozorovateľnosť u vášho agenta AutoGen.

**Manuálne vytváranie úsekov:** Hoci knižnice na implementáciu pozorovateľnosti poskytujú dobrý základ, často existujú prípady, keď je potrebné podrobnejšie alebo vlastné informácie. Môžete manuálne vytvárať úseky na pridanie vlastnej aplikačnej logiky. Dôležitejšie je, že môžu obohatiť automaticky alebo manuálne vytvorené úseky o vlastné atribúty (známe aj ako značky alebo metadáta). Tieto atribúty môžu zahŕňať údaje špecifické pre podnikanie, medzivýpočty alebo akýkoľvek kontext, ktorý môže byť užitočný na ladenie alebo analýzu, ako napríklad `user_id`, `session_id` alebo `model_version`.

Príklad manuálneho vytvárania trás a úsekov pomocou [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnotenie agenta

Pozorovateľnosť nám poskytuje metriky, ale hodnotenie je proces analýzy týchto údajov (a vykonávania testov) na určenie, ako dobre AI agent funguje a ako ho možno zlepšiť. Inými slovami, keď máte trasy a metriky, ako ich využijete na posúdenie agenta a prijímanie rozhodnutí?

Pravidelné hodnotenie je dôležité, pretože AI agenti sú často nedeterministickí a môžu sa vyvíjať (prostredníctvom aktualizácií alebo zmeny správania modelu) – bez hodnotenia by ste nevedeli, či váš "inteligentný agent" skutočne plní svoju úlohu dobre alebo či sa zhoršil.

Existujú dve kategórie hodnotení AI agentov: **online hodnotenie** a **offline hodnotenie**. Obe sú hodnotné a navzájom sa dopĺňajú. Zvyčajne začíname s offline hodnotením, pretože to je minimálny potrebný krok pred nasadením akéhokoľvek agenta.

### Offline hodnotenie

![Položky datasetu v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Toto zahŕňa hodnotenie agenta v kontrolovanom prostredí, zvyčajne pomocou testovacích datasetov, nie živých používateľských dotazov. Používate kurátorské datasety, kde viete, aký je očakávaný výstup alebo správne správanie, a potom na nich spustíte vášho agenta.

Napríklad, ak ste vytvorili agenta na riešenie matematických slovných úloh, môžete mať [testovací dataset](https://huggingface.co/datasets/gsm8k) so 100 úlohami s známymi odpoveďami. Offline hodnotenie sa často vykonáva počas vývoja (a môže byť súčasťou CI/CD pipeline) na kontrolu zlepšení alebo ochranu pred regresiami. Výhodou je, že je **opakované a môžete získať jasné metriky presnosti, pretože máte referenčné hodnoty**. Môžete tiež simulovať používateľské dotazy a merať odpovede agenta voči ideálnym odpovediam alebo použiť automatizované metriky, ako je uvedené vyššie.

Hlavnou výzvou pri offline hodnotení je zabezpečiť, aby váš testovací dataset bol komplexný a zostal relevantný – agent môže dobre fungovať na pevnom testovacom sete, ale naraziť na veľmi odlišné dotazy v produkcii. Preto by ste mali testovacie sety aktualizovať novými hraničnými prípadmi a príkladmi, ktoré odrážajú reálne scenáre​. Kombinácia malých "rýchlych testovacích" prípadov a väčších hodnotiacich setov je užitočná: malé sety na rýchle kontroly a väčšie na širšie metriky výkonu​.

### Online hodnotenie 

![Prehľad metrík pozorovateľnosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Toto sa týka hodnotenia agenta v živom, reálnom prostredí, teda počas skutočného používania v produkcii. Online hodnotenie zahŕňa monitorovanie výkonu agenta na reálnych interakciách používateľov a neustálu analýzu výsledkov.

Napríklad môžete sledovať miery úspešnosti, skóre spokojnosti používateľov alebo iné metriky na živom prenose. Výhodou online hodnotenia je, že **zachytáva veci, ktoré by ste v laboratórnom prostredí nemuseli predvídať** – môžete pozorovať zmenu modelu v priebehu času (ak sa účinnosť agenta zhoršuje, keď sa menia vzory vstupov) a zachytiť neočakávané dotazy alebo situácie, ktoré neboli v testovacích dátach​. Poskytuje skutočný obraz o tom, ako sa agent správa v reálnom svete.

Online hodnotenie často zahŕňa zhromažďovanie implicitnej a explicitnej spätnej väzby od používateľov, ako bolo uvedené, a prípadne spúšťanie tieňových testov alebo A/B testov (kde nová verzia agenta beží paralelne na porovnanie so starou). Výzvou je, že môže byť náročné získať spoľahlivé označenia alebo skóre pre živé interakcie – môžete sa spoliehať na spätnú väzbu od používateľov alebo downstream metriky (napríklad či používateľ klikol na výsledok).

### Kombinácia oboch

Online a offline hodnotenia nie sú navzájom vylučujúce; sú vysoko komplementárne. Poznatky z online monitorovania (napr. nové typy používateľských dotazov, kde agent funguje zle) môžu byť použité na rozšírenie a zlepšenie offline testovacích datasetov. Naopak, agenti, ktorí dobre fungujú v offline testoch, môžu byť potom s väčšou istotou nasadení a monitorovaní online.

V skutočnosti mnoho tímov prijíma cyklus:

_hodnotenie offline -> nasadenie -> monitorovanie online -> zhromažďovanie nových prípadov zlyhania -> pridanie do offline datasetu -> zdokonalenie agenta -> opakovanie_.

## Bežné problémy

Pri nasadzovaní AI agentov do produkcie sa môžete stretnúť s rôznymi výzvami. Tu sú niektoré bežné problémy a ich možné riešenia:

| **Problém**   

- Upravte definované parametre, výzvy a názvy nástrojov.  |
| Multi-agentový systém nefunguje konzistentne | - Upravte výzvy pre každého agenta tak, aby boli špecifické a odlišné od seba.<br>- Vytvorte hierarchický systém pomocou "smerovacieho" alebo riadiaceho agenta, ktorý určí, ktorý agent je ten správny. |

Mnohé z týchto problémov je možné identifikovať efektívnejšie, ak je zavedená pozorovateľnosť. Stopy a metriky, o ktorých sme hovorili skôr, pomáhajú presne určiť, kde v pracovnom postupe agenta dochádza k problémom, čo robí ladenie a optimalizáciu oveľa efektívnejšími.

## Riadenie nákladov

Tu sú niektoré stratégie na riadenie nákladov pri nasadzovaní AI agentov do produkcie:

**Používanie menších modelov:** Malé jazykové modely (Small Language Models, SLMs) môžu dobre fungovať pri určitých agentických prípadoch použitia a výrazne znížia náklady. Ako sme už spomenuli, vytvorenie hodnotiaceho systému na určenie a porovnanie výkonu oproti väčším modelom je najlepší spôsob, ako pochopiť, ako dobre bude SLM fungovať vo vašom prípade použitia. Zvážte použitie SLM pre jednoduchšie úlohy, ako je klasifikácia zámerov alebo extrakcia parametrov, a väčšie modely si ponechajte na zložité úvahy.

**Používanie smerovacieho modelu:** Podobnou stratégiou je použitie rôznorodých modelov a ich veľkostí. Môžete použiť LLM/SLM alebo serverless funkciu na smerovanie požiadaviek na základe ich zložitosti k najvhodnejším modelom. To pomôže znížiť náklady a zároveň zabezpečiť výkon pri správnych úlohách. Napríklad, jednoduché dotazy smerujte na menšie, rýchlejšie modely a drahé veľké modely používajte iba na zložité úlohy vyžadujúce hlboké uvažovanie.

**Ukladanie odpovedí do vyrovnávacej pamäte:** Identifikácia bežných požiadaviek a úloh a poskytovanie odpovedí ešte predtým, ako prejdú vaším agentickým systémom, je dobrý spôsob, ako znížiť objem podobných požiadaviek. Môžete dokonca implementovať proces na určenie, ako podobná je požiadavka voči vašim uloženým odpovediam, pomocou jednoduchších AI modelov. Táto stratégia môže výrazne znížiť náklady na často kladené otázky alebo bežné pracovné postupy.

## Pozrime sa, ako to funguje v praxi

V [ukážkovom notebooku tejto sekcie](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) uvidíme príklady, ako môžeme používať nástroje na pozorovateľnosť na monitorovanie a hodnotenie nášho agenta.

## Predchádzajúca lekcia

[Metakognitívny návrhový vzor](../09-metacognition/README.md)

## Nasledujúca lekcia

[MCP](../11-mcp/README.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.