<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:38:10+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "it"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.it.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_
# AI Agents in Produzione

## Introduzione

In questa lezione vedremo:

- Come pianificare efficacemente il deployment del tuo AI Agent in produzione.
- Errori comuni e problemi che potresti incontrare durante il deployment del tuo AI Agent in produzione.
- Come gestire i costi mantenendo comunque le prestazioni del tuo AI Agent.

## Obiettivi di Apprendimento

Al termine di questa lezione, saprai/avrai compreso:

- Tecniche per migliorare le prestazioni, i costi e l’efficacia di un sistema AI Agent in produzione.
- Cosa e come valutare i tuoi AI Agents.
- Come controllare i costi durante il deployment degli AI Agents in produzione.

È importante distribuire AI Agents affidabili. Dai un’occhiata anche alla lezione "Building Trustworthy AI Agents".

## Valutare gli AI Agents

Prima, durante e dopo il deployment degli AI Agents, avere un sistema adeguato per valutarli è fondamentale. Questo garantirà che il sistema sia allineato con i tuoi obiettivi e quelli degli utenti.

Per valutare un AI Agent, è importante poter valutare non solo l’output dell’agente, ma anche l’intero sistema in cui opera. Questo include, ma non si limita a:

- La richiesta iniziale al modello.
- La capacità dell’agente di identificare l’intento dell’utente.
- La capacità dell’agente di individuare lo strumento giusto per svolgere il compito.
- La risposta dello strumento alla richiesta dell’agente.
- La capacità dell’agente di interpretare la risposta dello strumento.
- Il feedback dell’utente alla risposta dell’agente.

Questo ti permette di individuare aree di miglioramento in modo più modulare. Potrai quindi monitorare l’effetto delle modifiche a modelli, prompt, strumenti e altri componenti con maggiore efficienza.

## Problemi Comuni e Soluzioni Potenziali con gli AI Agents

| **Problema**                                   | **Soluzione Potenziale**                                                                                                                                                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI Agent non esegue i compiti in modo coerente | - Affina il prompt fornito all’AI Agent; sii chiaro sugli obiettivi.<br>- Identifica dove suddividere i compiti in sotto-compiti e gestirli con più agenti può essere utile.                                                  |
| AI Agent entra in loop continui                 | - Assicurati di avere termini e condizioni di terminazione chiari in modo che l’Agent sappia quando fermare il processo.<br>- Per compiti complessi che richiedono ragionamento e pianificazione, usa un modello più grande specializzato in questi compiti. |
| Le chiamate agli strumenti dell’AI Agent non funzionano bene | - Testa e valida l’output dello strumento al di fuori del sistema agente.<br>- Affina i parametri definiti, i prompt e la denominazione degli strumenti.                                                                     |
| Sistema Multi-Agent non performa in modo coerente | - Affina i prompt dati a ciascun agente per assicurarti che siano specifici e distinti tra loro.<br>- Costruisci un sistema gerarchico usando un agente "routing" o controller per determinare quale agente è quello corretto. |

## Gestione dei Costi

Ecco alcune strategie per gestire i costi del deployment degli AI Agents in produzione:

- **Caching delle Risposte** - Identificare richieste e compiti comuni e fornire le risposte prima che passino attraverso il sistema agentico è un buon modo per ridurre il volume di richieste simili. Puoi anche implementare un flusso per valutare quanto una richiesta sia simile a quelle memorizzate usando modelli AI più semplici.

- **Uso di Modelli Più Piccoli** - I Small Language Models (SLM) possono funzionare bene in alcuni casi d’uso agentici e ridurre significativamente i costi. Come detto prima, costruire un sistema di valutazione per determinare e confrontare le prestazioni rispetto a modelli più grandi è il modo migliore per capire quanto bene un SLM si comporterà nel tuo caso d’uso.

- **Uso di un Modello Router** - Una strategia simile è usare una varietà di modelli e dimensioni. Puoi usare un LLM/SLM o una funzione serverless per indirizzare le richieste in base alla complessità verso i modelli più adatti. Questo aiuta a ridurre i costi garantendo comunque le prestazioni sui compiti giusti.

## Congratulazioni

Questa è attualmente l’ultima lezione di "AI Agents for Beginners".

Abbiamo in programma di aggiungere altre lezioni basate sul feedback e sui cambiamenti di questo settore in continua crescita, quindi torna a trovarci presto.

Se vuoi continuare a imparare e costruire con gli AI Agents, unisciti al <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Organizziamo workshop, tavole rotonde della community e sessioni "ask me anything" lì.

Abbiamo anche una raccolta Learn con materiali aggiuntivi che possono aiutarti a iniziare a costruire AI Agents in produzione.

## Lezione Precedente

[Metacognition Design Pattern](../09-metacognition/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.