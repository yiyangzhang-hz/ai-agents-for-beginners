<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8693a24942b670e3cb8def77f92513f9",
  "translation_date": "2025-08-21T14:08:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "my"
}
-->
## သင်ခန်းစာ စတင်ခြင်း

ဒီသင်ခန်းစာမှာ သင်တန်းရဲ့ code sample တွေကို ဘယ်လို run လုပ်ရမလဲဆိုတာကို လေ့လာပါမယ်။

## ဒီ Repo ကို Clone လုပ်မယ် ဒါမှမဟုတ် Fork လုပ်မယ်

စတင်ရန်အတွက် GitHub Repository ကို Clone လုပ်ပါ ဒါမှမဟုတ် Fork လုပ်ပါ။ ဒါက သင့်ကိုယ်ပိုင် version ကို ရရှိစေပြီး code ကို run လုပ်နိုင်၊ စမ်းသပ်နိုင်၊ ပြင်ဆင်နိုင်ပါမယ်။

ဒီအဆင့်ကို GitHub link ကို နှိပ်ပြီးလုပ်နိုင်ပါတယ်။

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.my.png)

## Code ကို Run လုပ်ခြင်း

ဒီသင်တန်းမှာ Jupyter Notebooks တွေကို အသုံးပြုပြီး AI Agents တည်ဆောက်ဖို့ လက်တွေ့လုပ်ဆောင်နိုင်တဲ့ အတွေ့အကြုံရရှိစေမှာပါ။

Code sample တွေမှာ အောက်ပါ framework တွေကို အသုံးပြုထားပါတယ်-

**GitHub Account လိုအပ်သည် - အခမဲ့**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace (autogen.ipynb)

**Azure Subscription လိုအပ်သည်**:
3) Azure AI Foundry + Azure AI Agent Service (azureaiagent.ipynb)

သုံးမျိုးလုံးကို စမ်းသပ်ကြည့်ဖို့ အကြံပြုပါတယ်။ သင့်အတွက် အကောင်းဆုံးအလုပ်လုပ်နိုင်တဲ့ option ကို ရွေးချယ်နိုင်ပါတယ်။

သင်ရွေးချယ်တဲ့ option အပေါ်မူတည်ပြီး အောက်ပါ setup အဆင့်တွေကို လိုက်နာရပါမယ်။

## လိုအပ်ချက်များ

- Python 3.12+
  - **NOTE**: Python3.12 မရှိပါက Python3.12 ကို install လုပ်ပါ။ ပြီးရင် requirements.txt ဖိုင်ထဲက version တွေကို သေချာစွာ install လုပ်ဖို့ python3.12 ကို အသုံးပြုပြီး venv တည်ဆောက်ပါ။
- GitHub Account - GitHub Models Marketplace ကို အသုံးပြုရန်
- Azure Subscription - Azure AI Foundry ကို အသုံးပြုရန်
- Azure AI Foundry Account - Azure AI Agent Service ကို အသုံးပြုရန်

ဒီ repository ရဲ့ root မှာ `requirements.txt` ဖိုင်ကို ထည့်သွင်းထားပြီး Python packages တွေကို install လုပ်နိုင်ပါတယ်။

Terminal မှာ အောက်ပါ command ကို run လုပ်ပါ:

```bash
pip install -r requirements.txt
```

Python virtual environment တည်ဆောက်ပြီး conflicts မဖြစ်စေရန် အကြံပြုပါတယ်။

## VSCode ကို Setup လုပ်ပါ
VSCode မှာ Python ရဲ့ မှန်ကန်တဲ့ version ကို အသုံးပြုထားတာကို သေချာပါစေ။

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models ကို အသုံးပြုရန် Setup လုပ်ခြင်း

### အဆင့် ၁: GitHub Personal Access Token (PAT) ကို ရယူပါ

ဒီသင်တန်းမှာ GitHub Models Marketplace ကို အသုံးပြုထားပြီး Large Language Models (LLMs) တွေကို အခမဲ့ access ရရှိစေပါတယ်။

GitHub Models ကို အသုံးပြုဖို့ [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) တစ်ခုကို ဖန်တီးရပါမယ်။

GitHub Account မှာ အောက်ပါအဆင့်တွေကို လိုက်နာပါ:

[Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ကို လိုက်နာပြီး token ကို လိုအပ်တဲ့ permission တွေကိုပဲပေးပါ။

1. **Developer settings** မှာ `Fine-grained tokens` ကို ရွေးပါ။
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.my.png)

    ပြီးရင် `Generate new token` ကို ရွေးပါ။

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.my.png)

2. Token ရဲ့ ရည်ရွယ်ချက်ကို ဖော်ပြတဲ့ နာမည်တစ်ခုကို ထည့်သွင်းပါ။

    🔐 Token Duration Recommendation

    အကြံပြုထားတဲ့ သက်တမ်း: 30 ရက်  
    ပိုမိုလုံခြုံမှုအတွက် 7 ရက်လိုမျိုး သက်တမ်းကို ရွေးချယ်နိုင်ပါတယ် 🛡️  
    သင်တန်းကို အချိန်မကုန်အောင် ပြီးမြောက်စေဖို့ အကောင်းဆုံးနည်းလမ်းတစ်ခုဖြစ်ပါတယ် 🚀။

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.my.png)

3. Token ရဲ့ scope ကို သင့် fork repository အတွက်သာ ကန့်သတ်ပါ။

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.my.png)

4. Token ရဲ့ permission တွေကို ကန့်သတ်ပါ: **Permissions** tab မှာ **Account** ကို ရွေးပြီး "+ Add permissions" button ကို နှိပ်ပါ။ Dropdown မှာ **Models** ကို ရှာပြီး checkbox ကို အမှန်ခြစ်ပါ။
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.my.png)

5. Token ကို ဖန်တီးမည့်အခါမှာ လိုအပ်တဲ့ permission တွေကို ပြန်လည်စစ်ဆေးပါ။ ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.my.png)

6. Token ကို ဖန်တီးပြီးနောက် password manager vault တစ်ခုလိုမျိုး လုံခြုံတဲ့နေရာမှာ သိမ်းဆည်းပါ။ ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.my.png)

ဖန်တီးထားတဲ့ token ကို copy လုပ်ပါ။ `.env` ဖိုင်ထဲမှာ ထည့်သွင်းပါ။

### အဆင့် ၂: `.env` ဖိုင်ကို ဖန်တီးပါ

Terminal မှာ အောက်ပါ command ကို run လုပ်ပါ:

```bash
cp .env.example .env
```

ဒီ command က `.env` ဖိုင်ကို ဖန်တီးပြီး environment variables တွေကို ထည့်သွင်းနိုင်တဲ့နေရာကို ဖန်တီးပေးပါမယ်။

Token ကို copy လုပ်ပြီး `.env` ဖိုင်ကို text editor မှာ ဖွင့်ပါ။ `GITHUB_TOKEN` field မှာ token ကို paste လုပ်ပါ။
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.my.png)

အခု သင့် code sample တွေကို run လုပ်နိုင်ပါပြီ။

## Azure AI Foundry နှင့် Azure AI Agent Service ကို အသုံးပြုရန် Setup လုပ်ခြင်း

### အဆင့် ၁: Azure Project Endpoint ကို ရယူပါ

Azure AI Foundry မှ hub နှင့် project တစ်ခုကို ဖန်တီးရန်အဆင့်တွေကို [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources) မှာ လေ့လာပါ။

Project ကို ဖန်တီးပြီးနောက် connection string ကို ရယူပါ။

Azure AI Foundry portal ရဲ့ **Overview** page မှာ သွားပါ။

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.my.png)

### အဆင့် ၂: `.env` ဖိုင်ကို ဖန်တီးပါ

Terminal မှာ အောက်ပါ command ကို run လုပ်ပါ:

```bash
cp .env.example .env
```

ဒီ command က `.env` ဖိုင်ကို ဖန်တီးပြီး environment variables တွေကို ထည့်သွင်းနိုင်တဲ့နေရာကို ဖန်တီးပေးပါမယ်။

Token ကို copy လုပ်ပြီး `.env` ဖိုင်ကို text editor မှာ ဖွင့်ပါ။ `PROJECT_ENDPOINT` field မှာ token ကို paste လုပ်ပါ။

### အဆင့် ၃: Azure မှာ Sign In လုပ်ပါ

လုံခြုံရေးအတွက် [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ကို အသုံးပြုပါ။

Terminal ကို ဖွင့်ပြီး `az login --use-device-code` command ကို run လုပ်ပါ။

Login ပြီးနောက် subscription ကို terminal မှာ ရွေးပါ။

## Azure Search နှင့် Azure OpenAI အတွက် အပို Environment Variables

Agentic RAG Lesson - Lesson 5 မှာ Azure Search နှင့် Azure OpenAI ကို အသုံးပြုထားတဲ့ sample တွေပါဝင်ပါတယ်။

ဒီ sample တွေကို run လုပ်ချင်ပါက `.env` ဖိုင်ထဲမှာ အောက်ပါ environment variables တွေကို ထည့်သွင်းပါ:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - **Overview** page ရဲ့ **Project details** မှာ ရှာပါ။
- `AZURE_AI_PROJECT_NAME` - **Overview** page ရဲ့ အပေါ်ဆုံးမှာ ရှာပါ။
- `AZURE_OPENAI_SERVICE` - **Overview** page ရဲ့ **Included capabilities** tab မှာ ရှာပါ။

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** ရဲ့ **Overview** page မှာ **Project properties** ကို သွားပါ။
- `GLOBAL_LLM_SERVICE` - **Connected resources** မှာ **Azure AI Services** connection name ကို ရှာပါ။

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Embedding model ကို ရွေးပြီး **Deployment name** ကို မှတ်သားပါ။
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chat model ကို ရွေးပြီး **Deployment name** ကို မှတ်သားပါ။

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** မှာ သွားပြီး **Keys and Endpoint** မှာ "Language APIs" endpoint ကို copy လုပ်ပါ။
- `AZURE_OPENAI_API_KEY` - KEY 1 ဒါမှမဟုတ် KEY 2 ကို copy လုပ်ပါ။
- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** resource ရဲ့ **Overview** page မှာ ရှာပါ။
- `AZURE_SEARCH_API_KEY` - **Settings** > **Keys** မှာ admin key ကို copy လုပ်ပါ။

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page မှာ **Latest GA API release** ကို ရှာပါ။

### Keyless Authentication ကို Setup လုပ်ပါ

Credentials တွေကို hardcode မလုပ်ဘဲ Azure OpenAI အတွက် keyless connection ကို အသုံးပြုပါ။ `DefaultAzureCredential` ကို import လုပ်ပြီး function ကို later call လုပ်ပါ။

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## အခက်အခဲရှိပါက?

Setup ကို run လုပ်ရာမှာ အခက်အခဲရှိပါက...

## နောက်သင်ခန်းစာ

အခု သင့် code ကို run လုပ်ဖို့ ပြင်ဆင်ပြီးပါပြီ။ AI Agents ရဲ့ ကမ္ဘာကို ပိုမိုလေ့လာဖို့ အဆင်ပြေပါစေ!

[AI Agents နှင့် Agent Use Cases ကို မိတ်ဆက်ခြင်း](../01-intro-to-ai-agents/README.md)

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်ခြင်းကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲသုံးစားမှု သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။