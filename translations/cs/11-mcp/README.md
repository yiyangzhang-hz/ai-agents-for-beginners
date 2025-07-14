<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:50:18+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "cs"
}
-->
# Lekce 11: Integrace Model Context Protocol (MCP)

## Úvod do Model Context Protocol (MCP)

Model Context Protocol (MCP) je moderní rámec navržený pro standardizaci komunikace mezi AI modely a klientskými aplikacemi. MCP slouží jako most mezi AI modely a aplikacemi, které je využívají, a poskytuje jednotné rozhraní bez ohledu na konkrétní implementaci modelu.

Klíčové vlastnosti MCP:

- **Standardizovaná komunikace**: MCP zavádí společný jazyk pro komunikaci aplikací s AI modely
- **Vylepšená správa kontextu**: Umožňuje efektivní předávání kontextu AI modelům
- **Kompatibilita napříč platformami**: Funguje v různých programovacích jazycích včetně C#, Java, JavaScript, Python a TypeScript
- **Bezproblémová integrace**: Vývojářům usnadňuje integraci různých AI modelů do jejich aplikací

MCP je obzvlášť užitečný při vývoji AI agentů, protože umožňuje agentům komunikovat s různými systémy a zdroji dat prostřednictvím jednotného protokolu, což zvyšuje jejich flexibilitu a výkon.

## Cíle učení
- Pochopit, co je MCP a jakou roli hraje ve vývoji AI agentů
- Nastavit a nakonfigurovat MCP server pro integraci s GitHubem
- Vytvořit multi-agentní systém pomocí nástrojů MCP
- Implementovat RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Požadavky
- Python 3.8+
- Node.js 14+
- Azure předplatné
- GitHub účet
- Základní znalost Semantic Kernel

## Instrukce pro nastavení

1. **Nastavení prostředí**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurace Azure služeb**
   - Vytvořte Azure Cognitive Search zdroj
   - Nastavte Azure OpenAI službu
   - Nakonfigurujte proměnné prostředí v `.env`

3. **Nastavení MCP serveru**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projektu

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

## Hlavní komponenty

### 1. Multi-agentní systém
- GitHub Agent: Analýza repozitářů
- Hackathon Agent: Doporučení projektů
- Events Agent: Návrhy technologických akcí

### 2. Integrace Azure
- Cognitive Search pro indexaci akcí
- Azure OpenAI pro inteligenci agentů
- Implementace RAG vzoru

### 3. MCP nástroje
- Analýza GitHub repozitářů
- Kontrola kódu
- Extrakce metadat

## Procházení kódu

Ukázka demonstruje:
1. Integraci MCP serveru
2. Orchestrace multi-agentního systému
3. Integraci Azure Cognitive Search
4. Implementaci RAG vzoru

Hlavní funkce:
- Analýza GitHub repozitářů v reálném čase
- Inteligentní doporučení projektů
- Párování akcí pomocí Azure Search
- Streamování odpovědí s Chainlit

## Spuštění ukázky

Pro podrobné instrukce a další informace navštivte [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Spusťte MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Spusťte aplikaci:
   ```bash
   chainlit run app.py -w
   ```

3. Otestujte integraci:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Řešení problémů

Běžné problémy a jejich řešení:
1. Problémy s připojením k MCP
   - Ověřte, že server běží
   - Zkontrolujte dostupnost portu
   - Potvrďte platnost GitHub tokenů

2. Problémy s Azure Search
   - Ověřte connection stringy
   - Zkontrolujte existenci indexu
   - Potvrďte nahrání dokumentů

## Další kroky
- Prozkoumejte další MCP nástroje
- Implementujte vlastní agenty
- Vylepšete schopnosti RAG
- Přidejte více zdrojů akcí

## Zdroje
- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentace](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentace Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Průvodce Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.