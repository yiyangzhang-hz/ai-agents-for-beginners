<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:47:30+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pl"
}
-->
# Lekcja 11: Integracja Model Context Protocol (MCP)

## Wprowadzenie do Model Context Protocol (MCP)

Model Context Protocol (MCP) to nowoczesne rozwiązanie zaprojektowane w celu standaryzacji interakcji między modelami AI a aplikacjami klienckimi. MCP pełni rolę pomostu między modelami AI a aplikacjami, które z nich korzystają, zapewniając spójny interfejs niezależnie od implementacji modelu.

Kluczowe cechy MCP:

- **Standaryzowana komunikacja**: MCP ustanawia wspólny język do komunikacji aplikacji z modelami AI  
- **Ulepszone zarządzanie kontekstem**: Umożliwia efektywne przekazywanie informacji kontekstowych do modeli AI  
- **Kompatybilność wieloplatformowa**: Działa w różnych językach programowania, w tym C#, Java, JavaScript, Python i TypeScript  
- **Bezproblemowa integracja**: Pozwala deweloperom łatwo integrować różne modele AI w swoich aplikacjach  

MCP jest szczególnie cenny w rozwoju agentów AI, ponieważ umożliwia agentom interakcję z różnymi systemami i źródłami danych za pomocą zunifikowanego protokołu, co czyni agentów bardziej elastycznymi i wydajnymi.

## Cele nauki
- Zrozumieć, czym jest MCP i jaka jest jego rola w rozwoju agentów AI  
- Skonfigurować i uruchomić serwer MCP do integracji z GitHub  
- Zbudować system wieloagentowy korzystając z narzędzi MCP  
- Wdrożyć RAG (Retrieval Augmented Generation) z użyciem Azure Cognitive Search  

## Wymagania wstępne
- Python 3.8+  
- Node.js 14+  
- Subskrypcja Azure  
- Konto GitHub  
- Podstawowa znajomość Semantic Kernel  

## Instrukcje konfiguracji

1. **Konfiguracja środowiska**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracja usług Azure**  
   - Utwórz zasób Azure Cognitive Search  
   - Skonfiguruj usługę Azure OpenAI  
   - Ustaw zmienne środowiskowe w pliku `.env`  

3. **Konfiguracja serwera MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projektu

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Główne komponenty

### 1. System wieloagentowy
- Agent GitHub: analiza repozytoriów  
- Agent Hackathon: rekomendacje projektów  
- Agent Wydarzeń: sugestie wydarzeń technologicznych  

### 2. Integracja z Azure
- Cognitive Search do indeksowania wydarzeń  
- Azure OpenAI dla inteligencji agentów  
- Implementacja wzorca RAG  

### 3. Narzędzia MCP
- Analiza repozytoriów GitHub  
- Inspekcja kodu  
- Ekstrakcja metadanych  

## Przegląd kodu

Przykład demonstruje:  
1. Integrację serwera MCP  
2. Orkiestrację systemu wieloagentowego  
3. Integrację z Azure Cognitive Search  
4. Implementację wzorca RAG  

Kluczowe funkcje:  
- Analiza repozytoriów GitHub w czasie rzeczywistym  
- Inteligentne rekomendacje projektów  
- Dopasowywanie wydarzeń z użyciem Azure Search  
- Strumieniowe odpowiedzi z Chainlit  

## Uruchamianie przykładu

Szczegółowe instrukcje konfiguracji i dodatkowe informacje znajdziesz w [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Uruchom serwer MCP:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Włącz aplikację:  
   ```bash
   chainlit run app.py -w
   ```

3. Przetestuj integrację:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Rozwiązywanie problemów

Typowe problemy i ich rozwiązania:  
1. Problemy z połączeniem MCP  
   - Sprawdź, czy serwer działa  
   - Zweryfikuj dostępność portu  
   - Potwierdź poprawność tokenów GitHub  

2. Problemy z Azure Search  
   - Sprawdź poprawność connection stringów  
   - Zweryfikuj istnienie indeksu  
   - Upewnij się, że dokumenty zostały przesłane  

## Kolejne kroki
- Poznaj dodatkowe narzędzia MCP  
- Stwórz własnych agentów  
- Rozbuduj możliwości RAG  
- Dodaj więcej źródeł wydarzeń  

## Zasoby
- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Dokumentacja Azure Cognitive Search](https://learn.microsoft.com/azure/search/)  
- [Przewodniki Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.