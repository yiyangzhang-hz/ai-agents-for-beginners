<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:49:55+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sw"
}
-->
# Somo la 11: Muunganisho wa Itifaki ya Muktadha wa Mfano (MCP)

## Utangulizi wa Itifaki ya Muktadha wa Mfano (MCP)

Itifaki ya Muktadha wa Mfano (MCP) ni mfumo wa kisasa ulioundwa kuweka viwango vya mawasiliano kati ya mifano ya AI na programu za wateja. MCP hutumika kama daraja kati ya mifano ya AI na programu zinazotumia mifano hiyo, ikitoa kiolesura cha kawaida bila kujali jinsi mfano ulivyojengwa.

Mambo muhimu kuhusu MCP:

- **Mawasiliano Yenye Viwango**: MCP huanzisha lugha ya kawaida kwa programu kuwasiliana na mifano ya AI  
- **Usimamizi Bora wa Muktadha**: Huruhusu kuwasilisha taarifa za muktadha kwa ufanisi kwa mifano ya AI  
- **Ulinganifu wa Majukwaa Mbalimbali**: Inafanya kazi kwa lugha mbalimbali za programu kama C#, Java, JavaScript, Python, na TypeScript  
- **Muunganisho Rahisi**: Inawawezesha watengenezaji kuunganisha mifano tofauti ya AI kwa urahisi katika programu zao  

MCP ni muhimu hasa katika maendeleo ya maajenti wa AI kwani huruhusu maajenti kuingiliana na mifumo na vyanzo mbalimbali vya data kupitia itifaki moja, na kufanya maajenti kuwa na ufanisi zaidi na nguvu zaidi.

## Malengo ya Kujifunza
- Kuelewa MCP ni nini na nafasi yake katika maendeleo ya maajenti wa AI  
- Kuweka na kusanidi seva ya MCP kwa ajili ya muunganisho wa GitHub  
- Kujenga mfumo wa maajenti wengi kwa kutumia zana za MCP  
- Kutekeleza RAG (Retrieval Augmented Generation) kwa kutumia Azure Cognitive Search  

## Mahitaji ya Awali
- Python 3.8+  
- Node.js 14+  
- Usajili wa Azure  
- Akaunti ya GitHub  
- Uelewa wa msingi wa Semantic Kernel  

## Maelekezo ya Usanidi

1. **Usanidi wa Mazingira**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Sanidi Huduma za Azure**  
   - Tengeneza rasilimali ya Azure Cognitive Search  
   - Sanidi huduma ya Azure OpenAI  
   - Weka vigezo vya mazingira katika `.env`  

3. **Usanidi wa Seva ya MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Muundo wa Mradi

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

## Vipengele Muhimu

### 1. Mfumo wa Maajenti Wengi  
- Maajenti wa GitHub: Uchambuzi wa hifadhidata  
- Maajenti wa Hackathon: Mapendekezo ya miradi  
- Maajenti wa Matukio: Mapendekezo ya matukio ya teknolojia  

### 2. Muunganisho wa Azure  
- Cognitive Search kwa kuweka kumbukumbu za matukio  
- Azure OpenAI kwa akili ya maajenti  
- Utekelezaji wa muundo wa RAG  

### 3. Zana za MCP  
- Uchambuzi wa hifadhidata za GitHub  
- Ukaguzi wa msimbo  
- Utoaji wa metadata  

## Maelezo ya Msimbo

Mfano unaonyesha:  
1. Muunganisho wa seva ya MCP  
2. Uendeshaji wa maajenti wengi  
3. Muunganisho wa Azure Cognitive Search  
4. Utekelezaji wa muundo wa RAG  

Sifa kuu:  
- Uchambuzi wa hifadhidata za GitHub kwa wakati halisi  
- Mapendekezo ya miradi yenye akili  
- Ulinganifu wa matukio kwa kutumia Azure Search  
- Majibu yanayotiririka kwa kutumia Chainlit  

## Kuendesha Mfano

Kwa maelekezo ya kina ya usanidi na taarifa zaidi, rejelea [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Anzisha seva ya MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Anzisha programu:  
   ```bash
   chainlit run app.py -w
   ```

3. Jaribu muunganisho:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Utatuzi wa Matatizo

Matatizo ya kawaida na suluhisho:  
1. Matatizo ya Muunganisho wa MCP  
   - Hakikisha seva inaendeshwa  
   - Angalia upatikanaji wa bandari  
   - Thibitisha tokeni za GitHub  

2. Matatizo ya Azure Search  
   - Hakiki mnyororo wa muunganisho  
   - Angalia kuwepo kwa index  
   - Hakiki upakiaji wa hati  

## Hatua Zifuatazo
- Chunguza zana zaidi za MCP  
- Tekeleza maajenti maalum  
- Boresha uwezo wa RAG  
- Ongeza vyanzo zaidi vya matukio  

## Rasilimali
- [MCP kwa Waanzilishi](https://aka.ms/mcp-for-beginners)  
- [Nyaraka za MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Nyaraka za Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [Mwongozo wa Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Kiarifu cha Kutotegemea**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubebei dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.