<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:09+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "hu"
}
-->
# MCP Server Integrációs Útmutató

## Előfeltételek
- Telepített Node.js (14-es vagy újabb verzió)
- npm csomagkezelő
- Python környezet a szükséges függőségekkel

## Beállítási lépések

1. **MCP Server csomag telepítése**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Server indítása**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   A szerver elindul, és megjelenik egy csatlakozási URL.

3. **Kapcsolat ellenőrzése**
   - Keresd a dugó ikont (🔌) a Chainlit felületeden
   - Egy szám (1) jelenik meg a dugó ikon mellett, ami a sikeres kapcsolatot jelzi
   - A konzolon megjelenik: "GitHub plugin setup completed successfully" (további státusz sorokkal együtt)

## Hibakeresés

### Gyakori problémák

1. **Port ütközés**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Megoldás: Változtasd meg a portot a következővel:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Hitelesítési problémák**
   - Győződj meg róla, hogy a GitHub hitelesítő adatok helyesen vannak beállítva
   - Ellenőrizd, hogy a .env fájl tartalmazza a szükséges tokeneket
   - Ellenőrizd a GitHub API hozzáférést

3. **Kapcsolódás sikertelen**
   - Ellenőrizd, hogy a szerver a várt porton fut-e
   - Nézd meg a tűzfal beállításokat
   - Győződj meg róla, hogy a Python környezetben megvannak a szükséges csomagok

## Kapcsolat ellenőrzése

Az MCP szerver megfelelően csatlakozik, ha:
1. A konzolon megjelenik a "GitHub plugin setup completed successfully"
2. A kapcsolati naplókban látható: "✓ MCP Connection Status: Active"
3. A GitHub parancsok működnek a chat felületen

## Környezeti változók

Szükségesek a .env fájlban:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kapcsolat tesztelése

Küldd el ezt a tesztüzenetet a chatben:
```
Show me the repositories for username: [GitHub Username]
```
Sikeres válasz esetén megjelenik a tároló információ.

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.