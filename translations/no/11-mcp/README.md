<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:34+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "no"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integrasjon

## Introduksjon til Model Context Protocol (MCP)

Model Context Protocol (MCP) er en banebrytende rammeverk designet for å standardisere samhandling mellom AI-modeller og klientapplikasjoner. MCP fungerer som en bro mellom AI-modeller og applikasjonene som bruker dem, og tilbyr et konsistent grensesnitt uavhengig av den underliggende modellimplementeringen.

Viktige aspekter ved MCP:

- **Standardisert kommunikasjon**: MCP etablerer et felles språk for applikasjoner å kommunisere med AI-modeller
- **Forbedret kontekststyring**: Gjør det mulig å effektivt overføre kontekstuell informasjon til AI-modeller
- **Tverrplattform-kompatibilitet**: Fungerer på tvers av flere programmeringsspråk, inkludert C#, Java, JavaScript, Python og TypeScript
- **Sømløs integrasjon**: Gjør det enkelt for utviklere å integrere ulike AI-modeller i sine applikasjoner

MCP er spesielt verdifull i utvikling av AI-agenter, da det lar agenter samhandle med ulike systemer og datakilder gjennom en enhetlig protokoll, noe som gjør agentene mer fleksible og kraftfulle.

## Læringsmål
- Forstå hva MCP er og hvilken rolle det har i utvikling av AI-agenter
- Sette opp og konfigurere en MCP-server for GitHub-integrasjon
- Bygge et multi-agent system ved hjelp av MCP-verktøy
- Implementere RAG (Retrieval Augmented Generation) med Azure Cognitive Search

## Forutsetninger
- Python 3.8+
- Node.js 14+
- Azure-abonnement
- GitHub-konto
- Grunnleggende forståelse av Semantic Kernel

## Oppsettinstruksjoner

1. **Miljøoppsett**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurer Azure-tjenester**
   - Opprett en Azure Cognitive Search-ressurs
   - Sett opp Azure OpenAI-tjenesten
   - Konfigurer miljøvariabler i `.env`

3. **MCP Server-oppsett**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Prosjektstruktur

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

## Kjernekomponenter

### 1. Multi-Agent System
- GitHub Agent: Repository-analyse
- Hackathon Agent: Prosjektanbefalinger
- Events Agent: Forslag til teknologiske arrangementer

### 2. Azure-integrasjon
- Cognitive Search for indeksering av arrangementer
- Azure OpenAI for agentintelligens
- Implementering av RAG-mønsteret

### 3. MCP-verktøy
- Analyse av GitHub-repositorier
- Kodeinspeksjon
- Metadatauttrekk

## Gjennomgang av kode

Eksempelet viser:
1. MCP-serverintegrasjon
2. Orkestrering av multi-agent system
3. Integrasjon med Azure Cognitive Search
4. Implementering av RAG-mønsteret

Nøkkelfunksjoner:
- Sanntidsanalyse av GitHub-repositorier
- Intelligente prosjektanbefalinger
- Arrangementmatching ved bruk av Azure Search
- Strømming av svar med Chainlit

## Kjøre eksempelet

For detaljerte oppsettinstruksjoner og mer informasjon, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start MCP-serveren:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start applikasjonen:
   ```bash
   chainlit run app.py -w
   ```

3. Test integrasjonen:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Feilsøking

Vanlige problemer og løsninger:
1. MCP-tilkoblingsproblemer
   - Sjekk at serveren kjører
   - Kontroller at porten er tilgjengelig
   - Bekreft GitHub-tokens

2. Azure Search-problemer
   - Valider tilkoblingsstrenger
   - Sjekk at indeksen eksisterer
   - Bekreft opplasting av dokumenter

## Neste steg
- Utforsk flere MCP-verktøy
- Implementer egendefinerte agenter
- Forbedre RAG-funksjonalitet
- Legg til flere arrangementskilder

## Ressurser
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.