<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:46:44+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pa"
}
-->
# ਪਾਠ 11: ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੰਟੀਗ੍ਰੇਸ਼ਨ

## ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਦਾ ਪਰਿਚਯ

ਮਾਡਲ ਕਾਂਟੈਕਸਟ ਪ੍ਰੋਟੋਕੋਲ (MCP) ਇੱਕ ਅਗੇਤਰ ਫਰੇਮਵਰਕ ਹੈ ਜੋ AI ਮਾਡਲਾਂ ਅਤੇ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਇੰਟਰੈਕਸ਼ਨਾਂ ਨੂੰ ਸਧਾਰਨ ਬਣਾਉਂਦਾ ਹੈ। MCP AI ਮਾਡਲਾਂ ਅਤੇ ਉਹਨਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਪੁਲ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜੋ ਉਨ੍ਹਾਂ ਨੂੰ ਵਰਤਦੀਆਂ ਹਨ, ਜਿਸ ਨਾਲ ਮਾਡਲ ਦੀ ਅੰਦਰੂਨੀ ਬਣਤਰ ਤੋਂ ਬਿਨਾਂ ਇੱਕ ਸਥਿਰ ਇੰਟਰਫੇਸ ਮਿਲਦਾ ਹੈ।

MCP ਦੇ ਮੁੱਖ ਪਹਲੂ:

- **ਮਿਆਰੀਕ੍ਰਿਤ ਸੰਚਾਰ**: MCP ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ AI ਮਾਡਲਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਇੱਕ ਸਾਂਝੀ ਭਾਸ਼ਾ ਸਥਾਪਤ ਕਰਦਾ ਹੈ  
- **ਸੰਧਰਭ ਪ੍ਰਬੰਧਨ ਵਿੱਚ ਸੁਧਾਰ**: AI ਮਾਡਲਾਂ ਨੂੰ ਸੰਧਰਭ ਜਾਣਕਾਰੀ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਭੇਜਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ  
- **ਕ੍ਰਾਸ-ਪਲੇਟਫਾਰਮ ਅਨੁਕੂਲਤਾ**: C#, Java, JavaScript, Python ਅਤੇ TypeScript ਸਮੇਤ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹੈ  
- **ਸੁਗਮ ਇੰਟੀਗ੍ਰੇਸ਼ਨ**: ਵਿਕਾਸਕਾਰਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ AI ਮਾਡਲਾਂ ਨੂੰ ਆਪਣੀਆਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਆਸਾਨੀ ਨਾਲ ਜੋੜਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ  

MCP ਖਾਸ ਕਰਕੇ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਬਹੁਤ ਕੀਮਤੀ ਹੈ ਕਿਉਂਕਿ ਇਹ ਏਜੰਟਾਂ ਨੂੰ ਵੱਖ-ਵੱਖ ਸਿਸਟਮਾਂ ਅਤੇ ਡਾਟਾ ਸਰੋਤਾਂ ਨਾਲ ਇੱਕ ਸਾਂਝੇ ਪ੍ਰੋਟੋਕੋਲ ਰਾਹੀਂ ਇੰਟਰੈਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਏਜੰਟ ਹੋਰ ਲਚਕੀਲੇ ਅਤੇ ਸ਼ਕਤੀਸ਼ਾਲੀ ਬਣ ਜਾਂਦੇ ਹਨ।

## ਸਿੱਖਣ ਦੇ ਉਦੇਸ਼
- MCP ਕੀ ਹੈ ਅਤੇ AI ਏਜੰਟ ਵਿਕਾਸ ਵਿੱਚ ਇਸ ਦੀ ਭੂਮਿਕਾ ਨੂੰ ਸਮਝਣਾ  
- GitHub ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਲਈ MCP ਸਰਵਰ ਸੈਟਅਪ ਅਤੇ ਸੰਰਚਨਾ ਕਰਨਾ  
- MCP ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਉਣਾ  
- Azure Cognitive Search ਨਾਲ RAG (Retrieval Augmented Generation) ਲਾਗੂ ਕਰਨਾ  

## ਲੋੜੀਂਦੇ ਪੂਰਵ-ਸ਼ਰਤਾਂ
- Python 3.8+  
- Node.js 14+  
- Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ  
- GitHub ਖਾਤਾ  
- Semantic Kernel ਦੀ ਬੁਨਿਆਦੀ ਸਮਝ  

## ਸੈਟਅਪ ਨਿਰਦੇਸ਼

1. **ਵਾਤਾਵਰਣ ਸੈਟਅਪ**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure ਸੇਵਾਵਾਂ ਦੀ ਸੰਰਚਨਾ**  
   - Azure Cognitive Search ਸਰੋਤ ਬਣਾਓ  
   - Azure OpenAI ਸੇਵਾ ਸੈਟਅਪ ਕਰੋ  
   - `.env` ਵਿੱਚ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈਟ ਕਰੋ  

3. **MCP ਸਰਵਰ ਸੈਟਅਪ**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## ਪ੍ਰੋਜੈਕਟ ਦੀ ਬਣਤਰ

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## ਮੁੱਖ ਹਿੱਸੇ

### 1. ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ  
- GitHub ਏਜੰਟ: ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- Hackathon ਏਜੰਟ: ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ਾਂ  
- Events ਏਜੰਟ: ਟੈਕ ਇਵੈਂਟ ਸੁਝਾਅ  

### 2. Azure ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਇਵੈਂਟ ਇੰਡੈਕਸਿੰਗ ਲਈ Cognitive Search  
- ਏਜੰਟ ਬੁੱਧੀਮਤਾ ਲਈ Azure OpenAI  
- RAG ਪੈਟਰਨ ਲਾਗੂ ਕਰਨਾ  

### 3. MCP ਟੂਲਜ਼  
- GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- ਕੋਡ ਜਾਂਚ  
- ਮੈਟਾਡੇਟਾ ਨਿਕਾਸ਼  

## ਕੋਡ ਵਾਕਥਰੂ

ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਦਰਸਾਇਆ ਗਿਆ ਹੈ:  
1. MCP ਸਰਵਰ ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
2. ਮਲਟੀ-ਏਜੰਟ ਸੰਗਠਨ  
3. Azure Cognitive Search ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
4. RAG ਪੈਟਰਨ ਲਾਗੂ ਕਰਨਾ  

ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:  
- ਰੀਅਲ-ਟਾਈਮ GitHub ਰਿਪੋਜ਼ਟਰੀ ਵਿਸ਼ਲੇਸ਼ਣ  
- ਬੁੱਧੀਮਾਨ ਪ੍ਰੋਜੈਕਟ ਸਿਫਾਰਸ਼ਾਂ  
- Azure Search ਨਾਲ ਇਵੈਂਟ ਮੇਲ  
- Chainlit ਨਾਲ ਸਟ੍ਰੀਮਿੰਗ ਜਵਾਬ  

## ਨਮੂਨਾ ਚਲਾਉਣਾ

ਵਿਸਤਾਰਪੂਰਵਕ ਸੈਟਅਪ ਨਿਰਦੇਸ਼ਾਂ ਅਤੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ, [Github MCP Server Example README](./code_samples/github-mcp/README.md) ਨੂੰ ਵੇਖੋ।

1. MCP ਸਰਵਰ ਸ਼ੁਰੂ ਕਰੋ:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. ਐਪਲੀਕੇਸ਼ਨ ਲਾਂਚ ਕਰੋ:  
   ```bash
   chainlit run app.py -w
   ```

3. ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## ਸਮੱਸਿਆ ਨਿਵਾਰਣ

ਆਮ ਸਮੱਸਿਆਵਾਂ ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਹੱਲ:  
1. MCP ਕਨੈਕਸ਼ਨ ਸਮੱਸਿਆਵਾਂ  
   - ਸਰਵਰ ਚੱਲ ਰਿਹਾ ਹੈ ਜਾਂ ਨਹੀਂ ਜਾਂਚੋ  
   - ਪੋਰਟ ਉਪਲਬਧਤਾ ਦੀ ਜਾਂਚ ਕਰੋ  
   - GitHub ਟੋਕਨ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ  

2. Azure Search ਸਮੱਸਿਆਵਾਂ  
   - ਕਨੈਕਸ਼ਨ ਸਟਰਿੰਗ ਦੀ ਜਾਂਚ ਕਰੋ  
   - ਇੰਡੈਕਸ ਮੌਜੂਦਗੀ ਦੀ ਜਾਂਚ ਕਰੋ  
   - ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ  

## ਅਗਲੇ ਕਦਮ
- ਵਾਧੂ MCP ਟੂਲਜ਼ ਦੀ ਖੋਜ ਕਰੋ  
- ਕਸਟਮ ਏਜੰਟ ਲਾਗੂ ਕਰੋ  
- RAG ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਓ  
- ਹੋਰ ਇਵੈਂਟ ਸਰੋਤ ਸ਼ਾਮਲ ਕਰੋ  

## ਸਰੋਤ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।