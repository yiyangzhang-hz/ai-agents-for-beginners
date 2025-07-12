<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:21:44+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "pa"
}
-->
# Github MCP ਸਰਵਰ ਉਦਾਹਰਨ

## ਵੇਰਵਾ

ਇਹ ਇੱਕ ਡੈਮੋ ਸੀ ਜੋ Microsoft Reactor ਦੁਆਰਾ ਹੋਏ AI Agents Hackathon ਲਈ ਬਣਾਇਆ ਗਿਆ ਸੀ।

ਇਹ ਟੂਲ ਵਰਤੋਂਕਾਰ ਦੇ Github ਰਿਪੋਜ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਹੈਕਾਥਾਨ ਪ੍ਰੋਜੈਕਟਾਂ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ।  
ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:

1. **Github Agent** - Github MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਰਿਪੋਜ਼ ਅਤੇ ਉਹਨਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ।  
2. **Hackathon Agent** - Github Agent ਤੋਂ ਮਿਲੀ ਜਾਣਕਾਰੀ ਨੂੰ ਲੈ ਕੇ, ਵਰਤੋਂਕਾਰ ਦੇ ਪ੍ਰੋਜੈਕਟਾਂ, ਵਰਤੇ ਗਏ ਭਾਸ਼ਾਵਾਂ ਅਤੇ AI Agents ਹੈਕਾਥਾਨ ਦੇ ਪ੍ਰੋਜੈਕਟ ਟ੍ਰੈਕਸ ਦੇ ਆਧਾਰ 'ਤੇ ਰਚਨਾਤਮਕ ਹੈਕਾਥਾਨ ਪ੍ਰੋਜੈਕਟ ਵਿਚਾਰ ਲਿਆਉਂਦਾ ਹੈ।  
3. **Events Agent** - ਹੈਕਾਥਾਨ ਏਜੰਟ ਦੀ ਸਿਫਾਰਸ਼ ਦੇ ਆਧਾਰ 'ਤੇ, Events Agent AI Agent Hackathon ਸੀਰੀਜ਼ ਦੇ ਸੰਬੰਧਿਤ ਇਵੈਂਟਾਂ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰੇਗਾ।  

## ਕੋਡ ਚਲਾਉਣਾ

### Environment Variables

ਇਸ ਡੈਮੋ ਵਿੱਚ Azure Open AI Service, Semantic Kernel, Github MCP Server ਅਤੇ Azure AI Search ਵਰਤੇ ਗਏ ਹਨ।

ਇਹਨਾਂ ਟੂਲਜ਼ ਨੂੰ ਵਰਤਣ ਲਈ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਹੀ Environment Variables ਸੈੱਟ ਹਨ:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Chainlit ਸਰਵਰ ਚਲਾਉਣਾ

MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ, ਇਹ ਡੈਮੋ Chainlit ਨੂੰ ਚੈਟ ਇੰਟਰਫੇਸ ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

ਸਰਵਰ ਚਲਾਉਣ ਲਈ, ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਵਰਤੋ:

```bash
chainlit run app.py -w
```

ਇਸ ਨਾਲ ਤੁਹਾਡਾ Chainlit ਸਰਵਰ `localhost:8000` 'ਤੇ ਚੱਲੇਗਾ ਅਤੇ ਤੁਹਾਡੇ Azure AI Search ਇੰਡੈਕਸ ਨੂੰ `event-descriptions.md` ਦੀ ਸਮੱਗਰੀ ਨਾਲ ਭਰ ਦੇਵੇਗਾ।

## MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨਾ

Github MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ, "Type your message here.." ਚੈਟ ਬਾਕਸ ਹੇਠਾਂ "plug" ਆਈਕਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.pa.png)

ਉੱਥੋਂ "Connect an MCP" 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ Github MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ ਕਮਾਂਡ ਸ਼ਾਮਲ ਕਰੋ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" ਨੂੰ ਆਪਣੇ ਅਸਲੀ Personal Access Token ਨਾਲ ਬਦਲੋ।

ਜੁੜਨ ਤੋਂ ਬਾਅਦ, plug ਆਈਕਨ ਦੇ ਨਾਲ (1) ਦਿਖਾਈ ਦੇਵੇਗਾ ਜੋ ਕਨੈਕਸ਼ਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ। ਜੇ ਨਹੀਂ, ਤਾਂ `chainlit run app.py -w` ਨਾਲ Chainlit ਸਰਵਰ ਨੂੰ ਰੀਸਟਾਰਟ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ।

## ਡੈਮੋ ਵਰਤਣਾ

ਹੈਕਾਥਾਨ ਪ੍ਰੋਜੈਕਟਾਂ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਨ ਵਾਲੇ ਏਜੰਟ ਵਰਕਫਲੋ ਨੂੰ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ ਇਹੋ ਜਿਹਾ ਸੁਨੇਹਾ ਲਿਖ ਸਕਦੇ ਹੋ:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ਤੁਹਾਡੇ ਬੇਨਤੀ ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੇਗਾ ਅਤੇ ਇਹ ਤੈਅ ਕਰੇਗਾ ਕਿ ਕਿਹੜੇ ਏਜੰਟ (GitHub, Hackathon, ਅਤੇ Events) ਤੁਹਾਡੇ ਸਵਾਲ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਹਨ। ਇਹ ਏਜੰਟ ਮਿਲ ਕੇ GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ, ਪ੍ਰੋਜੈਕਟ ਵਿਚਾਰ ਅਤੇ ਸੰਬੰਧਿਤ ਟੈਕ ਇਵੈਂਟਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਪੂਰੀ ਸਿਫਾਰਿਸ਼ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।