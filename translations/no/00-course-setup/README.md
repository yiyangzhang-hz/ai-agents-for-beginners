<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8693a24942b670e3cb8def77f92513f9",
  "translation_date": "2025-08-21T13:19:05+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Kursoppsett

## Introduksjon

Denne leksjonen dekker hvordan du kan kjøre kodeeksemplene i dette kurset.

## Klon eller fork dette repoet

For å komme i gang, vennligst klon eller fork GitHub-repositoriet. Dette vil lage din egen versjon av kursmaterialet slik at du kan kjøre, teste og tilpasse koden!

Dette kan gjøres ved å klikke på lenken til

Du bør nå ha din egen forkede versjon av dette kurset på følgende lenke:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.no.png)

## Kjøre koden

Dette kurset tilbyr en serie Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker enten:

**Krever GitHub-konto - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Merket som (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Merket som (autogen.ipynb)

**Krever Azure-abonnement**:  
3) Azure AI Foundry + Azure AI Agent Service. Merket som (azureaiagent.ipynb)

Vi oppfordrer deg til å prøve alle tre typene eksempler for å se hvilken som fungerer best for deg.

Uansett hvilket alternativ du velger, vil det avgjøre hvilke oppsettsteg du må følge nedenfor:

## Krav

- Python 3.12+  
  - **MERK**: Hvis du ikke har Python 3.12 installert, sørg for å installere det. Opprett deretter ditt virtuelle miljø (venv) ved å bruke python3.12 for å sikre at de riktige versjonene installeres fra requirements.txt-filen.
- En GitHub-konto - For tilgang til GitHub Models Marketplace
- Azure-abonnement - For tilgang til Azure AI Foundry
- Azure AI Foundry-konto - For tilgang til Azure AI Agent Service

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i roten av repositoriet:

```bash
pip install -r requirements.txt
```  
Vi anbefaler å opprette et virtuelt Python-miljø for å unngå konflikter og problemer.

## Oppsett av VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Oppsett for eksempler som bruker GitHub-modeller

### Steg 1: Hent din GitHub Personal Access Token (PAT)

Dette kurset bruker GitHub Models Marketplace, som gir gratis tilgang til Large Language Models (LLMs) som du vil bruke til å bygge AI-agenter.

For å bruke GitHub-modellene må du opprette en [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Dette kan gjøres ved å gå til din GitHub-konto.

Vennligst følg [Prinsippet om minst privilegium](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) når du oppretter tokenet ditt. Dette betyr at du kun skal gi tokenet de tillatelsene det trenger for å kjøre kodeeksemplene i dette kurset.

1. Velg alternativet `Fine-grained tokens` på venstre side av skjermen ved å navigere til **Developer settings**  
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.no.png)

   Velg deretter `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.no.png)

2. Skriv inn et beskrivende navn for tokenet som gjenspeiler formålet, slik at det er enkelt å identifisere senere.

   🔐 Anbefalt varighet for token

   Anbefalt varighet: 30 dager  
   For en mer sikker tilnærming kan du velge en kortere periode—som 7 dager 🛡️  
   Det er en flott måte å sette et personlig mål og fullføre kurset mens læringsmomentet er høyt 🚀.

   ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.no.png)

3. Begrens tokenets omfang til din fork av dette repositoriet.

   ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.no.png)

4. Begrens tokenets tillatelser: Under **Permissions**, klikk på **Account**-fanen, og klikk på "+ Add permissions"-knappen. En rullegardinmeny vil vises. Søk etter **Models** og merk av i boksen for det.  
   ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.no.png)

5. Verifiser de nødvendige tillatelsene før du genererer tokenet. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.no.png)

6. Før du genererer tokenet, sørg for at du er klar til å lagre tokenet på et sikkert sted, som en passordhåndterer, da det ikke vil bli vist igjen etter at du har opprettet det. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.no.png)

Kopier ditt nye token som du nettopp har opprettet. Du vil nå legge dette til i `.env`-filen som er inkludert i dette kurset.

### Steg 2: Opprett din `.env`-fil

For å opprette `.env`-filen, kjør følgende kommando i terminalen.

```bash
cp .env.example .env
```

Dette vil kopiere eksempel-filen og opprette en `.env` i katalogen din, hvor du fyller inn verdiene for miljøvariablene.

Med tokenet ditt kopiert, åpne `.env`-filen i din favoritt teksteditor og lim inn tokenet i `GITHUB_TOKEN`-feltet.  
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.no.png)

Du skal nå kunne kjøre kodeeksemplene i dette kurset.

## Oppsett for eksempler som bruker Azure AI Foundry og Azure AI Agent Service

### Steg 1: Hent din Azure-prosjekt-endepunkt

Følg stegene for å opprette en hub og et prosjekt i Azure AI Foundry som beskrevet her: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Når du har opprettet prosjektet ditt, må du hente tilkoblingsstrengen for prosjektet ditt.

Dette kan gjøres ved å gå til **Overview**-siden for prosjektet ditt i Azure AI Foundry-portalen.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.no.png)

### Steg 2: Opprett din `.env`-fil

For å opprette `.env`-filen, kjør følgende kommando i terminalen.

```bash
cp .env.example .env
```

Dette vil kopiere eksempel-filen og opprette en `.env` i katalogen din, hvor du fyller inn verdiene for miljøvariablene.

Med tokenet ditt kopiert, åpne `.env`-filen i din favoritt teksteditor og lim inn tokenet i `PROJECT_ENDPOINT`-feltet.

### Steg 3: Logg inn på Azure

Som en sikkerhetsmessig beste praksis vil vi bruke [nøkkelfri autentisering](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) for å autentisere til Azure OpenAI med Microsoft Entra ID.

Åpne deretter en terminal og kjør `az login --use-device-code` for å logge inn på Azure-kontoen din.

Når du har logget inn, velg abonnementet ditt i terminalen.

## Ytterligere miljøvariabler - Azure Search og Azure OpenAI

For Agentic RAG-leksjonen - Leksjon 5 - finnes det eksempler som bruker Azure Search og Azure OpenAI.

Hvis du vil kjøre disse eksemplene, må du legge til følgende miljøvariabler i `.env`-filen din:

### Oversiktsside (Prosjekt)

- `AZURE_SUBSCRIPTION_ID` - Sjekk **Project details** på **Overview**-siden for prosjektet ditt.

- `AZURE_AI_PROJECT_NAME` - Se øverst på **Overview**-siden for prosjektet ditt.

- `AZURE_OPENAI_SERVICE` - Finn dette i **Included capabilities**-fanen for **Azure OpenAI Service** på **Overview**-siden.

### Administrasjonssenter

- `AZURE_OPENAI_RESOURCE_GROUP` - Gå til **Project properties** på **Overview**-siden for **Management Center**.

- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, finn navnet på **Azure AI Services**-tilkoblingen. Hvis det ikke er oppført, sjekk **Azure-portalen** under ressursgruppen din for navnet på AI Services-ressursen.

### Modeller + Endepunktside

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Velg din embedding-modell (f.eks. `text-embedding-ada-002`) og noter **Deployment name** fra modelldetaljene.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Velg din chat-modell (f.eks. `gpt-4o-mini`) og noter **Deployment name** fra modelldetaljene.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Se etter **Azure AI services**, klikk på det, gå deretter til **Resource Management**, **Keys and Endpoint**, bla ned til "Azure OpenAI endpoints", og kopier den som sier "Language APIs".

- `AZURE_OPENAI_API_KEY` - Fra samme skjerm, kopier NØKKEL 1 eller NØKKEL 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Finn ressursen din for **Azure AI Search**, klikk på den, og se **Overview**.

- `AZURE_SEARCH_API_KEY` - Gå deretter til **Settings** og deretter **Keys** for å kopiere den primære eller sekundære administratørnøkkelen.

### Ekstern nettside

- `AZURE_OPENAI_API_VERSION` - Besøk siden [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) under **Latest GA API release**.

### Oppsett av nøkkelfri autentisering

I stedet for å hardkode legitimasjonen din, vil vi bruke en nøkkelfri tilkobling med Azure OpenAI. For å gjøre dette, vil vi importere `DefaultAzureCredential` og senere kalle funksjonen `DefaultAzureCredential` for å hente legitimasjonen.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Sitter du fast?

Hvis du har problemer med å kjøre dette oppsettet, hopp inn i vår

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om AI-agenter!  

[Introduksjon til AI-agenter og bruksområder](../01-intro-to-ai-agents/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.