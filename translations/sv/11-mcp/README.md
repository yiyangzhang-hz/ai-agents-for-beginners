<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:14+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sv"
}
-->
# Lektion 11: Model Context Protocol (MCP) Integration

## Introduktion till Model Context Protocol (MCP)

Model Context Protocol (MCP) är ett avancerat ramverk som är utformat för att standardisera interaktioner mellan AI-modeller och klientapplikationer. MCP fungerar som en brygga mellan AI-modeller och de applikationer som använder dem, och erbjuder ett enhetligt gränssnitt oavsett underliggande modellimplementation.

Viktiga aspekter av MCP:

- **Standardiserad kommunikation**: MCP etablerar ett gemensamt språk för applikationer att kommunicera med AI-modeller
- **Förbättrad kontexthantering**: Möjliggör effektiv överföring av kontextuell information till AI-modeller
- **Plattformsoberoende kompatibilitet**: Fungerar över flera programmeringsspråk inklusive C#, Java, JavaScript, Python och TypeScript
- **Sömlös integration**: Gör det enkelt för utvecklare att integrera olika AI-modeller i sina applikationer

MCP är särskilt värdefullt vid utveckling av AI-agenter eftersom det tillåter agenter att interagera med olika system och datakällor via ett enhetligt protokoll, vilket gör agenterna mer flexibla och kraftfulla.

## Lärandemål
- Förstå vad MCP är och dess roll i utveckling av AI-agenter
- Sätta upp och konfigurera en MCP-server för GitHub-integration
- Bygga ett multi-agent system med MCP-verktyg
- Implementera RAG (Retrieval Augmented Generation) med Azure Cognitive Search

## Förkunskaper
- Python 3.8+
- Node.js 14+
- Azure-prenumeration
- GitHub-konto
- Grundläggande förståelse för Semantic Kernel

## Installationsinstruktioner

1. **Miljöinställning**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurera Azure-tjänster**
   - Skapa en Azure Cognitive Search-resurs
   - Sätt upp Azure OpenAI-tjänsten
   - Konfigurera miljövariabler i `.env`

3. **MCP-serverinställning**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektstruktur

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

## Kärnkomponenter

### 1. Multi-Agent System
- GitHub Agent: Repository-analys
- Hackathon Agent: Projektrekommendationer
- Events Agent: Förslag på teknikevenemang

### 2. Azure-integration
- Cognitive Search för indexering av evenemang
- Azure OpenAI för agentintelligens
- Implementering av RAG-mönstret

### 3. MCP-verktyg
- Analys av GitHub-repositorier
- Kodinspektion
- Metadatautvinning

## Genomgång av koden

Exemplet visar:
1. MCP-serverintegration
2. Multi-agent orkestrering
3. Azure Cognitive Search-integration
4. Implementering av RAG-mönstret

Viktiga funktioner:
- Realtidsanalys av GitHub-repositorier
- Intelligenta projektrekommendationer
- Matchning av evenemang med Azure Search
- Strömmande svar med Chainlit

## Köra exemplet

För detaljerade installationsinstruktioner och mer information, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Starta MCP-servern:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Starta applikationen:
   ```bash
   chainlit run app.py -w
   ```

3. Testa integrationen:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Felsökning

Vanliga problem och lösningar:
1. MCP-anslutningsproblem
   - Kontrollera att servern körs
   - Kontrollera porttillgänglighet
   - Bekräfta GitHub-token

2. Problem med Azure Search
   - Validera anslutningssträngar
   - Kontrollera att index finns
   - Verifiera dokumentuppladdning

## Nästa steg
- Utforska fler MCP-verktyg
- Implementera egna agenter
- Förbättra RAG-funktionalitet
- Lägg till fler evenemangskällor

## Resurser
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.