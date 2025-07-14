<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:43+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "id"
}
-->
# Panduan Integrasi MCP Server

## Prasyarat
- Node.js terpasang (versi 14 atau lebih baru)
- npm sebagai package manager
- Lingkungan Python dengan dependensi yang dibutuhkan

## Langkah Pengaturan

1. **Pasang Paket MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Jalankan MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server akan mulai dan menampilkan URL koneksi.

3. **Verifikasi Koneksi**  
   - Cari ikon colokan (🔌) di antarmuka Chainlit Anda  
   - Angka (1) akan muncul di samping ikon colokan menandakan koneksi berhasil  
   - Konsol akan menampilkan: "GitHub plugin setup completed successfully" (beserta baris status tambahan)

## Pemecahan Masalah

### Masalah Umum

1. **Konflik Port**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solusi: Ganti port dengan menggunakan:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Masalah Autentikasi**  
   - Pastikan kredensial GitHub sudah dikonfigurasi dengan benar  
   - Periksa file .env berisi token yang diperlukan  
   - Verifikasi akses API GitHub

3. **Koneksi Gagal**  
   - Pastikan server berjalan di port yang diharapkan  
   - Periksa pengaturan firewall  
   - Pastikan lingkungan Python memiliki paket yang dibutuhkan

## Verifikasi Koneksi

MCP server Anda terhubung dengan benar ketika:  
1. Konsol menampilkan "GitHub plugin setup completed successfully"  
2. Log koneksi menunjukkan "✓ MCP Connection Status: Active"  
3. Perintah GitHub berfungsi di antarmuka chat

## Variabel Lingkungan

Diperlukan di file .env Anda:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Pengujian Koneksi

Kirim pesan uji ini di chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Respon yang berhasil akan menampilkan informasi repositori.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.