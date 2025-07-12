<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:01:34+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pl"
}
-->
, i  
- Czy mogę bezpośrednio zintegrować moje istniejące narzędzia z ekosystemu Azure, czy potrzebuję rozwiązań samodzielnych?  
- Czym jest usługa Azure AI Agents i jak mi pomaga?

## Cele nauki

Celem tej lekcji jest pomóc Ci zrozumieć:

- Rola AI Agent Frameworks w rozwoju AI.  
- Jak wykorzystać AI Agent Frameworks do budowy inteligentnych agentów.  
- Kluczowe możliwości oferowane przez AI Agent Frameworks.  
- Różnice między AutoGen, Semantic Kernel i Azure AI Agent Service.

## Czym są AI Agent Frameworks i co umożliwiają deweloperom?

Tradycyjne frameworki AI mogą pomóc Ci zintegrować AI z Twoimi aplikacjami i ulepszyć je na następujące sposoby:

- **Personalizacja**: AI może analizować zachowania i preferencje użytkowników, aby dostarczać spersonalizowane rekomendacje, treści i doświadczenia.  
Przykład: Serwisy streamingowe, takie jak Netflix, używają AI do sugerowania filmów i programów na podstawie historii oglądania, co zwiększa zaangażowanie i satysfakcję użytkowników.  
- **Automatyzacja i efektywność**: AI może automatyzować powtarzalne zadania, usprawniać przepływy pracy i poprawiać efektywność operacyjną.  
Przykład: Aplikacje obsługi klienta wykorzystują chatboty zasilane AI do obsługi typowych zapytań, skracając czas odpowiedzi i odciążając pracowników od bardziej złożonych problemów.  
- **Ulepszone doświadczenie użytkownika**: AI może poprawić ogólne doświadczenie użytkownika, oferując inteligentne funkcje, takie jak rozpoznawanie głosu, przetwarzanie języka naturalnego i tekst predykcyjny.  
Przykład: Wirtualni asystenci, tacy jak Siri i Google Assistant, używają AI do rozumienia i reagowania na polecenia głosowe, ułatwiając interakcję z urządzeniami.

### Brzmi świetnie, ale po co nam AI Agent Framework?

AI Agent Frameworks to coś więcej niż zwykłe frameworki AI. Są zaprojektowane, aby umożliwić tworzenie inteligentnych agentów, którzy mogą wchodzić w interakcje z użytkownikami, innymi agentami i środowiskiem, aby osiągać określone cele. Tacy agenci mogą wykazywać autonomiczne zachowania, podejmować decyzje i dostosowywać się do zmieniających się warunków. Spójrzmy na kluczowe możliwości oferowane przez AI Agent Frameworks:

- **Współpraca i koordynacja agentów**: Umożliwiają tworzenie wielu agentów AI, którzy mogą współpracować, komunikować się i koordynować działania, aby rozwiązywać złożone zadania.  
- **Automatyzacja i zarządzanie zadaniami**: Zapewniają mechanizmy automatyzacji wieloetapowych przepływów pracy, delegowania zadań i dynamicznego zarządzania zadaniami między agentami.  
- **Zrozumienie kontekstu i adaptacja**: Wyposażają agentów w zdolność rozumienia kontekstu, dostosowywania się do zmieniającego się środowiska i podejmowania decyzji na podstawie informacji w czasie rzeczywistym.

Podsumowując, agenci pozwalają Ci zrobić więcej, przenieść automatyzację na wyższy poziom, tworzyć inteligentniejsze systemy, które potrafią się uczyć i adaptować do otoczenia.

## Jak szybko prototypować, iterować i ulepszać możliwości agenta?

To dynamicznie zmieniający się obszar, ale istnieją pewne wspólne elementy w większości AI Agent Frameworks, które pomagają szybko prototypować i iterować, mianowicie modułowe komponenty, narzędzia do współpracy i uczenie się w czasie rzeczywistym. Przyjrzyjmy się im bliżej:

- **Używaj modułowych komponentów**: SDK AI oferują gotowe komponenty, takie jak konektory AI i pamięci, wywoływanie funkcji za pomocą języka naturalnego lub wtyczek kodu, szablony promptów i inne.  
- **Wykorzystuj narzędzia do współpracy**: Projektuj agentów z określonymi rolami i zadaniami, co pozwala testować i udoskonalać współpracujące przepływy pracy.  
- **Ucz się w czasie rzeczywistym**: Wdrażaj pętle sprzężenia zwrotnego, gdzie agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie.

### Używaj modułowych komponentów

SDK takie jak Microsoft Semantic Kernel i LangChain oferują gotowe komponenty, takie jak konektory AI, szablony promptów i zarządzanie pamięcią.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą szybko składać te komponenty, tworząc funkcjonalny prototyp bez konieczności zaczynania od zera, co pozwala na szybkie eksperymentowanie i iteracje.

**Jak to działa w praktyce**: Możesz użyć gotowego parsera do wyodrębniania informacji z danych wejściowych użytkownika, modułu pamięci do przechowywania i pobierania danych oraz generatora promptów do interakcji z użytkownikami, wszystko bez konieczności budowania tych komponentów od podstaw.

**Przykładowy kod**. Spójrzmy na przykład, jak można użyć gotowego konektora AI z Semantic Kernel w Pythonie i .Net, który wykorzystuje automatyczne wywoływanie funkcji, aby model odpowiadał na dane wejściowe użytkownika:

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

Z tego przykładu widać, jak można wykorzystać gotowy parser do wyodrębnienia kluczowych informacji z danych wejściowych użytkownika, takich jak miejsce wylotu, miejsce docelowe i data rezerwacji lotu. Takie modułowe podejście pozwala skupić się na logice wysokiego poziomu.

### Wykorzystuj narzędzia do współpracy

Frameworki takie jak CrewAI, Microsoft AutoGen i Semantic Kernel ułatwiają tworzenie wielu agentów, którzy mogą współpracować.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą projektować agentów z określonymi rolami i zadaniami, co pozwala testować i udoskonalać współpracujące przepływy pracy oraz poprawiać ogólną efektywność systemu.

**Jak to działa w praktyce**: Możesz stworzyć zespół agentów, z których każdy ma specjalistyczną funkcję, taką jak pobieranie danych, analiza czy podejmowanie decyzji. Agenci mogą się komunikować i wymieniać informacjami, aby osiągnąć wspólny cel, np. odpowiedzieć na zapytanie użytkownika lub wykonać zadanie.

**Przykładowy kod (AutoGen)**:

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

W powyższym kodzie widać, jak można stworzyć zadanie, które wymaga współpracy wielu agentów do analizy danych. Każdy agent wykonuje określoną funkcję, a zadanie jest realizowane przez koordynację agentów, aby osiągnąć pożądany rezultat. Tworząc dedykowanych agentów ze specjalistycznymi rolami, można poprawić efektywność i wydajność zadania.

### Ucz się w czasie rzeczywistym

Zaawansowane frameworki oferują możliwości rozumienia kontekstu i adaptacji w czasie rzeczywistym.

**Jak zespoły mogą z nich korzystać**: Zespoły mogą wdrażać pętle sprzężenia zwrotnego, gdzie agenci uczą się na podstawie interakcji i dynamicznie dostosowują swoje zachowanie, co prowadzi do ciągłego doskonalenia i ulepszania możliwości.

**Jak to działa w praktyce**: Agenci mogą analizować opinie użytkowników, dane środowiskowe i wyniki zadań, aby aktualizować swoją bazę wiedzy, dostosowywać algorytmy podejmowania decyzji i poprawiać wydajność z czasem. Ten iteracyjny proces uczenia pozwala agentom adaptować się do zmieniających się warunków i preferencji użytkowników, zwiększając skuteczność systemu.

## Jakie są różnice między frameworkami AutoGen, Semantic Kernel i Azure AI Agent Service?

Istnieje wiele sposobów porównania tych frameworków, ale spójrzmy na kluczowe różnice pod względem ich konstrukcji, możliwości i docelowych zastosowań:

## AutoGen

AutoGen to otwartoźródłowy framework opracowany przez Microsoft Research AI Frontiers Lab. Skupia się na zdarzeniowych, rozproszonych aplikacjach *agentowych*, umożliwiając współpracę wielu LLM i SLM, narzędzi oraz zaawansowanych wzorców projektowych wieloagentowych.

AutoGen opiera się na podstawowej koncepcji agentów, którzy są autonomicznymi bytami zdolnymi do postrzegania swojego otoczenia, podejmowania decyzji i podejmowania działań w celu osiągnięcia określonych celów. Agenci komunikują się za pomocą asynchronicznych wiadomości, co pozwala im działać niezależnie i równolegle, zwiększając skalowalność i responsywność systemu.

Według Wikipedii, aktor to _podstawowy element obliczeń współbieżnych. W odpowiedzi na otrzymaną wiadomość aktor może: podejmować lokalne decyzje, tworzyć kolejnych aktorów, wysyłać kolejne wiadomości oraz decydować, jak odpowiedzieć na następną otrzymaną wiadomość_.

**Przypadki użycia**: Automatyzacja generowania kodu, zadania analizy danych oraz tworzenie niestandardowych agentów do planowania i funkcji badawczych.

Oto kilka ważnych podstawowych pojęć AutoGen:

- **Agenci**. Agent to byt programowy, który:  
  - **Komunikuje się za pomocą wiadomości**, które mogą być synchroniczne lub asynchroniczne.  
  - **Utrzymuje własny stan**, który może być modyfikowany przez przychodzące wiadomości.  
  - **Wykonuje działania** w odpowiedzi na otrzymane wiadomości lub zmiany stanu. Działania te mogą modyfikować stan agenta i wywoływać efekty zewnętrzne, takie jak aktualizacja logów wiadomości, wysyłanie nowych wiadomości, wykonywanie kodu lub wywoływanie API.  

  Poniżej krótki fragment kodu, w którym tworzysz własnego agenta z funkcjami czatu:

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

    W powyższym kodzie `MyAssistant` został utworzony i dziedziczy po `RoutedAgent`. Ma handler wiadomości, który wypisuje zawartość wiadomości, a następnie wysyła odpowiedź za pomocą delegata `AssistantAgent`. Zwróć szczególną uwagę, jak przypisujemy do `self._delegate` instancję `AssistantAgent`, który jest gotowym agentem obsługującym uzupełnienia czatu.

    Teraz poinformujmy AutoGen o tym typie agenta i uruchommy program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    W powyższym kodzie agenci są rejestrowani w środowisku uruchomieniowym, a następnie wysyłana jest wiadomość do agenta, co skutkuje następującym wyjściem:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Wieloagentowość**. AutoGen wspiera tworzenie wielu agentów, którzy mogą współpracować, aby realizować złożone zadania. Agenci mogą się komunikować, dzielić informacjami i koordynować działania, aby efektywniej rozwiązywać problemy. Aby stworzyć system wieloagentowy, możesz zdefiniować różne typy agentów o wyspecjalizowanych funkcjach i rolach, takich jak pobieranie danych, analiza, podejmowanie decyzji i interakcja z użytkownikiem. Zobaczmy, jak wygląda taka konstrukcja:

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

    W powyższym kodzie mamy `GroupChatManager`, który jest zarejestrowany w środowisku uruchomieniowym. Ten menedżer odpowiada za koordynację interakcji między różnymi typami agentów, takimi jak pisarze, ilustratorzy, redaktorzy i użytkownicy.

- **Środowisko uruchomieniowe agentów**. Framework zapewnia środowisko uruchomieniowe, które umożliwia komunikację między agentami, zarządza ich tożsamościami i cyklem życia oraz egzekwuje granice bezpieczeństwa i prywatności. Oznacza to, że możesz uruchamiać swoich agentów w bezpiecznym i kontrolowanym środowisku, zapewniając im bezpieczną i efektywną interakcję. Istnieją dwa interesujące środowiska uruchomieniowe:  
  - **Środowisko samodzielne**. To dobre rozwiązanie dla aplikacji jednoprosesowych, gdzie wszyscy agenci są zaimplementowani w tym samym języku programowania i działają w tym samym procesie. Oto ilustracja, jak to działa:

Stos aplikacji

    *agenci komunikują się za pomocą wiadomości przez środowisko uruchomieniowe, które zarządza cyklem życia agentów*

  - **Rozproszone środowisko uruchomieniowe agentów** jest odpowiednie dla aplikacji wieloprocesowych, gdzie agenci mogą być zaimplementowani w różnych językach programowania i działać na różnych maszynach. Oto ilustracja, jak to działa:

## Semantic Kernel + Agent Framework

Semantic Kernel to gotowy do zastosowań korporacyjnych SDK do orkiestracji AI. Składa się z konektorów AI i pamięci oraz frameworka agentów.

Najpierw omówmy kilka podstawowych komponentów:

- **Konektory AI**: To interfejs do zewnętrznych usług AI i źródeł danych, dostępny zarówno w Pythonie, jak i C#.

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

  Oto prosty przykład, jak można utworzyć kernel i dodać usługę uzupełniania czatu. Semantic Kernel tworzy połączenie z zewnętrzną usługą AI, w tym przypadku Azure OpenAI Chat Completion.

- **Wtyczki (Plugins)**: Zawierają funkcje, które aplikacja może wykorzystać. Są dostępne zarówno gotowe wtyczki, jak i takie, które możesz stworzyć samodzielnie. Powiązanym pojęciem są "funkcje promptów". Zamiast podawać naturalne wskazówki do wywołania funkcji, udostępniasz modelowi określone funkcje. Na podstawie aktualnego kontekstu czatu model może zdecydować się wywołać jedną z tych funkcji, aby zrealizować żądanie lub zapytanie. Oto przykład:

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

  Tutaj najpierw masz szablon promptu `skPrompt`, który pozostawia miejsce na tekst wprowadzony przez użytkownika, `$userInput`. Następnie tworzysz funkcję kernela `SummarizeText` i importujesz ją do kernela pod nazwą wtyczki `SemanticFunctions`. Zwróć uwagę na nazwę funkcji, która pomaga Semantic Kernel zrozumieć, co funkcja robi i kiedy powinna być wywołana.

- **Funkcje natywne**: Są też funkcje natywne, które framework może wywołać bezpośrednio, aby wykonać zadanie. Oto przykład funkcji pobierającej zawartość pliku:

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

- **Pamięć**: Upraszcza i abstrahuje zarządzanie kontekstem dla aplikacji AI. Idea pamięci polega na tym, że jest to coś, o czym LLM powinien wiedzieć. Możesz przechowywać te informacje w magazynie wektorowym, który działa jak baza danych w pamięci lub baza wektorowa. Oto przykład bardzo uproszczonego scenariusza, gdzie *fakty* są dodawane do pamięci:

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

    Fakty te są następnie przechowywane w kolekcji pamięci `SummarizedAzureDocs`. To bardzo uproszczony przykład, ale widać, jak można przechowywać informacje w pamięci, aby LLM mógł z nich korzystać.
## Poprzednia lekcja

[Wprowadzenie do agentów AI i przypadków użycia agentów](../01-intro-to-ai-agents/README.md)

## Następna lekcja

[Zrozumienie wzorców projektowych agentów](../03-agentic-design-patterns/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.