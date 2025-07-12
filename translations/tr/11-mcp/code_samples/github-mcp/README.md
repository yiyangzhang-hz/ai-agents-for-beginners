<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:22:24+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "tr"
}
-->
# Github MCP Sunucu Örneği

## Açıklama

Bu, Microsoft Reactor tarafından düzenlenen AI Agents Hackathon için oluşturulmuş bir demodur.

Araç, bir kullanıcının Github depolarına dayanarak hackathon projeleri önermek için kullanılır.  
Bunun yapılma şekli:

1. **Github Agent** - Github MCP Sunucusunu kullanarak depoları ve bu depolarla ilgili bilgileri alır.  
2. **Hackathon Agent** - Github Agent’dan aldığı verilerle, kullanıcının projeleri, kullandığı diller ve AI Agents hackathonundaki proje kategorilerine göre yaratıcı hackathon proje fikirleri üretir.  
3. **Events Agent** - Hackathon agentının önerilerine dayanarak, AI Agent Hackathon serisinden ilgili etkinlikleri önerir.  

## Kodu Çalıştırma

### Ortam Değişkenleri

Bu demo Azure Open AI Service, Semantic Kernel, Github MCP Sunucusu ve Azure AI Search kullanır.

Bu araçları kullanabilmek için uygun ortam değişkenlerinin ayarlandığından emin olun:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Chainlit Sunucusunu Çalıştırma

MCP sunucusuna bağlanmak için bu demo, sohbet arayüzü olarak Chainlit kullanır.

Sunucuyu çalıştırmak için terminalde aşağıdaki komutu kullanın:

```bash
chainlit run app.py -w
```

Bu, Chainlit sunucunuzu `localhost:8000` üzerinde başlatmalı ve Azure AI Search İndeksinizi `event-descriptions.md` içeriği ile doldurmalıdır.

## MCP Sunucusuna Bağlanma

Github MCP Sunucusuna bağlanmak için, "Type your message here.." sohbet kutusunun altındaki "fiş" simgesini seçin:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.tr.png)

Buradan "Connect an MCP" seçeneğine tıklayarak Github MCP Sunucusuna bağlanma komutunu ekleyebilirsiniz:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" kısmını gerçek Kişisel Erişim Tokenınız ile değiştirin.

Bağlandıktan sonra, fiş simgesinin yanında (1) görmelisiniz; bu bağlantının başarılı olduğunu gösterir. Eğer görmüyorsanız, `chainlit run app.py -w` komutuyla chainlit sunucusunu yeniden başlatmayı deneyin.

## Demoyu Kullanma

Hackathon projeleri önermeye yönelik ajan iş akışını başlatmak için şu şekilde bir mesaj yazabilirsiniz:

"Github kullanıcısı koreyspace için hackathon projeleri öner"

Router Agent, isteğinizi analiz edecek ve sorgunuzu en iyi şekilde karşılayacak ajan kombinasyonunu (GitHub, Hackathon ve Events) belirleyecektir. Ajanlar, Github depo analizine, proje fikirlerine ve ilgili teknoloji etkinliklerine dayalı kapsamlı öneriler sunmak için birlikte çalışır.

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.