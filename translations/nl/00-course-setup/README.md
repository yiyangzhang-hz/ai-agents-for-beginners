<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-29T17:25:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Cursusinstelling

## Introductie

Deze les behandelt hoe je de codevoorbeelden van deze cursus kunt uitvoeren.

## Sluit je aan bij andere cursisten en krijg hulp

Voordat je begint met het klonen van je repository, sluit je aan bij het [AI Agents For Beginners Discord-kanaal](https://aka.ms/ai-agents/discord) om hulp te krijgen bij de installatie, vragen over de cursus te stellen of om in contact te komen met andere cursisten.

## Clone of Fork deze Repository

Om te beginnen, clone of fork de GitHub Repository. Hiermee maak je je eigen versie van het cursusmateriaal zodat je de code kunt uitvoeren, testen en aanpassen!

Dit kan worden gedaan door op de link te klikken naar

Je zou nu je eigen geforkte versie van deze cursus moeten hebben via de volgende link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.nl.png)

## De code uitvoeren

Deze cursus biedt een reeks Jupyter Notebooks waarmee je praktische ervaring kunt opdoen in het bouwen van AI Agents.

De codevoorbeelden maken gebruik van:

**Vereist een GitHub-account - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Gelabeld als (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Gelabeld als (autogen.ipynb)

**Vereist een Azure-abonnement**:
3) Azure AI Foundry + Azure AI Agent Service. Gelabeld als (azureaiagent.ipynb)

We moedigen je aan om alle drie de soorten voorbeelden uit te proberen om te zien welke het beste bij je past.

Welke optie je ook kiest, dit bepaalt welke installatie-instructies je hieronder moet volgen:

## Vereisten

- Python 3.12+
  - **NOTE**: Als je Python3.12 niet hebt geïnstalleerd, zorg er dan voor dat je het installeert. Maak vervolgens je venv aan met python3.12 om ervoor te zorgen dat de juiste versies worden geïnstalleerd vanuit het requirements.txt-bestand.
- Een GitHub-account - Voor toegang tot de GitHub Models Marketplace
- Azure-abonnement - Voor toegang tot Azure AI Foundry
- Azure AI Foundry-account - Voor toegang tot de Azure AI Agent Service

We hebben een `requirements.txt`-bestand opgenomen in de root van deze repository dat alle vereiste Python-pakketten bevat om de codevoorbeelden uit te voeren.

Je kunt ze installeren door het volgende commando in je terminal uit te voeren in de root van de repository:

```bash
pip install -r requirements.txt
```
We raden aan om een Python virtual environment te maken om conflicten en problemen te voorkomen.

## VSCode instellen
Zorg ervoor dat je de juiste versie van Python gebruikt in VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Instellen voor voorbeelden met GitHub Models 

### Stap 1: Haal je GitHub Personal Access Token (PAT) op

Deze cursus maakt gebruik van de GitHub Models Marketplace, die gratis toegang biedt tot Large Language Models (LLMs) die je zult gebruiken om AI Agents te bouwen.

Om de GitHub Models te gebruiken, moet je een [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) aanmaken.

Dit kan worden gedaan door naar je GitHub-account te gaan.

Volg het [Principe van Minimale Toegang](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) bij het aanmaken van je token. Dit betekent dat je het token alleen de rechten moet geven die nodig zijn om de codevoorbeelden in deze cursus uit te voeren.

1. Selecteer de optie `Fine-grained tokens` aan de linkerkant van je scherm door naar **Developer settings** te gaan.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.nl.png)

    Selecteer vervolgens `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.nl.png)

2. Geef je token een beschrijvende naam die het doel ervan weerspiegelt, zodat je het later gemakkelijk kunt identificeren.

    🔐 Aanbevolen tokenduur

    Aanbevolen duur: 30 dagen
    Voor een veiliger aanpak kun je kiezen voor een kortere periode, zoals 7 dagen 🛡️
    Dit is een geweldige manier om jezelf een persoonlijk doel te stellen en de cursus te voltooien terwijl je leerdrang hoog is 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.nl.png)

3. Beperk de reikwijdte van het token tot je fork van deze repository.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.nl.png)

4. Beperk de rechten van het token: Onder **Permissions**, klik op het tabblad **Account** en klik op de knop "+ Add permissions". Er verschijnt een dropdown. Zoek naar **Models** en vink het vakje aan.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.nl.png)

5. Controleer de vereiste rechten voordat je het token genereert. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.nl.png)

6. Zorg ervoor dat je het token op een veilige plek opslaat, zoals een wachtwoordmanager, aangezien het niet opnieuw wordt weergegeven nadat je het hebt aangemaakt. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.nl.png)

Kopieer je nieuwe token dat je zojuist hebt aangemaakt. Je voegt dit nu toe aan je `.env`-bestand dat bij deze cursus is inbegrepen.

### Stap 2: Maak je `.env`-bestand

Om je `.env`-bestand te maken, voer je het volgende commando uit in je terminal.

```bash
cp .env.example .env
```

Dit kopieert het voorbeeldbestand en maakt een `.env` in je directory waar je de waarden voor de omgevingsvariabelen invult.

Met je gekopieerde token open je het `.env`-bestand in je favoriete teksteditor en plak je je token in het `GITHUB_TOKEN`-veld.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.nl.png)

Je zou nu de codevoorbeelden van deze cursus moeten kunnen uitvoeren.

## Instellen voor voorbeelden met Azure AI Foundry en Azure AI Agent Service

### Stap 1: Haal je Azure Project Endpoint op

Volg de stappen om een hub en project te maken in Azure AI Foundry die hier te vinden zijn: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Zodra je je project hebt aangemaakt, moet je de verbindingsreeks voor je project ophalen.

Dit kan worden gedaan door naar de **Overview**-pagina van je project in de Azure AI Foundry-portal te gaan.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.nl.png)

### Stap 2: Maak je `.env`-bestand

Om je `.env`-bestand te maken, voer je het volgende commando uit in je terminal.

```bash
cp .env.example .env
```

Dit kopieert het voorbeeldbestand en maakt een `.env` in je directory waar je de waarden voor de omgevingsvariabelen invult.

Met je gekopieerde token open je het `.env`-bestand in je favoriete teksteditor en plak je je token in het `PROJECT_ENDPOINT`-veld.

### Stap 3: Log in bij Azure

Als een beveiligingsmaatregel gebruiken we [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) om te authenticeren bij Azure OpenAI met Microsoft Entra ID.

Open vervolgens een terminal en voer `az login --use-device-code` uit om in te loggen bij je Azure-account.

Zodra je bent ingelogd, selecteer je je abonnement in de terminal.

## Extra omgevingsvariabelen - Azure Search en Azure OpenAI 

Voor de Agentic RAG-les - Les 5 - zijn er voorbeelden die gebruik maken van Azure Search en Azure OpenAI.

Als je deze voorbeelden wilt uitvoeren, moet je de volgende omgevingsvariabelen toevoegen aan je `.env`-bestand:

### Overzichtspagina (Project)

- `AZURE_SUBSCRIPTION_ID` - Controleer **Project details** op de **Overview**-pagina van je project.

- `AZURE_AI_PROJECT_NAME` - Kijk bovenaan de **Overview**-pagina van je project.

- `AZURE_OPENAI_SERVICE` - Vind dit in het tabblad **Included capabilities** voor **Azure OpenAI Service** op de **Overview**-pagina.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Ga naar **Project properties** op de **Overview**-pagina van het **Management Center**.

- `GLOBAL_LLM_SERVICE` - Onder **Connected resources**, vind de **Azure AI Services**-verbinding. Als deze niet wordt vermeld, controleer dan de **Azure portal** onder je resourcegroep voor de AI Services-resource.

### Models + Endpoints-pagina

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecteer je embedding-model (bijv. `text-embedding-ada-002`) en noteer de **Deployment name** uit de modeldetails.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecteer je chatmodel (bijv. `gpt-4o-mini`) en noteer de **Deployment name** uit de modeldetails.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Zoek naar **Azure AI services**, klik erop, ga naar **Resource Management**, **Keys and Endpoint**, scroll naar beneden naar "Azure OpenAI endpoints" en kopieer degene die "Language APIs" zegt.

- `AZURE_OPENAI_API_KEY` - Kopieer vanaf hetzelfde scherm KEY 1 of KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Vind je **Azure AI Search**-resource, klik erop en bekijk **Overview**.

- `AZURE_SEARCH_API_KEY` - Ga vervolgens naar **Settings** en daarna **Keys** om de primaire of secundaire beheerderssleutel te kopiëren.

### Externe webpagina

- `AZURE_OPENAI_API_VERSION` - Bezoek de [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release)-pagina onder **Latest GA API release**.

### Keyless authentication instellen

In plaats van je inloggegevens hard te coderen, gebruiken we een keyless verbinding met Azure OpenAI. Hiervoor importeren we `DefaultAzureCredential` en roepen we later de functie `DefaultAzureCredential` aan om de inloggegevens te verkrijgen.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Vastgelopen?

Als je problemen hebt met deze installatie, spring dan in onze

## Volgende les

Je bent nu klaar om de code voor deze cursus uit te voeren. Veel plezier met het leren over de wereld van AI Agents! 

[Introductie tot AI Agents en Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.