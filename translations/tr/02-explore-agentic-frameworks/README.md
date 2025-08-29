<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-29T13:17:58+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "tr"
}
-->
[![Yapay Zeka Ajanı Çerçevelerini Keşfetmek](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.tr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Yapay Zeka Ajanı Çerçevelerini Keşfetmek

Yapay zeka ajanı çerçeveleri, yapay zeka ajanlarının oluşturulmasını, dağıtılmasını ve yönetilmesini kolaylaştırmak için tasarlanmış yazılım platformlarıdır. Bu çerçeveler, geliştiricilere karmaşık yapay zeka sistemlerinin geliştirilmesini kolaylaştıran önceden oluşturulmuş bileşenler, soyutlamalar ve araçlar sunar.

Bu çerçeveler, yapay zeka ajanı geliştirmedeki yaygın zorluklara standart yaklaşımlar sunarak geliştiricilerin uygulamalarının benzersiz yönlerine odaklanmalarına yardımcı olur. Ayrıca, yapay zeka sistemlerinin ölçeklenebilirliğini, erişilebilirliğini ve verimliliğini artırır.

## Giriş 

Bu derste şunlar ele alınacaktır:

- Yapay Zeka Ajanı Çerçeveleri nedir ve geliştiricilere neler sağlar?
- Takımlar bu çerçeveleri kullanarak ajanlarının yeteneklerini hızlıca nasıl prototipleyebilir, yineleyebilir ve geliştirebilir?
- Microsoft tarafından oluşturulan çerçeve ve araçlar arasındaki farklar nelerdir?
- Mevcut Azure ekosistemi araçlarımı doğrudan entegre edebilir miyim, yoksa bağımsız çözümler mi kullanmam gerekir?
- Azure AI Agents hizmeti nedir ve bana nasıl yardımcı olur?

## Öğrenme Hedefleri

Bu dersin hedefleri şunlardır:

- Yapay Zeka Ajanı Çerçevelerinin yapay zeka geliştirmedeki rolünü anlamak.
- Yapay Zeka Ajanı Çerçevelerini kullanarak akıllı ajanlar oluşturmayı öğrenmek.
- Yapay Zeka Ajanı Çerçevelerinin sağladığı temel yetenekleri anlamak.
- AutoGen, Semantic Kernel ve Azure AI Agent Service arasındaki farkları öğrenmek.

## Yapay Zeka Ajanı Çerçeveleri nedir ve geliştiricilere neler sağlar?

Geleneksel yapay zeka çerçeveleri, yapay zekayı uygulamalarınıza entegre etmenize ve bu uygulamaları şu şekillerde geliştirmenize yardımcı olabilir:

- **Kişiselleştirme**: Yapay zeka, kullanıcı davranışlarını ve tercihlerini analiz ederek kişiselleştirilmiş öneriler, içerikler ve deneyimler sunabilir.
Örnek: Netflix gibi yayın hizmetleri, izleme geçmişine dayalı olarak film ve dizi önerileri sunarak kullanıcı etkileşimini ve memnuniyetini artırır.
- **Otomasyon ve Verimlilik**: Yapay zeka, tekrarlayan görevleri otomatikleştirebilir, iş akışlarını kolaylaştırabilir ve operasyonel verimliliği artırabilir.
Örnek: Müşteri hizmeti uygulamaları, yaygın soruları yanıtlamak için yapay zeka destekli sohbet botlarını kullanarak yanıt sürelerini kısaltır ve insan temsilcilerin daha karmaşık sorunlara odaklanmasını sağlar.
- **Geliştirilmiş Kullanıcı Deneyimi**: Yapay zeka, ses tanıma, doğal dil işleme ve tahminli metin gibi akıllı özellikler sunarak genel kullanıcı deneyimini iyileştirebilir.
Örnek: Siri ve Google Asistan gibi sanal asistanlar, sesli komutları anlayıp yanıtlayarak kullanıcıların cihazlarıyla daha kolay etkileşim kurmasını sağlar.

### Bunların hepsi harika görünüyor, peki neden Yapay Zeka Ajanı Çerçevesine ihtiyacımız var?

Yapay Zeka Ajanı çerçeveleri, yalnızca yapay zeka çerçevelerinden daha fazlasını temsil eder. Kullanıcılarla, diğer ajanlarla ve çevreyle etkileşim kurarak belirli hedeflere ulaşabilen akıllı ajanların oluşturulmasını sağlarlar. Bu ajanlar, otonom davranışlar sergileyebilir, kararlar alabilir ve değişen koşullara uyum sağlayabilir. İşte Yapay Zeka Ajanı Çerçevelerinin sağladığı bazı temel yetenekler:

- **Ajan İşbirliği ve Koordinasyonu**: Birlikte çalışabilen, iletişim kurabilen ve karmaşık görevleri çözmek için koordinasyon sağlayabilen birden fazla yapay zeka ajanı oluşturmayı mümkün kılar.
- **Görev Otomasyonu ve Yönetimi**: Çok adımlı iş akışlarını otomatikleştirmek, görevleri devretmek ve ajanlar arasında dinamik görev yönetimi sağlamak için mekanizmalar sunar.
- **Bağlamsal Anlama ve Uyum**: Ajanlara bağlamı anlama, değişen ortamlara uyum sağlama ve gerçek zamanlı bilgilere dayanarak kararlar alma yeteneği kazandırır.

Özetle, ajanlar daha fazlasını yapmanıza, otomasyonu bir sonraki seviyeye taşımanıza ve çevresinden öğrenip uyum sağlayabilen daha akıllı sistemler oluşturmanıza olanak tanır.

## Ajanın Yeteneklerini Hızlıca Prototiplemek, Yinelemek ve Geliştirmek Nasıl Mümkün?

Bu hızla değişen bir alan, ancak çoğu Yapay Zeka Ajanı Çerçevesinde ortak olan bazı unsurlar, hızlı prototipleme ve yineleme yapmanıza yardımcı olabilir: modüler bileşenler, işbirliği araçları ve gerçek zamanlı öğrenme. Bunları biraz daha detaylandıralım:

- **Modüler Bileşenler Kullanın**: Yapay zeka SDK'ları, yapay zeka ve bellek bağlayıcıları, doğal dil veya kod eklentileri kullanarak işlev çağırma, istem şablonları ve daha fazlası gibi önceden oluşturulmuş bileşenler sunar.
- **İşbirliği Araçlarından Yararlanın**: Belirli rollere ve görevlere sahip ajanlar tasarlayarak işbirlikçi iş akışlarını test edin ve geliştirin.
- **Gerçek Zamanlı Öğrenin**: Ajanların etkileşimlerden öğrenip davranışlarını dinamik olarak ayarladığı geri bildirim döngüleri uygulayın.

### Modüler Bileşenler Kullanın

Microsoft Semantic Kernel ve LangChain gibi SDK'lar, yapay zeka bağlayıcıları, istem şablonları ve bellek yönetimi gibi önceden oluşturulmuş bileşenler sunar.

**Takımlar bunu nasıl kullanabilir**: Takımlar, sıfırdan başlamadan işlevsel bir prototip oluşturmak için bu bileşenleri hızla bir araya getirebilir, bu da hızlı deney ve yineleme yapmalarını sağlar.

**Pratikte nasıl çalışır**: Kullanıcı girdisinden bilgi çıkarmak için önceden oluşturulmuş bir ayrıştırıcı, veri depolamak ve geri çağırmak için bir bellek modülü ve kullanıcılarla etkileşim kurmak için bir istem oluşturucu kullanabilirsiniz; bunların hiçbirini sıfırdan oluşturmanıza gerek kalmaz.

**Örnek kod**. İşte Semantic Kernel Python ve .Net ile önceden oluşturulmuş bir Yapay Zeka Bağlayıcısını kullanarak modelin kullanıcı girdisine yanıt vermesini sağlayan otomatik işlev çağırma örnekleri:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Bu örnekten, kullanıcı girdisinden (örneğin, bir uçuş rezervasyon isteğinin çıkış noktası, varış noktası ve tarihi gibi) önemli bilgileri çıkarmak için önceden oluşturulmuş bir ayrıştırıcıyı nasıl kullanabileceğinizi görebilirsiniz. Bu modüler yaklaşım, yüksek seviyeli mantığa odaklanmanıza olanak tanır.

### İşbirliği Araçlarından Yararlanın

CrewAI, Microsoft AutoGen ve Semantic Kernel gibi çerçeveler, birlikte çalışabilen birden fazla ajan oluşturmayı kolaylaştırır.

**Takımlar bunu nasıl kullanabilir**: Takımlar, belirli rollere ve görevlere sahip ajanlar tasarlayarak işbirlikçi iş akışlarını test edebilir ve genel sistem verimliliğini artırabilir.

**Pratikte nasıl çalışır**: Veri alma, analiz veya karar verme gibi özel bir işlevi olan bir ajan ekibi oluşturabilirsiniz. Bu ajanlar, bir kullanıcı sorgusuna yanıt verme veya bir görevi tamamlama gibi ortak bir hedefe ulaşmak için iletişim kurabilir ve bilgi paylaşabilir.

**Örnek kod (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Yukarıdaki kodda, birden fazla ajanın birlikte çalışarak veri analizini içeren bir görevi nasıl gerçekleştirdiğini görebilirsiniz. Her ajan belirli bir işlevi yerine getirir ve görev, istenen sonuca ulaşmak için ajanların koordinasyonu ile yürütülür. Özel rollere sahip ajanlar oluşturarak görev verimliliğini ve performansını artırabilirsiniz.

### Gerçek Zamanlı Öğrenin

Gelişmiş çerçeveler, gerçek zamanlı bağlam anlama ve uyum sağlama yetenekleri sunar.

**Takımlar bunu nasıl kullanabilir**: Takımlar, ajanların etkileşimlerden öğrenip davranışlarını dinamik olarak ayarladığı geri bildirim döngüleri uygulayabilir. Bu, ajanların yeteneklerinin sürekli iyileştirilmesine ve geliştirilmesine yol açar.

**Pratikte nasıl çalışır**: Ajanlar, kullanıcı geri bildirimlerini, çevresel verileri ve görev sonuçlarını analiz ederek bilgi tabanlarını güncelleyebilir, karar verme algoritmalarını ayarlayabilir ve zamanla performanslarını artırabilir. Bu yinelemeli öğrenme süreci, ajanların değişen koşullara ve kullanıcı tercihlerine uyum sağlamasını sağlar ve genel sistem etkinliğini artırır.

## AutoGen, Semantic Kernel ve Azure AI Agent Service arasındaki farklar nelerdir?

Bu çerçeveleri karşılaştırmanın birçok yolu vardır, ancak tasarım, yetenekler ve hedef kullanım durumları açısından bazı temel farklara bakalım:

## AutoGen

AutoGen, Microsoft Research'ün AI Frontiers Lab tarafından geliştirilen açık kaynaklı bir çerçevedir. Olay odaklı, dağıtılmış *ajanik* uygulamalara odaklanır ve birden fazla LLM, SLM, araç ve gelişmiş çoklu ajan tasarım desenlerini destekler.

AutoGen, çevresini algılayabilen, kararlar alabilen ve belirli hedeflere ulaşmak için eylemler gerçekleştirebilen otonom varlıklar olan ajanlar kavramı etrafında inşa edilmiştir. Ajanlar, asenkron mesajlar aracılığıyla iletişim kurar, bu da onların bağımsız ve paralel çalışmasını sağlayarak sistemin ölçeklenebilirliğini ve yanıt verebilirliğini artırır.
Peki, Semantic Kernel çerçevesinin temellerini öğrendik, peki ya Agent Framework?

## Azure AI Agent Hizmeti

Azure AI Agent Hizmeti, Microsoft Ignite 2024'te tanıtılan daha yeni bir eklemedir. Llama 3, Mistral ve Cohere gibi açık kaynaklı LLM'leri doğrudan çağırmak gibi daha esnek modellerle yapay zeka ajanları geliştirme ve dağıtma imkanı sunar.

Azure AI Agent Hizmeti, kurumsal uygulamalara uygun hale getiren daha güçlü kurumsal güvenlik mekanizmaları ve veri depolama yöntemleri sağlar.

AutoGen ve Semantic Kernel gibi çoklu ajan orkestrasyon çerçeveleriyle kutudan çıktığı gibi çalışır.

Bu hizmet şu anda Genel Önizleme aşamasındadır ve ajanlar oluşturmak için Python ve C# dillerini destekler.

Semantic Kernel Python kullanarak, kullanıcı tanımlı bir eklentiyle bir Azure AI Agent oluşturabiliriz:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Temel Kavramlar

Azure AI Agent Hizmeti aşağıdaki temel kavramlara sahiptir:

- **Ajan**. Azure AI Agent Hizmeti, Azure AI Foundry ile entegre çalışır. AI Foundry içinde bir AI Ajanı, soruları yanıtlamak (RAG), eylemleri gerçekleştirmek veya iş akışlarını tamamen otomatikleştirmek için kullanılabilen "akıllı" bir mikro hizmet olarak hareket eder. Bunu, üretken yapay zeka modellerinin gücünü, gerçek dünya veri kaynaklarına erişim ve etkileşim sağlayan araçlarla birleştirerek başarır. İşte bir ajan örneği:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Bu örnekte, `gpt-4o-mini` modeli, `my-agent` adı ve `You are helpful agent` talimatlarıyla bir ajan oluşturulmuştur. Ajan, kod yorumlama görevlerini gerçekleştirmek için araçlar ve kaynaklarla donatılmıştır.

- **Konular ve mesajlar**. Konu, başka bir önemli kavramdır. Bir ajan ile bir kullanıcı arasındaki bir konuşmayı veya etkileşimi temsil eder. Konular, bir konuşmanın ilerlemesini izlemek, bağlam bilgilerini saklamak ve etkileşimin durumunu yönetmek için kullanılabilir. İşte bir konu örneği:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Yukarıdaki kodda, bir konu oluşturulmuştur. Daha sonra, konuya bir mesaj gönderilmiştir. `create_and_process_run` çağrılarak, ajandan konu üzerinde çalışma yapması istenmiştir. Son olarak, mesajlar alınır ve ajanın yanıtını görmek için kaydedilir. Mesajlar, kullanıcı ile ajan arasındaki konuşmanın ilerlemesini gösterir. Ayrıca, mesajların metin, resim veya dosya gibi farklı türlerde olabileceğini anlamak önemlidir; örneğin, ajanın çalışması bir resim veya metin yanıtı ile sonuçlanabilir. Bir geliştirici olarak, bu bilgiyi yanıtı daha fazla işlemek veya kullanıcıya sunmak için kullanabilirsiniz.

- **Diğer AI çerçeveleriyle entegrasyon**. Azure AI Agent Hizmeti, AutoGen ve Semantic Kernel gibi diğer çerçevelerle etkileşim kurabilir, bu da uygulamanızın bir kısmını bu çerçevelerden birinde oluşturabileceğiniz ve örneğin Agent hizmetini bir orkestratör olarak kullanabileceğiniz anlamına gelir veya her şeyi Agent hizmetinde oluşturabilirsiniz.

**Kullanım Alanları**: Azure AI Agent Hizmeti, güvenli, ölçeklenebilir ve esnek yapay zeka ajan dağıtımı gerektiren kurumsal uygulamalar için tasarlanmıştır.

## Bu çerçeveler arasındaki fark nedir?

Bu çerçeveler arasında çok fazla örtüşme var gibi görünüyor, ancak tasarım, yetenekler ve hedef kullanım alanları açısından bazı temel farklılıklar bulunuyor:

- **AutoGen**: Çoklu ajan sistemleri üzerine öncü araştırmalara odaklanan bir deney çerçevesidir. Karmaşık çoklu ajan sistemlerini denemek ve prototiplemek için en iyi yerdir.
- **Semantic Kernel**: Kurumsal ajan uygulamaları oluşturmak için üretime hazır bir ajan kütüphanesidir. Olay odaklı, dağıtılmış ajan uygulamalarına odaklanır ve birden fazla LLM ve SLM, araçlar ve tekli/çoklu ajan tasarım desenlerini etkinleştirir.
- **Azure AI Agent Hizmeti**: Azure Foundry'de bir platform ve dağıtım hizmetidir. Azure OpenAI, Azure AI Search, Bing Search ve kod yürütme gibi Azure Foundry tarafından desteklenen hizmetlere bağlantı kurmayı sağlar.

Hâlâ hangisini seçeceğinizden emin değil misiniz?

### Kullanım Alanları

Bazı yaygın kullanım alanlarını gözden geçirerek size yardımcı olmaya çalışalım:

> S: Deney yapıyorum, öğreniyorum ve kavram kanıtı ajan uygulamaları oluşturuyorum ve hızlı bir şekilde oluşturup denemek istiyorum.
>
> C: Bu senaryo için AutoGen iyi bir seçim olacaktır, çünkü olay odaklı, dağıtılmış ajan uygulamalarına odaklanır ve gelişmiş çoklu ajan tasarım desenlerini destekler.

> S: Bu kullanım alanı için AutoGen'i Semantic Kernel ve Azure AI Agent Hizmeti'nden daha iyi bir seçim yapan nedir?
>
> C: AutoGen, özellikle olay odaklı, dağıtılmış ajan uygulamaları için tasarlanmıştır ve kod üretimi ve veri analizi görevlerini otomatikleştirmek için iyi bir şekilde uygundur. Karmaşık çoklu ajan sistemlerini verimli bir şekilde oluşturmak için gerekli araçları ve yetenekleri sağlar.

> S: Burada Azure AI Agent Hizmeti de işe yarayabilir gibi görünüyor, kod üretimi ve daha fazlası için araçlara sahip, değil mi?
>
> C: Evet, Azure AI Agent Hizmeti, ajanlar için bir platform hizmetidir ve birden fazla model, Azure AI Search, Bing Search ve Azure Functions için yerleşik yetenekler ekler. Ajanlarınızı Foundry Portal'da kolayca oluşturup ölçekli bir şekilde dağıtmanızı sağlar.

> S: Hâlâ kafam karıştı, bana tek bir seçenek söyleyin.
>
> C: Uygulamanızı önce Semantic Kernel'de oluşturmak ve ardından ajanın dağıtımı için Azure AI Agent Hizmeti'ni kullanmak harika bir seçimdir. Bu yaklaşım, ajanlarınızı kolayca kalıcı hale getirmenizi sağlarken, Semantic Kernel'de çoklu ajan sistemleri oluşturma gücünden yararlanmanızı sağlar. Ayrıca, Semantic Kernel'in AutoGen'de bir bağlayıcısı vardır, bu da her iki çerçeveyi birlikte kullanmayı kolaylaştırır.

Anahtar farkları bir tabloda özetleyelim:

| Çerçeve | Odak | Temel Kavramlar | Kullanım Alanları |
| --- | --- | --- | --- |
| AutoGen | Olay odaklı, dağıtılmış ajan uygulamaları | Ajanlar, Kişilikler, Fonksiyonlar, Veriler | Kod üretimi, veri analizi görevleri |
| Semantic Kernel | İnsan benzeri metin içeriği anlama ve üretme | Ajanlar, Modüler Bileşenler, İşbirliği | Doğal dil anlama, içerik üretimi |
| Azure AI Agent Hizmeti | Esnek modeller, kurumsal güvenlik, Kod üretimi, Araç çağırma | Modülerlik, İşbirliği, Süreç Orkestrasyonu | Güvenli, ölçeklenebilir ve esnek yapay zeka ajan dağıtımı |

Bu çerçevelerin her biri için ideal kullanım alanı nedir?

## Mevcut Azure ekosistem araçlarımı doğrudan entegre edebilir miyim yoksa bağımsız çözümler mi kullanmam gerekiyor?

Cevap evet, mevcut Azure ekosistem araçlarınızı özellikle Azure AI Agent Hizmeti ile doğrudan entegre edebilirsiniz, çünkü bu hizmet diğer Azure hizmetleriyle sorunsuz çalışacak şekilde tasarlanmıştır. Örneğin, Bing, Azure AI Search ve Azure Functions'ı entegre edebilirsiniz. Ayrıca, Azure AI Foundry ile derin bir entegrasyon da bulunmaktadır.

AutoGen ve Semantic Kernel için de Azure hizmetleriyle entegrasyon yapabilirsiniz, ancak bu, Azure hizmetlerini kodunuzdan çağırmanızı gerektirebilir. Bir başka entegrasyon yöntemi, Azure SDK'larını kullanarak ajanlarınızdan Azure hizmetleriyle etkileşim kurmaktır. Ayrıca, daha önce belirtildiği gibi, AutoGen veya Semantic Kernel'de oluşturulan ajanlarınız için Azure AI Agent Hizmeti'ni bir orkestratör olarak kullanabilirsiniz, bu da Azure ekosistemine kolay erişim sağlar.

### AI Agent Framework'leri hakkında daha fazla sorunuz mu var?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılarak diğer öğrenenlerle tanışabilir, ofis saatlerine katılabilir ve AI Agent'lar hakkındaki sorularınıza yanıt alabilirsiniz.

## Kaynaklar

## Önceki Ders

[AI Agent'lara Giriş ve Kullanım Alanları](../01-intro-to-ai-agents/README.md)

## Sonraki Ders

[Agentic Tasarım Desenlerini Anlama](../03-agentic-design-patterns/README.md)

---

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.