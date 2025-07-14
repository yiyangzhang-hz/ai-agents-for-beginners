<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:46:12+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "bn"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Model Context Protocol (MCP) পরিচিতি

Model Context Protocol (MCP) একটি আধুনিক ফ্রেমওয়ার্ক যা AI মডেল এবং ক্লায়েন্ট অ্যাপ্লিকেশনগুলোর মধ্যে ইন্টারঅ্যাকশনকে স্ট্যান্ডার্ডাইজ করার জন্য তৈরি। MCP AI মডেল এবং সেগুলো ব্যবহারকারী অ্যাপ্লিকেশনগুলোর মধ্যে একটি সেতুবন্ধন হিসেবে কাজ করে, যা মডেলের অন্তর্নিহিত বাস্তবায়নের পার্থক্য নির্বিশেষে একটি সঙ্গতিপূর্ণ ইন্টারফেস প্রদান করে।

MCP এর মূল দিকগুলো:

- **স্ট্যান্ডার্ডাইজড কমিউনিকেশন**: MCP অ্যাপ্লিকেশনগুলোকে AI মডেলের সাথে যোগাযোগ করার জন্য একটি সাধারণ ভাষা প্রতিষ্ঠা করে
- **উন্নত কনটেক্সট ম্যানেজমেন্ট**: AI মডেলে প্রাসঙ্গিক তথ্য দক্ষতার সঙ্গে প্রেরণ করার সুযোগ দেয়
- **ক্রস-প্ল্যাটফর্ম সামঞ্জস্যতা**: C#, Java, JavaScript, Python, এবং TypeScript সহ বিভিন্ন প্রোগ্রামিং ভাষায় কাজ করে
- **সহজ ইন্টিগ্রেশন**: ডেভেলপারদের জন্য বিভিন্ন AI মডেল সহজেই তাদের অ্যাপ্লিকেশনে সংযুক্ত করার সুযোগ দেয়

AI এজেন্ট ডেভেলপমেন্টে MCP বিশেষভাবে মূল্যবান কারণ এটি এজেন্টদের বিভিন্ন সিস্টেম এবং ডেটা সোর্সের সাথে একটি একক প্রোটোকলের মাধ্যমে ইন্টারঅ্যাক্ট করার সুযোগ দেয়, ফলে এজেন্টগুলো আরও নমনীয় এবং শক্তিশালী হয়।

## শেখার উদ্দেশ্য
- MCP কী এবং AI এজেন্ট ডেভেলপমেন্টে এর ভূমিকা বোঝা
- GitHub ইন্টিগ্রেশনের জন্য MCP সার্ভার সেটআপ ও কনফিগার করা
- MCP টুলস ব্যবহার করে মাল্টি-এজেন্ট সিস্টেম তৈরি করা
- Azure Cognitive Search এর মাধ্যমে RAG (Retrieval Augmented Generation) বাস্তবায়ন করা

## প্রয়োজনীয়তা
- Python 3.8+
- Node.js 14+
- Azure সাবস্ক্রিপশন
- GitHub অ্যাকাউন্ট
- Semantic Kernel এর মৌলিক ধারণা

## সেটআপ নির্দেশিকা

1. **পরিবেশ সেটআপ**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure সার্ভিস কনফিগারেশন**
   - একটি Azure Cognitive Search রিসোর্স তৈরি করুন
   - Azure OpenAI সার্ভিস সেটআপ করুন
   - `.env` ফাইলে পরিবেশ ভেরিয়েবল কনফিগার করুন

3. **MCP সার্ভার সেটআপ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## প্রকল্পের কাঠামো

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## মূল উপাদানসমূহ

### ১. মাল্টি-এজেন্ট সিস্টেম
- GitHub Agent: রেপোজিটরি বিশ্লেষণ
- Hackathon Agent: প্রকল্পের সুপারিশ
- Events Agent: প্রযুক্তি ইভেন্টের পরামর্শ

### ২. Azure ইন্টিগ্রেশন
- ইভেন্ট ইনডেক্সিংয়ের জন্য Cognitive Search
- এজেন্ট বুদ্ধিমত্তার জন্য Azure OpenAI
- RAG প্যাটার্ন বাস্তবায়ন

### ৩. MCP টুলস
- GitHub রেপোজিটরি বিশ্লেষণ
- কোড পরিদর্শন
- মেটাডেটা আহরণ

## কোড ওয়াকথ্রু

নমুনাটি প্রদর্শন করে:
1. MCP সার্ভার ইন্টিগ্রেশন
2. মাল্টি-এজেন্ট সমন্বয়
3. Azure Cognitive Search ইন্টিগ্রেশন
4. RAG প্যাটার্ন বাস্তবায়ন

মূল বৈশিষ্ট্যসমূহ:
- রিয়েল-টাইম GitHub রেপোজিটরি বিশ্লেষণ
- বুদ্ধিমান প্রকল্পের সুপারিশ
- Azure Search ব্যবহার করে ইভেন্ট মিলানো
- Chainlit এর মাধ্যমে স্ট্রিমিং রেসপন্স

## নমুনা চালানো

বিস্তারিত সেটআপ নির্দেশিকা এবং আরও তথ্যের জন্য, [Github MCP Server Example README](./code_samples/github-mcp/README.md) দেখুন।

1. MCP সার্ভার চালু করুন:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. অ্যাপ্লিকেশন লঞ্চ করুন:
   ```bash
   chainlit run app.py -w
   ```

3. ইন্টিগ্রেশন পরীক্ষা করুন:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## সমস্যা সমাধান

সাধারণ সমস্যা এবং সমাধান:
1. MCP সংযোগ সমস্যা
   - সার্ভার চালু আছে কিনা যাচাই করুন
   - পোর্টের উপলব্ধতা পরীক্ষা করুন
   - GitHub টোকেন নিশ্চিত করুন

2. Azure Search সমস্যা
   - সংযোগ স্ট্রিং যাচাই করুন
   - ইনডেক্সের অস্তিত্ব পরীক্ষা করুন
   - ডকুমেন্ট আপলোড নিশ্চিত করুন

## পরবর্তী ধাপ
- অতিরিক্ত MCP টুলস অন্বেষণ করুন
- কাস্টম এজেন্ট তৈরি করুন
- RAG ক্ষমতা উন্নত করুন
- আরও ইভেন্ট সোর্স যোগ করুন

## সম্পদসমূহ
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।