<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:01+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "da"
}
-->
# MCP Server Integrationsguide

## Forudsætninger
- Node.js installeret (version 14 eller nyere)
- npm pakkehåndtering
- Python-miljø med nødvendige afhængigheder

## Opsætningstrin

1. **Installer MCP Server-pakken**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Start MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serveren burde starte og vise en tilslutnings-URL.

3. **Bekræft forbindelse**  
   - Kig efter stik-ikonet (🔌) i din Chainlit-grænseflade  
   - Et tal (1) skal vises ved siden af stik-ikonet, hvilket indikerer en vellykket forbindelse  
   - Konsollen skal vise: "GitHub plugin setup completed successfully" (sammen med yderligere statuslinjer)

## Fejlfinding

### Almindelige problemer

1. **Portkonflikt**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Løsning: Skift porten ved at bruge:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Autentificeringsproblemer**  
   - Sørg for, at GitHub-legitimationsoplysninger er korrekt konfigureret  
   - Tjek at .env-filen indeholder de nødvendige tokens  
   - Bekræft adgang til GitHub API

3. **Forbindelse mislykkedes**  
   - Bekræft at serveren kører på den forventede port  
   - Tjek firewall-indstillinger  
   - Bekræft at Python-miljøet har de nødvendige pakker

## Forbindelsesbekræftelse

Din MCP-server er korrekt tilsluttet, når:  
1. Konsollen viser "GitHub plugin setup completed successfully"  
2. Forbindelseslog viser "✓ MCP Connection Status: Active"  
3. GitHub-kommandoer fungerer i chatgrænsefladen

## Miljøvariabler

Påkrævet i din .env-fil:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Test af forbindelse

Send denne testbesked i chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Et vellykket svar vil vise oplysninger om repository.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.