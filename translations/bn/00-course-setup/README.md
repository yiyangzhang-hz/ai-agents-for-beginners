<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:28:26+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "bn"
}
-->
# কোর্স সেটআপ

## পরিচিতি

এই পাঠে আমরা এই কোর্সের কোড নমুনাগুলি কীভাবে চালাতে হয় তা শিখব।

## এই রিপোজিটরি ক্লোন বা ফর্ক করুন

শুরু করার জন্য, অনুগ্রহ করে GitHub রিপোজিটরিটি ক্লোন বা ফর্ক করুন। এটি আপনার নিজের কোর্স উপকরণের একটি সংস্করণ তৈরি করবে যাতে আপনি কোড চালাতে, পরীক্ষা করতে এবং পরিবর্তন করতে পারেন!

এটি করতে, লিঙ্কে ক্লিক করুন:

![ফর্ক করা রিপো](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.bn.png)

## কোড চালানো

এই কোর্সটি একটি সিরিজ জুপিটার নোটবুক সরবরাহ করে যা আপনাকে AI এজেন্ট তৈরি করার হাতে-কলমে অভিজ্ঞতা দেবে।

কোড নমুনাগুলি নিম্নলিখিত পদ্ধতিগুলির উপর নির্ভর করে:

**GitHub অ্যাকাউন্ট প্রয়োজন - ফ্রি**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace। লেবেল করা হয়েছে (semantic-kernel.ipynb)।
2) AutoGen Framework + GitHub Models Marketplace। লেবেল করা হয়েছে (autogen.ipynb)।

**Azure সাবস্ক্রিপশন প্রয়োজন**:
3) Azure AI Foundry + Azure AI Agent Service। লেবেল করা হয়েছে (azureaiagent.ipynb)।

আমরা আপনাকে তিনটি উদাহরণই চেষ্টা করার পরামর্শ দিই যাতে আপনি দেখতে পারেন কোনটি আপনার জন্য সবচেয়ে ভালো কাজ করে।

আপনি যেকোনো বিকল্প বেছে নিন, এটি নির্ধারণ করবে যে আপনাকে নিচের কোন সেটআপ ধাপগুলি অনুসরণ করতে হবে:

## প্রয়োজনীয়তা

- Python 3.12+
  - **NOTE**: যদি আপনার Python3.12 ইনস্টল না থাকে, নিশ্চিত করুন যে আপনি এটি ইনস্টল করেছেন। তারপর requirements.txt ফাইল থেকে সঠিক সংস্করণগুলি ইনস্টল করতে python3.12 ব্যবহার করে আপনার venv তৈরি করুন।
- একটি GitHub অ্যাকাউন্ট - GitHub Models Marketplace-এ অ্যাক্সেসের জন্য।
- Azure সাবস্ক্রিপশন - Azure AI Foundry-তে অ্যাক্সেসের জন্য।
- Azure AI Foundry অ্যাকাউন্ট - Azure AI Agent Service-এ অ্যাক্সেসের জন্য।

আমরা এই রিপোজিটরির মূল ফোল্ডারে একটি `requirements.txt` ফাইল অন্তর্ভুক্ত করেছি, যেখানে কোড নমুনাগুলি চালানোর জন্য প্রয়োজনীয় সমস্ত Python প্যাকেজ রয়েছে।

আপনি এটি ইনস্টল করতে পারেন নিচের কমান্ডটি চালিয়ে:

```bash
pip install -r requirements.txt
```
আমরা কোনো দ্বন্দ্ব এবং সমস্যা এড়াতে একটি Python ভার্চুয়াল এনভায়রনমেন্ট তৈরি করার পরামর্শ দিই।

## VSCode সেটআপ করুন
সুনিশ্চিত করুন যে আপনি VSCode-এ সঠিক Python সংস্করণ ব্যবহার করছেন।

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub মডেল ব্যবহার করে নমুনার জন্য সেটআপ

### ধাপ ১: আপনার GitHub Personal Access Token (PAT) সংগ্রহ করুন

এই কোর্সটি GitHub Models Marketplace ব্যবহার করে, যা আপনাকে বড় ভাষার মডেল (LLMs) বিনামূল্যে অ্যাক্সেস দেয় যা আপনি AI এজেন্ট তৈরি করতে ব্যবহার করবেন।

GitHub মডেল ব্যবহার করতে, আপনাকে একটি [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) তৈরি করতে হবে।

এটি আপনার GitHub অ্যাকাউন্টে গিয়ে করা যেতে পারে।

[Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) অনুসরণ করুন যখন আপনি আপনার টোকেন তৈরি করবেন। এর মানে হলো টোকেনকে শুধুমাত্র সেই অনুমতিগুলি দিন যা এই কোর্সের কোড নমুনাগুলি চালানোর জন্য প্রয়োজন।

1. আপনার স্ক্রিনের বাম দিকে `Fine-grained tokens` বিকল্পটি নির্বাচন করুন।

    তারপর `Generate new token` নির্বাচন করুন।

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.bn.png)

1. আপনার টোকেনের জন্য একটি বর্ণনামূলক নাম লিখুন যা এর উদ্দেশ্য প্রতিফলিত করে, যাতে এটি পরে সহজে চেনা যায়। একটি মেয়াদ শেষ হওয়ার তারিখ নির্ধারণ করুন (প্রস্তাবিত: ৩০ দিন; আপনি যদি আরও নিরাপদ অবস্থান চান তবে ৭ দিনের মতো একটি ছোট সময়কাল বেছে নিতে পারেন।)

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.bn.png)

1. টোকেনের স্কোপটি এই রিপোজিটরির আপনার ফর্কে সীমাবদ্ধ করুন।

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.bn.png)

1. টোকেনের অনুমতিগুলি সীমাবদ্ধ করুন: **Permissions** এর অধীনে, **Account Permissions** টগল করুন, **Models** এ যান এবং শুধুমাত্র GitHub মডেলের জন্য প্রয়োজনীয় পড়ার-অ্যাক্সেস সক্ষম করুন।

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.bn.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.bn.png)

আপনার সদ্য তৈরি করা টোকেনটি কপি করুন। এখন এটি এই কোর্সে অন্তর্ভুক্ত `.env` ফাইলে যোগ করুন।

### ধাপ ২: আপনার `.env` ফাইল তৈরি করুন

আপনার `.env` ফাইল তৈরি করতে, আপনার টার্মিনালে নিচের কমান্ডটি চালান।

```bash
cp .env.example .env
```

এটি উদাহরণ ফাইলটি কপি করবে এবং আপনার ডিরেক্টরিতে একটি `.env` তৈরি করবে যেখানে আপনি পরিবেশ ভেরিয়েবলের জন্য মানগুলি পূরণ করবেন।

আপনার টোকেন কপি করার পরে, আপনার প্রিয় টেক্সট এডিটরে `.env` ফাইলটি খুলুন এবং `GITHUB_TOKEN` ফিল্ডে আপনার টোকেন পেস্ট করুন।

এখন আপনি এই কোর্সের কোড নমুনাগুলি চালাতে সক্ষম হবেন।

## Azure AI Foundry এবং Azure AI Agent Service ব্যবহার করে নমুনার জন্য সেটআপ

### ধাপ ১: আপনার Azure প্রকল্পের এন্ডপয়েন্ট সংগ্রহ করুন

Azure AI Foundry-তে একটি হাব এবং প্রকল্প তৈরি করার ধাপগুলি অনুসরণ করুন এখানে: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

আপনার প্রকল্প তৈরি করার পরে, আপনাকে আপনার প্রকল্পের জন্য সংযোগ স্ট্রিং সংগ্রহ করতে হবে।

এটি Azure AI Foundry পোর্টালের **Overview** পৃষ্ঠায় গিয়ে করা যেতে পারে।

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.bn.png)

### ধাপ ২: আপনার `.env` ফাইল তৈরি করুন

আপনার `.env` ফাইল তৈরি করতে, আপনার টার্মিনালে নিচের কমান্ডটি চালান।

```bash
cp .env.example .env
```

এটি উদাহরণ ফাইলটি কপি করবে এবং আপনার ডিরেক্টরিতে একটি `.env` তৈরি করবে যেখানে আপনি পরিবেশ ভেরিয়েবলের জন্য মানগুলি পূরণ করবেন।

আপনার টোকেন কপি করার পরে, আপনার প্রিয় টেক্সট এডিটরে `.env` ফাইলটি খুলুন এবং `PROJECT_ENDPOINT` ফিল্ডে আপনার টোকেন পেস্ট করুন।

### ধাপ ৩: Azure-এ সাইন ইন করুন

নিরাপত্তার সেরা অনুশীলন হিসাবে, আমরা [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) ব্যবহার করব Microsoft Entra ID দিয়ে Azure OpenAI-তে প্রমাণীকরণের জন্য।

পরবর্তী ধাপে, একটি টার্মিনাল খুলুন এবং `az login --use-device-code` চালান আপনার Azure অ্যাকাউন্টে সাইন ইন করতে।

সাইন ইন করার পরে, টার্মিনালে আপনার সাবস্ক্রিপশন নির্বাচন করুন।

## অতিরিক্ত পরিবেশ ভেরিয়েবল - Azure Search এবং Azure OpenAI

Agentic RAG পাঠ - পাঠ ৫ - এর জন্য এমন কিছু নমুনা রয়েছে যা Azure Search এবং Azure OpenAI ব্যবহার করে।

আপনি যদি এই নমুনাগুলি চালাতে চান, তবে আপনাকে `.env` ফাইলে নিম্নলিখিত পরিবেশ ভেরিয়েবলগুলি যোগ করতে হবে:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - আপনার প্রকল্পের **Overview** পৃষ্ঠার **Project details** চেক করুন।

- `AZURE_AI_PROJECT_NAME` - আপনার প্রকল্পের **Overview** পৃষ্ঠার শীর্ষে দেখুন।

- `AZURE_OPENAI_SERVICE` - **Overview** পৃষ্ঠার **Included capabilities** ট্যাবে **Azure OpenAI Service** এর জন্য দেখুন।

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - **Management Center** এর **Overview** পৃষ্ঠার **Project properties** এ যান।

- `GLOBAL_LLM_SERVICE` - **Connected resources** এর অধীনে, **Azure AI Services** সংযোগের নাম খুঁজুন। যদি তালিকাভুক্ত না থাকে, তবে আপনার রিসোর্স গ্রুপের অধীনে Azure পোর্টালে AI Services রিসোর্সের নাম চেক করুন।

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - আপনার এমবেডিং মডেল (যেমন, `text-embedding-ada-002`) নির্বাচন করুন এবং মডেল বিবরণ থেকে **Deployment name** নোট করুন।

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - আপনার চ্যাট মডেল (যেমন, `gpt-4o-mini`) নির্বাচন করুন এবং মডেল বিবরণ থেকে **Deployment name** নোট করুন।

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - **Azure AI services** খুঁজুন, এটি ক্লিক করুন, তারপর **Resource Management**, **Keys and Endpoint** এ যান, "Azure OpenAI endpoints" এ স্ক্রোল করুন এবং "Language APIs" এর একটি কপি করুন।

- `AZURE_OPENAI_API_KEY` - একই স্ক্রিন থেকে, KEY 1 বা KEY 2 কপি করুন।

- `AZURE_SEARCH_SERVICE_ENDPOINT` - আপনার **Azure AI Search** রিসোর্স খুঁজুন, এটি ক্লিক করুন এবং **Overview** দেখুন।

- `AZURE_SEARCH_API_KEY` - তারপর **Settings** এ যান এবং **Keys** এ গিয়ে প্রাথমিক বা মাধ্যমিক অ্যাডমিন কী কপি করুন।

### External Webpage

- `AZURE_OPENAI_API_VERSION` - [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) পৃষ্ঠার **Latest GA API release** এর অধীনে দেখুন।

### Keyless Authentication সেটআপ করুন

আপনার শংসাপত্রগুলি হার্ডকোড করার পরিবর্তে, আমরা Azure OpenAI-এর সাথে একটি keyless সংযোগ ব্যবহার করব। এটি করতে, আমরা `DefaultAzureCredential` আমদানি করব এবং পরে শংসাপত্র পেতে `DefaultAzureCredential` ফাংশন কল করব।

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## কোথাও আটকে গেছেন?

যদি এই সেটআপ চালানোর সময় আপনার কোনো সমস্যা হয়, আমাদের 

## পরবর্তী পাঠ

এখন আপনি এই কোর্সের কোড চালানোর জন্য প্রস্তুত। AI এজেন্টের জগৎ সম্পর্কে আরও জানার জন্য শুভকামনা!

[AI এজেন্ট এবং এজেন্ট ব্যবহারের কেসগুলির পরিচিতি](../01-intro-to-ai-agents/README.md)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা তার জন্য দায়ী থাকব না।