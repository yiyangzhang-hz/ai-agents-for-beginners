<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:22:16+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "pl"
}
-->
# Przykład serwera Github MCP

## Opis

To była prezentacja stworzona na AI Agents Hackathon organizowany przez Microsoft Reactor.

Narzędzie służy do rekomendowania projektów hackathonowych na podstawie repozytoriów użytkownika na Githubie.  
Dzieje się to poprzez:

1. **Github Agent** – korzystanie z Github MCP Server do pobierania repozytoriów i informacji o nich.  
2. **Hackathon Agent** – przetwarza dane od Github Agenta i generuje kreatywne pomysły na projekty hackathonowe, bazując na projektach, językach używanych przez użytkownika oraz ścieżkach projektów dla AI Agents hackathonu.  
3. **Events Agent** – na podstawie sugestii Hackathon Agenta, Events Agent rekomenduje odpowiednie wydarzenia z serii AI Agent Hackathon.

## Uruchamianie kodu

### Zmienne środowiskowe

Ta prezentacja korzysta z Azure Open AI Service, Semantic Kernel, Github MCP Server oraz Azure AI Search.

Upewnij się, że masz poprawnie ustawione zmienne środowiskowe do korzystania z tych narzędzi:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Uruchamianie serwera Chainlit

Aby połączyć się z MCP server, ta prezentacja używa Chainlit jako interfejsu czatu.

Aby uruchomić serwer, użyj następującego polecenia w terminalu:

```bash
chainlit run app.py -w
```

To powinno uruchomić serwer Chainlit na `localhost:8000` oraz załadować zawartość `event-descriptions.md` do indeksu Azure AI Search.

## Łączenie się z MCP Server

Aby połączyć się z Github MCP Server, wybierz ikonę „wtyczki” pod polem czatu „Type your message here..”:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.pl.png)

Następnie kliknij „Connect an MCP”, aby dodać polecenie łączenia z Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Zamień "[YOUR PERSONAL ACCESS TOKEN]" na swój rzeczywisty Personal Access Token.

Po połączeniu powinieneś zobaczyć (1) obok ikony wtyczki, co potwierdza połączenie. Jeśli nie, spróbuj ponownie uruchomić serwer chainlit poleceniem `chainlit run app.py -w`.

## Korzystanie z prezentacji

Aby rozpocząć działanie agenta rekomendującego projekty hackathonowe, możesz wpisać wiadomość taką jak:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent przeanalizuje Twoje zapytanie i zdecyduje, która kombinacja agentów (GitHub, Hackathon i Events) najlepiej poradzi sobie z Twoim zapytaniem. Agenci współpracują, aby dostarczyć kompleksowe rekomendacje oparte na analizie repozytoriów GitHub, generowaniu pomysłów na projekty oraz odpowiednich wydarzeniach technologicznych.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.