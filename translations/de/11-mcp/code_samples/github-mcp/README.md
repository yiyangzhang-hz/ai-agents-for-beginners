<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:19:46+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "de"
}
-->
# Github MCP Server Beispiel

## Beschreibung

Dies ist eine Demo, die für den AI Agents Hackathon erstellt wurde, der im Microsoft Reactor stattfand.

Das Tool wird verwendet, um Hackathon-Projekte basierend auf den Github-Repositories eines Nutzers zu empfehlen.  
Dies geschieht durch:

1. **Github Agent** – Verwendet den Github MCP Server, um Repositories und Informationen zu diesen Repositories abzurufen.  
2. **Hackathon Agent** – Nutzt die Daten des Github Agent, um kreative Hackathon-Projektideen basierend auf den Projekten, den vom Nutzer verwendeten Programmiersprachen und den Projektkategorien des AI Agents Hackathons zu entwickeln.  
3. **Events Agent** – Basierend auf den Vorschlägen des Hackathon Agent empfiehlt der Events Agent relevante Veranstaltungen aus der AI Agent Hackathon-Reihe.  

## Ausführen des Codes

### Umgebungsvariablen

Diese Demo verwendet Azure Open AI Service, Semantic Kernel, den Github MCP Server und Azure AI Search.

Stelle sicher, dass die entsprechenden Umgebungsvariablen gesetzt sind, um diese Tools zu nutzen:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Starten des Chainlit Servers

Um eine Verbindung zum MCP Server herzustellen, verwendet diese Demo Chainlit als Chat-Oberfläche.

Um den Server zu starten, nutze folgenden Befehl im Terminal:

```bash
chainlit run app.py -w
```

Dadurch wird dein Chainlit Server auf `localhost:8000` gestartet und dein Azure AI Search Index mit dem Inhalt von `event-descriptions.md` befüllt.

## Verbindung zum MCP Server herstellen

Um eine Verbindung zum Github MCP Server herzustellen, wähle das „Stecker“-Symbol unterhalb des Chat-Felds „Type your message here..“ aus:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.de.png)

Dort kannst du auf „Connect an MCP“ klicken, um den Befehl zum Verbinden mit dem Github MCP Server hinzuzufügen:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Ersetze "[YOUR PERSONAL ACCESS TOKEN]" durch deinen tatsächlichen Personal Access Token.

Nach der Verbindung solltest du eine (1) neben dem Stecker-Symbol sehen, die bestätigt, dass die Verbindung steht. Falls nicht, versuche den Chainlit Server mit `chainlit run app.py -w` neu zu starten.

## Nutzung der Demo

Um den Agenten-Workflow zu starten, der Hackathon-Projekte empfiehlt, kannst du eine Nachricht wie diese eingeben:

„Empfehle Hackathon-Projekte für den Github-Nutzer koreyspace“

Der Router Agent analysiert deine Anfrage und entscheidet, welche Kombination von Agenten (Github, Hackathon und Events) am besten geeignet ist, um deine Anfrage zu bearbeiten. Die Agenten arbeiten zusammen, um umfassende Empfehlungen basierend auf der Analyse der Github-Repositories, der Projektideen und relevanter Tech-Events zu liefern.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.