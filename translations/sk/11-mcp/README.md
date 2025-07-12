<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:50:30+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sk"
}
-->
# Lekcia 11: Integrácia Model Context Protocol (MCP)

## Úvod do Model Context Protocol (MCP)

Model Context Protocol (MCP) je moderný rámec navrhnutý na štandardizáciu interakcií medzi AI modelmi a klientskymi aplikáciami. MCP slúži ako most medzi AI modelmi a aplikáciami, ktoré ich používajú, a poskytuje jednotné rozhranie bez ohľadu na implementáciu samotného modelu.

Kľúčové aspekty MCP:

- **Štandardizovaná komunikácia**: MCP vytvára spoločný jazyk pre aplikácie na komunikáciu s AI modelmi
- **Vylepšené riadenie kontextu**: Umožňuje efektívne odovzdávanie kontextuálnych informácií AI modelom
- **Kompatibilita naprieč platformami**: Funguje v rôznych programovacích jazykoch vrátane C#, Java, JavaScript, Python a TypeScript
- **Bezproblémová integrácia**: Vývojárom umožňuje ľahko integrovať rôzne AI modely do ich aplikácií

MCP je obzvlášť cenný pri vývoji AI agentov, pretože umožňuje agentom komunikovať s rôznymi systémami a zdrojmi dát prostredníctvom jednotného protokolu, čím sa agenti stávajú flexibilnejšími a výkonnejšími.

## Ciele učenia
- Pochopiť, čo je MCP a jeho úlohu vo vývoji AI agentov
- Nastaviť a nakonfigurovať MCP server pre integráciu s GitHubom
- Vytvoriť multi-agentný systém pomocou MCP nástrojov
- Implementovať RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Predpoklady
- Python 3.8+
- Node.js 14+
- Predplatné Azure
- GitHub účet
- Základné znalosti Semantic Kernel

## Inštrukcie na nastavenie

1. **Nastavenie prostredia**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurácia Azure služieb**
   - Vytvorte Azure Cognitive Search zdroj
   - Nastavte Azure OpenAI službu
   - Nakonfigurujte premenné prostredia v `.env`

3. **Nastavenie MCP servera**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Štruktúra projektu

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

## Hlavné komponenty

### 1. Multi-agentný systém
- GitHub Agent: Analýza repozitárov
- Hackathon Agent: Odporúčania projektov
- Events Agent: Návrhy technologických podujatí

### 2. Integrácia Azure
- Cognitive Search pre indexovanie podujatí
- Azure OpenAI pre inteligenciu agentov
- Implementácia RAG vzoru

### 3. MCP nástroje
- Analýza GitHub repozitárov
- Kontrola kódu
- Extrakcia metadát

## Prehľad kódu

Ukážka demonštruje:
1. Integráciu MCP servera
2. Orchestru multi-agentov
3. Integráciu Azure Cognitive Search
4. Implementáciu RAG vzoru

Kľúčové funkcie:
- Analýza GitHub repozitárov v reálnom čase
- Inteligentné odporúčania projektov
- Zladenie podujatí pomocou Azure Search
- Streamovanie odpovedí s Chainlit

## Spustenie ukážky

Pre podrobné inštrukcie a ďalšie informácie si pozrite [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Spustite MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Spustite aplikáciu:
   ```bash
   chainlit run app.py -w
   ```

3. Otestujte integráciu:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Riešenie problémov

Bežné problémy a riešenia:
1. Problémy s pripojením MCP
   - Skontrolujte, či server beží
   - Overte dostupnosť portu
   - Potvrďte platnosť GitHub tokenov

2. Problémy s Azure Search
   - Overte pripojovacie reťazce
   - Skontrolujte existenciu indexu
   - Potvrďte nahratie dokumentov

## Ďalšie kroky
- Preskúmajte ďalšie MCP nástroje
- Implementujte vlastných agentov
- Vylepšite schopnosti RAG
- Pridajte viac zdrojov podujatí

## Zdroje
- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentácia](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentácia Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Príručky Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.