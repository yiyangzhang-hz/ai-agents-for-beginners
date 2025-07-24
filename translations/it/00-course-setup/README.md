<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:39:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "it"
}
-->
# Configurazione del Corso

## Introduzione

Questa lezione spiegherà come eseguire gli esempi di codice di questo corso.

## Clonare o Forkare questo Repository

Per iniziare, clona o fork il repository GitHub. Questo ti permetterà di avere una tua versione del materiale del corso, così potrai eseguire, testare e modificare il codice!

Puoi farlo cliccando sul link per

Dovresti ora avere la tua versione forkata di questo corso al seguente link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.it.png)

## Esecuzione del Codice

Questo corso offre una serie di Jupyter Notebook che puoi eseguire per fare pratica nella creazione di Agenti AI.

Gli esempi di codice utilizzano:

**Richiede un Account GitHub - Gratuito**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Etichettato come (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Etichettato come (autogen.ipynb)  

**Richiede un Abbonamento Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. Etichettato come (azureaiagent.ipynb)  

Ti incoraggiamo a provare tutti e tre i tipi di esempi per vedere quale funziona meglio per te.

Qualunque opzione tu scelga, determinerà quali passaggi di configurazione seguire di seguito:

## Requisiti

- Python 3.12+  
  - **NOTA**: Se non hai Python 3.12 installato, assicurati di installarlo. Poi crea il tuo ambiente virtuale usando python3.12 per garantire che vengano installate le versioni corrette dal file requirements.txt.  
- Un Account GitHub - Per accedere al GitHub Models Marketplace  
- Abbonamento Azure - Per accedere ad Azure AI Foundry  
- Account Azure AI Foundry - Per accedere al servizio Azure AI Agent  

Abbiamo incluso un file `requirements.txt` nella radice di questo repository che contiene tutti i pacchetti Python necessari per eseguire gli esempi di codice.

Puoi installarli eseguendo il seguente comando nel terminale nella radice del repository:

```bash
pip install -r requirements.txt
```  
Ti consigliamo di creare un ambiente virtuale Python per evitare conflitti e problemi.

## Configurare VSCode
Assicurati di utilizzare la versione corretta di Python in VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configurazione per gli Esempi con i Modelli GitHub 

### Passaggio 1: Recupera il tuo GitHub Personal Access Token (PAT)

Questo corso utilizza il GitHub Models Marketplace, che offre accesso gratuito a Modelli di Linguaggio di Grandi Dimensioni (LLM) che userai per creare Agenti AI.

Per utilizzare i Modelli GitHub, dovrai creare un [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Puoi farlo accedendo al tuo Account GitHub.

Segui il [Principio del Minimo Privilegio](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) quando crei il tuo token. Questo significa che dovresti assegnare al token solo i permessi necessari per eseguire gli esempi di codice di questo corso.

1. Seleziona l'opzione `Fine-grained tokens` sul lato sinistro dello schermo.

    Poi seleziona `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.it.png)

1. Inserisci un nome descrittivo per il tuo token che rifletta il suo scopo, rendendolo facile da identificare in seguito. Imposta una data di scadenza (consigliato: 30 giorni; puoi scegliere un periodo più breve, come 7 giorni, se preferisci una maggiore sicurezza).

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.it.png)

1. Limita l'ambito del token al tuo fork di questo repository.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.it.png)

1. Restringi i permessi del token: Sotto **Permissions**, attiva **Account Permissions**, vai a **Models** e abilita solo l'accesso in lettura richiesto per i Modelli GitHub.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.it.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.it.png)

Copia il nuovo token che hai appena creato. Ora lo aggiungerai al file `.env` incluso in questo corso.

### Passaggio 2: Crea il tuo File `.env`

Per creare il file `.env`, esegui il seguente comando nel terminale.

```bash
cp .env.example .env
```

Questo copierà il file di esempio e creerà un `.env` nella tua directory, dove potrai inserire i valori per le variabili di ambiente.

Con il tuo token copiato, apri il file `.env` nel tuo editor di testo preferito e incolla il token nel campo `GITHUB_TOKEN`.

Ora dovresti essere in grado di eseguire gli esempi di codice di questo corso.

## Configurazione per gli Esempi con Azure AI Foundry e Azure AI Agent Service

### Passaggio 1: Recupera l'Endpoint del tuo Progetto Azure

Segui i passaggi per creare un hub e un progetto in Azure AI Foundry qui: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Una volta creato il tuo progetto, dovrai recuperare la stringa di connessione per il tuo progetto.

Puoi farlo accedendo alla pagina **Overview** del tuo progetto nel portale Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.it.png)

### Passaggio 2: Crea il tuo File `.env`

Per creare il file `.env`, esegui il seguente comando nel terminale.

```bash
cp .env.example .env
```

Questo copierà il file di esempio e creerà un `.env` nella tua directory, dove potrai inserire i valori per le variabili di ambiente.

Con il tuo token copiato, apri il file `.env` nel tuo editor di testo preferito e incolla il token nel campo `PROJECT_ENDPOINT`.

### Passaggio 3: Accedi ad Azure

Come buona pratica di sicurezza, utilizzeremo [l'autenticazione senza chiavi](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) per autenticarti ad Azure OpenAI con Microsoft Entra ID.

Successivamente, apri un terminale ed esegui `az login --use-device-code` per accedere al tuo account Azure.

Una volta effettuato l'accesso, seleziona il tuo abbonamento nel terminale.

## Variabili di Ambiente Aggiuntive - Azure Search e Azure OpenAI 

Per la lezione Agentic RAG - Lezione 5 - ci sono esempi che utilizzano Azure Search e Azure OpenAI.

Se vuoi eseguire questi esempi, dovrai aggiungere le seguenti variabili di ambiente al tuo file `.env`:

### Pagina Overview (Progetto)

- `AZURE_SUBSCRIPTION_ID` - Controlla **Project details** nella pagina **Overview** del tuo progetto.

- `AZURE_AI_PROJECT_NAME` - Guarda in alto nella pagina **Overview** del tuo progetto.

- `AZURE_OPENAI_SERVICE` - Trova questo nella scheda **Included capabilities** per **Azure OpenAI Service** nella pagina **Overview**.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Vai a **Project properties** nella pagina **Overview** del **Management Center**.

- `GLOBAL_LLM_SERVICE` - Sotto **Connected resources**, trova il nome della connessione **Azure AI Services**. Se non è elencato, controlla il **portale Azure** sotto il tuo gruppo di risorse per il nome della risorsa AI Services.

### Pagina Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Seleziona il tuo modello di embedding (es. `text-embedding-ada-002`) e annota il **Deployment name** dai dettagli del modello.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Seleziona il tuo modello di chat (es. `gpt-4o-mini`) e annota il **Deployment name** dai dettagli del modello.

### Portale Azure

- `AZURE_OPENAI_ENDPOINT` - Cerca **Azure AI services**, cliccaci sopra, poi vai a **Resource Management**, **Keys and Endpoint**, scorri fino agli "Azure OpenAI endpoints" e copia quello che dice "Language APIs".

- `AZURE_OPENAI_API_KEY` - Dalla stessa schermata, copia KEY 1 o KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Trova la tua risorsa **Azure AI Search**, cliccaci sopra e guarda **Overview**.

- `AZURE_SEARCH_API_KEY` - Poi vai a **Settings** e poi **Keys** per copiare la chiave primaria o secondaria dell'amministratore.

### Pagina Esterna

- `AZURE_OPENAI_API_VERSION` - Visita la pagina [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sotto **Latest GA API release**.

### Configurare l'autenticazione senza chiavi

Invece di codificare le tue credenziali, utilizzeremo una connessione senza chiavi con Azure OpenAI. Per farlo, importeremo `DefaultAzureCredential` e successivamente chiameremo la funzione `DefaultAzureCredential` per ottenere le credenziali.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bloccato da qualche parte?

Se hai problemi con questa configurazione, entra nel nostro

## Prossima Lezione

Ora sei pronto per eseguire il codice di questo corso. Buon apprendimento sul mondo degli Agenti AI!

[Introduzione agli Agenti AI e ai Casi d'Uso degli Agenti](../01-intro-to-ai-agents/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.