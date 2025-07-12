<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:55+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "tl"
}
-->
# MCP Server Integration Guide

## Mga Kinakailangan
- Nakainstall ang Node.js (bersyon 14 pataas)
- npm package manager
- Python environment na may mga kinakailangang dependencies

## Mga Hakbang sa Setup

1. **I-install ang MCP Server Package**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Simulan ang MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Dapat magsimula ang server at ipakita ang connection URL.

3. **Suriin ang Koneksyon**
   - Hanapin ang plug icon (🔌) sa iyong Chainlit interface
   - Dapat lumabas ang bilang (1) sa tabi ng plug icon bilang tanda ng matagumpay na koneksyon
   - Dapat ipakita sa console ang: "GitHub plugin setup completed successfully" (kasama ang iba pang status lines)

## Pag-aayos ng Problema

### Karaniwang Isyu

1. **Port Conflict**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Solusyon: Palitan ang port gamit ang:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Mga Isyu sa Authentication**
   - Siguraduhing tama ang pagkaka-configure ng GitHub credentials
   - Suriin na ang .env file ay may mga kinakailangang token
   - Tiyaking may access sa GitHub API

3. **Nabigong Koneksyon**
   - Tiyaking tumatakbo ang server sa inaasahang port
   - Suriin ang mga firewall settings
   - Siguraduhing may mga kinakailangang package ang Python environment

## Pagpapatunay ng Koneksyon

Tamang konektado ang iyong MCP server kapag:
1. Ipinapakita ng console ang "GitHub plugin setup completed successfully"
2. Ipinapakita ng connection logs ang "✓ MCP Connection Status: Active"
3. Gumagana ang mga GitHub command sa chat interface

## Mga Environment Variable

Kinakailangan sa iyong .env file:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Pagsubok ng Koneksyon

Ipadala ang test message na ito sa chat:
```
Show me the repositories for username: [GitHub Username]
```
Ang matagumpay na tugon ay magpapakita ng impormasyon tungkol sa repository.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.