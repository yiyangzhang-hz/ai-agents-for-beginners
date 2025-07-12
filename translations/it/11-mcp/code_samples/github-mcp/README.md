<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:22:08+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "it"
}
-->
# Esempio di Server Github MCP

## Descrizione

Questa è stata una demo creata per l'AI Agents Hackathon ospitato tramite il Microsoft Reactor.

Lo strumento viene utilizzato per consigliare progetti per hackathon basati sui repository Github di un utente.  
Questo avviene tramite:

1. **Github Agent** - Utilizza il Github MCP Server per recuperare i repository e le informazioni relative a questi.
2. **Hackathon Agent** - Prende i dati dal Github Agent e genera idee creative per progetti hackathon basandosi sui progetti, i linguaggi usati dall'utente e le tracce del progetto per l'AI Agents hackathon.
3. **Events Agent** - In base al suggerimento dell'hackathon agent, l'events agent raccomanda eventi rilevanti dalla serie AI Agent Hackathon.

## Esecuzione del codice

### Variabili d'ambiente

Questa demo utilizza Azure Open AI Service, Semantic Kernel, il Github MCP Server e Azure AI Search.

Assicurati di aver impostato correttamente le variabili d'ambiente per utilizzare questi strumenti:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Avvio del Chainlit Server

Per connettersi al MCP server, questa demo usa Chainlit come interfaccia chat.

Per avviare il server, usa il seguente comando nel terminale:

```bash
chainlit run app.py -w
```

Questo dovrebbe avviare il tuo server Chainlit su `localhost:8000` e popolare l'indice Azure AI Search con il contenuto di `event-descriptions.md`.

## Connessione al MCP Server

Per connetterti al Github MCP Server, seleziona l'icona "plug" sotto la casella di chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.it.png)

Da lì puoi cliccare su "Connect an MCP" per aggiungere il comando che connette al Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Sostituisci "[YOUR PERSONAL ACCESS TOKEN]" con il tuo Personal Access Token reale.

Dopo la connessione, dovresti vedere un (1) accanto all'icona plug per confermare che è connesso. In caso contrario, prova a riavviare il server chainlit con `chainlit run app.py -w`.

## Uso della Demo

Per avviare il flusso di lavoro dell'agente che consiglia progetti per hackathon, puoi scrivere un messaggio come:

"Consiglia progetti hackathon per l'utente Github koreyspace"

Il Router Agent analizzerà la tua richiesta e determinerà quale combinazione di agenti (GitHub, Hackathon e Events) è più adatta a gestire la tua query. Gli agenti lavorano insieme per fornire raccomandazioni complete basate sull'analisi dei repository GitHub, l'ideazione di progetti e gli eventi tech rilevanti.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.