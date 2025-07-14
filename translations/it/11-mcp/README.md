<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:47:20+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "it"
}
-->
# Lezione 11: Integrazione del Model Context Protocol (MCP)

## Introduzione al Model Context Protocol (MCP)

Il Model Context Protocol (MCP) è un framework all’avanguardia progettato per standardizzare le interazioni tra modelli di intelligenza artificiale e applicazioni client. MCP funge da ponte tra i modelli AI e le applicazioni che li utilizzano, offrendo un’interfaccia coerente indipendentemente dall’implementazione del modello sottostante.

Aspetti chiave di MCP:

- **Comunicazione standardizzata**: MCP stabilisce un linguaggio comune per le applicazioni che comunicano con i modelli AI  
- **Gestione avanzata del contesto**: consente di passare in modo efficiente informazioni contestuali ai modelli AI  
- **Compatibilità multipiattaforma**: funziona con diversi linguaggi di programmazione tra cui C#, Java, JavaScript, Python e TypeScript  
- **Integrazione senza soluzione di continuità**: permette agli sviluppatori di integrare facilmente diversi modelli AI nelle loro applicazioni  

MCP è particolarmente utile nello sviluppo di agenti AI, poiché consente agli agenti di interagire con vari sistemi e fonti di dati tramite un protocollo unificato, rendendo gli agenti più flessibili e potenti.

## Obiettivi di apprendimento
- Comprendere cos’è MCP e il suo ruolo nello sviluppo di agenti AI  
- Configurare e impostare un server MCP per l’integrazione con GitHub  
- Costruire un sistema multi-agente utilizzando gli strumenti MCP  
- Implementare RAG (Retrieval Augmented Generation) con Azure Cognitive Search  

## Prerequisiti
- Python 3.8+  
- Node.js 14+  
- Abbonamento Azure  
- Account GitHub  
- Conoscenze di base di Semantic Kernel  

## Istruzioni per la configurazione

1. **Configurazione dell’ambiente**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurare i servizi Azure**  
   - Creare una risorsa Azure Cognitive Search  
   - Impostare il servizio Azure OpenAI  
   - Configurare le variabili d’ambiente in `.env`  

3. **Configurazione del server MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struttura del progetto

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

## Componenti principali

### 1. Sistema multi-agente
- GitHub Agent: analisi dei repository  
- Hackathon Agent: raccomandazioni di progetto  
- Events Agent: suggerimenti su eventi tecnologici  

### 2. Integrazione Azure
- Cognitive Search per l’indicizzazione degli eventi  
- Azure OpenAI per l’intelligenza degli agenti  
- Implementazione del pattern RAG  

### 3. Strumenti MCP
- Analisi dei repository GitHub  
- Ispezione del codice  
- Estrazione di metadata  

## Panoramica del codice

L’esempio dimostra:  
1. Integrazione del server MCP  
2. Orchestrazione multi-agente  
3. Integrazione con Azure Cognitive Search  
4. Implementazione del pattern RAG  

Caratteristiche principali:  
- Analisi in tempo reale dei repository GitHub  
- Raccomandazioni intelligenti di progetto  
- Corrispondenza eventi tramite Azure Search  
- Risposte in streaming con Chainlit  

## Esecuzione dell’esempio

Per istruzioni dettagliate sulla configurazione e ulteriori informazioni, consulta il [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Avvia il server MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Avvia l’applicazione:  
   ```bash
   chainlit run app.py -w
   ```

3. Testa l’integrazione:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Risoluzione dei problemi

Problemi comuni e soluzioni:  
1. Problemi di connessione MCP  
   - Verifica che il server sia in esecuzione  
   - Controlla la disponibilità della porta  
   - Conferma i token GitHub  

2. Problemi con Azure Search  
   - Verifica le stringhe di connessione  
   - Controlla l’esistenza dell’indice  
   - Verifica il caricamento dei documenti  

## Passi successivi
- Esplorare ulteriori strumenti MCP  
- Implementare agenti personalizzati  
- Potenziare le capacità RAG  
- Aggiungere altre fonti di eventi  

## Risorse
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.