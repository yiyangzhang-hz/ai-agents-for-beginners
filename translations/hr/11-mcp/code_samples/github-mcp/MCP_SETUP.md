<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:54+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "hr"
}
-->
# MCP Vodič za Integraciju Servera

## Preduvjeti
- Instaliran Node.js (verzija 14 ili novija)
- npm paketni upravitelj
- Python okruženje s potrebnim ovisnostima

## Koraci za Postavljanje

1. **Instalirajte MCP Server Paket**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Pokrenite MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server bi se trebao pokrenuti i prikazati URL za povezivanje.

3. **Provjerite Povezanost**
   - Potražite ikonu utikača (🔌) u vašem Chainlit sučelju
   - Broj (1) bi se trebao pojaviti pored ikone utikača, što označava uspješnu vezu
   - Konzola bi trebala prikazati: "GitHub plugin setup completed successfully" (uz dodatne linije statusa)

## Rješavanje Problema

### Česti Problemi

1. **Sukob Portova**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Rješenje: Promijenite port koristeći:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemi s Autentifikacijom**
   - Provjerite jesu li GitHub vjerodajnice ispravno konfigurirane
   - Provjerite sadrži li .env datoteka potrebne tokene
   - Potvrdite pristup GitHub API-ju

3. **Povezivanje Neuspješno**
   - Provjerite radi li server na očekivanom portu
   - Provjerite postavke vatrozida
   - Provjerite ima li Python okruženje potrebne pakete

## Provjera Povezanosti

Vaš MCP server je ispravno povezan kada:
1. Konzola prikazuje "GitHub plugin setup completed successfully"
2. Zapisi veze prikazuju "✓ MCP Connection Status: Active"
3. GitHub naredbe rade u chat sučelju

## Varijable Okruženja

Potrebne u vašoj .env datoteci:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testiranje Povezanosti

Pošaljite ovu testnu poruku u chat:
```
Show me the repositories for username: [GitHub Username]
```
Uspješan odgovor prikazat će informacije o repozitoriju.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.