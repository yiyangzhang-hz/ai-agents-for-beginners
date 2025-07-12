<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:02+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "sw"
}
-->
# MCP Server Mwongozo wa Muunganisho

## Mahitaji ya Awali
- Node.js imewekwa (toleo 14 au zaidi)
- Meneja wa pakiti wa npm
- Mazingira ya Python yenye utegemezi unaohitajika

## Hatua za Usanidi

1. **Sakinisha Pakiti ya MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Anzisha MCP Server**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Server inapaswa kuanza na kuonyesha URL ya muunganisho.

3. **Thibitisha Muunganisho**
   - Tafuta ikoni ya plagi (🔌) kwenye kiolesura chako cha Chainlit
   - Nambari (1) inapaswa kuonekana kando ya ikoni ya plagi kuonyesha muunganisho umefanikiwa
   - Kwenye console inapaswa kuonyesha: "GitHub plugin setup completed successfully" (pamoja na mistari mingine ya hali)

## Utatuzi wa Matatizo

### Masuala Yanayojirudia Mara kwa Mara

1. **Mgongano wa Bandari**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Suluhisho: Badilisha bandari kwa kutumia:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Matatizo ya Uthibitishaji**
   - Hakikisha maelezo ya GitHub yamewekwa ipasavyo
   - Angalia faili la .env lina tokeni zinazohitajika
   - Thibitisha upatikanaji wa API ya GitHub

3. **Muunganisho Umeshindikana**
   - Hakikisha server inaendesha kwenye bandari inayotarajiwa
   - Angalia mipangilio ya firewall
   - Thibitisha mazingira ya Python yana pakiti zinazohitajika

## Uthibitishaji wa Muunganisho

Server yako ya MCP imeunganishwa ipasavyo wakati:
1. Console inaonyesha "GitHub plugin setup completed successfully"
2. Logi za muunganisho zinaonyesha "✓ MCP Connection Status: Active"
3. Amri za GitHub zinafanya kazi kwenye kiolesura cha mazungumzo

## Mabadiliko ya Mazingira

Yanahitajika kwenye faili lako la .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kupima Muunganisho

Tuma ujumbe huu wa majaribio kwenye mazungumzo:
```
Show me the repositories for username: [GitHub Username]
```
Jibu la mafanikio litaonyesha taarifa za hifadhidata.

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.