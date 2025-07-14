<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:16:30+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "tr"
}
-->
# MCP Sunucu Entegrasyon Rehberi

## Ön Koşullar
- Node.js yüklü (sürüm 14 veya üzeri)
- npm paket yöneticisi
- Gerekli bağımlılıklarla Python ortamı

## Kurulum Adımları

1. **MCP Sunucu Paketini Yükleyin**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Sunucusunu Başlatın**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   Sunucu başlamalı ve bir bağlantı URL'si göstermelidir.

3. **Bağlantıyı Doğrulayın**
   - Chainlit arayüzünüzde fiş simgesini (🔌) arayın
   - Fiş simgesinin yanında (1) sayısı görünmeli, bu başarılı bağlantıyı gösterir
   - Konsolda şu mesaj görünmeli: "GitHub plugin setup completed successfully" (ek durum satırları ile birlikte)

## Sorun Giderme

### Yaygın Sorunlar

1. **Port Çakışması**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   Çözüm: Portu şu şekilde değiştirin:
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Kimlik Doğrulama Sorunları**
   - GitHub kimlik bilgilerinin doğru yapılandırıldığından emin olun
   - .env dosyasının gerekli tokenları içerdiğini kontrol edin
   - GitHub API erişimini doğrulayın

3. **Bağlantı Başarısız**
   - Sunucunun beklenen portta çalıştığını teyit edin
   - Güvenlik duvarı ayarlarını kontrol edin
   - Python ortamında gerekli paketlerin yüklü olduğunu doğrulayın

## Bağlantı Doğrulama

MCP sunucunuz doğru şekilde bağlıdır, eğer:
1. Konsolda "GitHub plugin setup completed successfully" mesajı görünür
2. Bağlantı kayıtlarında "✓ MCP Connection Status: Active" ifadesi yer alır
3. GitHub komutları sohbet arayüzünde çalışır

## Ortam Değişkenleri

.env dosyanızda gerekli olanlar:
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Bağlantıyı Test Etme

Sohbette bu test mesajını gönderin:
```
Show me the repositories for username: [GitHub Username]
```
Başarılı bir yanıt depo bilgilerini gösterecektir.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.