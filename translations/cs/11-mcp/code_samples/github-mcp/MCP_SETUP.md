<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:16+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "cs"
}
-->
# Průvodce integrací MCP serveru

## Požadavky
- Nainstalovaný Node.js (verze 14 nebo vyšší)
- Správce balíčků npm
- Python prostředí s potřebnými závislostmi

## Kroky nastavení

1. **Nainstalujte balíček MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Spusťte MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server by se měl spustit a zobrazit URL pro připojení.

3. **Ověřte připojení**
   - Hledejte ikonu zástrčky (🔌) ve vašem rozhraní Chainlit
   - Vedle ikony zástrčky by se mělo objevit číslo (1), které značí úspěšné připojení
   - V konzoli by se mělo zobrazit: "GitHub plugin setup completed successfully" (spolu s dalšími stavovými řádky)

## Řešení problémů

### Běžné problémy

1. **Konflikt portu**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Řešení: Změňte port pomocí:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problémy s autentizací**
   - Ujistěte se, že jsou správně nastaveny GitHub přihlašovací údaje
   - Zkontrolujte, že soubor .env obsahuje požadované tokeny
   - Ověřte přístup k GitHub API

3. **Selhání připojení**
   - Potvrďte, že server běží na očekávaném portu
   - Zkontrolujte nastavení firewallu
   - Ověřte, že Python prostředí má nainstalované potřebné balíčky

## Ověření připojení

Váš MCP server je správně připojen, když:
1. Konzole zobrazí "GitHub plugin setup completed successfully"
2. V protokolech připojení se objeví "✓ MCP Connection Status: Active"
3. GitHub příkazy fungují v chatovém rozhraní

## Proměnné prostředí

Požadované ve vašem .env souboru:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testování připojení

Pošlete tuto testovací zprávu v chatu:
```
Show me the repositories for username: [GitHub Username]
```
Úspěšná odpověď zobrazí informace o repozitáři.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.