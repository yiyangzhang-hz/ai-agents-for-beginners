<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:24:56+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "sr"
}
-->
# Github MCP сервер пример

## Опис

Ово је демо направљен за AI Agents Hackathon који је организовао Microsoft Reactor.

Овај алат се користи за препоруку хакатон пројеката на основу корисникових Github репозиторијума.  
То се ради на следећи начин:

1. **Github Agent** – Користи Github MCP Server за преузимање репозиторијума и информација о тим репозиторијумима.  
2. **Hackathon Agent** – Узима податке од Github Agenta и осмишљава креативне идеје за хакатон пројекте на основу пројеката, језика које корисник користи и пројектних смерница за AI Agents хакатон.  
3. **Events Agent** – На основу предлога Hackathon Agenta, Events Agent препоручује релевантне догађаје из серије AI Agent Hackathon.

## Покретање кода

### Променљиве окружења

Овај демо користи Azure Open AI Service, Semantic Kernel, Github MCP Server и Azure AI Search.

Проверите да ли сте подесили одговарајуће променљиве окружења за коришћење ових алата:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Покретање Chainlit сервера

За повезивање са MCP сервером, овај демо користи Chainlit као интерфејс за ћаскање.

Да бисте покренули сервер, у терминалу укуцајте следећу команду:

```bash
chainlit run app.py -w
```

Ово ће покренути ваш Chainlit сервер на `localhost:8000` и истовремено попунити ваш Azure AI Search индекс са садржајем из `event-descriptions.md`.

## Повезивање са MCP сервером

Да бисте се повезали са Github MCP Server-ом, изаберите икону „прикључка“ испод поља за ћаскање „Type your message here..“:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.sr.png)

Одатле можете кликнути на „Connect an MCP“ да бисте додали команду за повезивање са Github MCP Server-ом:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Замените "[YOUR PERSONAL ACCESS TOKEN]" вашим стварним Personal Access Token-ом.

Након повезивања, требало би да видите (1) поред иконе прикључка као потврду да је веза успостављена. Уколико није, покушајте да поново покренете chainlit сервер са `chainlit run app.py -w`.

## Коришћење демоа

Да бисте покренули агентски ток рада за препоруку хакатон пројеката, можете унети поруку као што је:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ће анализирати ваш захтев и одредити која комбинација агената (GitHub, Hackathon и Events) је најпогоднија за обраду вашег упита. Агенти сарађују како би пружили свеобухватне препоруке на основу анализе Github репозиторијума, осмишљавања пројеката и релевантних технолошких догађаја.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.