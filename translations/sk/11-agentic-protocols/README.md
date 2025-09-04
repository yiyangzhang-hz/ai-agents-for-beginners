<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T09:08:37+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "sk"
}
-->
# Používanie agentických protokolov (MCP, A2A a NLWeb)

[![Agentické protokoly](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.sk.png)](https://youtu.be/X-Dh9R3Opn8)

S rastúcim využívaním AI agentov rastie aj potreba protokolov, ktoré zabezpečujú štandardizáciu, bezpečnosť a podporujú otvorené inovácie. V tejto lekcii sa pozrieme na tri protokoly, ktoré sa snažia splniť tieto požiadavky – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii sa naučíme:

• Ako **MCP** umožňuje AI agentom prístup k externým nástrojom a dátam na splnenie úloh používateľa.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša rozhrania v prirodzenom jazyku na akúkoľvek webovú stránku, čím umožňuje AI agentom objavovať a interagovať s obsahom.

## Ciele učenia

• **Identifikovať** hlavný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť**, ako každý protokol uľahčuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozpoznať** odlišné úlohy, ktoré každý protokol zohráva pri budovaní komplexných agentických systémov.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob, ako môžu aplikácie poskytovať kontext a nástroje pre LLM. To umožňuje "univerzálny adaptér" na rôzne zdroje dát a nástroje, ku ktorým sa AI agenti môžu konzistentne pripájať.

Pozrime sa na komponenty MCP, výhody v porovnaní s priamym používaním API a príklad, ako by AI agenti mohli využívať MCP server.

### Hlavné komponenty MCP

MCP funguje na **klient-server architektúre** a jeho hlavné komponenty sú:

• **Hostitelia** sú LLM aplikácie (napríklad editor kódu ako VSCode), ktoré iniciujú pripojenia k MCP serveru.

• **Klienti** sú komponenty v rámci hostiteľskej aplikácie, ktoré udržiavajú jedinečné pripojenia k serverom.

• **Servery** sú ľahké programy, ktoré poskytujú špecifické schopnosti.

Protokol obsahuje tri hlavné primitívy, ktoré definujú schopnosti MCP servera:

• **Nástroje**: Ide o konkrétne akcie alebo funkcie, ktoré môže AI agent vyvolať na vykonanie úlohy. Napríklad, služba počasia môže ponúkať nástroj "získať počasie" alebo e-commerce server môže ponúkať nástroj "kúpiť produkt". MCP servery inzerujú názov, popis a schému vstupov/výstupov každého nástroja vo svojom zozname schopností.

• **Zdroje**: Ide o dáta alebo dokumenty iba na čítanie, ktoré môže MCP server poskytovať a klienti ich môžu na požiadanie získať. Príklady zahŕňajú obsah súborov, databázové záznamy alebo logy. Zdroje môžu byť textové (ako kód alebo JSON) alebo binárne (ako obrázky alebo PDF).

• **Šablóny**: Ide o preddefinované šablóny, ktoré poskytujú navrhované výzvy, umožňujúce zložitejšie pracovné postupy.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické objavovanie nástrojov**: Agenti môžu dynamicky prijímať zoznam dostupných nástrojov zo servera spolu s popismi ich funkcií. To je v kontraste s tradičnými API, ktoré často vyžadujú statické kódovanie pre integrácie, čo znamená, že akákoľvek zmena API si vyžaduje aktualizáciu kódu. MCP ponúka prístup "integrovať raz", čo vedie k väčšej prispôsobivosti.

• **Interoperabilita medzi LLM**: MCP funguje naprieč rôznymi LLM, čo poskytuje flexibilitu pri výbere modelov na základe výkonu.

• **Štandardizovaná bezpečnosť**: MCP obsahuje štandardnú metódu autentifikácie, čo zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. To je jednoduchšie ako správa rôznych kľúčov a typov autentifikácie pre rôzne tradičné API.

### Príklad MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.sk.png)

Predstavte si, že používateľ chce rezervovať let pomocou AI asistenta poháňaného MCP.

1. **Pripojenie**: AI asistent (MCP klient) sa pripojí k MCP serveru poskytovanému leteckou spoločnosťou.

2. **Objavovanie nástrojov**: Klient sa opýta MCP servera leteckej spoločnosti: "Aké nástroje máte k dispozícii?" Server odpovie nástrojmi ako "vyhľadať lety" a "rezervovať lety".

3. **Vyvolanie nástroja**: Používateľ požiada AI asistenta: "Prosím, vyhľadaj let z Portlandu do Honolulu." AI asistent, využívajúc svoj LLM, identifikuje, že potrebuje zavolať nástroj "vyhľadať lety" a odovzdá relevantné parametre (pôvod, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, ktorý funguje ako obal, vykoná skutočné volanie na interné API leteckej spoločnosti. Získa informácie o letoch (napr. JSON dáta) a pošle ich späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent predstaví možnosti letov. Keď si používateľ vyberie let, asistent môže vyvolať nástroj "rezervovať let" na tom istom MCP serveri, čím dokončí rezerváciu.

## Agent-to-Agent Protocol (A2A)

Kým MCP sa zameriava na pripojenie LLM k nástrojom, **Agent-to-Agent (A2A) protokol** ide o krok ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A spája AI agentov naprieč rôznymi organizáciami, prostrediami a technologickými zásobníkmi na splnenie spoločnej úlohy.

Preskúmame komponenty a výhody A2A spolu s príkladom jeho aplikácie v našej cestovnej aplikácii.

### Hlavné komponenty A2A

A2A sa zameriava na umožnenie komunikácie medzi agentmi a ich spoluprácu na splnení podúlohy používateľa. Každý komponent protokolu k tomu prispieva:

#### Agent Card

Podobne ako MCP server zdieľa zoznam nástrojov, Agent Card obsahuje:
- Názov agenta.
- **Popis všeobecných úloh**, ktoré vykonáva.
- **Zoznam špecifických zručností** s popismi, ktoré pomáhajú iným agentom (alebo dokonca ľudským používateľom) pochopiť, kedy a prečo by chceli zavolať tohto agenta.
- **Aktuálnu URL adresu koncového bodu** agenta.
- **Verziu** a **schopnosti** agenta, ako sú streamovanie odpovedí a push notifikácie.

#### Agent Executor

Agent Executor je zodpovedný za **odovzdanie kontextu používateľského rozhovoru vzdialenému agentovi**, ktorý tento kontext potrebuje na pochopenie úlohy, ktorú má splniť. V A2A serveri agent používa svoj vlastný Large Language Model (LLM) na spracovanie prichádzajúcich požiadaviek a vykonávanie úloh pomocou svojich interných nástrojov.

#### Artefakt

Keď vzdialený agent dokončí požadovanú úlohu, jeho výsledok sa vytvorí ako artefakt. Artefakt **obsahuje výsledok práce agenta**, **popis toho, čo bolo dokončené**, a **textový kontext**, ktorý sa posiela cez protokol. Po odoslaní artefaktu sa spojenie s vzdialeným agentom uzavrie, kým nebude opäť potrebné.

#### Fronta udalostí

Tento komponent sa používa na **spracovanie aktualizácií a odovzdávanie správ**. Je obzvlášť dôležitý v produkčných agentických systémoch, aby sa zabránilo uzavretiu spojenia medzi agentmi pred dokončením úlohy, najmä keď dokončenie úlohy môže trvať dlhší čas.

### Výhody A2A

• **Zlepšená spolupráca**: Umožňuje agentom od rôznych dodávateľov a platforiem interagovať, zdieľať kontext a spolupracovať, čím uľahčuje automatizáciu naprieč tradične oddelenými systémami.

• **Flexibilita výberu modelu**: Každý A2A agent si môže vybrať, ktorý LLM použije na spracovanie svojich požiadaviek, čo umožňuje optimalizované alebo špecificky prispôsobené modely pre jednotlivých agentov, na rozdiel od jedného LLM pripojenia v niektorých scenároch MCP.

• **Integrovaná autentifikácia**: Autentifikácia je priamo integrovaná do A2A protokolu, čo poskytuje robustný bezpečnostný rámec pre interakcie agentov.

### Príklad A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.sk.png)

Rozšírme náš scenár rezervácie cesty, tentokrát pomocou A2A.

1. **Požiadavka používateľa na multi-agenta**: Používateľ komunikuje s "Cestovným agentom" (A2A klient/agent), napríklad slovami: "Prosím, zarezervuj celú cestu do Honolulu na budúci týždeň, vrátane letu, hotela a prenájmu auta."

2. **Orchestrácia cestovným agentom**: Cestovný agent prijme túto komplexnú požiadavku. Použije svoj LLM na analýzu úlohy a určí, že potrebuje komunikovať s inými špecializovanými agentmi.

3. **Komunikácia medzi agentmi**: Cestovný agent potom použije A2A protokol na pripojenie k downstream agentom, ako sú "Letecký agent", "Hotelový agent" a "Agent na prenájom áut", ktoré vytvorili rôzne spoločnosti.

4. **Delegované vykonanie úloh**: Cestovný agent pošle špecifické úlohy týmto špecializovaným agentom (napr. "Nájdi lety do Honolulu", "Rezervuj hotel", "Prenajmi auto"). Každý z týchto špecializovaných agentov, ktorý prevádzkuje svoje vlastné LLM a využíva svoje vlastné nástroje (ktoré môžu byť sami MCP servery), vykoná svoju špecifickú časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci downstream agenti dokončia svoje úlohy, cestovný agent skompiluje výsledky (detaily letu, potvrdenie hotela, rezerváciu auta) a pošle komplexnú, chatovú odpoveď späť používateľovi.

## Natural Language Web (NLWeb)

Webové stránky už dlho slúžia ako primárny spôsob, ako používatelia získavajú informácie a dáta na internete.

Pozrime sa na rôzne komponenty NLWeb, výhody NLWeb a príklad, ako NLWeb funguje v našej cestovnej aplikácii.

### Komponenty NLWeb

- **NLWeb aplikácia (jadrový kód služby)**: Systém, ktorý spracováva otázky v prirodzenom jazyku. Spája rôzne časti platformy na vytváranie odpovedí. Môžete si ho predstaviť ako **motor, ktorý poháňa funkcie prirodzeného jazyka** na webovej stránke.

- **NLWeb protokol**: Ide o **základný súbor pravidiel pre interakciu v prirodzenom jazyku** s webovou stránkou. Posiela odpovede vo formáte JSON (často pomocou Schema.org). Jeho účelom je vytvoriť jednoduchý základ pre "AI Web", podobne ako HTML umožnil zdieľanie dokumentov online.

- **MCP server (Model Context Protocol Endpoint)**: Každé nastavenie NLWeb funguje aj ako **MCP server**. To znamená, že môže **zdieľať nástroje (napríklad metódu "ask") a dáta** s inými AI systémami. V praxi to umožňuje, aby obsah a schopnosti webovej stránky boli použiteľné AI agentmi, čím sa stránka stáva súčasťou širšieho "ekosystému agentov".

- **Modely vkladania (Embedding Models)**: Tieto modely sa používajú na **konverziu obsahu webovej stránky na číselné reprezentácie nazývané vektory** (embeddingy). Tieto vektory zachytávajú význam spôsobom, ktorý počítače dokážu porovnávať a vyhľadávať. Sú uložené v špeciálnej databáze a používatelia si môžu vybrať, ktorý model vkladania chcú použiť.

- **Vektorová databáza (mechanizmus vyhľadávania)**: Táto databáza **ukladá embeddingy obsahu webovej stránky**. Keď niekto položí otázku, NLWeb skontroluje vektorovú databázu, aby rýchlo našiel najrelevantnejšie informácie. Poskytuje rýchly zoznam možných odpovedí, zoradených podľa podobnosti. NLWeb pracuje s rôznymi systémami na ukladanie vektorov, ako sú Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.sk.png)

Zvážme našu cestovnú webovú stránku, tentokrát poháňanú NLWeb.

1. **Získavanie dát**: Existujúce katalógy produktov cestovnej webovej stránky (napr. zoznamy letov, popisy hotelov, balíčky zájazdov) sú naformátované pomocou Schema.org alebo načítané prostredníctvom RSS feedov. Nástroje NLWeb spracujú tieto štruktúrované dáta, vytvoria embeddingy a uložia ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Dotaz v prirodzenom jazyku (človek)**: Používateľ navštívi webovú stránku a namiesto prechádzania menu zadá do chatového rozhrania: "Nájdi mi rodinný hotel v Honolulu s bazénom na budúci týždeň."

3. **Spracovanie NLWeb**: NLWeb aplikácia prijme tento dotaz. Pošle dotaz do LLM na pochopenie a zároveň prehľadá svoju vektorovú databázu pre relevantné hotelové ponuky.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, identifikovať najlepšie zhody na základe kritérií "rodinný", "bazén" a "Honolulu" a potom formátuje odpoveď v prirodzenom jazyku. Dôležité je, že odpoveď odkazuje na skutočné hotely z katalógu webovej stránky, čím sa vyhýba vymysleným informáciám.

5. **Interakcia AI agenta**: Pretože NLWeb slúži ako MCP server, externý AI cestovný agent by sa mohol tiež pripojiť k NLWeb inštancii tejto webovej stránky. AI agent by potom mohol použiť metódu `ask` MCP na priamy dotaz na webovú stránku: `ask("Sú v oblasti Honolulu vegánske reštaurácie odporúčané hotelom?")`. NLWeb inštancia by to spracovala, využila svoju databázu informácií o reštauráciách (ak je načítaná) a vrátila štruktúrovanú JSON odpoveď.

### Máte ďalšie otázky o MCP/A2A/NLWeb?

Pridajte sa na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [MCP

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny preklad vykonaný človekom. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.