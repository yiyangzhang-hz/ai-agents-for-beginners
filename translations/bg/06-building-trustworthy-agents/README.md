<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f57852cac3a86c4a5ef47f793cc12178",
  "translation_date": "2025-07-12T10:32:31+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "bg"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.bg.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Създаване на надеждни AI агенти

## Въведение

В този урок ще разгледаме:

- Как да създаваме и внедряваме безопасни и ефективни AI агенти
- Важни съображения за сигурността при разработката на AI агенти
- Как да запазим поверителността на данните и потребителите при разработката на AI агенти

## Цели на обучението

След завършване на този урок ще можете да:

- Идентифицирате и намалявате рисковете при създаването на AI агенти
- Прилагате мерки за сигурност, за да осигурите правилно управление на данните и достъпа
- Създавате AI агенти, които запазват поверителността на данните и осигуряват качествено потребителско изживяване

## Безопасност

Нека първо разгледаме как да изградим безопасни агентни приложения. Безопасността означава, че AI агентът изпълнява задачите си според предназначението. Като създатели на агентни приложения, разполагаме с методи и инструменти за максимизиране на безопасността:

### Създаване на рамка за системни съобщения

Ако някога сте създавали AI приложение с помощта на големи езикови модели (LLMs), знаете колко е важно да се проектира стабилен системен prompt или системно съобщение. Тези prompts задават мета правилата, инструкциите и насоките за това как LLM ще взаимодейства с потребителя и данните.

За AI агенти системният prompt е още по-важен, тъй като AI агентите ще се нуждаят от много конкретни инструкции, за да изпълнят задачите, които сме им възложили.

За да създадем мащабируеми системни prompts, можем да използваме рамка за системни съобщения за изграждане на един или повече агенти в нашето приложение:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.bg.png)

#### Стъпка 1: Създаване на мета системно съобщение

Мета prompt ще се използва от LLM, за да генерира системните prompts за агентите, които създаваме. Проектираме го като шаблон, за да можем ефективно да създаваме множество агенти при нужда.

Ето пример за мета системно съобщение, което бихме дали на LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Стъпка 2: Създаване на основен prompt

Следващата стъпка е да създадем основен prompt, който описва AI агента. Трябва да включите ролята на агента, задачите, които ще изпълнява, и други отговорности на агента.

Ето пример:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Стъпка 3: Предоставяне на основното системно съобщение на LLM

Сега можем да оптимизираме това системно съобщение, като предоставим мета системното съобщение като системно съобщение и нашето основно системно съобщение.

Това ще създаде системно съобщение, което е по-добре проектирано за насочване на нашите AI агенти:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Стъпка 4: Итерация и подобрение

Ценността на тази рамка за системни съобщения е, че улеснява мащабирането при създаване на системни съобщения за множество агенти, както и подобряването на системните съобщения с времето. Рядко ще имате системно съобщение, което работи перфектно от първия път за целия ви случай на употреба. Възможността да правите малки корекции и подобрения чрез промяна на основното системно съобщение и повторното му подаване през системата ще ви позволи да сравнявате и оценявате резултатите.

## Разбиране на заплахите

За да създадем надеждни AI агенти, е важно да разберем и намалим рисковете и заплахите за вашия AI агент. Нека разгледаме само някои от различните заплахи за AI агентите и как можете по-добре да планирате и се подготвите за тях.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.bg.png)

### Задачи и инструкции

**Описание:** Злонамерени лица се опитват да променят инструкциите или целите на AI агента чрез prompts или манипулиране на входните данни.

**Намаляване на риска:** Изпълнявайте проверки за валидност и филтри за входните данни, за да откривате потенциално опасни prompts преди те да бъдат обработени от AI агента. Тъй като тези атаки обикновено изискват честа комуникация с агента, ограничаването на броя на ходовете в разговора е друг начин за предотвратяване на този тип атаки.

### Достъп до критични системи

**Описание:** Ако AI агентът има достъп до системи и услуги, които съхраняват чувствителни данни, нападателите могат да компрометират комуникацията между агента и тези услуги. Това могат да бъдат директни атаки или косвени опити за получаване на информация за тези системи чрез агента.

**Намаляване на риска:** AI агентите трябва да имат достъп до системите само при необходимост, за да се предотвратят тези видове атаки. Комуникацията между агента и системата също трябва да бъде защитена. Прилагането на автентикация и контрол на достъпа е друг начин за защита на тази информация.

### Претоварване на ресурси и услуги

**Описание:** AI агентите могат да използват различни инструменти и услуги за изпълнение на задачи. Нападателите могат да използват тази възможност, за да атакуват тези услуги, като изпращат голям обем заявки чрез AI агента, което може да доведе до сривове на системата или високи разходи.

**Намаляване на риска:** Внедрете политики за ограничаване на броя заявки, които AI агентът може да изпраща към дадена услуга. Ограничаването на броя на ходовете в разговора и заявките към вашия AI агент е друг начин за предотвратяване на този тип атаки.

### Отравяне на базата знания

**Описание:** Този тип атака не е насочена директно към AI агента, а към базата знания и други услуги, които AI агентът използва. Това може да включва корупция на данните или информацията, които AI агентът използва за изпълнение на задачи, водещо до пристрастни или нежелани отговори към потребителя.

**Намаляване на риска:** Извършвайте редовна проверка на данните, които AI агентът използва в своите работни процеси. Осигурете, че достъпът до тези данни е защитен и може да бъде променян само от доверени лица, за да се избегне този тип атака.

### Каскадни грешки

**Описание:** AI агентите използват различни инструменти и услуги за изпълнение на задачи. Грешки, причинени от нападатели, могат да доведат до сривове на други системи, към които AI агентът е свързан, което прави атаката по-широко разпространена и по-трудна за отстраняване.

**Намаляване на риска:** Един от методите за избягване на това е AI агентът да работи в ограничена среда, например изпълнявайки задачи в Docker контейнер, за да се предотвратят директни атаки върху системата. Създаването на резервни механизми и логика за повторен опит при грешки от определени системи е друг начин за предотвратяване на по-големи сривове.

## Човек в цикъла

Друг ефективен начин за създаване на надеждни AI агентни системи е използването на човек в цикъла. Това създава поток, в който потребителите могат да дават обратна връзка на агентите по време на изпълнението. Потребителите всъщност действат като агенти в мултиагентна система, като одобряват или прекратяват текущия процес.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.bg.png)

Ето примерен код с AutoGen, който показва как се реализира тази концепция:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Заключение

Създаването на надеждни AI агенти изисква внимателно проектиране, стабилни мерки за сигурност и непрекъснати подобрения. Чрез прилагане на структурирани системи за мета prompting, разбиране на потенциалните заплахи и използване на стратегии за намаляване на риска, разработчиците могат да създадат AI агенти, които са както безопасни, така и ефективни. Освен това, включването на човек в цикъла гарантира, че AI агентите остават съобразени с нуждите на потребителите, като същевременно минимизират рисковете. С развитието на AI, поддържането на проактивен подход към сигурността, поверителността и етичните аспекти ще бъде ключово за изграждането на доверие и надеждност в системите, базирани на AI.

## Допълнителни ресурси

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Отговорно използване на AI - обзор</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Оценка на генеративни AI модели и AI приложения</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Системни съобщения за безопасност</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Шаблон за оценка на риска</a>

## Предишен урок

[Agentic RAG](../05-agentic-rag/README.md)

## Следващ урок

[Planning Design Pattern](../07-planning-design/README.md)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.