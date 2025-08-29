<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T13:13:41+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "tr"
}
-->
[![Nasıl İyi AI Ajanları Tasarlanır](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.tr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanımı Tasarım Deseni

Araçlar ilginçtir çünkü AI ajanlarının daha geniş bir yetenek yelpazesine sahip olmasını sağlar. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek ajan artık çok çeşitli eylemleri gerçekleştirebilir. Bu bölümde, AI ajanlarının hedeflerine ulaşmak için belirli araçları nasıl kullanabileceğini açıklayan Araç Kullanımı Tasarım Deseni'ni inceleyeceğiz.

## Giriş

Bu derste şu sorulara cevap arıyoruz:

- Araç kullanımı tasarım deseni nedir?
- Hangi kullanım durumlarına uygulanabilir?
- Tasarım desenini uygulamak için hangi unsurlar/gerekli yapı taşları vardır?
- Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken nelere dikkat edilmelidir?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Araç Kullanımı Tasarım Deseni'ni ve amacını tanımlamak.
- Araç Kullanımı Tasarım Deseni'nin uygulanabilir olduğu kullanım durumlarını belirlemek.
- Tasarım desenini uygulamak için gerekli temel unsurları anlamak.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirliği sağlamak için dikkat edilmesi gereken hususları tanımak.

## Araç Kullanımı Tasarım Deseni Nedir?

**Araç Kullanımı Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için harici araçlarla etkileşim kurma yeteneği kazandırmaya odaklanır. Araçlar, bir ajanın eylemleri gerçekleştirmek için çalıştırabileceği kodlardır. Bir araç, bir hesap makinesi gibi basit bir fonksiyon ya da hisse senedi fiyatlarını sorgulama veya hava durumu tahmini gibi üçüncü taraf bir hizmete yapılan bir API çağrısı olabilir. AI ajanları bağlamında, araçlar **model tarafından oluşturulan fonksiyon çağrılarına** yanıt olarak çalıştırılmak üzere tasarlanmıştır.

## Hangi kullanım durumlarına uygulanabilir?

AI ajanları, karmaşık görevleri tamamlamak, bilgi almak veya kararlar vermek için araçlardan yararlanabilir. Araç kullanımı tasarım deseni, genellikle veritabanları, web hizmetleri veya kod yorumlayıcılar gibi harici sistemlerle dinamik etkileşim gerektiren senaryolarda kullanılır. Bu yetenek, aşağıdaki gibi çeşitli kullanım durumları için faydalıdır:

- **Dinamik Bilgi Alma:** Ajanlar, güncel verileri almak için harici API'leri veya veritabanlarını sorgulayabilir (örneğin, bir SQLite veritabanını veri analizi için sorgulama, hisse senedi fiyatlarını veya hava durumu bilgilerini alma).
- **Kod Çalıştırma ve Yorumlama:** Ajanlar, matematiksel problemleri çözmek, raporlar oluşturmak veya simülasyonlar yapmak için kod veya betikler çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta hizmetleri veya veri hatları gibi araçları entegre ederek tekrarlayan veya çok adımlı iş akışlarını otomatikleştirme.
- **Müşteri Desteği:** Ajanlar, CRM sistemleri, biletleme platformları veya bilgi tabanlarıyla etkileşim kurarak kullanıcı sorularını çözebilir.
- **İçerik Üretimi ve Düzenleme:** Ajanlar, dilbilgisi denetleyicileri, metin özetleyiciler veya içerik güvenliği değerlendiricileri gibi araçlardan yararlanarak içerik oluşturma görevlerinde yardımcı olabilir.

## Araç Kullanımı Tasarım Deseni'ni uygulamak için gerekli unsurlar/yapı taşları nelerdir?

Bu yapı taşları, AI ajanının çok çeşitli görevleri yerine getirmesini sağlar. Araç Kullanımı Tasarım Deseni'ni uygulamak için gerekli temel unsurlara bakalım:

- **Fonksiyon/Araç Şemaları:** Kullanılabilir araçların detaylı tanımları, fonksiyon adı, amacı, gerekli parametreler ve beklenen çıktılar dahil. Bu şemalar, LLM'nin hangi araçların mevcut olduğunu ve geçerli istekleri nasıl oluşturacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı:** Kullanıcının niyetine ve konuşma bağlamına göre araçların nasıl ve ne zaman çağrılacağını yöneten mantık. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya araç kullanımını dinamik olarak belirleyen koşullu akışları içerebilir.

- **Mesaj İşleme Sistemi:** Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi:** Ajanı, basit fonksiyonlardan karmaşık harici hizmetlere kadar çeşitli araçlara bağlayan altyapı.

- **Hata Yönetimi ve Doğrulama:** Araç çalıştırma hatalarını ele alma, parametreleri doğrulama ve beklenmeyen yanıtları yönetme mekanizmaları.

- **Durum Yönetimi:** Konuşma bağlamını, önceki araç etkileşimlerini ve çok adımlı etkileşimlerde tutarlılığı sağlamak için kalıcı verileri izler.

Şimdi, Fonksiyon/Araç Çağrısını daha ayrıntılı inceleyelim.

### Fonksiyon/Araç Çağrısı

Fonksiyon çağrısı, Büyük Dil Modellerinin (LLM'ler) araçlarla etkileşim kurmasını sağlamanın birincil yoludur. 'Fonksiyon' ve 'Araç' terimlerini genellikle birbirinin yerine kullanıldığını göreceksiniz çünkü 'fonksiyonlar' (yeniden kullanılabilir kod blokları), ajanların görevleri yerine getirmek için kullandığı 'araçlardır'. Bir fonksiyonun kodunun çalıştırılabilmesi için, LLM'nin kullanıcı isteğini fonksiyonun açıklamasıyla karşılaştırması gerekir. Bunun için, mevcut tüm fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM, görev için en uygun fonksiyonu seçer ve adını ve argümanlarını döndürür. Seçilen fonksiyon çalıştırılır, yanıtı LLM'ye geri gönderilir ve bu bilgi kullanıcının isteğine yanıt vermek için kullanılır.

Ajanlar için fonksiyon çağrısını uygulamak isteyen geliştiricilerin şunlara ihtiyacı vardır:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Tanımlanan her fonksiyon için kod

Bir şehirdeki mevcut zamanı almak örneğini kullanalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Tüm modeller fonksiyon çağrısını desteklemez, bu yüzden kullandığınız LLM'nin bunu desteklediğinden emin olmanız önemlidir. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI istemcisini başlatarak başlayabiliriz.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Bir Fonksiyon Şeması Oluşturun:**

    Daha sonra, fonksiyon adını, fonksiyonun ne yaptığının açıklamasını ve fonksiyon parametrelerinin adlarını ve açıklamalarını içeren bir JSON şeması tanımlayacağız. Bu şemayı, daha önce oluşturulan istemciye ve San Francisco'daki zamanı bulma isteğiyle birlikte ileteceğiz. Önemli olan, bir **araç çağrısının** döndürülmesidir, sorunun nihai cevabı değil. Daha önce belirtildiği gibi, LLM görev için seçtiği fonksiyonun adını ve ona iletilecek argümanları döndürür.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Görevi yerine getirmek için gereken fonksiyon kodu:**

    Artık LLM'nin hangi fonksiyonun çalıştırılması gerektiğini seçtiğini biliyoruz, görevi yerine getirecek kodun uygulanması ve çalıştırılması gerekiyor. 
    Python'da mevcut zamanı almak için kodu uygulayabiliriz. Ayrıca, nihai sonucu elde etmek için response_message'dan ad ve argümanları çıkarmak için kod yazmamız gerekecek.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Fonksiyon Çağrısı, çoğu ajan araç kullanımı tasarımının merkezindedir, ancak sıfırdan uygulamak bazen zorlayıcı olabilir. [Ders 2'de](../../../02-explore-agentic-frameworks) öğrendiğimiz gibi, ajan çerçeveleri bize araç kullanımını uygulamak için önceden oluşturulmuş yapı taşları sağlar.

## Ajan Çerçeveleri ile Araç Kullanımı Örnekleri

Farklı ajan çerçevelerini kullanarak Araç Kullanımı Tasarım Deseni'ni nasıl uygulayabileceğinize dair bazı örnekler:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>, Büyük Dil Modelleri (LLM'lerle) çalışan .NET, Python ve Java geliştiricileri için açık kaynaklı bir AI çerçevesidir. Fonksiyon çağrısını kullanmayı, fonksiyonlarınızı ve parametrelerini modele otomatik olarak açıklayan bir süreç olan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serileştirme</a> yoluyla basitleştirir. Ayrıca model ve kodunuz arasındaki iletişimi yönetir. Semantic Kernel gibi bir ajan çerçevesi kullanmanın bir diğer avantajı, <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Dosya Arama</a> ve <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kod Yorumlayıcı</a> gibi önceden oluşturulmuş araçlara erişim sağlamasıdır.

Aşağıdaki diyagram, Semantic Kernel ile fonksiyon çağrısı sürecini göstermektedir:

![fonksiyon çağrısı](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.tr.png)

Semantic Kernel'de fonksiyonlar/araçlar <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Eklentiler</a> olarak adlandırılır. Daha önce gördüğümüz `get_current_time` fonksiyonunu, bir sınıfa dönüştürerek ve fonksiyonu içine koyarak bir eklentiye dönüştürebiliriz. Ayrıca, fonksiyonun açıklamasını alan `kernel_function` dekoratörünü içe aktarabiliriz. GetCurrentTimePlugin ile bir çekirdek oluşturduğunuzda, çekirdek fonksiyonu ve parametrelerini otomatik olarak serileştirir ve bu süreçte LLM'ye gönderilecek şemayı oluşturur.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>, geliştiricilerin yüksek kaliteli ve genişletilebilir AI ajanlarını güvenli bir şekilde oluşturmasını, dağıtmasını ve ölçeklendirmesini sağlamak için tasarlanmış daha yeni bir ajan çerçevesidir. Temel bilgi işlem ve depolama kaynaklarını yönetme gereksinimi olmadan çalışır. Özellikle kurumsal uygulamalar için faydalıdır çünkü tamamen yönetilen bir hizmettir ve kurumsal düzeyde güvenlik sağlar.

LLM API'si ile doğrudan geliştirme ile karşılaştırıldığında, Azure AI Agent Service şu avantajları sunar:

- Otomatik araç çağrısı – bir araç çağrısını ayrıştırmaya, aracı çalıştırmaya ve yanıtı işlemeye gerek yoktur; bunların tümü artık sunucu tarafında yapılır.
- Güvenli bir şekilde yönetilen veri – kendi konuşma durumunuzu yönetmek yerine, ihtiyacınız olan tüm bilgileri saklamak için diyalog geçmişine güvenebilirsiniz.
- Hazır araçlar – Bing, Azure AI Search ve Azure Functions gibi veri kaynaklarınızla etkileşim kurmak için kullanabileceğiniz araçlar.

Azure AI Agent Service'deki araçlar iki kategoriye ayrılabilir:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Arama ile Temellendirme</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI Tanımlı Araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service, bu araçları bir `toolset` olarak birlikte kullanmamıza olanak tanır. Ayrıca, belirli bir konuşmadan gelen mesajların geçmişini takip eden `threads` kullanır.

Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verileriniz hakkında soruları yanıtlayabilecek bir konuşma ajanı geliştirmek istiyorsunuz.

Aşağıdaki görsel, satış verilerinizi analiz etmek için Azure AI Agent Service'i nasıl kullanabileceğinizi göstermektedir:

![Agentic Service Uygulamada](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.tr.jpg)

Bu hizmetle herhangi bir aracı kullanmak için bir istemci oluşturabilir ve bir araç veya araç seti tanımlayabilirsiniz. Bunu pratikte uygulamak için aşağıdaki Python kodunu kullanabiliriz. LLM, araç setine bakarak kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu mu yoksa önceden oluşturulmuş Kod Yorumlayıcıyı mı kullanacağına karar verebilir.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken nelere dikkat edilmelidir?

LLM'ler tarafından dinamik olarak oluşturulan SQL ile ilgili yaygın bir endişe, özellikle SQL enjeksiyonu veya veritabanını düşürme veya değiştirme gibi kötü niyetli eylemler riskidir. Bu endişeler geçerli olsa da, veritabanı erişim izinlerini doğru bir şekilde yapılandırarak etkili bir şekilde azaltılabilir. Çoğu veritabanı için bu, veritabanını salt okunur olarak yapılandırmayı içerir. PostgreSQL veya Azure SQL gibi veritabanı hizmetleri için uygulamaya salt okunur (SELECT) rol atanmalıdır.

Uygulamayı güvenli bir ortamda çalıştırmak, korumayı daha da artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden çıkarılır ve kullanıcı dostu bir şema ile salt okunur bir veritabanına veya veri ambarına dönüştürülür. Bu yaklaşım, verilerin güvenli, performans ve erişilebilirlik için optimize edilmiş olmasını ve uygulamanın sınırlı, salt okunur erişime sahip olmasını sağlar.

### Araç Kullanımı Tasarım Desenleri hakkında daha fazla sorunuz mu var?
[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve AI Agents ile ilgili sorularınıza yanıt alabilirsiniz.

## Ek Kaynaklar

## Önceki Ders

[Agentic Tasarım Kalıplarını Anlamak](../03-agentic-design-patterns/README.md)

## Sonraki Ders

[Agentic RAG](../05-agentic-rag/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.