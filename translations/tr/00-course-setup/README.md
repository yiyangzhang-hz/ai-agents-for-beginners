<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:42:07+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tr"
}
-->
# Kurs Kurulumu

## Giriş

Bu derste, kursun kod örneklerini nasıl çalıştıracağınızı öğreneceksiniz.

## Bu Depoyu Klonlayın veya Çatallayın

Başlamak için lütfen GitHub Deposunu klonlayın veya çatallayın. Bu, kurs materyallerinin kendi versiyonunu oluşturmanızı sağlar, böylece kodu çalıştırabilir, test edebilir ve üzerinde değişiklik yapabilirsiniz!

Bunu yapmak için bağlantıya tıklayabilirsiniz:

![Çatallanmış Depo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.tr.png)

## Kodu Çalıştırma

Bu kurs, yapay zeka ajanları oluşturmayı deneyimlemeniz için çalıştırabileceğiniz bir dizi Jupyter Notebook sunar.

Kod örnekleri şu araçları kullanır:

**GitHub Hesabı Gerektirir - Ücretsiz**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. (semantic-kernel.ipynb olarak etiketlenmiştir)
2) AutoGen Framework + GitHub Models Marketplace. (autogen.ipynb olarak etiketlenmiştir)

**Azure Aboneliği Gerektirir**:
3) Azure AI Foundry + Azure AI Agent Service. (azureaiagent.ipynb olarak etiketlenmiştir)

Hangi seçeneği tercih ederseniz edin, aşağıdaki kurulum adımlarını takip etmeniz gerekecek:

## Gereksinimler

- Python 3.12+
  - **NOT**: Python 3.12 yüklü değilse, yüklediğinizden emin olun. Daha sonra requirements.txt dosyasından doğru sürümlerin yüklendiğinden emin olmak için python3.12 kullanarak sanal bir ortam oluşturun.
- GitHub Hesabı - GitHub Models Marketplace'e erişim için
- Azure Aboneliği - Azure AI Foundry'e erişim için
- Azure AI Foundry Hesabı - Azure AI Agent Service'e erişim için

Bu depoda, kod örneklerini çalıştırmak için gerekli tüm Python paketlerini içeren bir `requirements.txt` dosyası bulunmaktadır.

Bu paketleri, terminalinizde depo kök dizininde aşağıdaki komutu çalıştırarak yükleyebilirsiniz:

```bash
pip install -r requirements.txt
```
Herhangi bir çakışma ve sorun yaşamamak için bir Python sanal ortamı oluşturmanızı öneririz.

## VSCode Kurulumu
VSCode'da doğru Python sürümünü kullandığınızdan emin olun.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## GitHub Modellerini Kullanarak Örnekler için Kurulum 

### Adım 1: GitHub Kişisel Erişim Jetonunuzu (PAT) Alın

Bu kurs, GitHub Models Marketplace'i kullanır ve bu, yapay zeka ajanları oluşturmak için kullanacağınız Büyük Dil Modellerine (LLM'ler) ücretsiz erişim sağlar.

GitHub Modellerini kullanmak için bir [GitHub Kişisel Erişim Jetonu](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) oluşturmanız gerekecek.

Bunu GitHub hesabınızda yapabilirsiniz.

Lütfen jeton oluştururken [En Az Ayrıcalık İlkesi](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ilkesini izleyin. Bu, jetona yalnızca bu kurstaki kod örneklerini çalıştırmak için gereken izinleri vermeniz gerektiği anlamına gelir.

1. Ekranınızın sol tarafında `Fine-grained tokens` seçeneğini seçin.

    Ardından `Generate new token` seçeneğini seçin.

    ![Jeton Oluştur](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.tr.png)

1. Jetonunuz için amacını yansıtan açıklayıcı bir ad girin, böylece daha sonra kolayca tanımlayabilirsiniz. Bir son kullanma tarihi belirleyin (önerilen: 30 gün; daha güvenli bir yaklaşım için 7 gün gibi daha kısa bir süre seçebilirsiniz).

    ![Jeton Adı ve Son Kullanma Tarihi](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.tr.png)

1. Jetonun kapsamını bu deponun çatallanmış versiyonuyla sınırlayın.

    ![Kapsamı Çatallanmış Depoyla Sınırlayın](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.tr.png)

1. Jetonun izinlerini kısıtlayın: **Permissions** altında, **Account Permissions**'ı açın, **Models**'a gidin ve yalnızca GitHub Modelleri için gereken okuma erişimini etkinleştirin.

    ![Hesap İzinleri](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.tr.png)

    ![Modeller Okuma Erişimi](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.tr.png)

Yeni oluşturduğunuz jetonu kopyalayın. Şimdi bu jetonu, bu kursa dahil edilen `.env` dosyanıza ekleyeceksiniz.

### Adım 2: `.env` Dosyanızı Oluşturun

`.env` dosyanızı oluşturmak için terminalinizde aşağıdaki komutu çalıştırın.

```bash
cp .env.example .env
```

Bu, örnek dosyayı kopyalayacak ve dizininizde bir `.env` dosyası oluşturacaktır. Bu dosyada ortam değişkenleri için değerleri doldurabilirsiniz.

Kopyaladığınız jetonla, favori metin düzenleyicinizi kullanarak `.env` dosyasını açın ve jetonunuzu `GITHUB_TOKEN` alanına yapıştırın.

Artık bu kursun kod örneklerini çalıştırabilirsiniz.

## Azure AI Foundry ve Azure AI Agent Service Kullanarak Örnekler için Kurulum

### Adım 1: Azure Proje Uç Noktanızı Alın

Azure AI Foundry'de bir hub ve proje oluşturma adımlarını buradan takip edin: [Hub kaynaklarına genel bakış](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Projenizi oluşturduktan sonra, projeniz için bağlantı dizesini almanız gerekecek.

Bu, Azure AI Foundry portalındaki projenizin **Genel Bakış** sayfasına giderek yapılabilir.

![Proje Bağlantı Dizesi](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.tr.png)

### Adım 2: `.env` Dosyanızı Oluşturun

`.env` dosyanızı oluşturmak için terminalinizde aşağıdaki komutu çalıştırın.

```bash
cp .env.example .env
```

Bu, örnek dosyayı kopyalayacak ve dizininizde bir `.env` dosyası oluşturacaktır. Bu dosyada ortam değişkenleri için değerleri doldurabilirsiniz.

Kopyaladığınız jetonla, favori metin düzenleyicinizi kullanarak `.env` dosyasını açın ve jetonunuzu `PROJECT_ENDPOINT` alanına yapıştırın.

### Adım 3: Azure'a Giriş Yapın

Bir güvenlik en iyi uygulaması olarak, Microsoft Entra ID ile Azure OpenAI'ye [anahtarsız kimlik doğrulama](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) kullanacağız.

Sonraki adımda, bir terminal açın ve Azure hesabınıza giriş yapmak için `az login --use-device-code` komutunu çalıştırın.

Giriş yaptıktan sonra, terminalde aboneliğinizi seçin.

## Ek Ortam Değişkenleri - Azure Search ve Azure OpenAI 

Agentic RAG Dersi - Ders 5 - için Azure Search ve Azure OpenAI kullanan örnekler bulunmaktadır.

Bu örnekleri çalıştırmak istiyorsanız, `.env` dosyanıza aşağıdaki ortam değişkenlerini eklemeniz gerekecek:

### Genel Bakış Sayfası (Proje)

- `AZURE_SUBSCRIPTION_ID` - Projenizin **Genel Bakış** sayfasındaki **Proje detayları** bölümünü kontrol edin.

- `AZURE_AI_PROJECT_NAME` - Projenizin **Genel Bakış** sayfasının üst kısmına bakın.

- `AZURE_OPENAI_SERVICE` - **Genel Bakış** sayfasındaki **Dahil edilen yetenekler** sekmesinde **Azure OpenAI Service**'i bulun.

### Yönetim Merkezi

- `AZURE_OPENAI_RESOURCE_GROUP` - **Yönetim Merkezi**'nin **Genel Bakış** sayfasındaki **Proje özellikleri** bölümüne gidin.

- `GLOBAL_LLM_SERVICE` - **Bağlı kaynaklar** altında **Azure AI Services** bağlantı adını bulun. Listelenmemişse, kaynak grubunuzdaki AI Services kaynak adını kontrol etmek için **Azure portalı**na bakın.

### Modeller + Uç Noktalar Sayfası

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Gömme modelinizi seçin (ör. `text-embedding-ada-002`) ve model detaylarından **Dağıtım adını** not edin.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Sohbet modelinizi seçin (ör. `gpt-4o-mini`) ve model detaylarından **Dağıtım adını** not edin.

### Azure Portalı

- `AZURE_OPENAI_ENDPOINT` - **Azure AI hizmetleri**ni bulun, üzerine tıklayın, ardından **Kaynak Yönetimi**, **Anahtarlar ve Uç Nokta**ya gidin, "Azure OpenAI uç noktaları"na kadar aşağı kaydırın ve "Dil API'leri" yazanını kopyalayın.

- `AZURE_OPENAI_API_KEY` - Aynı ekrandan, ANAHTAR 1 veya ANAHTAR 2'yi kopyalayın.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - **Azure AI Search** kaynağınızı bulun, üzerine tıklayın ve **Genel Bakış** bölümünü kontrol edin.

- `AZURE_SEARCH_API_KEY` - Ardından **Ayarlar** ve ardından **Anahtarlar**a giderek birincil veya ikincil yönetici anahtarını kopyalayın.

### Harici Web Sayfası

- `AZURE_OPENAI_API_VERSION` - [API sürüm yaşam döngüsü](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sayfasını **En Son GA API sürümü** altında ziyaret edin.

### Anahtarsız Kimlik Doğrulama Kurulumu

Kimlik bilgilerinizi kodda sabitlemek yerine, Azure OpenAI ile anahtarsız bir bağlantı kullanacağız. Bunu yapmak için, `DefaultAzureCredential`'ı içe aktaracağız ve daha sonra kimlik bilgilerini almak için `DefaultAzureCredential` fonksiyonunu çağıracağız.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bir Yerde Takıldınız mı?

Bu kurulumu çalıştırırken herhangi bir sorun yaşarsanız, bizimle iletişime geçebilirsiniz.

## Sonraki Ders

Artık bu kursun kodlarını çalıştırmaya hazırsınız. Yapay zeka ajanları dünyası hakkında daha fazla şey öğrenirken iyi eğlenceler!

[AI Ajanlarına Giriş ve Ajan Kullanım Durumları](../01-intro-to-ai-agents/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.