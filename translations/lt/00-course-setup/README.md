<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-30T15:03:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "lt"
}
-->
# Kurso Nustatymai

## Įvadas

Šioje pamokoje aptarsime, kaip paleisti šio kurso kodo pavyzdžius.

## Prisijunkite prie kitų mokinių ir gaukite pagalbos

Prieš pradėdami klonuoti savo saugyklą, prisijunkite prie [AI Agents For Beginners Discord kanalo](https://aka.ms/ai-agents/discord), kad gautumėte pagalbos dėl nustatymų, atsakymų į klausimus apie kursą ar galėtumėte bendrauti su kitais mokiniais.

## Klonuokite arba „forkinkite“ šią saugyklą

Norėdami pradėti, prašome klonuoti arba „forkinti“ GitHub saugyklą. Tai leis jums turėti savo kurso medžiagos versiją, kad galėtumėte paleisti, testuoti ir koreguoti kodą!

Tai galima padaryti paspaudus nuorodą į

Jūs dabar turėtumėte turėti savo „forkintą“ šio kurso versiją šioje nuorodoje:

![Forkinta saugykla](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.lt.png)

## Kodo paleidimas

Šis kursas siūlo seriją Jupyter užrašų knygelių, kurias galite paleisti, kad praktiškai išmoktumėte kurti AI agentus.

Kodo pavyzdžiai naudoja:

**Reikalinga GitHub paskyra - nemokama**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Pažymėta kaip (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Pažymėta kaip (autogen.ipynb)

**Reikalinga Azure prenumerata**:
3) Azure AI Foundry + Azure AI Agent Service. Pažymėta kaip (azureaiagent.ipynb)

Rekomenduojame išbandyti visus tris pavyzdžių tipus, kad pamatytumėte, kuris jums labiausiai tinka.

Pasirinktas variantas nulems, kokių nustatymo veiksmų reikės laikytis toliau:

## Reikalavimai

- Python 3.12+
  - **PASTABA**: Jei neturite įdiegto Python 3.12, įdiekite jį. Tada sukurkite savo venv naudodami python3.12, kad užtikrintumėte, jog iš `requirements.txt` failo bus įdiegtos tinkamos versijos.
- GitHub paskyra - norint pasiekti GitHub Models Marketplace
- Azure prenumerata - norint pasiekti Azure AI Foundry
- Azure AI Foundry paskyra - norint pasiekti Azure AI Agent Service

Šios saugyklos šakniniame kataloge įtraukėme `requirements.txt` failą, kuriame yra visi reikalingi Python paketai, kad galėtumėte paleisti kodo pavyzdžius.

Juos galite įdiegti paleisdami šią komandą terminale, būdami saugyklos šakniniame kataloge:

```bash
pip install -r requirements.txt
```
Rekomenduojame sukurti Python virtualią aplinką, kad išvengtumėte konfliktų ir problemų.

## VSCode nustatymas
Įsitikinkite, kad naudojate tinkamą Python versiją VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Nustatymai pavyzdžiams naudojant GitHub modelius

### 1 žingsnis: Gaukite savo GitHub asmeninį prieigos raktą (PAT)

Šis kursas naudoja GitHub Models Marketplace, kuris suteikia nemokamą prieigą prie didelių kalbos modelių (LLMs), kuriuos naudosite AI agentams kurti.

Norėdami naudoti GitHub modelius, turėsite sukurti [GitHub asmeninį prieigos raktą](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Tai galima padaryti einant į savo GitHub paskyrą.

Prašome laikytis [Minimalios privilegijos principo](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) kuriant savo raktą. Tai reiškia, kad turėtumėte suteikti raktui tik tas teises, kurios būtinos šio kurso kodo pavyzdžiams paleisti.

1. Pasirinkite `Fine-grained tokens` parinktį kairėje ekrano pusėje, eidami į **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.lt.png)

    Tada pasirinkite `Generate new token`.

    ![Sukurti raktą](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.lt.png)

2. Įveskite aprašomąjį rakto pavadinimą, kuris atspindėtų jo paskirtį, kad vėliau būtų lengva jį atpažinti.

    🔐 Rakto galiojimo trukmės rekomendacija

    Rekomenduojama trukmė: 30 dienų  
    Norėdami užtikrinti didesnį saugumą, galite pasirinkti trumpesnį laikotarpį, pvz., 7 dienas 🛡️  
    Tai puikus būdas nustatyti asmeninį tikslą ir baigti kursą, kol jūsų mokymosi tempas yra aukštas 🚀.

    ![Rakto pavadinimas ir galiojimo data](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.lt.png)

3. Apribokite rakto taikymo sritį savo šios saugyklos „forkui“.

    ![Apriboti taikymo sritį „fork“ saugyklai](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.lt.png)

4. Apribokite rakto teises: Skiltyje **Permissions** spustelėkite **Account** skirtuką ir spustelėkite mygtuką "+ Add permissions". Atsiras išskleidžiamasis meniu. Prašome ieškoti **Models** ir pažymėti langelį.

    ![Pridėti modelių leidimą](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.lt.png)

5. Patikrinkite reikalingas teises prieš generuodami raktą.  
    ![Patikrinti teises](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.lt.png)

6. Prieš generuodami raktą, įsitikinkite, kad esate pasiruošę saugoti raktą saugioje vietoje, pvz., slaptažodžių tvarkyklės saugykloje, nes jis nebus rodomas dar kartą po sukūrimo.  
    ![Saugiai saugoti raktą](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.lt.png)

Nukopijuokite naują raktą, kurį ką tik sukūrėte. Dabar pridėsite jį prie savo `.env` failo, kuris yra įtrauktas į šį kursą.

### 2 žingsnis: Sukurkite savo `.env` failą

Norėdami sukurti savo `.env` failą, paleiskite šią komandą terminale.

```bash
cp .env.example .env
```

Tai nukopijuos pavyzdinį failą ir sukurs `.env` jūsų kataloge, kur užpildysite aplinkos kintamųjų reikšmes.

Nukopijavę savo raktą, atidarykite `.env` failą savo mėgstamiausiame teksto redaktoriuje ir įklijuokite savo raktą į `GITHUB_TOKEN` lauką.  
![GitHub rakto laukas](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.lt.png)

Dabar turėtumėte galėti paleisti šio kurso kodo pavyzdžius.

## Nustatymai pavyzdžiams naudojant Azure AI Foundry ir Azure AI Agent Service

### 1 žingsnis: Gaukite savo Azure projekto galinį tašką

Sekite Azure AI Foundry centro ir projekto kūrimo veiksmus, pateiktus čia: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Sukūrę savo projektą, turėsite gauti savo projekto prisijungimo eilutę.

Tai galima padaryti einant į **Overview** puslapį savo projekte Azure AI Foundry portale.

![Projekto prisijungimo eilutė](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.lt.png)

### 2 žingsnis: Sukurkite savo `.env` failą

Norėdami sukurti savo `.env` failą, paleiskite šią komandą terminale.

```bash
cp .env.example .env
```

Tai nukopijuos pavyzdinį failą ir sukurs `.env` jūsų kataloge, kur užpildysite aplinkos kintamųjų reikšmes.

Nukopijavę savo raktą, atidarykite `.env` failą savo mėgstamiausiame teksto redaktoriuje ir įklijuokite savo raktą į `PROJECT_ENDPOINT` lauką.

### 3 žingsnis: Prisijunkite prie Azure

Kaip saugumo geriausią praktiką, naudosime [autentifikaciją be raktų](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), kad prisijungtume prie Azure OpenAI su Microsoft Entra ID.

Atidarykite terminalą ir paleiskite `az login --use-device-code`, kad prisijungtumėte prie savo Azure paskyros.

Prisijungę terminale pasirinkite savo prenumeratą.

## Papildomi aplinkos kintamieji - Azure Search ir Azure OpenAI

Agentic RAG pamokai - 5 pamoka - yra pavyzdžių, kurie naudoja Azure Search ir Azure OpenAI.

Jei norite paleisti šiuos pavyzdžius, turėsite pridėti šiuos aplinkos kintamuosius į savo `.env` failą:

### Projekto apžvalgos puslapis

- `AZURE_SUBSCRIPTION_ID` - Patikrinkite **Project details** skiltyje **Overview** puslapyje savo projekte.

- `AZURE_AI_PROJECT_NAME` - Pažiūrėkite į viršų **Overview** puslapyje savo projekte.

- `AZURE_OPENAI_SERVICE` - Raskite tai **Included capabilities** skirtuke **Azure OpenAI Service** skiltyje **Overview** puslapyje.

### Valdymo centras

- `AZURE_OPENAI_RESOURCE_GROUP` - Eikite į **Project properties** skiltyje **Overview** puslapyje **Management Center**.

- `GLOBAL_LLM_SERVICE` - Skiltyje **Connected resources** raskite **Azure AI Services** prisijungimo pavadinimą. Jei nėra sąraše, patikrinkite **Azure portalą** savo išteklių grupėje dėl AI Services ištekliaus pavadinimo.

### Modeliai + galinių taškų puslapis

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Pasirinkite savo įterpimo modelį (pvz., `text-embedding-ada-002`) ir užsirašykite **Deployment name** iš modelio detalių.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Pasirinkite savo pokalbių modelį (pvz., `gpt-4o-mini`) ir užsirašykite **Deployment name** iš modelio detalių.

### Azure portalas

- `AZURE_OPENAI_ENDPOINT` - Ieškokite **Azure AI services**, spustelėkite ant jo, tada eikite į **Resource Management**, **Keys and Endpoint**, slinkite žemyn iki "Azure OpenAI endpoints" ir nukopijuokite tą, kuris sako "Language APIs".

- `AZURE_OPENAI_API_KEY` - Iš to paties ekrano nukopijuokite KEY 1 arba KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Raskite savo **Azure AI Search** išteklių, spustelėkite jį ir peržiūrėkite **Overview**.

- `AZURE_SEARCH_API_KEY` - Tada eikite į **Settings** ir tada **Keys**, kad nukopijuotumėte pirminį arba antrinį administratoriaus raktą.

### Išorinė svetainė

- `AZURE_OPENAI_API_VERSION` - Apsilankykite [API versijų gyvavimo ciklo](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) puslapyje skiltyje **Latest GA API release**.

### Nustatyti autentifikaciją be raktų

Užuot kodavę savo kredencialus, naudosime autentifikaciją be raktų su Azure OpenAI. Tam importuosime `DefaultAzureCredential` ir vėliau iškviesime `DefaultAzureCredential` funkciją, kad gautume kredencialą.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Užstrigote?

Jei turite kokių nors problemų paleidžiant šiuos nustatymus, prisijunkite prie mūsų

arba.

## Kita pamoka

Dabar esate pasiruošę paleisti šio kurso kodą. Smagaus mokymosi apie AI agentų pasaulį!

[Įvadas į AI agentus ir jų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.