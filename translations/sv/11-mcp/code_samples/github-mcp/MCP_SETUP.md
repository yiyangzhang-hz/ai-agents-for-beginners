<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:16:54+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sv"
}
-->
# MCP Server Integrationsguide

## Förutsättningar
- Node.js installerat (version 14 eller högre)
- npm paketchef
- Python-miljö med nödvändiga beroenden

## Installationssteg

1. **Installera MCP Server-paketet**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Starta MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Servern bör starta och visa en anslutnings-URL.

3. **Verifiera anslutning**  
   - Leta efter pluggsymbolen (🔌) i din Chainlit-gränssnitt  
   - En siffra (1) ska visas bredvid pluggsymbolen som indikerar en lyckad anslutning  
   - Konsolen ska visa: "GitHub plugin setup completed successfully" (tillsammans med ytterligare statusrader)

## Felsökning

### Vanliga problem

1. **Portkonflikt**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Lösning: Byt port med:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentiseringsproblem**  
   - Säkerställ att GitHub-uppgifter är korrekt konfigurerade  
   - Kontrollera att .env-filen innehåller nödvändiga tokens  
   - Verifiera GitHub API-åtkomst

3. **Anslutning misslyckades**  
   - Bekräfta att servern körs på förväntad port  
   - Kontrollera brandväggsinställningar  
   - Verifiera att Python-miljön har nödvändiga paket

## Verifiering av anslutning

Din MCP-server är korrekt ansluten när:  
1. Konsolen visar "GitHub plugin setup completed successfully"  
2. Anslutningsloggar visar "✓ MCP Connection Status: Active"  
3. GitHub-kommandon fungerar i chattgränssnittet

## Miljövariabler

Krävs i din .env-fil:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testa anslutning

Skicka detta testmeddelande i chatten:  
```
Show me the repositories for username: [GitHub Username]
```  
Ett lyckat svar visar information om repository.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.