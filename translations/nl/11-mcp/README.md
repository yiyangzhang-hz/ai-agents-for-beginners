<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:56+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "nl"
}
-->
# Les 11: Model Context Protocol (MCP) Integratie

## Introductie tot Model Context Protocol (MCP)

Het Model Context Protocol (MCP) is een geavanceerd raamwerk dat is ontworpen om de interacties tussen AI-modellen en clientapplicaties te standaardiseren. MCP fungeert als een brug tussen AI-modellen en de applicaties die ze gebruiken, en biedt een consistente interface ongeacht de onderliggende modelimplementatie.

Belangrijke aspecten van MCP:

- **Gestandaardiseerde Communicatie**: MCP creëert een gemeenschappelijke taal voor applicaties om met AI-modellen te communiceren
- **Verbeterd Contextbeheer**: Maakt efficiënt doorgeven van contextuele informatie aan AI-modellen mogelijk
- **Cross-platform Compatibiliteit**: Werkt met diverse programmeertalen zoals C#, Java, JavaScript, Python en TypeScript
- **Naadloze Integratie**: Stelt ontwikkelaars in staat om eenvoudig verschillende AI-modellen in hun applicaties te integreren

MCP is vooral waardevol bij de ontwikkeling van AI-agenten, omdat het agenten in staat stelt om via een uniform protocol met verschillende systemen en databronnen te communiceren, waardoor agenten flexibeler en krachtiger worden.

## Leerdoelen
- Begrijpen wat MCP is en welke rol het speelt in AI-agentontwikkeling
- Een MCP-server opzetten en configureren voor GitHub-integratie
- Een multi-agent systeem bouwen met MCP-tools
- RAG (Retrieval Augmented Generation) implementeren met Azure Cognitive Search

## Vereisten
- Python 3.8+
- Node.js 14+
- Azure-abonnement
- GitHub-account
- Basiskennis van Semantic Kernel

## Installatie-instructies

1. **Omgeving opzetten**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-diensten configureren**  
   - Maak een Azure Cognitive Search-resource aan  
   - Stel de Azure OpenAI-service in  
   - Configureer omgevingsvariabelen in `.env`

3. **MCP-server opzetten**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projectstructuur

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

## Kerncomponenten

### 1. Multi-Agent Systeem
- GitHub Agent: Repository-analyse  
- Hackathon Agent: Projectaanbevelingen  
- Events Agent: Suggesties voor technische evenementen

### 2. Azure Integratie
- Cognitive Search voor het indexeren van evenementen  
- Azure OpenAI voor agentintelligentie  
- Implementatie van het RAG-patroon

### 3. MCP Tools
- Analyse van GitHub-repositories  
- Code-inspectie  
- Extractie van metadata

## Code-uitleg

De voorbeeldcode laat zien:  
1. Integratie van de MCP-server  
2. Orkestratie van meerdere agenten  
3. Integratie met Azure Cognitive Search  
4. Implementatie van het RAG-patroon

Belangrijke functies:  
- Real-time analyse van GitHub-repositories  
- Intelligente projectaanbevelingen  
- Evenementenmatching met Azure Search  
- Streaming responses met Chainlit

## De sample uitvoeren

Voor gedetailleerde installatie-instructies en meer informatie, raadpleeg de [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start de MCP-server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Start de applicatie:  
   ```bash
   chainlit run app.py -w
   ```

3. Test de integratie:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Problemen oplossen

Veelvoorkomende problemen en oplossingen:  
1. MCP-verbinding problemen  
   - Controleer of de server draait  
   - Controleer of de poort beschikbaar is  
   - Bevestig de GitHub-tokens

2. Problemen met Azure Search  
   - Valideer de verbindingsstrings  
   - Controleer of de index bestaat  
   - Controleer of documenten zijn geüpload

## Volgende stappen
- Verken extra MCP-tools  
- Implementeer aangepaste agenten  
- Versterk RAG-mogelijkheden  
- Voeg meer evenementbronnen toe

## Bronnen
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.