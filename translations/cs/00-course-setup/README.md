<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T09:08:02+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "cs"
}
-->
# Nastavení kurzu

## Úvod

Tato lekce se zaměřuje na to, jak spustit ukázky kódu z tohoto kurzu.

## Naklonování nebo forknutí tohoto repozitáře

Nejprve si prosím naklonujte nebo forkněte GitHub repozitář. Tím získáte vlastní verzi materiálů kurzu, abyste mohli spouštět, testovat a upravovat kód!

To lze provést kliknutím na odkaz na

Měli byste nyní mít vlastní forknutou verzi tohoto kurzu na následujícím odkazu:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.cs.png)

## Spuštění kódu

Tento kurz nabízí sérii Jupyter Notebooků, které si můžete spustit, abyste získali praktické zkušenosti s vytvářením AI agentů.

Ukázky kódu využívají buď:

**Vyžaduje GitHub účet - zdarma**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Označeno jako (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Označeno jako (autogen.ipynb)  

**Vyžaduje předplatné Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. Označeno jako (azureaiagent.ipynb)  

Doporučujeme vyzkoušet všechny tři typy příkladů, abyste zjistili, který vám nejlépe vyhovuje.

Podle toho, kterou možnost si vyberete, budete muset postupovat podle příslušných kroků nastavení uvedených níže:

## Požadavky

- Python 3.12+  
  - **POZNÁMKA**: Pokud nemáte nainstalovaný Python 3.12, ujistěte se, že jej nainstalujete. Poté vytvořte svůj virtuální prostředí (venv) pomocí python3.12, aby byly správné verze nainstalovány ze souboru requirements.txt.  
- GitHub účet - pro přístup k GitHub Models Marketplace  
- Předplatné Azure - pro přístup k Azure AI Foundry  
- Azure AI Foundry účet - pro přístup k Azure AI Agent Service  

V kořenovém adresáři tohoto repozitáře jsme zahrnuli soubor `requirements.txt`, který obsahuje všechny potřebné Python balíčky pro spuštění ukázek kódu.

Můžete je nainstalovat spuštěním následujícího příkazu v terminálu v kořenovém adresáři repozitáře:

```bash
pip install -r requirements.txt
```  
Doporučujeme vytvořit Python virtuální prostředí, abyste předešli konfliktům a problémům.

## Nastavení VSCode
Ujistěte se, že používáte správnou verzi Pythonu v prostředí VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nastavení pro ukázky využívající GitHub Models 

### Krok 1: Získání vašeho GitHub Personal Access Token (PAT)

Tento kurz využívá GitHub Models Marketplace, který poskytuje bezplatný přístup k velkým jazykovým modelům (LLMs), které budete používat k vytváření AI agentů.

Pro použití GitHub Models budete muset vytvořit [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

To lze provést přechodem na váš

GitHub účet.

Postupujte podle [Principu minimálních oprávnění](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) při vytváření tokenu. To znamená, že byste měli tokenu přidělit pouze ta oprávnění, která jsou nezbytná pro spuštění ukázek kódu v tomto kurzu.

1. Na levé straně obrazovky vyberte možnost `Fine-grained tokens`.

    Poté vyberte `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.cs.png)

1. Zadejte popisný název pro váš token, který odráží jeho účel, aby bylo později snadné jej identifikovat. Nastavte datum vypršení platnosti (doporučeno: 30 dní; můžete zvolit kratší období, například 7 dní, pokud preferujete vyšší úroveň zabezpečení).

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.cs.png)

1. Omezte rozsah tokenu na váš fork tohoto repozitáře.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.cs.png)

1. Omezte oprávnění tokenu: V části **Permissions** přepněte na **Account Permissions**, přejděte na **Models** a povolte pouze přístup pro čtení potřebný pro GitHub Models.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.cs.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.cs.png)

Zkopírujte svůj nový token, který jste právě vytvořili. Nyní jej přidáte do souboru `.env` zahrnutého v tomto kurzu.

### Krok 2: Vytvoření souboru `.env`

Pro vytvoření souboru `.env` spusťte následující příkaz v terminálu.

```bash
cp .env.example .env
```

Tím zkopírujete příkladový soubor a vytvoříte `.env` ve vašem adresáři, kde vyplníte hodnoty pro proměnné prostředí.

Se zkopírovaným tokenem otevřete soubor `.env` ve svém oblíbeném textovém editoru a vložte svůj token do pole `GITHUB_TOKEN`.

Nyní byste měli být schopni spustit ukázky kódu z tohoto kurzu.

## Nastavení pro ukázky využívající Azure AI Foundry a Azure AI Agent Service

### Krok 1: Získání koncového bodu vašeho projektu Azure

Postupujte podle kroků pro vytvoření hubu a projektu v Azure AI Foundry, které naleznete zde: [Přehled zdrojů hubu](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Jakmile vytvoříte svůj projekt, budete muset získat připojovací řetězec pro váš projekt.

To lze provést přechodem na stránku **Přehled** vašeho projektu v portálu Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.cs.png)

### Krok 2: Vytvoření souboru `.env`

Pro vytvoření souboru `.env` spusťte následující příkaz v terminálu.

```bash
cp .env.example .env
```

Tím zkopírujete příkladový soubor a vytvoříte `.env` ve vašem adresáři, kde vyplníte hodnoty pro proměnné prostředí.

Se zkopírovaným tokenem otevřete soubor `.env` ve svém oblíbeném textovém editoru a vložte svůj token do pole `PROJECT_ENDPOINT`.

### Krok 3: Přihlášení do Azure

Jako bezpečnostní nejlepší praxi použijeme [autentizaci bez klíče](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) pro autentizaci do Azure OpenAI pomocí Microsoft Entra ID.

Dále otevřete terminál a spusťte `az login --use-device-code` pro přihlášení do svého Azure účtu.

Jakmile se přihlásíte, vyberte své předplatné v terminálu.

## Další proměnné prostředí - Azure Search a Azure OpenAI 

Pro lekci Agentic RAG - Lekce 5 - existují ukázky, které využívají Azure Search a Azure OpenAI.

Pokud chcete tyto ukázky spustit, budete muset přidat následující proměnné prostředí do svého souboru `.env`:

### Stránka Přehled (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Zkontrolujte **Podrobnosti projektu** na stránce **Přehled** vašeho projektu.

- `AZURE_AI_PROJECT_NAME` - Podívejte se na horní část stránky **Přehled** vašeho projektu.

- `AZURE_OPENAI_SERVICE` - Najděte to na kartě **Zahrnuté schopnosti** pro **Azure OpenAI Service** na stránce **Přehled**.

### Centrum správy

- `AZURE_OPENAI_RESOURCE_GROUP` - Přejděte na **Vlastnosti projektu** na stránce **Přehled** v **Centru správy**.

- `GLOBAL_LLM_SERVICE` - V části **Připojené zdroje** najděte název připojení **Azure AI Services**. Pokud není uveden, zkontrolujte **Azure portal** ve své skupině zdrojů pro název zdroje AI Services.

### Stránka Modely + Koncové body

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vyberte svůj model pro vkládání (např. `text-embedding-ada-002`) a poznamenejte si **Název nasazení** z podrobností modelu.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vyberte svůj chatovací model (např. `gpt-4o-mini`) a poznamenejte si **Název nasazení** z podrobností modelu.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Vyhledejte **Azure AI services**, klikněte na něj, poté přejděte na **Správa zdrojů**, **Klíče a koncový bod**, sjeďte dolů na "Azure OpenAI endpoints" a zkopírujte ten, který říká "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na stejné obrazovce zkopírujte KLÍČ 1 nebo KLÍČ 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Najděte svůj zdroj **Azure AI Search**, klikněte na něj a podívejte se na **Přehled**.

- `AZURE_SEARCH_API_KEY` - Poté přejděte na **Nastavení** a poté **Klíče**, abyste zkopírovali primární nebo sekundární administrátorský klíč.

### Externí webová stránka

- `AZURE_OPENAI_API_VERSION` - Navštivte stránku [Životní cyklus verzí API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) pod **Nejnovější GA vydání API**.

### Nastavení autentizace bez klíče

Místo pevného zakódování vašich přihlašovacích údajů použijeme připojení bez klíče s Azure OpenAI. K tomu importujeme `DefaultAzureCredential` a později zavoláme funkci `DefaultAzureCredential` pro získání přihlašovacích údajů.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Nějaký problém?

Pokud narazíte na jakékoli problémy při nastavování, připojte se do našeho

## Další lekce

Nyní jste připraveni spustit kód pro tento kurz. Přejeme vám příjemné učení o světě AI agentů!

[Úvod do AI agentů a jejich využití](../01-intro-to-ai-agents/README.md)

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatizovaný překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.