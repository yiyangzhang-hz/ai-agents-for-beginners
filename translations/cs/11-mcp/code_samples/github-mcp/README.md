<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:24:23+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "cs"
}
-->
# Github MCP Server Příklad

## Popis

Toto bylo demo vytvořené pro AI Agents Hackathon pořádaný prostřednictvím Microsoft Reactor.

Nástroj slouží k doporučování hackathon projektů na základě uživatelových Github repozitářů.  
To se provádí takto:

1. **Github Agent** – Používá Github MCP Server k získání repozitářů a informací o nich.  
2. **Hackathon Agent** – Zpracuje data od Github Agenta a přijde s kreativními nápady na hackathon projekty založenými na projektech, programovacích jazycích používaných uživatelem a tématech AI Agents hackathonu.  
3. **Events Agent** – Na základě návrhů hackathon agenta doporučí relevantní akce z řady AI Agent Hackathon.

## Spuštění kódu

### Proměnné prostředí

Toto demo využívá Azure Open AI Service, Semantic Kernel, Github MCP Server a Azure AI Search.

Ujistěte se, že máte správně nastavené proměnné prostředí pro použití těchto nástrojů:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Spuštění Chainlit Serveru

Pro připojení k MCP serveru toto demo používá Chainlit jako chatovací rozhraní.

Pro spuštění serveru použijte v terminálu následující příkaz:

```bash
chainlit run app.py -w
```

Tím by se měl spustit váš Chainlit server na `localhost:8000` a zároveň se naplní váš Azure AI Search Index obsahem souboru `event-descriptions.md`.

## Připojení k MCP Serveru

Pro připojení k Github MCP Serveru klikněte na ikonu „zásuvky“ pod chatovacím polem „Type your message here..“:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.cs.png)

Odtud můžete kliknout na „Connect an MCP“ a přidat příkaz pro připojení k Github MCP Serveru:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Nahraďte "[YOUR PERSONAL ACCESS TOKEN]" svým skutečným osobním přístupovým tokenem.

Po připojení byste měli vedle ikony zásuvky vidět (1), což potvrzuje připojení. Pokud ne, zkuste restartovat chainlit server příkazem `chainlit run app.py -w`.

## Použití Dema

Pro spuštění workflow agenta, který doporučuje hackathon projekty, můžete napsat zprávu například:

„Recommend hackathon projects for the Github user koreyspace“

Router Agent analyzuje váš požadavek a rozhodne, která kombinace agentů (GitHub, Hackathon a Events) je nejvhodnější pro zpracování dotazu. Agenti spolupracují, aby poskytli komplexní doporučení založená na analýze Github repozitářů, nápadech na projekty a relevantních technologických akcích.

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.