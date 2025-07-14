<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:19:01+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sl"
}
-->
# MCP Vodnik za integracijo strežnika

## Predpogoji
- Nameščen Node.js (različica 14 ali novejša)
- Upravljalnik paketov npm
- Python okolje z zahtevanimi odvisnostmi

## Koraki namestitve

1. **Namestite paket MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Zaženite MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Strežnik se mora zagnati in prikazati URL za povezavo.

3. **Preverite povezavo**
   - Poiščite ikono vtičnice (🔌) v vašem Chainlit vmesniku
   - Poleg ikone vtičnice se mora prikazati številka (1), kar pomeni uspešno povezavo
   - V konzoli naj bo prikazano: "GitHub plugin setup completed successfully" (skupaj z dodatnimi vrsticami stanja)

## Odpravljanje težav

### Pogoste težave

1. **Spor pristanišča**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Rešitev: Spremenite pristanišče z ukazom:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Težave z avtentikacijo**
   - Preverite, da so GitHub poverilnice pravilno nastavljene
   - Preverite, da datoteka .env vsebuje zahtevane žetone
   - Preverite dostop do GitHub API

3. **Povezava ni uspela**
   - Preverite, da strežnik teče na pričakovanem pristanišču
   - Preverite nastavitve požarnega zidu
   - Preverite, da ima Python okolje zahtevane pakete

## Preverjanje povezave

Vaš MCP strežnik je pravilno povezan, ko:
1. Konzola prikaže "GitHub plugin setup completed successfully"
2. Povezovalni zapisi kažejo "✓ MCP Connection Status: Active"
3. Ukazi za GitHub delujejo v klepetalnem vmesniku

## Okoljske spremenljivke

Zahtevane v vaši datoteki .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testiranje povezave

Pošljite to testno sporočilo v klepet:
```
Show me the repositories for username: [GitHub Username]
```
Uspešen odgovor bo prikazal informacije o repozitoriju.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.