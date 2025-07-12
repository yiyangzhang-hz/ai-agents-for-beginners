<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:44:09+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "de"
}
-->
# Lektion 11: Model Context Protocol (MCP) Integration

## Einführung in das Model Context Protocol (MCP)

Das Model Context Protocol (MCP) ist ein modernes Framework, das entwickelt wurde, um die Interaktionen zwischen KI-Modellen und Client-Anwendungen zu standardisieren. MCP fungiert als Brücke zwischen KI-Modellen und den Anwendungen, die sie nutzen, und bietet eine einheitliche Schnittstelle, unabhängig von der zugrunde liegenden Modellimplementierung.

Wichtige Aspekte von MCP:

- **Standardisierte Kommunikation**: MCP schafft eine gemeinsame Sprache, damit Anwendungen mit KI-Modellen kommunizieren können
- **Verbessertes Kontextmanagement**: Ermöglicht die effiziente Übergabe von Kontextinformationen an KI-Modelle
- **Plattformübergreifende Kompatibilität**: Funktioniert mit verschiedenen Programmiersprachen wie C#, Java, JavaScript, Python und TypeScript
- **Nahtlose Integration**: Erlaubt Entwicklern, verschiedene KI-Modelle einfach in ihre Anwendungen einzubinden

MCP ist besonders wertvoll in der Entwicklung von KI-Agenten, da es Agenten ermöglicht, über ein einheitliches Protokoll mit verschiedenen Systemen und Datenquellen zu interagieren, wodurch die Agenten flexibler und leistungsfähiger werden.

## Lernziele
- Verstehen, was MCP ist und welche Rolle es in der Entwicklung von KI-Agenten spielt
- Einrichten und Konfigurieren eines MCP-Servers für die GitHub-Integration
- Aufbau eines Multi-Agenten-Systems mit MCP-Tools
- Implementierung von RAG (Retrieval Augmented Generation) mit Azure Cognitive Search

## Voraussetzungen
- Python 3.8+
- Node.js 14+
- Azure-Abonnement
- GitHub-Konto
- Grundkenntnisse in Semantic Kernel

## Einrichtung

1. **Umgebung einrichten**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-Dienste konfigurieren**  
   - Erstellen einer Azure Cognitive Search-Ressource  
   - Einrichten des Azure OpenAI-Dienstes  
   - Konfigurieren der Umgebungsvariablen in `.env`

3. **MCP-Server einrichten**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektstruktur

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

## Kernkomponenten

### 1. Multi-Agenten-System
- GitHub Agent: Repository-Analyse  
- Hackathon Agent: Projekt-Empfehlungen  
- Events Agent: Vorschläge für Tech-Events

### 2. Azure-Integration
- Cognitive Search zur Event-Indizierung  
- Azure OpenAI für Agenten-Intelligenz  
- Umsetzung des RAG-Musters

### 3. MCP-Tools
- Analyse von GitHub-Repositories  
- Code-Inspektion  
- Metadatenextraktion

## Code-Durchgang

Das Beispiel zeigt:  
1. Integration des MCP-Servers  
2. Orchestrierung von Multi-Agenten  
3. Integration von Azure Cognitive Search  
4. Umsetzung des RAG-Musters

Wichtige Funktionen:  
- Echtzeit-Analyse von GitHub-Repositories  
- Intelligente Projekt-Empfehlungen  
- Event-Abgleich mit Azure Search  
- Streaming-Antworten mit Chainlit

## Ausführen des Beispiels

Für detaillierte Einrichtungshinweise und weitere Informationen siehe die [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. MCP-Server starten:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Anwendung starten:  
   ```bash
   chainlit run app.py -w
   ```

3. Integration testen:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Fehlerbehebung

Häufige Probleme und Lösungen:  
1. MCP-Verbindungsprobleme  
   - Prüfen, ob der Server läuft  
   - Verfügbarkeit des Ports prüfen  
   - GitHub-Tokens bestätigen

2. Azure Search-Probleme  
   - Verbindungszeichenfolgen validieren  
   - Vorhandensein des Index prüfen  
   - Dokumenten-Upload überprüfen

## Nächste Schritte
- Weitere MCP-Tools erkunden  
- Eigene Agenten implementieren  
- RAG-Funktionalitäten erweitern  
- Weitere Event-Quellen hinzufügen

## Ressourcen
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.