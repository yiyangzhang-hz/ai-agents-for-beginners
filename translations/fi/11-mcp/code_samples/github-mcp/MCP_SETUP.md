<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:15+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "fi"
}
-->
# MCP Serverin Integrointiohje

## Esivaatimukset
- Node.js asennettuna (versio 14 tai uudempi)
- npm-pakettienhallinta
- Python-ympäristö tarvittavine riippuvuuksineen

## Asennusohjeet

1. **Asenna MCP Server -paketti**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Käynnistä MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Palvelimen pitäisi käynnistyä ja näyttää yhteys-URL.

3. **Varmista yhteys**
   - Etsi Chainlit-käyttöliittymästä pistokkeen kuvake (🔌)
   - Pistokkeen viereen pitäisi ilmestyä numero (1), joka tarkoittaa onnistunutta yhteyttä
   - Konsolissa pitäisi näkyä: "GitHub plugin setup completed successfully" (sekä muita tilarivejä)

## Vianetsintä

### Yleiset ongelmat

1. **Porttikonflikti**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Ratkaisu: Vaihda porttia komennolla:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Todennusongelmat**
   - Varmista, että GitHub-tunnukset on määritetty oikein
   - Tarkista, että .env-tiedostossa on tarvittavat tokenit
   - Varmista GitHub API -käyttöoikeudet

3. **Yhteys epäonnistui**
   - Varmista, että palvelin on käynnissä oikealla portilla
   - Tarkista palomuuriasetukset
   - Varmista, että Python-ympäristö sisältää tarvittavat paketit

## Yhteyden varmistus

MCP-serverisi on oikein yhdistetty, kun:
1. Konsolissa näkyy "GitHub plugin setup completed successfully"
2. Yhteyslokissa lukee "✓ MCP Connection Status: Active"
3. GitHub-komennot toimivat chat-käyttöliittymässä

## Ympäristömuuttujat

Vaaditaan .env-tiedostossasi:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Yhteyden testaus

Lähetä tämä testiviesti chatissa:
```
Show me the repositories for username: [GitHub Username]
```
Onnistunut vastaus näyttää repositorion tiedot.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.