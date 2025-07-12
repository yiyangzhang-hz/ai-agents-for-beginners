<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:25:34+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "uk"
}
-->
# Приклад сервера Github MCP

## Опис

Це демо було створене для AI Agents Hackathon, який проходив у Microsoft Reactor.

Інструмент використовується для рекомендації проектів для хакатону на основі репозиторіїв користувача на Github.  
Це реалізується за допомогою:

1. **Github Agent** – Використовує Github MCP Server для отримання репозиторіїв та інформації про них.  
2. **Hackathon Agent** – Обробляє дані від Github Agent і генерує креативні ідеї проектів для хакатону, враховуючи проекти, мови програмування користувача та треки проектів для AI Agents hackathon.  
3. **Events Agent** – На основі пропозицій Hackathon Agent рекомендує відповідні події з серії AI Agent Hackathon.

## Запуск коду

### Змінні середовища

Це демо використовує Azure Open AI Service, Semantic Kernel, Github MCP Server та Azure AI Search.

Переконайтеся, що у вас налаштовані відповідні змінні середовища для роботи з цими інструментами:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Запуск Chainlit Server

Для підключення до MCP server це демо використовує Chainlit як чат-інтерфейс.

Щоб запустити сервер, виконайте у терміналі таку команду:

```bash
chainlit run app.py -w
```

Це має запустити ваш Chainlit сервер на `localhost:8000` та заповнити індекс Azure AI Search вмістом файлу `event-descriptions.md`.

## Підключення до MCP Server

Щоб підключитися до Github MCP Server, оберіть іконку "штекера" під полем для введення повідомлення "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.uk.png)

Далі натисніть "Connect an MCP", щоб додати команду для підключення до Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Замініть "[YOUR PERSONAL ACCESS TOKEN]" на ваш реальний персональний токен доступу.

Після підключення біля іконки штекера має з’явитися (1), що підтверджує з’єднання. Якщо ні, спробуйте перезапустити chainlit сервер командою `chainlit run app.py -w`.

## Використання демо

Щоб розпочати роботу агента з рекомендації проектів для хакатону, введіть повідомлення на кшталт:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent проаналізує ваш запит і визначить, яка комбінація агентів (GitHub, Hackathon та Events) найкраще підходить для обробки вашого запиту. Агенти працюють разом, щоб надати комплексні рекомендації на основі аналізу репозиторіїв GitHub, ідей для проектів та відповідних технічних подій.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.