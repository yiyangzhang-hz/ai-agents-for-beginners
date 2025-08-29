<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6600bebb86f72f3f62a9163fcce9566",
  "translation_date": "2025-08-29T13:23:48+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "tr"
}
-->
# Agentik Protokolleri Kullanımı (MCP, A2A ve NLWeb)

[![Agentik Protokolleri](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.tr.png)](https://youtu.be/X-Dh9R3Opn8)

Yapay zeka ajanlarının kullanımı arttıkça, standartlaşmayı, güvenliği ve açık inovasyonu destekleyen protokollere olan ihtiyaç da artıyor. Bu derste, bu ihtiyacı karşılamayı hedefleyen üç protokolü ele alacağız: Model Context Protocol (MCP), Agent to Agent (A2A) ve Natural Language Web (NLWeb).

## Giriş

Bu derste şunları ele alacağız:

• **MCP**'nin yapay zeka ajanlarının kullanıcı görevlerini tamamlamak için harici araçlara ve verilere erişmesini nasıl sağladığını.

• **A2A**'nın farklı yapay zeka ajanları arasında iletişim ve iş birliğini nasıl mümkün kıldığını.

• **NLWeb**'in herhangi bir web sitesine doğal dil arayüzleri getirerek yapay zeka ajanlarının içeriği keşfetmesini ve etkileşimde bulunmasını nasıl sağladığını.

## Öğrenme Hedefleri

• Yapay zeka ajanları bağlamında MCP, A2A ve NLWeb'in temel amacını ve faydalarını **tanımlayın**.

• Her bir protokolün LLM'ler, araçlar ve diğer ajanlar arasındaki iletişimi ve etkileşimi nasıl kolaylaştırdığını **açıklayın**.

• Karmaşık agentik sistemler oluştururken her bir protokolün oynadığı farklı rolleri **tanıyın**.

## Model Context Protocol

**Model Context Protocol (MCP)**, uygulamaların LLM'lere bağlam ve araç sağlaması için standart bir yöntem sunan açık bir standarttır. Bu, yapay zeka ajanlarının tutarlı bir şekilde bağlanabileceği farklı veri kaynaklarına ve araçlara yönelik "evrensel bir adaptör" sağlar.

MCP'nin bileşenlerine, doğrudan API kullanımına kıyasla sunduğu avantajlara ve yapay zeka ajanlarının bir MCP sunucusunu nasıl kullanabileceğine dair bir örneğe bakalım.

### MCP Temel Bileşenleri

MCP, bir **istemci-sunucu mimarisi** üzerinde çalışır ve temel bileşenleri şunlardır:

• **Hosts**: MCP sunucusuna bağlantı başlatan LLM uygulamalarıdır (örneğin, VSCode gibi bir kod editörü).

• **Clients**: Sunucu ile birebir bağlantıları sürdüren ana uygulama içindeki bileşenlerdir.

• **Servers**: Belirli yetenekleri sunan hafif programlardır.

Protokol, bir MCP sunucusunun yeteneklerini oluşturan üç temel ilkeyi içerir:

• **Tools**: Yapay zeka ajanının bir eylemi gerçekleştirmek için çağırabileceği ayrı eylemler veya işlevlerdir. Örneğin, bir hava durumu servisi "hava durumu al" aracını veya bir e-ticaret sunucusu "ürün satın al" aracını sunabilir. MCP sunucuları, her aracın adını, açıklamasını ve giriş/çıkış şemasını yetenek listelerinde belirtir.

• **Resources**: MCP sunucusunun sağlayabileceği ve istemcilerin talep üzerine alabileceği salt okunur veri öğeleri veya belgelerdir. Örnekler arasında dosya içerikleri, veritabanı kayıtları veya günlük dosyaları bulunur. Kaynaklar metin (kod veya JSON gibi) veya ikili (görüntüler veya PDF'ler gibi) olabilir.

• **Prompts**: Daha karmaşık iş akışlarını mümkün kılan önerilen istemleri sağlayan önceden tanımlanmış şablonlardır.

### MCP'nin Faydaları

MCP, yapay zeka ajanları için önemli avantajlar sunar:

• **Dinamik Araç Keşfi**: Ajanlar, bir sunucudan mevcut araçların listesini ve ne yaptıklarına dair açıklamaları dinamik olarak alabilir. Bu, geleneksel API'lerin genellikle entegrasyonlar için statik kodlama gerektirdiği ve herhangi bir API değişikliğinin kod güncellemelerini zorunlu kıldığı durumlara kıyasla farklıdır. MCP, "bir kez entegre et" yaklaşımı sunarak daha fazla uyarlanabilirlik sağlar.

• **LLM'ler Arasında Uyumluluk**: MCP, farklı LLM'ler arasında çalışır ve daha iyi performans için temel modelleri değiştirme esnekliği sağlar.

• **Standartlaştırılmış Güvenlik**: MCP, ek MCP sunucularına erişim eklerken ölçeklenebilirliği artıran standart bir kimlik doğrulama yöntemi içerir. Bu, çeşitli geleneksel API'ler için farklı anahtarları ve kimlik doğrulama türlerini yönetmekten daha basittir.

### MCP Örneği

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.tr.png)

Bir kullanıcının MCP destekli bir yapay zeka asistanı kullanarak uçak bileti rezervasyonu yapmak istediğini hayal edin.

1. **Bağlantı**: Yapay zeka asistanı (MCP istemcisi), bir havayolu tarafından sağlanan MCP sunucusuna bağlanır.

2. **Araç Keşfi**: İstemci, havayolunun MCP sunucusuna "Hangi araçlarınız var?" diye sorar. Sunucu, "uçuş ara" ve "uçuş rezervasyonu yap" gibi araçlarla yanıt verir.

3. **Araç Çağrısı**: Daha sonra yapay zeka asistanına "Lütfen Portland'dan Honolulu'ya bir uçuş ara" dersiniz. Yapay zeka asistanı, LLM'ini kullanarak "uçuş ara" aracını çağırması gerektiğini belirler ve ilgili parametreleri (kalkış, varış) MCP sunucusuna iletir.

4. **İşlem ve Yanıt**: MCP sunucusu, havayolunun dahili rezervasyon API'sine gerçek çağrıyı yapar. Ardından uçuş bilgilerini (örneğin, JSON verileri) alır ve yapay zeka asistanına geri gönderir.

5. **İleri Etkileşim**: Yapay zeka asistanı uçuş seçeneklerini sunar. Bir uçuş seçtiğinizde, asistan aynı MCP sunucusundaki "uçuş rezervasyonu yap" aracını çağırarak rezervasyonu tamamlayabilir.

## Agent-to-Agent Protocol (A2A)

MCP, LLM'leri araçlara bağlamaya odaklanırken, **Agent-to-Agent (A2A) protokolü** bunu bir adım öteye taşıyarak farklı yapay zeka ajanları arasında iletişim ve iş birliğini mümkün kılar. A2A, farklı organizasyonlar, ortamlar ve teknoloji yığınları arasında yapay zeka ajanlarını bir araya getirerek ortak bir görevi tamamlamalarını sağlar.

A2A'nın bileşenlerini ve faydalarını inceleyeceğiz ve seyahat uygulamamızda nasıl uygulanabileceğine dair bir örnek vereceğiz.

### A2A Temel Bileşenleri

A2A, ajanlar arasında iletişimi mümkün kılmaya ve kullanıcı alt görevlerini tamamlamak için birlikte çalışmalarını sağlamaya odaklanır. Protokolün her bir bileşeni buna katkıda bulunur:

#### Agent Kartı

Bir MCP sunucusunun araç listesini paylaşmasına benzer şekilde, bir Agent Kartı şunlara sahiptir:
    ◦ Ajanın adı.  
    ◦ Tamamladığı genel görevlerin **açıklaması**.  
    ◦ Diğer ajanların (veya insan kullanıcıların) bu ajanı ne zaman ve neden çağırmak isteyeceğini anlamalarına yardımcı olmak için **belirli becerilerin listesi** ve açıklamaları.  
    ◦ Ajanın **mevcut Endpoint URL'si**.  
    ◦ Ajanın **versiyonu** ve **yetenekleri** (örneğin, akış yanıtları ve push bildirimleri).  

#### Agent Executor

Agent Executor, **kullanıcı sohbetinin bağlamını uzak ajana iletmekten** sorumludur. Uzak ajan, tamamlanması gereken görevi anlamak için bu bağlama ihtiyaç duyar. Bir A2A sunucusunda, bir ajan gelen istekleri ayrıştırmak ve kendi dahili araçlarını kullanarak görevleri yerine getirmek için kendi Büyük Dil Modelini (LLM) kullanır.

#### Artifact

Uzak bir ajan talep edilen görevi tamamladıktan sonra, çalışmasının ürünü bir artifact olarak oluşturulur. Artifact, **ajanın çalışmasının sonucunu**, **tamamlanan şeyin açıklamasını** ve **protokol üzerinden gönderilen metin bağlamını** içerir. Artifact gönderildikten sonra, uzak ajanla bağlantı tekrar ihtiyaç duyulana kadar kapatılır.

#### Event Queue

Bu bileşen, **güncellemeleri işlemek ve mesajları iletmek** için kullanılır. Özellikle üretimde, görev tamamlama sürelerinin daha uzun sürebileceği durumlarda, ajanlar arasındaki bağlantının görev tamamlanmadan önce kapanmasını önlemek için önemlidir.

### A2A'nın Faydaları

• **Gelişmiş İş Birliği**: Farklı satıcılar ve platformlardan ajanların etkileşimde bulunmasını, bağlam paylaşmasını ve birlikte çalışmasını sağlar, geleneksel olarak bağlantısız sistemler arasında sorunsuz otomasyonu kolaylaştırır.

• **Model Seçim Esnekliği**: Her A2A ajanı, taleplerini karşılamak için hangi LLM'i kullanacağına karar verebilir, bu da her ajan için optimize edilmiş veya ince ayar yapılmış modellerin kullanılmasına olanak tanır. Bu, bazı MCP senaryolarındaki tek bir LLM bağlantısından farklıdır.

• **Yerleşik Kimlik Doğrulama**: Kimlik doğrulama doğrudan A2A protokolüne entegre edilmiştir, ajan etkileşimleri için sağlam bir güvenlik çerçevesi sağlar.

### A2A Örneği

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.tr.png)

Seyahat rezervasyonu senaryomuzu genişletelim, ancak bu kez A2A kullanarak.

1. **Kullanıcı Talebi Multi-Agent'e**: Bir kullanıcı, "Travel Agent" A2A istemcisi/ajanı ile etkileşime girer ve şöyle der: "Lütfen önümüzdeki hafta için Honolulu'ya bir gezi rezervasyonu yap, uçuşlar, otel ve kiralık araba dahil."

2. **Travel Agent'in Orkestrasyonu**: Travel Agent bu karmaşık talebi alır. Görevi anlamak ve diğer uzman ajanlarla etkileşimde bulunması gerektiğini belirlemek için LLM'ini kullanır.

3. **Ajanlar Arası İletişim**: Travel Agent, A2A protokolünü kullanarak "Havayolu Ajanı", "Otel Ajanı" ve "Araba Kiralama Ajanı" gibi alt ajanlarla bağlantı kurar.

4. **Görevlerin Delege Edilmesi**: Travel Agent, bu uzman ajanlara belirli görevler gönderir (örneğin, "Honolulu'ya uçuş bul", "Otel rezervasyonu yap", "Araba kirala"). Bu uzman ajanların her biri, kendi LLM'lerini çalıştırır ve kendi araçlarını kullanır (bunlar MCP sunucuları da olabilir) ve rezervasyonun belirli bir kısmını gerçekleştirir.

5. **Birleştirilmiş Yanıt**: Tüm alt ajanlar görevlerini tamamladıktan sonra, Travel Agent sonuçları (uçuş detayları, otel onayı, araba kiralama rezervasyonu) derler ve kullanıcıya kapsamlı, sohbet tarzı bir yanıt gönderir.

## Natural Language Web (NLWeb)

Web siteleri, uzun zamandır kullanıcıların internet üzerinden bilgi ve verilere erişmesi için birincil yol olmuştur.

NLWeb'in farklı bileşenlerine, NLWeb'in faydalarına ve seyahat uygulamamıza bakarak NLWeb'in nasıl çalıştığına dair bir örneğe bakalım.

### NLWeb Bileşenleri

- **NLWeb Uygulaması (Çekirdek Hizmet Kodu)**: Doğal dil sorularını işleyen sistemdir. Platformun farklı parçalarını birleştirerek yanıtlar oluşturur. Bunu, bir web sitesinin doğal dil özelliklerini çalıştıran **motor** olarak düşünebilirsiniz.

- **NLWeb Protokolü**: Bir web sitesiyle doğal dil etkileşimi için **temel bir kurallar setidir**. Yanıtları JSON formatında gönderir (genellikle Schema.org kullanarak). Amacı, HTML'in çevrimiçi belgeleri paylaşmayı mümkün kıldığı gibi, "AI Web" için basit bir temel oluşturmaktır.

- **MCP Sunucusu (Model Context Protocol Endpoint)**: Her NLWeb kurulumu aynı zamanda bir **MCP sunucusu** olarak çalışır. Bu, diğer yapay zeka sistemleriyle **araçları (örneğin, bir "sorma" yöntemi) ve verileri** paylaşabileceği anlamına gelir. Pratikte, bu web sitesinin içeriğini ve yeteneklerini yapay zeka ajanları tarafından kullanılabilir hale getirir ve siteyi daha geniş bir "ajan ekosisteminin" parçası haline getirir.

- **Embedding Modelleri**: Bu modeller, web sitesi içeriğini **vektörler** (embedding'ler) adı verilen sayısal temsillere dönüştürmek için kullanılır. Bu vektörler, bilgisayarların anlamı karşılaştırmasını ve aramasını sağlayacak şekilde anlamı yakalar. Özel bir veritabanında saklanır ve kullanıcılar hangi embedding modelini kullanmak istediklerini seçebilir.

- **Vektör Veritabanı (Geri Alma Mekanizması)**: Bu veritabanı, **web sitesi içeriğinin embedding'lerini** saklar. Birisi bir soru sorduğunda, NLWeb vektör veritabanını kontrol ederek en alakalı bilgiyi hızlıca bulur. En benzer olanları sıralayarak hızlı bir yanıt listesi verir. NLWeb, Qdrant, Snowflake, Milvus, Azure AI Search ve Elasticsearch gibi farklı vektör depolama sistemleriyle çalışır.

### NLWeb Örneği

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.tr.png)

Seyahat rezervasyonu web sitemizi tekrar ele alalım, ancak bu kez NLWeb tarafından destekleniyor.

1. **Veri Alımı**: Seyahat web sitesinin mevcut ürün katalogları (örneğin, uçuş listeleri, otel açıklamaları, tur paketleri) Schema.org kullanılarak biçimlendirilir veya RSS beslemeleri aracılığıyla yüklenir. NLWeb'in araçları bu yapılandırılmış veriyi alır, embedding'ler oluşturur ve bunları yerel veya uzak bir vektör veritabanında saklar.

2. **Doğal Dil Sorgusu (İnsan)**: Bir kullanıcı web sitesini ziyaret eder ve menülerde gezinmek yerine bir sohbet arayüzüne şunu yazar: "Honolulu'da havuzlu, aile dostu bir otel bul bana, önümüzdeki hafta için."

3. **NLWeb İşleme**: NLWeb uygulaması bu sorguyu alır. Sorguyu anlamak için bir LLM'e gönderir ve aynı zamanda vektör veritabanında ilgili otel listelerini arar.

4. **Doğru Sonuçlar**: LLM, veritabanından gelen arama sonuçlarını yorumlamaya, "aile dostu", "havuz" ve "Honolulu" kriterlerine göre en iyi eşleşmeleri belirlemeye ve ardından doğal dilde bir yanıt biçimlendirmeye yardımcı olur. Önemli olan, yanıtın web sitesinin katalogundaki gerçek otellere atıfta bulunmasıdır, uydurma bilgilerden kaçınılır.

5. **Yapay Zeka Ajanı Etkileşimi**: NLWeb bir MCP sunucusu olarak hizmet verdiğinden, harici bir yapay zeka seyahat ajanı da bu web sitesinin NLWeb örneğine bağlanabilir. Yapay zeka ajanı, web sitesine doğrudan şu şekilde bir sorgu gönderebilir: `ask("Honolulu bölgesinde otelin önerdiği vegan dostu restoranlar var mı?")`. NLWeb örneği bunu işler, restoran bilgileri (eğer yüklendiyse) veritabanından yararlanarak ve yapılandırılmış bir JSON yanıtı döndürerek yanıt verir.

### MCP/A2A/NLWeb Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenicilerle tanışmak, ofis saatlerine katılmak ve yapay zeka ajanlarıyla ilgili sorularınızı yanıtlamak için [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kanalına katılın.

## Kaynaklar

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)  

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.