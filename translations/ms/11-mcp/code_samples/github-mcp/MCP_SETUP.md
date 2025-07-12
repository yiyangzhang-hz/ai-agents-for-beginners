<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:49+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ms"
}
-->
# Panduan Integrasi Pelayan MCP

## Prasyarat
- Node.js dipasang (versi 14 atau ke atas)
- Pengurus pakej npm
- Persekitaran Python dengan kebergantungan yang diperlukan

## Langkah Persediaan

1. **Pasang Pakej Pelayan MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Mulakan Pelayan MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Pelayan sepatutnya bermula dan memaparkan URL sambungan.

3. **Sahkan Sambungan**  
   - Cari ikon palam (🔌) dalam antara muka Chainlit anda  
   - Nombor (1) sepatutnya muncul di sebelah ikon palam menandakan sambungan berjaya  
   - Konsol akan memaparkan: "GitHub plugin setup completed successfully" (berserta baris status tambahan)

## Penyelesaian Masalah

### Isu Biasa

1. **Konflik Port**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Penyelesaian: Tukar port menggunakan:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Isu Pengesahan**  
   - Pastikan kelayakan GitHub dikonfigurasikan dengan betul  
   - Semak fail .env mengandungi token yang diperlukan  
   - Sahkan akses API GitHub

3. **Sambungan Gagal**  
   - Sahkan pelayan berjalan pada port yang dijangka  
   - Semak tetapan firewall  
   - Sahkan persekitaran Python mempunyai pakej yang diperlukan

## Pengesahan Sambungan

Pelayan MCP anda disambungkan dengan betul apabila:  
1. Konsol memaparkan "GitHub plugin setup completed successfully"  
2. Log sambungan menunjukkan "✓ MCP Connection Status: Active"  
3. Arahan GitHub berfungsi dalam antara muka sembang

## Pembolehubah Persekitaran

Diperlukan dalam fail .env anda:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Ujian Sambungan

Hantar mesej ujian ini dalam sembang:  
```
Show me the repositories for username: [GitHub Username]
```  
Respons berjaya akan memaparkan maklumat repositori.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.