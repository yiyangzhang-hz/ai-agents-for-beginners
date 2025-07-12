<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:22+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "nl"
}
-->
# MCP Server Integratiehandleiding

## Vereisten
- Node.js geïnstalleerd (versie 14 of hoger)
- npm package manager
- Python-omgeving met benodigde afhankelijkheden

## Installatiestappen

1. **Installeer MCP Server Package**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Start MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   De server zou moeten starten en een verbindings-URL tonen.

3. **Verbinding Controleren**  
   - Zoek naar het stekker-icoon (🔌) in je Chainlit-interface  
   - Er zou een nummer (1) naast het stekker-icoon moeten verschijnen, wat een succesvolle verbinding aangeeft  
   - De console zou moeten tonen: "GitHub plugin setup completed successfully" (samen met extra statusregels)

## Problemen Oplossen

### Veelvoorkomende Problemen

1. **Poortconflict**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Oplossing: wijzig de poort met:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Authenticatieproblemen**  
   - Zorg dat GitHub-gegevens correct zijn ingesteld  
   - Controleer of het .env-bestand de benodigde tokens bevat  
   - Verifieer toegang tot de GitHub API

3. **Verbinding Mislukt**  
   - Controleer of de server draait op de verwachte poort  
   - Controleer firewall-instellingen  
   - Verifieer dat de Python-omgeving de benodigde pakketten heeft

## Verbindingscontrole

Je MCP-server is correct verbonden wanneer:  
1. De console toont "GitHub plugin setup completed successfully"  
2. Verbindingslogs tonen "✓ MCP Connection Status: Active"  
3. GitHub-commando’s werken in de chatinterface

## Omgevingsvariabelen

Vereist in je .env-bestand:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Verbinding Testen

Stuur dit testbericht in de chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Een succesvolle reactie toont informatie over de repository.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.