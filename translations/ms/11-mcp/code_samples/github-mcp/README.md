<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:23:51+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "ms"
}
-->
# Contoh Pelayan Github MCP

## Penerangan

Ini adalah demo yang dibuat untuk AI Agents Hackathon yang dianjurkan melalui Microsoft Reactor.

Alat ini digunakan untuk mencadangkan projek hackathon berdasarkan repositori Github pengguna.
Ini dilakukan dengan:

1. **Github Agent** - Menggunakan Pelayan MCP Github untuk mendapatkan repositori dan maklumat tentang repositori tersebut.
2. **Hackathon Agent** - Mengambil data dari Github Agent dan menghasilkan idea projek hackathon yang kreatif berdasarkan projek, bahasa yang digunakan oleh pengguna dan trek projek untuk AI Agents hackathon.
3. **Events Agent** - Berdasarkan cadangan hackathon agent, events agent akan mencadangkan acara yang berkaitan dari siri AI Agent Hackathon.

## Menjalankan kod

### Pembolehubah Persekitaran

Demo ini menggunakan Azure Open AI Service, Semantic Kernel, Pelayan MCP Github dan Azure AI Search.

Pastikan anda telah menetapkan pembolehubah persekitaran yang betul untuk menggunakan alat-alat ini:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Menjalankan Pelayan Chainlit

Untuk berhubung dengan pelayan MCP, demo ini menggunakan Chainlit sebagai antara muka sembang.

Untuk menjalankan pelayan, gunakan arahan berikut dalam terminal anda:

```bash
chainlit run app.py -w
```

Ini akan memulakan pelayan Chainlit anda pada `localhost:8000` serta mengisi Indeks Azure AI Search anda dengan kandungan `event-descriptions.md`.

## Berhubung dengan Pelayan MCP

Untuk berhubung dengan Pelayan MCP Github, pilih ikon "plug" di bawah kotak sembang "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.ms.png)

Dari situ anda boleh klik pada "Connect an MCP" untuk menambah arahan bagi berhubung dengan Pelayan MCP Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Gantikan "[YOUR PERSONAL ACCESS TOKEN]" dengan Token Akses Peribadi anda yang sebenar.

Selepas berhubung, anda sepatutnya melihat (1) di sebelah ikon plug untuk mengesahkan sambungan. Jika tidak, cuba mulakan semula pelayan chainlit dengan `chainlit run app.py -w`.

## Menggunakan Demo

Untuk memulakan aliran kerja agen mencadangkan projek hackathon, anda boleh taip mesej seperti:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent akan menganalisis permintaan anda dan menentukan gabungan agen (GitHub, Hackathon, dan Events) yang paling sesuai untuk mengendalikan pertanyaan anda. Agen-agen ini bekerjasama untuk memberikan cadangan menyeluruh berdasarkan analisis repositori GitHub, idea projek, dan acara teknologi yang berkaitan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.