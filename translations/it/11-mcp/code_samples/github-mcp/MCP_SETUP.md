<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:16:15+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "it"
}
-->
# Guida all'Integrazione del Server MCP

## Prerequisiti
- Node.js installato (versione 14 o superiore)
- Gestore di pacchetti npm
- Ambiente Python con le dipendenze necessarie

## Passaggi per la Configurazione

1. **Installa il Pacchetto MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Avvia il Server MCP**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Il server dovrebbe avviarsi e mostrare un URL di connessione.

3. **Verifica la Connessione**
   - Cerca l'icona della spina (🔌) nella tua interfaccia Chainlit
   - Dovrebbe apparire un numero (1) accanto all'icona della spina che indica la connessione riuscita
   - La console dovrebbe mostrare: "GitHub plugin setup completed successfully" (insieme ad altre righe di stato)

## Risoluzione dei Problemi

### Problemi Comuni

1. **Conflitto di Porta**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Soluzione: Cambia la porta usando:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemi di Autenticazione**
   - Assicurati che le credenziali GitHub siano configurate correttamente
   - Controlla che il file .env contenga i token richiesti
   - Verifica l'accesso all'API di GitHub

3. **Connessione Fallita**
   - Conferma che il server sia in esecuzione sulla porta prevista
   - Controlla le impostazioni del firewall
   - Verifica che l'ambiente Python abbia i pacchetti necessari

## Verifica della Connessione

Il tuo server MCP è correttamente connesso quando:
1. La console mostra "GitHub plugin setup completed successfully"
2. I log di connessione mostrano "✓ MCP Connection Status: Active"
3. I comandi GitHub funzionano nell'interfaccia chat

## Variabili d'Ambiente

Richieste nel tuo file .env:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Test della Connessione

Invia questo messaggio di test in chat:
```
Show me the repositories for username: [GitHub Username]
```
Una risposta positiva mostrerà le informazioni del repository.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.