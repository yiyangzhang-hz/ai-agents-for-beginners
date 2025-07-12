<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:24+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "da"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Introduktion til Model Context Protocol (MCP)

Model Context Protocol (MCP) er en banebrydende ramme, der er designet til at standardisere interaktioner mellem AI-modeller og klientapplikationer. MCP fungerer som en bro mellem AI-modeller og de applikationer, der bruger dem, og tilbyder en ensartet grænseflade uanset den underliggende modelimplementering.

Vigtige aspekter ved MCP:

- **Standardiseret kommunikation**: MCP etablerer et fælles sprog for applikationer til at kommunikere med AI-modeller  
- **Forbedret kontekststyring**: Muliggør effektiv overførsel af kontekstuel information til AI-modeller  
- **Platformuafhængig kompatibilitet**: Fungerer på tværs af forskellige programmeringssprog, herunder C#, Java, JavaScript, Python og TypeScript  
- **Sømløs integration**: Gør det nemt for udviklere at integrere forskellige AI-modeller i deres applikationer  

MCP er særligt værdifuld i udviklingen af AI-agenter, da den tillader agenter at interagere med forskellige systemer og datakilder gennem en samlet protokol, hvilket gør agenterne mere fleksible og kraftfulde.

## Læringsmål
- Forstå hvad MCP er, og hvilken rolle det spiller i udviklingen af AI-agenter  
- Opsætte og konfigurere en MCP-server til GitHub-integration  
- Bygge et multi-agent system ved hjælp af MCP-værktøjer  
- Implementere RAG (Retrieval Augmented Generation) med Azure Cognitive Search  

## Forudsætninger
- Python 3.8+  
- Node.js 14+  
- Azure-abonnement  
- GitHub-konto  
- Grundlæggende forståelse af Semantic Kernel  

## Opsætningsvejledning

1. **Miljøopsætning**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurer Azure-tjenester**  
   - Opret en Azure Cognitive Search-ressource  
   - Opsæt Azure OpenAI-service  
   - Konfigurer miljøvariabler i `.env`  

3. **MCP Serveropsætning**  
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

## Kernekomponenter

### 1. Multi-Agent System  
- GitHub Agent: Repository-analyse  
- Hackathon Agent: Projektanbefalinger  
- Events Agent: Forslag til teknologibegivenheder  

### 2. Azure Integration  
- Cognitive Search til indeksering af begivenheder  
- Azure OpenAI til agentintelligens  
- Implementering af RAG-mønsteret  

### 3. MCP Værktøjer  
- Analyse af GitHub repositories  
- Kodeinspektion  
- Metadataudtrækning  

## Gennemgang af koden

Eksemplet demonstrerer:  
1. MCP-serverintegration  
2. Multi-agent orkestrering  
3. Azure Cognitive Search-integration  
4. Implementering af RAG-mønsteret  

Nøglefunktioner:  
- Realtidsanalyse af GitHub repositories  
- Intelligente projektanbefalinger  
- Begivenhedsmatching ved hjælp af Azure Search  
- Streaming af svar med Chainlit  

## Kørsel af eksemplet

For detaljerede opsætningsinstruktioner og mere information, se [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start MCP-serveren:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start applikationen:  
   ```bash
   chainlit run app.py -w
   ```

3. Test integrationen:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Fejlfinding

Almindelige problemer og løsninger:  
1. MCP-forbindelsesproblemer  
   - Bekræft at serveren kører  
   - Tjek porttilgængelighed  
   - Bekræft GitHub-tokens  

2. Azure Search-problemer  
   - Valider forbindelsesstrenge  
   - Tjek om indekset findes  
   - Bekræft dokumentupload  

## Næste skridt
- Udforsk flere MCP-værktøjer  
- Implementer brugerdefinerede agenter  
- Forbedr RAG-funktionaliteter  
- Tilføj flere begivenhedskilder  

## Ressourcer
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.