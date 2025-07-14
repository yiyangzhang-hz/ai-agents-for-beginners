<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:24+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sk"
}
-->
# MCP Sprievodca integráciou servera

## Požiadavky
- Nainštalovaný Node.js (verzia 14 alebo novšia)
- Správca balíčkov npm
- Python prostredie s potrebnými závislosťami

## Kroky nastavenia

1. **Inštalácia balíka MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Spustenie MCP Servera**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server by sa mal spustiť a zobraziť URL na pripojenie.

3. **Overenie pripojenia**
   - V rozhraní Chainlit hľadajte ikonu zástrčky (🔌)
   - Vedľa ikony zástrčky by sa mala zobraziť číslica (1), čo znamená úspešné pripojenie
   - V konzole by sa malo zobraziť: "GitHub plugin setup completed successfully" (spolu s ďalšími stavovými riadkami)

## Riešenie problémov

### Bežné problémy

1. **Konflikt portu**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Riešenie: Zmeňte port pomocou:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problémy s autentifikáciou**
   - Skontrolujte, či sú GitHub prihlasovacie údaje správne nastavené
   - Overte, že sú v súbore .env potrebné tokeny
   - Skontrolujte prístup k GitHub API

3. **Pripojenie zlyhalo**
   - Uistite sa, že server beží na očakávanom porte
   - Skontrolujte nastavenia firewallu
   - Overte, či Python prostredie obsahuje potrebné balíky

## Overenie pripojenia

Váš MCP server je správne pripojený, keď:
1. Konzola zobrazí "GitHub plugin setup completed successfully"
2. V logoch pripojenia sa zobrazí "✓ MCP Connection Status: Active"
3. GitHub príkazy fungujú v chatovom rozhraní

## Premenné prostredia

Povinné v súbore .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testovanie pripojenia

Pošlite túto testovaciu správu v chate:
```
Show me the repositories for username: [GitHub Username]
```
Úspešná odpoveď zobrazí informácie o repozitári.

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.