<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T08:24:25+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "tr"
}
-->
# Agentik Protokolleri Kullanma (MCP, A2A ve NLWeb)

[![Agentik Protokolleri](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.tr.png)](https://youtu.be/X-Dh9R3Opn8)

Yapay zeka ajanlarının kullanımı arttıkça, standartlaşmayı, güvenliği ve açık inovasyonu destekleyen protokollere olan ihtiyaç da artıyor. Bu derste, bu ihtiyacı karşılamayı hedefleyen üç protokolü ele alacağız: Model Bağlam Protokolü (MCP), Ajanlar Arası (A2A) ve Doğal Dil Web (NLWeb).

## Giriş

Bu derste şunları ele alacağız:

• **MCP**'nin, yapay zeka ajanlarının kullanıcı görevlerini tamamlamak için harici araçlara ve verilere erişmesini nasıl sağladığını.

• **A2A**'nın farklı yapay zeka ajanları arasında iletişim ve iş birliğini nasıl mümkün kıldığını.

• **NLWeb**'in, yapay zeka ajanlarının içerikleri keşfetmesini ve etkileşimde bulunmasını sağlayarak herhangi bir web sitesine doğal dil arayüzleri nasıl getirdiğini.

## Öğrenme Hedefleri

• Yapay zeka ajanları bağlamında MCP, A2A ve NLWeb'in temel amacını ve faydalarını **tanımlayın**.

• Her bir protokolün, LLM'ler, araçlar ve diğer ajanlar arasındaki iletişim ve etkileşimi nasıl kolaylaştırdığını **açıklayın**.

• Karmaşık agentik sistemler oluştururken her bir protokolün oynadığı farklı rolleri **tanıyın**.

## Model Bağlam Protokolü

**Model Bağlam Protokolü (MCP)**, uygulamaların LLM'lere bağlam ve araçlar sağlaması için standartlaştırılmış bir yol sunan açık bir standarttır. Bu, yapay zeka ajanlarının farklı veri kaynaklarına ve araçlara tutarlı bir şekilde bağlanmasını sağlayan bir "evrensel adaptör" işlevi görür.

MCP'nin bileşenlerine, doğrudan API kullanımına kıyasla sunduğu avantajlara ve yapay zeka ajanlarının bir MCP sunucusunu nasıl kullanabileceğine dair bir örneğe bakalım.

### MCP Temel Bileşenleri

MCP, bir **istemci-sunucu mimarisi** üzerinde çalışır ve temel bileşenleri şunlardır:

• **Hostlar**, bir MCP Sunucusuna bağlantı başlatan LLM uygulamalarıdır (örneğin, VSCode gibi bir kod editörü).

• **İstemciler**, host uygulama içinde sunucularla bire bir bağlantıları sürdüren bileşenlerdir.

• **Sunucular**, belirli yetenekleri ortaya çıkaran hafif programlardır.

Protokol, bir MCP Sunucusunun yeteneklerini oluşturan üç temel ilkeyi içerir:

• **Araçlar**: Bunlar, bir yapay zeka ajanının bir eylemi gerçekleştirmek için çağırabileceği ayrı eylemler veya işlevlerdir. Örneğin, bir hava durumu servisi "hava durumu al" aracını veya bir e-ticaret sunucusu "ürün satın al" aracını sunabilir. MCP sunucuları, her aracın adını, açıklamasını ve giriş/çıkış şemasını yetenek listelerinde belirtir.

• **Kaynaklar**: Bunlar, bir MCP sunucusunun sağlayabileceği ve istemcilerin talep üzerine alabileceği salt okunur veri öğeleri veya belgelerdir. Örnekler arasında dosya içerikleri, veritabanı kayıtları veya günlük dosyaları bulunur. Kaynaklar metin (kod veya JSON gibi) veya ikili (görseller veya PDF'ler gibi) olabilir.

• **İstemler**: Bunlar, daha karmaşık iş akışlarına olanak tanıyan önerilen istem şablonlarıdır.

### MCP'nin Faydaları

MCP, yapay zeka ajanları için önemli avantajlar sunar:

• **Dinamik Araç Keşfi**: Ajanlar, bir sunucudan mevcut araçların bir listesini ve bunların ne yaptıklarına dair açıklamaları dinamik olarak alabilir. Bu, genellikle entegrasyonlar için statik kodlama gerektiren geleneksel API'lere kıyasla bir avantajdır. MCP, "bir kez entegre et" yaklaşımı sunarak daha fazla uyarlanabilirlik sağlar.

• **LLM'ler Arasında Uyumluluk**: MCP, farklı LLM'ler arasında çalışır ve daha iyi performans için temel modelleri değiştirme esnekliği sağlar.

• **Standartlaştırılmış Güvenlik**: MCP, ek MCP sunucularına erişim eklerken ölçeklenebilirliği artıran standart bir kimlik doğrulama yöntemi içerir. Bu, çeşitli geleneksel API'ler için farklı anahtarları ve kimlik doğrulama türlerini yönetmekten daha basittir.

### MCP Örneği

![MCP Diyagramı](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.tr.png)

Bir kullanıcının MCP destekli bir yapay zeka asistanı kullanarak uçak bileti ayırtmak istediğini hayal edin.

1. **Bağlantı**: Yapay zeka asistanı (MCP istemcisi), bir havayolu tarafından sağlanan bir MCP sunucusuna bağlanır.

2. **Araç Keşfi**: İstemci, havayolunun MCP sunucusuna "Hangi araçlarınız mevcut?" diye sorar. Sunucu, "uçuşları ara" ve "uçuşları ayırt" gibi araçlarla yanıt verir.

3. **Araç Çağrısı**: Daha sonra yapay zeka asistanına, "Lütfen Portland'dan Honolulu'ya bir uçuş ara" dersiniz. Yapay zeka asistanı, LLM'ini kullanarak "uçuşları ara" aracını çağırması gerektiğini belirler ve ilgili parametreleri (kalkış, varış) MCP sunucusuna iletir.

4. **Uygulama ve Yanıt**: MCP sunucusu, havayolunun dahili rezervasyon API'sine gerçek çağrıyı yapar. Daha sonra uçuş bilgilerini (örneğin JSON verisi) alır ve yapay zeka asistanına geri gönderir.

5. **Daha Fazla Etkileşim**: Yapay zeka asistanı uçuş seçeneklerini sunar. Bir uçuş seçtiğinizde, asistan aynı MCP sunucusundaki "uçuşu ayırt" aracını çağırabilir ve rezervasyonu tamamlar.

## Ajanlar Arası Protokol (A2A)

MCP, LLM'leri araçlara bağlamaya odaklanırken, **Ajanlar Arası (A2A) protokolü**, farklı yapay zeka ajanları arasında iletişim ve iş birliğini mümkün kılar. A2A, farklı organizasyonlar, ortamlar ve teknoloji yığınları arasında yapay zeka ajanlarını bağlayarak ortak bir görevi tamamlamalarını sağlar.

A2A'nın bileşenlerini ve faydalarını inceleyecek ve seyahat uygulamamızda nasıl uygulanabileceğine dair bir örnek göreceğiz.

### A2A Temel Bileşenleri

A2A, ajanlar arasında iletişimi sağlama ve onların kullanıcı görevlerinin bir alt görevini tamamlamak için birlikte çalışmalarını sağlama üzerine odaklanır. Protokolün her bir bileşeni buna katkıda bulunur:

#### Ajan Kartı

Bir MCP sunucusunun araç listesini paylaşmasına benzer şekilde, bir Ajan Kartı şunları içerir:
- Ajanın Adı.
- Tamamladığı genel görevlerin bir **açıklaması**.
- Diğer ajanların (veya insan kullanıcıların) bu ajanı ne zaman ve neden çağırmak isteyeceğini anlamalarına yardımcı olmak için **belirli becerilerin bir listesi** ve açıklamaları.
- Ajanın **mevcut Uç Nokta URL'si**.
- Ajanın **sürümü** ve **yetenekleri** (örneğin, akış yanıtları ve anlık bildirimler).

#### Ajan Yürütücüsü

Ajan Yürütücüsü, **kullanıcı sohbet bağlamını uzak ajana iletmekten** sorumludur. Uzak ajan, tamamlanması gereken görevi anlamak için bu bağlama ihtiyaç duyar. Bir A2A sunucusunda, bir ajan gelen istekleri ayrıştırmak ve kendi dahili araçlarını kullanarak görevleri yürütmek için kendi Büyük Dil Modelini (LLM) kullanır.

#### Eser

Bir uzak ajan istenen görevi tamamladıktan sonra, çalışmasının ürünü bir eser olarak oluşturulur. Bir eser, **ajanın çalışmasının sonucunu**, **tamamlanan şeyin bir açıklamasını** ve protokol aracılığıyla gönderilen **metin bağlamını** içerir. Eser gönderildikten sonra, uzak ajanla bağlantı, tekrar ihtiyaç duyulana kadar kapatılır.

#### Olay Kuyruğu

Bu bileşen, **güncellemeleri işlemek ve mesajları iletmek** için kullanılır. Özellikle, görev tamamlama sürelerinin daha uzun sürebileceği durumlarda, üretim ortamlarında ajanik sistemlerde ajanlar arasındaki bağlantının bir görev tamamlanmadan önce kapanmasını önlemek için önemlidir.

### A2A'nın Faydaları

• **Geliştirilmiş İş Birliği**: Farklı satıcılar ve platformlardan ajanların etkileşimde bulunmasını, bağlam paylaşmasını ve birlikte çalışmasını sağlar. Geleneksel olarak bağlantısız sistemler arasında sorunsuz otomasyonu kolaylaştırır.

• **Model Seçim Esnekliği**: Her A2A ajanı, isteklerini yerine getirmek için hangi LLM'i kullanacağına karar verebilir. Bu, bazı MCP senaryolarındaki tek bir LLM bağlantısının aksine, her ajan için optimize edilmiş veya ince ayar yapılmış modellerin kullanılmasına olanak tanır.

• **Entegre Kimlik Doğrulama**: Kimlik doğrulama, A2A protokolüne doğrudan entegre edilmiştir ve ajan etkileşimleri için sağlam bir güvenlik çerçevesi sağlar.

### A2A Örneği

![A2A Diyagramı](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.tr.png)

Seyahat rezervasyonu senaryomuzu genişletelim, ancak bu kez A2A kullanarak.

1. **Kullanıcıdan Çoklu Ajan Talebi**: Bir kullanıcı, "Seyahat Ajanı" A2A istemcisi/ajanıyla etkileşime girer ve "Lütfen önümüzdeki hafta için Honolulu'ya bir uçuş, bir otel ve bir kiralık araba içeren bir gezi ayarla" der.

2. **Seyahat Ajanı Tarafından Düzenleme**: Seyahat Ajanı bu karmaşık isteği alır. Görevi anlamak ve diğer uzman ajanlarla etkileşim kurması gerektiğine karar vermek için LLM'ini kullanır.

3. **Ajanlar Arası İletişim**: Seyahat Ajanı, A2A protokolünü kullanarak, farklı şirketler tarafından oluşturulan bir "Havayolu Ajanı," bir "Otel Ajanı" ve bir "Araç Kiralama Ajanı" gibi alt ajanlarla bağlantı kurar.

4. **Görevlerin Delege Edilmesi**: Seyahat Ajanı, bu uzman ajanlara belirli görevler gönderir (örneğin, "Honolulu'ya uçuş bul," "Bir otel ayırt," "Bir araba kirala"). Bu uzman ajanların her biri, kendi LLM'lerini çalıştırır ve kendi araçlarını kullanır (bunlar MCP sunucuları olabilir).

5. **Birleştirilmiş Yanıt**: Tüm alt ajanlar görevlerini tamamladıktan sonra, Seyahat Ajanı sonuçları (uçuş detayları, otel onayı, araç kiralama rezervasyonu) derler ve kullanıcıya kapsamlı, sohbet tarzı bir yanıt gönderir.

## Doğal Dil Web (NLWeb)

Web siteleri, uzun zamandır kullanıcıların internet üzerinden bilgi ve verilere erişmesinin birincil yolu olmuştur.

NLWeb'in farklı bileşenlerine, NLWeb'in faydalarına ve seyahat uygulamamıza bakarak NLWeb'in nasıl çalıştığına dair bir örneğe göz atalım.

### NLWeb Bileşenleri

- **NLWeb Uygulaması (Çekirdek Hizmet Kodu)**: Doğal dil sorularını işleyen sistemdir. Platformun farklı bölümlerini bağlayarak yanıtlar oluşturur. Bunu, bir web sitesinin doğal dil özelliklerini çalıştıran **motor** olarak düşünebilirsiniz.

- **NLWeb Protokolü**: Bir web sitesiyle doğal dil etkileşimi için **temel bir kurallar setidir**. Yanıtları JSON formatında gönderir (genellikle Schema.org kullanarak). Amacı, "AI Web" için basit bir temel oluşturmaktır; tıpkı HTML'nin çevrimiçi belgeleri paylaşmayı mümkün kıldığı gibi.

- **MCP Sunucusu (Model Bağlam Protokolü Uç Noktası)**: Her NLWeb kurulumu aynı zamanda bir **MCP sunucusu** olarak çalışır. Bu, **araçları (örneğin, bir "sor" yöntemi) ve verileri** diğer yapay zeka sistemleriyle paylaşabileceği anlamına gelir. Pratikte, bu, web sitesinin içeriğini ve yeteneklerini yapay zeka ajanları tarafından kullanılabilir hale getirir ve siteyi daha geniş bir "ajan ekosisteminin" parçası yapar.

- **Gömme Modelleri**: Bu modeller, **web sitesi içeriğini vektör adı verilen sayısal temsillere dönüştürmek** için kullanılır. Bu vektörler, bilgisayarların anlamı karşılaştırmasını ve aramasını sağlayacak şekilde anlamı yakalar. Bunlar özel bir veritabanında saklanır ve kullanıcılar hangi gömme modelini kullanacaklarını seçebilir.

- **Vektör Veritabanı (Geri Alma Mekanizması)**: Bu veritabanı, **web sitesi içeriğinin gömmelerini saklar**. Birisi bir soru sorduğunda, NLWeb vektör veritabanını kontrol ederek en alakalı bilgiyi hızlıca bulur. En olası yanıtların bir listesini, benzerlik sırasına göre sıralanmış şekilde verir. NLWeb, Qdrant, Snowflake, Milvus, Azure AI Search ve Elasticsearch gibi farklı vektör depolama sistemleriyle çalışır.

### NLWeb Örneği

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.tr.png)

Seyahat rezervasyonu web sitemizi tekrar ele alalım, ancak bu kez NLWeb tarafından destekleniyor.

1. **Veri Alımı**: Seyahat web sitesinin mevcut ürün katalogları (örneğin, uçuş listeleri, otel açıklamaları, tur paketleri), Schema.org kullanılarak biçimlendirilir veya RSS beslemeleri aracılığıyla yüklenir. NLWeb'in araçları bu yapılandırılmış verileri alır, gömmeler oluşturur ve bunları yerel veya uzak bir vektör veritabanında saklar.

2. **Doğal Dil Sorgusu (İnsan)**: Bir kullanıcı web sitesini ziyaret eder ve menülerde gezinmek yerine bir sohbet arayüzüne şunu yazar: "Honolulu'da havuzlu, aile dostu bir otel bul."

3. **NLWeb İşleme**: NLWeb uygulaması bu sorguyu alır. Sorguyu anlamak için bir LLM'e gönderir ve aynı anda vektör veritabanında ilgili otel listelerini arar.

4. **Doğru Sonuçlar**: LLM, veritabanından gelen arama sonuçlarını yorumlamaya, "aile dostu," "havuz" ve "Honolulu" kriterlerine göre en iyi eşleşmeleri belirlemeye yardımcı olur ve ardından doğal dilde bir yanıt oluşturur. Yanıt, web sitesinin kataloğundaki gerçek otellere atıfta bulunur ve uydurma bilgilerden kaçınır.

5. **Yapay Zeka Ajanı Etkileşimi**: NLWeb bir MCP sunucusu olarak hizmet verdiğinden, harici bir yapay zeka seyahat ajanı da bu web sitesinin NLWeb örneğine bağlanabilir. Yapay zeka ajanı, web sitesine doğrudan şu şekilde sorgu gönderebilir: `ask("Otelin önerdiği Honolulu bölgesindeki vegan dostu restoranlar var mı?")`. NLWeb örneği bunu işler, restoran bilgileri (eğer yüklüyse) veritabanından alır ve yapılandırılmış bir JSON yanıtı döndürür.

### MCP/A2A/NLWeb Hakkında Daha Fazla Sorunuz mu Var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kanalına katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve yapay zeka ajanlarıyla ilgili sorularınıza yanıt alabilirsiniz.

## Kaynaklar

- [MCP'ye Yeni Başlayanlar için](https://aka.ms/mcp-for-beginners)  
- [MCP Dokümantasyonu](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Deposu](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Kılavuzları](https://learn.microsoft.com/semantic-kernel/)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yorumlamalardan sorumlu değiliz.