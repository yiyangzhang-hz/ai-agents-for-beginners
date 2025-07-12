<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:08+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "no"
}
-->
# MCP Server Integrasjonsguide

## Forutsetninger
- Node.js installert (versjon 14 eller nyere)
- npm pakkehåndterer
- Python-miljø med nødvendige avhengigheter

## Oppsett

1. **Installer MCP Server-pakken**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Start MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serveren skal starte og vise en tilkoblings-URL.

3. **Verifiser tilkobling**  
   - Se etter pluggikonet (🔌) i Chainlit-grensesnittet ditt  
   - Et tall (1) skal vises ved siden av pluggikonet som indikerer vellykket tilkobling  
   - Konsollen skal vise: "GitHub plugin setup completed successfully" (sammen med flere statuslinjer)

## Feilsøking

### Vanlige problemer

1. **Portkonflikt**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Løsning: Endre port ved å bruke:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentiseringsproblemer**  
   - Sørg for at GitHub-legitimasjon er riktig konfigurert  
   - Sjekk at .env-filen inneholder nødvendige tokens  
   - Verifiser tilgang til GitHub API

3. **Tilkobling mislyktes**  
   - Bekreft at serveren kjører på forventet port  
   - Sjekk brannmurinnstillinger  
   - Verifiser at Python-miljøet har nødvendige pakker

## Verifisering av tilkobling

Din MCP-server er riktig tilkoblet når:  
1. Konsollen viser "GitHub plugin setup completed successfully"  
2. Tilkoblingslogger viser "✓ MCP Connection Status: Active"  
3. GitHub-kommandoer fungerer i chattegrensesnittet

## Miljøvariabler

Påkrevd i din .env-fil:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Test av tilkobling

Send denne testmeldingen i chatten:  
```
Show me the repositories for username: [GitHub Username]
```  
Et vellykket svar vil vise informasjon om repository.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.