<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:23:43+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "id"
}
-->
# Contoh Server Github MCP

## Deskripsi

Ini adalah demo yang dibuat untuk AI Agents Hackathon yang diselenggarakan melalui Microsoft Reactor.

Alat ini digunakan untuk merekomendasikan proyek hackathon berdasarkan repositori Github pengguna.  
Ini dilakukan dengan cara:

1. **Github Agent** - Menggunakan Github MCP Server untuk mengambil repositori dan informasi tentang repositori tersebut.  
2. **Hackathon Agent** - Mengambil data dari Github Agent dan menghasilkan ide proyek hackathon kreatif berdasarkan proyek, bahasa yang digunakan oleh pengguna, dan jalur proyek untuk AI Agents hackathon.  
3. **Events Agent** - Berdasarkan saran dari hackathon agent, events agent akan merekomendasikan acara yang relevan dari seri AI Agent Hackathon.  

## Menjalankan kode

### Variabel Lingkungan

Demo ini menggunakan Azure Open AI Service, Semantic Kernel, Github MCP Server, dan Azure AI Search.

Pastikan Anda sudah mengatur variabel lingkungan yang tepat untuk menggunakan alat-alat ini:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Menjalankan Server Chainlit

Untuk terhubung ke MCP server, demo ini menggunakan Chainlit sebagai antarmuka chat.

Untuk menjalankan server, gunakan perintah berikut di terminal Anda:

```bash
chainlit run app.py -w
```

Ini akan memulai server Chainlit Anda di `localhost:8000` serta mengisi Azure AI Search Index Anda dengan konten dari `event-descriptions.md`.

## Menghubungkan ke MCP Server

Untuk terhubung ke Github MCP Server, pilih ikon "plug" di bawah kotak chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.id.png)

Dari sana, Anda bisa klik "Connect an MCP" untuk menambahkan perintah menghubungkan ke Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ganti "[YOUR PERSONAL ACCESS TOKEN]" dengan Personal Access Token Anda yang sebenarnya.

Setelah terhubung, Anda akan melihat angka (1) di sebelah ikon plug sebagai tanda koneksi berhasil. Jika tidak, coba restart server chainlit dengan `chainlit run app.py -w`.

## Menggunakan Demo

Untuk memulai alur kerja agen dalam merekomendasikan proyek hackathon, Anda bisa mengetik pesan seperti:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent akan menganalisis permintaan Anda dan menentukan kombinasi agen (GitHub, Hackathon, dan Events) yang paling tepat untuk menangani pertanyaan Anda. Para agen bekerja sama untuk memberikan rekomendasi menyeluruh berdasarkan analisis repositori GitHub, ide proyek, dan acara teknologi yang relevan.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.