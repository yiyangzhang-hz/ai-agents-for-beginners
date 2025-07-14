<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:49:26+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "id"
}
-->
# Pelajaran 11: Integrasi Model Context Protocol (MCP)

## Pengenalan Model Context Protocol (MCP)

Model Context Protocol (MCP) adalah kerangka kerja mutakhir yang dirancang untuk menstandarisasi interaksi antara model AI dan aplikasi klien. MCP berfungsi sebagai jembatan antara model AI dan aplikasi yang menggunakannya, menyediakan antarmuka yang konsisten tanpa memandang implementasi model di baliknya.

Aspek utama MCP:

- **Komunikasi Terstandarisasi**: MCP menetapkan bahasa umum bagi aplikasi untuk berkomunikasi dengan model AI
- **Manajemen Konteks yang Ditingkatkan**: Memungkinkan pengiriman informasi kontekstual ke model AI secara efisien
- **Kompatibilitas Lintas Platform**: Bekerja di berbagai bahasa pemrograman termasuk C#, Java, JavaScript, Python, dan TypeScript
- **Integrasi Mulus**: Memudahkan pengembang mengintegrasikan berbagai model AI ke dalam aplikasi mereka

MCP sangat berharga dalam pengembangan agen AI karena memungkinkan agen berinteraksi dengan berbagai sistem dan sumber data melalui protokol yang terpadu, menjadikan agen lebih fleksibel dan kuat.

## Tujuan Pembelajaran
- Memahami apa itu MCP dan perannya dalam pengembangan agen AI
- Menyiapkan dan mengonfigurasi server MCP untuk integrasi GitHub
- Membangun sistem multi-agen menggunakan alat MCP
- Menerapkan RAG (Retrieval Augmented Generation) dengan Azure Cognitive Search

## Prasyarat
- Python 3.8+
- Node.js 14+
- Langganan Azure
- Akun GitHub
- Pemahaman dasar tentang Semantic Kernel

## Instruksi Pengaturan

1. **Pengaturan Lingkungan**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfigurasi Layanan Azure**
   - Buat sumber daya Azure Cognitive Search
   - Siapkan layanan Azure OpenAI
   - Konfigurasikan variabel lingkungan di `.env`

3. **Pengaturan Server MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktur Proyek

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

## Komponen Inti

### 1. Sistem Multi-Agen
- GitHub Agent: Analisis repositori
- Hackathon Agent: Rekomendasi proyek
- Events Agent: Saran acara teknologi

### 2. Integrasi Azure
- Cognitive Search untuk pengindeksan acara
- Azure OpenAI untuk kecerdasan agen
- Implementasi pola RAG

### 3. Alat MCP
- Analisis repositori GitHub
- Inspeksi kode
- Ekstraksi metadata

## Penjelasan Kode

Contoh ini menunjukkan:
1. Integrasi server MCP
2. Orkestrasi multi-agen
3. Integrasi Azure Cognitive Search
4. Implementasi pola RAG

Fitur utama:
- Analisis repositori GitHub secara real-time
- Rekomendasi proyek yang cerdas
- Pencocokan acara menggunakan Azure Search
- Respons streaming dengan Chainlit

## Menjalankan Contoh

Untuk instruksi pengaturan lebih rinci dan informasi lainnya, lihat [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Mulai server MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Jalankan aplikasi:
   ```bash
   chainlit run app.py -w
   ```

3. Uji integrasi:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Pemecahan Masalah

Masalah umum dan solusinya:
1. Masalah Koneksi MCP
   - Pastikan server berjalan
   - Periksa ketersediaan port
   - Konfirmasi token GitHub

2. Masalah Azure Search
   - Validasi string koneksi
   - Periksa keberadaan indeks
   - Verifikasi unggahan dokumen

## Langkah Selanjutnya
- Jelajahi alat MCP tambahan
- Implementasikan agen kustom
- Tingkatkan kemampuan RAG
- Tambahkan lebih banyak sumber acara

## Sumber Daya
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentasi Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Panduan Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.