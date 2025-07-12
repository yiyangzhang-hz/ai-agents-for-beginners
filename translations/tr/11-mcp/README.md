<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:47:40+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "tr"
}
-->
# Ders 11: Model Context Protocol (MCP) Entegrasyonu

## Model Context Protocol (MCP) Tanıtımı

Model Context Protocol (MCP), yapay zeka modelleri ile istemci uygulamaları arasındaki etkileşimleri standartlaştırmak için tasarlanmış ileri düzey bir çerçevedir. MCP, yapay zeka modelleri ile bu modelleri kullanan uygulamalar arasında bir köprü görevi görür ve altta yatan model uygulamasından bağımsız olarak tutarlı bir arayüz sağlar.

MCP’nin temel özellikleri:

- **Standartlaştırılmış İletişim**: Uygulamaların yapay zeka modelleriyle ortak bir dilde iletişim kurmasını sağlar
- **Gelişmiş Bağlam Yönetimi**: Yapay zeka modellerine bağlamsal bilgilerin verimli şekilde iletilmesine olanak tanır
- **Çapraz Platform Uyumluluğu**: C#, Java, JavaScript, Python ve TypeScript gibi çeşitli programlama dilleriyle çalışır
- **Sorunsuz Entegrasyon**: Geliştiricilerin farklı yapay zeka modellerini uygulamalarına kolayca entegre etmelerini sağlar

MCP, yapay zeka ajan geliştirmede özellikle değerlidir çünkü ajanların çeşitli sistemler ve veri kaynaklarıyla birleşik bir protokol üzerinden etkileşim kurmasını sağlayarak ajanları daha esnek ve güçlü hale getirir.

## Öğrenme Hedefleri
- MCP’nin ne olduğunu ve yapay zeka ajan geliştirmedeki rolünü anlamak
- GitHub entegrasyonu için MCP sunucusunu kurup yapılandırmak
- MCP araçları kullanarak çoklu ajan sistemi oluşturmak
- Azure Cognitive Search ile RAG (Retrieval Augmented Generation) uygulamak

## Ön Koşullar
- Python 3.8+
- Node.js 14+
- Azure aboneliği
- GitHub hesabı
- Semantic Kernel hakkında temel bilgi

## Kurulum Talimatları

1. **Ortam Kurulumu**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure Servislerini Yapılandırma**
   - Azure Cognitive Search kaynağı oluşturun
   - Azure OpenAI servisini kurun
   - `.env` dosyasında ortam değişkenlerini yapılandırın

3. **MCP Sunucu Kurulumu**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Proje Yapısı

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

## Temel Bileşenler

### 1. Çoklu Ajan Sistemi
- GitHub Ajanı: Depo analizi
- Hackathon Ajanı: Proje önerileri
- Etkinlik Ajanı: Teknoloji etkinliği önerileri

### 2. Azure Entegrasyonu
- Etkinlik indekslemesi için Cognitive Search
- Ajan zekası için Azure OpenAI
- RAG deseninin uygulanması

### 3. MCP Araçları
- GitHub depo analizi
- Kod incelemesi
- Meta veri çıkarımı

## Kod İncelemesi

Örnek şunları gösterir:
1. MCP sunucu entegrasyonu
2. Çoklu ajan koordinasyonu
3. Azure Cognitive Search entegrasyonu
4. RAG deseninin uygulanması

Öne çıkan özellikler:
- Gerçek zamanlı GitHub depo analizi
- Akıllı proje önerileri
- Azure Search ile etkinlik eşleştirme
- Chainlit ile akış halinde yanıtlar

## Örneği Çalıştırma

Detaylı kurulum talimatları ve daha fazla bilgi için [Github MCP Server Example README](./code_samples/github-mcp/README.md) dosyasına bakınız.

1. MCP sunucusunu başlatın:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Uygulamayı çalıştırın:
   ```bash
   chainlit run app.py -w
   ```

3. Entegrasyonu test edin:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Sorun Giderme

Yaygın sorunlar ve çözümleri:
1. MCP Bağlantı Sorunları
   - Sunucunun çalıştığını doğrulayın
   - Port kullanılabilirliğini kontrol edin
   - GitHub tokenlarını doğrulayın

2. Azure Search Sorunları
   - Bağlantı dizelerini kontrol edin
   - İndeksin varlığını doğrulayın
   - Belge yüklemesini kontrol edin

## Sonraki Adımlar
- Ek MCP araçlarını keşfedin
- Özel ajanlar geliştirin
- RAG yeteneklerini geliştirin
- Daha fazla etkinlik kaynağı ekleyin

## Kaynaklar
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.