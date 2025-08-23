<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8693a24942b670e3cb8def77f92513f9",
  "translation_date": "2025-08-21T13:50:04+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sk"
}
-->
# Nastavenie kurzu

## Úvod

Táto lekcia sa zaoberá tým, ako spustiť ukážky kódu z tohto kurzu.

## Klonovanie alebo Forkovanie tohto repozitára

Na začiatok si prosím klonujte alebo forknite GitHub repozitár. Týmto si vytvoríte vlastnú verziu materiálov kurzu, aby ste mohli spúšťať, testovať a upravovať kód!

Toto môžete urobiť kliknutím na odkaz na

Mali by ste mať vlastnú forknutú verziu tohto kurzu na nasledujúcom odkaze:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sk.png)

## Spúšťanie kódu

Tento kurz ponúka sériu Jupyter Notebookov, ktoré môžete spustiť, aby ste získali praktické skúsenosti s budovaním AI agentov.

Ukážky kódu používajú buď:

**Vyžaduje GitHub účet - zdarma**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označené ako (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Označené ako (autogen.ipynb)

**Vyžaduje Azure predplatné**:
3) Azure AI Foundry + Azure AI Agent Service. Označené ako (azureaiagent.ipynb)

Odporúčame vám vyskúšať všetky tri typy príkladov, aby ste zistili, ktorý vám najviac vyhovuje.

Podľa toho, ktorú možnosť si vyberiete, budete musieť postupovať podľa príslušných krokov nastavenia uvedených nižšie:

## Požiadavky

- Python 3.12+
  - **POZNÁMKA**: Ak nemáte nainštalovaný Python 3.12, uistite sa, že ho nainštalujete. Potom vytvorte svoj venv pomocou python3.12, aby ste zabezpečili správne verzie nainštalované zo súboru requirements.txt.
- GitHub účet - na prístup k GitHub Models Marketplace
- Azure predplatné - na prístup k Azure AI Foundry
- Azure AI Foundry účet - na prístup k Azure AI Agent Service

V koreňovom adresári tohto repozitára sme zahrnuli súbor `requirements.txt`, ktorý obsahuje všetky potrebné Python balíčky na spustenie ukážok kódu.

Môžete ich nainštalovať spustením nasledujúceho príkazu vo vašom termináli v koreňovom adresári repozitára:

```bash
pip install -r requirements.txt
```
Odporúčame vytvoriť Python virtuálne prostredie, aby ste sa vyhli konfliktom a problémom.

## Nastavenie VSCode
Uistite sa, že používate správnu verziu Pythonu vo VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavenie pre ukážky s GitHub modelmi 

### Krok 1: Získanie vášho GitHub Personal Access Token (PAT)

Tento kurz využíva GitHub Models Marketplace, ktorý poskytuje bezplatný prístup k Large Language Models (LLMs), ktoré budete používať na budovanie AI agentov.

Na použitie GitHub modelov budete musieť vytvoriť [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Toto môžete urobiť vo vašom GitHub účte.

Prosím, dodržiavajte [Princíp minimálnych oprávnení](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) pri vytváraní vášho tokenu. To znamená, že by ste mali tokenu prideliť iba tie oprávnenia, ktoré sú potrebné na spustenie ukážok kódu v tomto kurze.

1. Na ľavej strane obrazovky vyberte možnosť `Fine-grained tokens` v sekcii **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sk.png)

    Potom vyberte `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sk.png)

2. Zadajte popisný názov pre váš token, ktorý odráža jeho účel, aby ste ho neskôr ľahko identifikovali.

    🔐 Odporúčanie pre trvanie tokenu

    Odporúčané trvanie: 30 dní
    Pre bezpečnejší prístup môžete zvoliť kratšie obdobie—napríklad 7 dní 🛡️
    Je to skvelý spôsob, ako si stanoviť osobný cieľ a dokončiť kurz, kým je vaše učebné tempo vysoké 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sk.png)

3. Obmedzte rozsah tokenu na váš fork tohto repozitára.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sk.png)

4. Obmedzte oprávnenia tokenu: V sekcii **Permissions** kliknite na záložku **Account** a potom na tlačidlo "+ Add permissions". Zobrazí sa rozbaľovacie menu. Vyhľadajte **Models** a zaškrtnite políčko.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sk.png)

5. Pred generovaním tokenu overte požadované oprávnenia. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sk.png)

6. Pred generovaním tokenu sa uistite, že ste pripravení uložiť token na bezpečné miesto, ako je trezor správcu hesiel, pretože po jeho vytvorení už nebude zobrazený. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sk.png)

Skopírujte váš nový token, ktorý ste práve vytvorili. Teraz ho pridáte do vášho `.env` súboru zahrnutého v tomto kurze.

### Krok 2: Vytvorenie vášho `.env` súboru

Na vytvorenie `.env` súboru spustite nasledujúci príkaz vo vašom termináli.

```bash
cp .env.example .env
```

Týmto sa skopíruje príkladový súbor a vytvorí `.env` vo vašom adresári, kde vyplníte hodnoty pre environmentálne premenné.

S vaším skopírovaným tokenom otvorte `.env` súbor vo vašom obľúbenom textovom editore a vložte váš token do poľa `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sk.png)

Teraz by ste mali byť schopní spustiť ukážky kódu z tohto kurzu.

## Nastavenie pre ukážky s Azure AI Foundry a Azure AI Agent Service

### Krok 1: Získanie vášho Azure Project Endpoint

Postupujte podľa krokov na vytvorenie hubu a projektu v Azure AI Foundry, ktoré nájdete tu: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Keď ste vytvorili váš projekt, budete musieť získať reťazec pripojenia pre váš projekt.

Toto môžete urobiť na stránke **Overview** vášho projektu v Azure AI Foundry portáli.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sk.png)

### Krok 2: Vytvorenie vášho `.env` súboru

Na vytvorenie `.env` súboru spustite nasledujúci príkaz vo vašom termináli.

```bash
cp .env.example .env
```

Týmto sa skopíruje príkladový súbor a vytvorí `.env` vo vašom adresári, kde vyplníte hodnoty pre environmentálne premenné.

S vaším skopírovaným tokenom otvorte `.env` súbor vo vašom obľúbenom textovom editore a vložte váš token do poľa `PROJECT_ENDPOINT`.

### Krok 3: Prihlásenie do Azure

Ako bezpečnostnú najlepšiu prax použijeme [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) na autentifikáciu do Azure OpenAI pomocou Microsoft Entra ID.

Ďalej otvorte terminál a spustite `az login --use-device-code`, aby ste sa prihlásili do vášho Azure účtu.

Keď ste prihlásení, vyberte vaše predplatné v termináli.

## Ďalšie environmentálne premenné - Azure Search a Azure OpenAI 

Pre lekciu Agentic RAG - Lekcia 5 - existujú ukážky, ktoré používajú Azure Search a Azure OpenAI.

Ak chcete spustiť tieto ukážky, budete musieť pridať nasledujúce environmentálne premenné do vášho `.env` súboru:

### Stránka prehľadu (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Skontrolujte **Project details** na stránke **Overview** vášho projektu.

- `AZURE_AI_PROJECT_NAME` - Pozrite sa na vrch stránky **Overview** vášho projektu.

- `AZURE_OPENAI_SERVICE` - Nájdite to v záložke **Included capabilities** pre **Azure OpenAI Service** na stránke **Overview**.

### Centrum správy

- `AZURE_OPENAI_RESOURCE_GROUP` - Choďte na **Project properties** na stránke **Overview** v **Management Center**.

- `GLOBAL_LLM_SERVICE` - Pod **Connected resources** nájdite názov pripojenia **Azure AI Services**. Ak nie je uvedený, skontrolujte **Azure portal** vo vašej skupine zdrojov pre názov zdroja AI Services.

### Stránka modelov + endpointov

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vyberte váš embedding model (napr. `text-embedding-ada-002`) a poznačte si **Deployment name** z detailov modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vyberte váš chat model (napr. `gpt-4o-mini`) a poznačte si **Deployment name** z detailov modelu.

### Azure portál

- `AZURE_OPENAI_ENDPOINT` - Nájdite **Azure AI services**, kliknite na to, potom choďte na **Resource Management**, **Keys and Endpoint**, posuňte sa dole na "Azure OpenAI endpoints" a skopírujte ten, ktorý hovorí "Language APIs".

- `AZURE_OPENAI_API_KEY` - Z tej istej obrazovky skopírujte KEY 1 alebo KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Nájdite váš **Azure AI Search** zdroj, kliknite na to a pozrite si **Overview**.

- `AZURE_SEARCH_API_KEY` - Potom choďte na **Settings** a potom **Keys**, aby ste skopírovali primárny alebo sekundárny admin kľúč.

### Externá webová stránka

- `AZURE_OPENAI_API_VERSION` - Navštívte stránku [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Latest GA API release**.

### Nastavenie keyless authentication

Namiesto hardcodovania vašich prihlasovacích údajov použijeme keyless pripojenie s Azure OpenAI. Na to importujeme `DefaultAzureCredential` a neskôr zavoláme funkciu `DefaultAzureCredential`, aby sme získali credential.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Niečo nefunguje?

Ak máte akékoľvek problémy s týmto nastavením, pripojte sa do našej

## Ďalšia lekcia

Teraz ste pripravení spustiť kód z tohto kurzu. Prajeme vám veľa úspechov pri objavovaní sveta AI agentov!

[Úvod do AI agentov a ich využitia](../01-intro-to-ai-agents/README.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.