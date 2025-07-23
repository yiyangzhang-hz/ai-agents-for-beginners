<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:48:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sv"
}
-->
# Kursinställning

## Introduktion

Den här lektionen kommer att täcka hur du kör kodexemplen i denna kurs.

## Klona eller Forka detta Repo

För att börja, klona eller forka GitHub-repositoriet. Detta skapar din egen version av kursmaterialet så att du kan köra, testa och anpassa koden!

Detta kan göras genom att klicka på länken till

Du bör nu ha din egen forkade version av kursen på följande länk:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sv.png)

## Köra koden

Den här kursen erbjuder en serie Jupyter Notebooks som du kan köra för att få praktisk erfarenhet av att bygga AI-agenter.

Kodexemplen använder antingen:

**Kräver GitHub-konto - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Märkt som (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Märkt som (autogen.ipynb)

**Kräver Azure-abonnemang**:
3) Azure AI Foundry + Azure AI Agent Service. Märkt som (azureaiagent.ipynb)

Vi uppmuntrar dig att prova alla tre typer av exempel för att se vilket som fungerar bäst för dig.

Vilket alternativ du än väljer kommer att avgöra vilka installationssteg du behöver följa nedan:

## Krav

- Python 3.12+
  - **OBS**: Om du inte har Python 3.12 installerat, se till att installera det. Skapa sedan din venv med python3.12 för att säkerställa att rätt versioner installeras från filen requirements.txt.
- Ett GitHub-konto - För åtkomst till GitHub Models Marketplace
- Azure-abonnemang - För åtkomst till Azure AI Foundry
- Azure AI Foundry-konto - För åtkomst till Azure AI Agent Service

Vi har inkluderat en `requirements.txt`-fil i roten av detta repo som innehåller alla nödvändiga Python-paket för att köra kodexemplen.

Du kan installera dem genom att köra följande kommando i din terminal i repo-rotmappen:

```bash
pip install -r requirements.txt
```
Vi rekommenderar att du skapar en Python-virtuell miljö för att undvika konflikter och problem.

## Installera VSCode
Se till att du använder rätt version av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Installation för exempel med GitHub-modeller

### Steg 1: Hämta din GitHub Personal Access Token (PAT)

Den här kursen använder GitHub Models Marketplace, som ger gratis åtkomst till Large Language Models (LLMs) som du kommer att använda för att bygga AI-agenter.

För att använda GitHub-modellerna måste du skapa en [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Detta kan göras genom att gå till din GitHub-konto.

Följ [Principen om minsta privilegier](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) när du skapar din token. Detta innebär att du endast bör ge token de behörigheter som krävs för att köra kodexemplen i denna kurs.

1. Välj alternativet `Fine-grained tokens` på vänster sida av skärmen.

    Välj sedan `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.sv.png)

1. Ange ett beskrivande namn för din token som reflekterar dess syfte, så att det blir lätt att identifiera senare. Ställ in ett utgångsdatum (rekommenderat: 30 dagar; du kan välja en kortare period som 7 dagar om du föredrar en säkrare inställning).

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sv.png)

1. Begränsa tokenens räckvidd till din fork av detta repo.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.sv.png)

1. Begränsa tokenens behörigheter: Under **Permissions**, aktivera **Account Permissions**, navigera till **Models** och aktivera endast den läsbehörighet som krävs för GitHub-modeller.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.sv.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.sv.png)

Kopiera din nya token som du just har skapat. Du kommer nu att lägga till detta i din `.env`-fil som ingår i denna kurs.

### Steg 2: Skapa din `.env`-fil

För att skapa din `.env`-fil, kör följande kommando i din terminal.

```bash
cp .env.example .env
```

Detta kopierar exempel-filen och skapar en `.env` i din katalog där du fyller i värdena för miljövariablerna.

Med din token kopierad, öppna `.env`-filen i din favorittextredigerare och klistra in din token i fältet `GITHUB_TOKEN`.

Du bör nu kunna köra kodexemplen i denna kurs.

## Installation för exempel med Azure AI Foundry och Azure AI Agent Service

### Steg 1: Hämta din Azure-projektendpoint

Följ stegen för att skapa en hub och ett projekt i Azure AI Foundry som finns här: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

När du har skapat ditt projekt måste du hämta anslutningssträngen för ditt projekt.

Detta kan göras genom att gå till **Overview**-sidan för ditt projekt i Azure AI Foundry-portalen.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sv.png)

### Steg 2: Skapa din `.env`-fil

För att skapa din `.env`-fil, kör följande kommando i din terminal.

```bash
cp .env.example .env
```

Detta kopierar exempel-filen och skapar en `.env` i din katalog där du fyller i värdena för miljövariablerna.

Med din token kopierad, öppna `.env`-filen i din favorittextredigerare och klistra in din token i fältet `PROJECT_ENDPOINT`.

### Steg 3: Logga in på Azure

Som en säkerhetsbästa praxis kommer vi att använda [nyckellös autentisering](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) för att autentisera till Azure OpenAI med Microsoft Entra ID.

Öppna sedan en terminal och kör `az login --use-device-code` för att logga in på ditt Azure-konto.

När du har loggat in, välj ditt abonnemang i terminalen.

## Ytterligare miljövariabler - Azure Search och Azure OpenAI

För lektionen Agentic RAG - Lektion 5 - finns det exempel som använder Azure Search och Azure OpenAI.

Om du vill köra dessa exempel måste du lägga till följande miljövariabler i din `.env`-fil:

### Översiktssida (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Kontrollera **Project details** på **Overview**-sidan för ditt projekt.

- `AZURE_AI_PROJECT_NAME` - Titta längst upp på **Overview**-sidan för ditt projekt.

- `AZURE_OPENAI_SERVICE` - Hitta detta i fliken **Included capabilities** för **Azure OpenAI Service** på **Overview**-sidan.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Gå till **Project properties** på **Overview**-sidan för **Management Center**.

- `GLOBAL_LLM_SERVICE` - Under **Connected resources**, hitta anslutningsnamnet för **Azure AI Services**. Om det inte listas, kontrollera **Azure portal** under din resursgrupp för AI Services-resursnamnet.

### Models + Endpoints-sida

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Välj din embedding-modell (t.ex. `text-embedding-ada-002`) och notera **Deployment name** från modellens detaljer.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Välj din chat-modell (t.ex. `gpt-4o-mini`) och notera **Deployment name** från modellens detaljer.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Leta efter **Azure AI services**, klicka på det, gå sedan till **Resource Management**, **Keys and Endpoint**, scrolla ner till "Azure OpenAI endpoints", och kopiera den som säger "Language APIs".

- `AZURE_OPENAI_API_KEY` - Från samma skärm, kopiera KEY 1 eller KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Hitta din **Azure AI Search**-resurs, klicka på den och se **Overview**.

- `AZURE_SEARCH_API_KEY` - Gå sedan till **Settings** och sedan **Keys** för att kopiera den primära eller sekundära admin-nyckeln.

### Extern webbsida

- `AZURE_OPENAI_API_VERSION` - Besök sidan [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) under **Latest GA API release**.

### Installera nyckellös autentisering

Istället för att hårdkoda dina autentiseringsuppgifter kommer vi att använda en nyckellös anslutning med Azure OpenAI. För att göra detta kommer vi att importera `DefaultAzureCredential` och senare kalla på funktionen `DefaultAzureCredential` för att få autentiseringen.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Fastnat någonstans?

Om du har några problem med att köra denna installation, hoppa in i vår

## Nästa lektion

Du är nu redo att köra koden för denna kurs. Lycka till med att lära dig mer om AI-agenter!

[Introduktion till AI-agenter och användningsfall för agenter](../01-intro-to-ai-agents/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.