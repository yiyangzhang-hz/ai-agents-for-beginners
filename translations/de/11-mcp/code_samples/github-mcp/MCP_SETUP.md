<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:14:09+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "de"
}
-->
# MCP Server Integrationsanleitung

## Voraussetzungen
- Node.js installiert (Version 14 oder höher)
- npm Paketmanager
- Python-Umgebung mit den benötigten Abhängigkeiten

## Einrichtungsschritte

1. **MCP Server Paket installieren**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCP Server starten**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Der Server sollte starten und eine Verbindungs-URL anzeigen.

3. **Verbindung überprüfen**  
   - Achte auf das Stecker-Symbol (🔌) in deiner Chainlit-Oberfläche  
   - Neben dem Stecker-Symbol sollte eine Zahl (1) erscheinen, die eine erfolgreiche Verbindung anzeigt  
   - Die Konsole sollte anzeigen: "GitHub plugin setup completed successfully" (zusammen mit weiteren Statusmeldungen)

## Fehlerbehebung

### Häufige Probleme

1. **Port-Konflikt**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Lösung: Ändere den Port mit:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Authentifizierungsprobleme**  
   - Stelle sicher, dass die GitHub-Zugangsdaten korrekt konfiguriert sind  
   - Prüfe, ob die .env-Datei die erforderlichen Tokens enthält  
   - Überprüfe den Zugriff auf die GitHub API

3. **Verbindung fehlgeschlagen**  
   - Vergewissere dich, dass der Server auf dem erwarteten Port läuft  
   - Prüfe die Firewall-Einstellungen  
   - Stelle sicher, dass die Python-Umgebung die benötigten Pakete installiert hat

## Verbindungsüberprüfung

Dein MCP Server ist korrekt verbunden, wenn:  
1. Die Konsole "GitHub plugin setup completed successfully" anzeigt  
2. Die Verbindungsprotokolle "✓ MCP Connection Status: Active" zeigen  
3. GitHub-Befehle in der Chat-Oberfläche funktionieren

## Umgebungsvariablen

Erforderlich in deiner .env-Datei:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Verbindung testen

Sende diese Testnachricht im Chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Eine erfolgreiche Antwort zeigt Informationen zum Repository an.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.