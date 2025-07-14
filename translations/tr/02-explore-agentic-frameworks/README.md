<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:02:20+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "tr"
}
-->
. Wikipedia'ya göre, bir aktör _eşzamanlı hesaplamanın temel yapı taşıdır. Aldığı bir mesaja yanıt olarak, bir aktör: yerel kararlar verebilir, daha fazla aktör oluşturabilir, daha fazla mesaj gönderebilir ve alınan sonraki mesaja nasıl yanıt vereceğini belirleyebilir_.

**Kullanım Alanları**: Kod üretimini otomatikleştirme, veri analizi görevleri ve planlama ile araştırma işlevleri için özel ajanlar oluşturma.

AutoGen'in bazı önemli temel kavramları şunlardır:

- **Ajanlar**. Bir ajan, şu özelliklere sahip bir yazılım varlığıdır:
  - **Mesajlar aracılığıyla iletişim kurar**, bu mesajlar senkron veya asenkron olabilir.
  - **Kendi durumunu korur**, bu durum gelen mesajlarla değiştirilebilir.
  - **Alınan mesajlara veya durumundaki değişikliklere yanıt olarak eylemler gerçekleştirir**. Bu eylemler ajanın durumunu değiştirebilir ve mesaj kayıtlarını güncelleme, yeni mesajlar gönderme, kod yürütme veya API çağrıları yapma gibi dış etkiler oluşturabilir.
    
  İşte Chat yeteneklerine sahip kendi ajanınızı oluşturduğunuz kısa bir kod örneği:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Önceki kodda, `MyAssistant` oluşturulmuş ve `RoutedAgent` sınıfından türetilmiştir. Mesaj içeriğini yazdıran ve ardından `AssistantAgent` delege kullanarak yanıt gönderen bir mesaj işleyicisi vardır. Özellikle, sohbet tamamlamalarını işleyebilen önceden oluşturulmuş bir ajan olan `AssistantAgent` örneğini `self._delegate`'e nasıl atadığımıza dikkat edin.

    Şimdi AutoGen'e bu ajan türünü bildirelim ve programı başlatalım:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Önceki kodda ajanlar çalışma zamanına kaydedilir ve ardından ajana bir mesaj gönderilir; bu da aşağıdaki çıktıyı üretir:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Çoklu ajanlar**. AutoGen, karmaşık görevleri başarmak için birlikte çalışabilen birden fazla ajan oluşturmayı destekler. Ajanlar iletişim kurabilir, bilgi paylaşabilir ve eylemlerini koordine ederek sorunları daha verimli çözebilir. Çoklu ajan sistemi oluşturmak için veri alma, analiz, karar verme ve kullanıcı etkileşimi gibi özel işlevlere ve rollere sahip farklı ajan türleri tanımlayabilirsiniz. Böyle bir oluşturmanın nasıl göründüğüne bakalım:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Önceki kodda, çalışma zamanına kaydedilen bir `GroupChatManager` vardır. Bu yönetici, yazarlar, illüstratörler, editörler ve kullanıcılar gibi farklı ajan türleri arasındaki etkileşimleri koordine etmekten sorumludur.

- **Ajan Çalışma Zamanı**. Çerçeve, ajanlar arasında iletişimi sağlayan, kimliklerini ve yaşam döngülerini yöneten ve güvenlik ile gizlilik sınırlarını uygulayan bir çalışma zamanı ortamı sunar. Bu, ajanlarınızı güvenli ve kontrollü bir ortamda çalıştırabileceğiniz anlamına gelir; böylece güvenli ve verimli etkileşim kurabilirler. İlgili iki çalışma zamanı vardır:
  - **Bağımsız çalışma zamanı**. Tüm ajanların aynı programlama dilinde uygulandığı ve aynı işlemde çalıştığı tek işlemli uygulamalar için iyi bir seçenektir. İşte nasıl çalıştığına dair bir görsel:

Uygulama yığını

    *ajanlar çalışma zamanı aracılığıyla mesajlarla iletişim kurar ve çalışma zamanı ajanların yaşam döngüsünü yönetir*

  - **Dağıtık ajan çalışma zamanı**, ajanların farklı programlama dillerinde uygulanabileceği ve farklı makinelerde çalışabileceği çok işlemli uygulamalar için uygundur. İşte nasıl çalıştığına dair bir görsel:

## Semantic Kernel + Ajan Çerçevesi

Semantic Kernel, kurumsal kullanıma hazır bir AI Orkestrasyon SDK'sıdır. AI ve bellek bağlayıcıları ile birlikte bir Ajan Çerçevesi içerir.

Öncelikle bazı temel bileşenlere bakalım:

- **AI Bağlayıcıları**: Hem Python hem de C# için dış AI hizmetleri ve veri kaynaklarıyla arayüz sağlar.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Burada, bir kernel oluşturup bir sohbet tamamlama servisi eklediğiniz basit bir örnek var. Semantic Kernel, bu durumda Azure OpenAI Chat Completion olmak üzere dış bir AI servisine bağlantı kurar.

- **Eklentiler (Plugins)**: Bir uygulamanın kullanabileceği işlevleri kapsüller. Hem hazır eklentiler hem de oluşturabileceğiniz özel eklentiler vardır. İlgili bir kavram "prompt fonksiyonlarıdır." Fonksiyon çağrısı için doğal dil ipuçları vermek yerine, belirli fonksiyonları modele yayınlarsınız. Mevcut sohbet bağlamına bağlı olarak model, bir isteği veya sorguyu tamamlamak için bu fonksiyonlardan birini çağırmayı seçebilir. İşte bir örnek:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Burada önce kullanıcıdan metin girişi için yer bırakan `skPrompt` adlı bir şablon prompt var, `$userInput`. Sonra `SummarizeText` adlı kernel fonksiyonunu oluşturup `SemanticFunctions` eklenti adıyla kernela aktarıyorsunuz. Semantic Kernel'in fonksiyonun ne yaptığını ve ne zaman çağrılması gerektiğini anlamasına yardımcı olan fonksiyon adına dikkat edin.

- **Yerel fonksiyon (Native function)**: Çerçeve tarafından doğrudan çağrılabilen yerel fonksiyonlar da vardır. İşte bir dosyadan içerik alan böyle bir fonksiyon örneği:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Bellek (Memory)**: AI uygulamaları için bağlam yönetimini soyutlar ve basitleştirir. Belleğin amacı, LLM'nin bilmesi gereken bilgileri depolamaktır. Bu bilgileri, genellikle bir bellek içi veritabanı, vektör veritabanı veya benzeri olan bir vektör deposunda saklayabilirsiniz. İşte *gerçekler* bellek koleksiyonuna eklendiği çok basitleştirilmiş bir senaryo örneği:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    Bu gerçekler daha sonra `SummarizedAzureDocs` adlı bellek koleksiyonunda saklanır. Bu çok basit bir örnek, ancak LLM'nin kullanması için bilgiyi bellekte nasıl depolayabileceğinizi görebilirsiniz.
## Önceki Ders

[AI Ajanlarına ve Ajan Kullanım Senaryolarına Giriş](../01-intro-to-ai-agents/README.md)

## Sonraki Ders

[Ajan Tasarım Desenlerini Anlamak](../03-agentic-design-patterns/README.md)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.