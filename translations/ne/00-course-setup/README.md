<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:31:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ne"
}
-->
# कोर्स सेटअप

## परिचय

यो पाठले यस कोर्सका कोड नमूनाहरू कसरी चलाउने भन्ने कुरा समेट्नेछ।

## यो रिपोजिटरी क्लोन वा फोर्क गर्नुहोस्

सुरु गर्नका लागि, कृपया GitHub रिपोजिटरी क्लोन वा फोर्क गर्नुहोस्। यसले तपाईंलाई कोर्स सामग्रीको आफ्नै संस्करण बनाउनेछ ताकि तपाईं कोड चलाउन, परीक्षण गर्न, र परिमार्जन गर्न सक्नुहुन्छ!

यो लिंकमा क्लिक गरेर गर्न सकिन्छ:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.ne.png)

## कोड चलाउने

यो कोर्सले Jupyter Notebooks को श्रृंखला प्रदान गर्दछ जसले तपाईंलाई AI एजेन्टहरू निर्माण गर्न व्यावहारिक अनुभव दिन्छ।

कोड नमूनाहरू निम्न प्रयोग गर्छन्:

**GitHub खाता आवश्यक - निःशुल्क**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। लेबल गरिएको (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace। लेबल गरिएको (autogen.ipynb)

**Azure सदस्यता आवश्यक**:
3) Azure AI Foundry + Azure AI Agent Service। लेबल गरिएको (azureaiagent.ipynb)

हामी तपाईंलाई तीन प्रकारका उदाहरणहरू प्रयास गर्न प्रोत्साहित गर्छौं ताकि कुन तपाईंको लागि सबैभन्दा राम्रो काम गर्छ भनेर थाहा पाउन सक्नुहुन्छ।

तपाईंले जुन विकल्प चयन गर्नुहुन्छ, त्यसले तलका सेटअप चरणहरू निर्धारण गर्नेछ:

## आवश्यकताहरू

- Python 3.12+
  - **NOTE**: यदि तपाईंले Python3.12 स्थापना गर्नुभएको छैन भने, सुनिश्चित गर्नुहोस् कि तपाईंले यसलाई स्थापना गर्नुभएको छ। त्यसपछि python3.12 प्रयोग गरेर आफ्नो venv सिर्जना गर्नुहोस् ताकि requirements.txt फाइलबाट सही संस्करणहरू स्थापना गरिएका छन्।
- GitHub खाता - GitHub Models Marketplace पहुँचको लागि
- Azure सदस्यता - Azure AI Foundry पहुँचको लागि
- Azure AI Foundry खाता - Azure AI Agent Service पहुँचको लागि

हामीले यस रिपोजिटरीको मूलमा `requirements.txt` फाइल समावेश गरेका छौं जसमा कोड नमूनाहरू चलाउन आवश्यक सबै Python प्याकेजहरू छन्।

तपाईं यसलाई निम्न आदेश चलाएर स्थापना गर्न सक्नुहुन्छ:

```bash
pip install -r requirements.txt
```
कुनै पनि द्वन्द्व र समस्याहरूबाट बच्न Python भर्चुअल वातावरण सिर्जना गर्न सिफारिस गरिन्छ।

## VSCode सेटअप
सुनिश्चित गर्नुहोस् कि तपाईंले VSCode मा सही संस्करणको Python प्रयोग गरिरहनुभएको छ।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Models प्रयोग गरेर नमूनाहरूको सेटअप

### चरण १: आफ्नो GitHub व्यक्तिगत पहुँच टोकन (PAT) प्राप्त गर्नुहोस्

यो कोर्सले GitHub Models Marketplace प्रयोग गर्दछ, जसले तपाईंलाई ठूलो भाषा मोडेलहरू (LLMs) नि:शुल्क पहुँच प्रदान गर्दछ जसलाई तपाईंले AI एजेन्टहरू निर्माण गर्न प्रयोग गर्नुहुनेछ।

GitHub Models प्रयोग गर्नका लागि, तपाईंले [GitHub व्यक्तिगत पहुँच टोकन](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) सिर्जना गर्नुपर्नेछ।

यो तपाईंको GitHub खातामा गएर गर्न सकिन्छ।

कृपया टोकन सिर्जना गर्दा [कम से कम विशेषाधिकारको सिद्धान्त](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) पालना गर्नुहोस्। यसको मतलब तपाईंले टोकनलाई यस कोर्सका कोड नमूनाहरू चलाउन आवश्यक अनुमति मात्र दिनुपर्छ।

1. आफ्नो स्क्रिनको बायाँपट्टि `Fine-grained tokens` विकल्प चयन गर्नुहोस्।

    त्यसपछि `Generate new token` चयन गर्नुहोस्।

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.ne.png)

1. टोकनको उद्देश्यलाई प्रतिबिम्बित गर्ने वर्णनात्मक नाम प्रविष्ट गर्नुहोस् ताकि पछि यसलाई सजिलै चिन्न सकियोस्। समाप्ति मिति सेट गर्नुहोस् (सिफारिस: ३० दिन; तपाईं चाहनुहुन्छ भने ७ दिन जस्तो छोटो अवधि चयन गर्न सक्नुहुन्छ।)

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.ne.png)

1. टोकनको स्कोपलाई यस रिपोजिटरीको फोर्कमा सीमित गर्नुहोस्।

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.ne.png)

1. टोकनको अनुमति प्रतिबन्धित गर्नुहोस्: **Permissions** अन्तर्गत, **Account Permissions** टगल गर्नुहोस्, **Models** मा जानुहोस् र GitHub Models को लागि आवश्यक मात्र पढ्ने पहुँच सक्षम गर्नुहोस्।

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.ne.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.ne.png)

तपाईंले अहिले सिर्जना गर्नुभएको नयाँ टोकन प्रतिलिपि गर्नुहोस्। अब तपाईंले यसलाई यस कोर्समा समावेश गरिएको `.env` फाइलमा थप्नुहुनेछ।

### चरण २: आफ्नो `.env` फाइल सिर्जना गर्नुहोस्

आफ्नो `.env` फाइल सिर्जना गर्न आफ्नो टर्मिनलमा निम्न आदेश चलाउनुहोस्।

```bash
cp .env.example .env
```

यसले उदाहरण फाइललाई प्रतिलिपि गर्नेछ र `.env` तपाईंको डाइरेक्टरीमा सिर्जना गर्नेछ जहाँ तपाईं वातावरण चरहरूको लागि मानहरू भर्न सक्नुहुन्छ।

तपाईंको टोकन प्रतिलिपि गरेर, `.env` फाइललाई आफ्नो मनपर्ने टेक्स्ट एडिटरमा खोल्नुहोस् र `GITHUB_TOKEN` फिल्डमा टोकन पेस्ट गर्नुहोस्।

अब तपाईं यस कोर्सका कोड नमूनाहरू चलाउन सक्षम हुनुहुनेछ।

## Azure AI Foundry र Azure AI Agent Service प्रयोग गरेर नमूनाहरूको सेटअप

### चरण १: आफ्नो Azure प्रोजेक्ट अन्त बिन्दु प्राप्त गर्नुहोस्

Azure AI Foundry मा हब र प्रोजेक्ट सिर्जना गर्ने चरणहरू यहाँ फेला पार्नुहोस्: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

एकपटक तपाईंले आफ्नो प्रोजेक्ट सिर्जना गर्नुभयो भने, तपाईंले आफ्नो प्रोजेक्टको लागि कनेक्शन स्ट्रिङ प्राप्त गर्नुपर्नेछ।

यो Azure AI Foundry पोर्टलमा आफ्नो प्रोजेक्टको **Overview** पृष्ठमा गएर गर्न सकिन्छ।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.ne.png)

### चरण २: आफ्नो `.env` फाइल सिर्जना गर्नुहोस्

आफ्नो `.env` फाइल सिर्जना गर्न आफ्नो टर्मिनलमा निम्न आदेश चलाउनुहोस्।

```bash
cp .env.example .env
```

यसले उदाहरण फाइललाई प्रतिलिपि गर्नेछ र `.env` तपाईंको डाइरेक्टरीमा सिर्जना गर्नेछ जहाँ तपाईं वातावरण चरहरूको लागि मानहरू भर्न सक्नुहुन्छ।

तपाईंको टोकन प्रतिलिपि गरेर, `.env` फाइललाई आफ्नो मनपर्ने टेक्स्ट एडिटरमा खोल्नुहोस् र `PROJECT_ENDPOINT` फिल्डमा टोकन पेस्ट गर्नुहोस्।

### चरण ३: Azure मा साइन इन गर्नुहोस्

सुरक्षाको राम्रो अभ्यासको रूपमा, हामी [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) प्रयोग गरेर Microsoft Entra ID सँग Azure OpenAI मा प्रमाणित गर्नेछौं।

अर्को, टर्मिनल खोल्नुहोस् र `az login --use-device-code` चलाएर आफ्नो Azure खातामा साइन इन गर्नुहोस्।

एकपटक तपाईंले लगइन गर्नुभयो भने, टर्मिनलमा आफ्नो सदस्यता चयन गर्नुहोस्।

## अतिरिक्त वातावरण चरहरू - Azure Search र Azure OpenAI

Agentic RAG पाठ - पाठ ५ - मा Azure Search र Azure OpenAI प्रयोग गर्ने नमूनाहरू छन्।

यदि तपाईं यी नमूनाहरू चलाउन चाहनुहुन्छ भने, तपाईंले आफ्नो `.env` फाइलमा निम्न वातावरण चरहरू थप्नुपर्नेछ:

### Overview पृष्ठ (प्रोजेक्ट)

- `AZURE_SUBSCRIPTION_ID` - **Overview** पृष्ठको **Project details** मा जाँच गर्नुहोस्।

- `AZURE_AI_PROJECT_NAME` - आफ्नो प्रोजेक्टको **Overview** पृष्ठको शीर्षमा हेर्नुहोस्।

- `AZURE_OPENAI_SERVICE` - **Overview** पृष्ठको **Included capabilities** ट्याबमा **Azure OpenAI Service** मा फेला पार्नुहोस्।

### व्यवस्थापन केन्द्र

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** को **Overview** पृष्ठमा **Project properties** मा जानुहोस्।

- `GLOBAL_LLM_SERVICE` - **Connected resources** अन्तर्गत, **Azure AI Services** कनेक्शन नाम फेला पार्नुहोस्। यदि सूचीबद्ध छैन भने, आफ्नो स्रोत समूह अन्तर्गत Azure पोर्टलमा AI Services स्रोत नाम जाँच गर्नुहोस्।

### Models + Endpoints पृष्ठ

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - आफ्नो embedding मोडेल चयन गर्नुहोस् (जस्तै, `text-embedding-ada-002`) र मोडेल विवरणबाट **Deployment name** नोट गर्नुहोस्।

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - आफ्नो chat मोडेल चयन गर्नुहोस् (जस्तै, `gpt-4o-mini`) र मोडेल विवरणबाट **Deployment name** नोट गर्नुहोस्।

### Azure पोर्टल

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** हेर्नुहोस्, यसमा क्लिक गर्नुहोस्, त्यसपछि **Resource Management**, **Keys and Endpoint** मा जानुहोस्, "Azure OpenAI endpoints" मा स्क्रोल गर्नुहोस्, र "Language APIs" भन्ने एक प्रतिलिपि गर्नुहोस्।

- `AZURE_OPENAI_API_KEY` - त्यही स्क्रिनबाट, KEY 1 वा KEY 2 प्रतिलिपि गर्नुहोस्।

- `AZURE_SEARCH_SERVICE_ENDPOINT` - आफ्नो **Azure AI Search** स्रोत फेला पार्नुहोस्, यसमा क्लिक गर्नुहोस्, र **Overview** हेर्नुहोस्।

- `AZURE_SEARCH_API_KEY` - त्यसपछि **Settings** मा जानुहोस् र **Keys** मा गएर प्राथमिक वा द्वितीयक प्रशासक कुञ्जी प्रतिलिपि गर्नुहोस्।

### बाह्य वेबपृष्ठ

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) पृष्ठ अन्तर्गत **Latest GA API release** हेर्नुहोस्।

### keyless authentication सेटअप गर्नुहोस्

तपाईंको प्रमाणहरू हार्डकोड गर्नुको सट्टा, हामी Azure OpenAI सँग keyless कनेक्शन प्रयोग गर्नेछौं। यसका लागि, हामी `DefaultAzureCredential` आयात गर्नेछौं र पछि प्रमाण प्राप्त गर्न `DefaultAzureCredential` फंक्शन कल गर्नेछौं।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## कतै अडिनुभयो?

यदि तपाईंलाई यो सेटअप चलाउन कुनै समस्या छ भने, हाम्रो 

## अर्को पाठ

अब तपाईं यस कोर्सका कोड चलाउन तयार हुनुहुन्छ। AI एजेन्टहरूको संसारबारे थप सिक्न शुभकामना!

[AI एजेन्टहरू र एजेन्ट प्रयोग केसहरूको परिचय](../01-intro-to-ai-agents/README.md)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।