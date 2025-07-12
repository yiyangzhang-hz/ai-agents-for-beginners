<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:46:23+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "mr"
}
-->
# धडा ११: Model Context Protocol (MCP) एकत्रीकरण

## Model Context Protocol (MCP) परिचय

Model Context Protocol (MCP) हा एक अत्याधुनिक फ्रेमवर्क आहे जो AI मॉडेल्स आणि क्लायंट अॅप्लिकेशन्समधील संवादासाठी एकसारखा मानक तयार करतो. MCP AI मॉडेल्स आणि त्यांचा वापर करणाऱ्या अॅप्लिकेशन्समधील पूल म्हणून काम करतो, ज्यामुळे मॉडेलच्या अंतर्गत अंमलबजावणीपासून स्वतंत्रपणे एकसारखा इंटरफेस मिळतो.

MCP चे मुख्य पैलू:

- **मानकीकृत संवाद**: MCP अॅप्लिकेशन्सना AI मॉडेल्सशी संवाद साधण्यासाठी एकसारखी भाषा प्रदान करतो
- **संदर्भ व्यवस्थापन सुधारणा**: AI मॉडेल्सना संदर्भात्मक माहिती प्रभावीपणे पाठवण्याची सोय
- **क्रॉस-प्लॅटफॉर्म सुसंगतता**: C#, Java, JavaScript, Python, आणि TypeScript यांसारख्या विविध प्रोग्रामिंग भाषांमध्ये कार्य करते
- **सुलभ एकत्रीकरण**: विकसकांना विविध AI मॉडेल्स त्यांच्या अॅप्लिकेशन्समध्ये सहजपणे समाकलित करण्याची परवानगी देते

MCP AI एजंट विकासात विशेषतः उपयुक्त आहे कारण हे एजंट्सना विविध प्रणाली आणि डेटा स्रोतांशी एकसंध प्रोटोकॉलद्वारे संवाद साधण्याची मुभा देते, ज्यामुळे एजंट्स अधिक लवचिक आणि सामर्थ्यशाली बनतात.

## शिकण्याचे उद्दिष्टे
- MCP काय आहे आणि AI एजंट विकासातील त्याची भूमिका समजून घेणे
- GitHub एकत्रीकरणासाठी MCP सर्व्हर सेटअप आणि कॉन्फिगर करणे
- MCP साधने वापरून मल्टी-एजंट सिस्टम तयार करणे
- Azure Cognitive Search सह RAG (Retrieval Augmented Generation) अंमलात आणणे

## पूर्वअट
- Python 3.8+
- Node.js 14+
- Azure सदस्यता
- GitHub खाते
- Semantic Kernel ची प्राथमिक समज

## सेटअप सूचना

1. **पर्यावरण सेटअप**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure सेवा कॉन्फिगर करा**
   - Azure Cognitive Search संसाधन तयार करा
   - Azure OpenAI सेवा सेटअप करा
   - `.env` मध्ये पर्यावरण चल सेट करा

3. **MCP सर्व्हर सेटअप**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## प्रकल्प रचना

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

## मुख्य घटक

### १. मल्टी-एजंट सिस्टम
- GitHub एजंट: रिपॉझिटरी विश्लेषण
- Hackathon एजंट: प्रकल्प शिफारसी
- Events एजंट: तंत्रज्ञान कार्यक्रम सूचना

### २. Azure एकत्रीकरण
- कार्यक्रम अनुक्रमणासाठी Cognitive Search
- एजंट बुद्धिमत्तेसाठी Azure OpenAI
- RAG पॅटर्न अंमलबजावणी

### ३. MCP साधने
- GitHub रिपॉझिटरी विश्लेषण
- कोड तपासणी
- मेटाडेटा काढणे

## कोड वॉकथ्रू

या नमुन्यात दाखवले आहे:
1. MCP सर्व्हर एकत्रीकरण
2. मल्टी-एजंट समन्वय
3. Azure Cognitive Search एकत्रीकरण
4. RAG पॅटर्न अंमलबजावणी

महत्त्वाच्या वैशिष्ट्ये:
- रिअल-टाइम GitHub रिपॉझिटरी विश्लेषण
- बुद्धिमान प्रकल्प शिफारसी
- Azure Search वापरून कार्यक्रम जुळवणी
- Chainlit सह स्ट्रीमिंग प्रतिसाद

## नमुना चालवणे

सविस्तर सेटअप सूचना आणि अधिक माहितीसाठी, [Github MCP Server Example README](./code_samples/github-mcp/README.md) पहा.

1. MCP सर्व्हर सुरू करा:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. अॅप्लिकेशन लॉन्च करा:
   ```bash
   chainlit run app.py -w
   ```

3. एकत्रीकरण तपासा:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## समस्या निवारण

सामान्य समस्या आणि उपाय:
1. MCP कनेक्शन समस्या
   - सर्व्हर चालू आहे का तपासा
   - पोर्ट उपलब्धता तपासा
   - GitHub टोकन्सची पुष्टी करा

2. Azure Search समस्या
   - कनेक्शन स्ट्रिंग्ज तपासा
   - अनुक्रमण अस्तित्वात आहे का तपासा
   - दस्तऐवज अपलोडची पुष्टी करा

## पुढील पावले
- अतिरिक्त MCP साधने एक्सप्लोर करा
- सानुकूल एजंट्स अंमलात आणा
- RAG क्षमता वाढवा
- अधिक कार्यक्रम स्रोत जोडा

## संसाधने
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.