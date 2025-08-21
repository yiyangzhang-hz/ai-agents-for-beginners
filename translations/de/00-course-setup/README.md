<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8693a24942b670e3cb8def77f92513f9",
  "translation_date": "2025-08-21T12:07:42+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Kursvorbereitung

## Einführung

In dieser Lektion erfahren Sie, wie Sie die Codebeispiele dieses Kurses ausführen können.

## Dieses Repository klonen oder forken

Beginnen Sie damit, das GitHub-Repository zu klonen oder zu forken. Dadurch erhalten Sie Ihre eigene Version des Kursmaterials, mit der Sie den Code ausführen, testen und anpassen können!

Dies kann durch Klicken auf den Link erfolgen.

Sie sollten nun Ihre eigene geforkte Version dieses Kurses unter folgendem Link haben:

![Geforktes Repository](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.de.png)

## Code ausführen

Dieser Kurs bietet eine Reihe von Jupyter Notebooks, die Sie ausführen können, um praktische Erfahrungen beim Erstellen von KI-Agenten zu sammeln.

Die Codebeispiele verwenden entweder:

**Erfordert ein GitHub-Konto - Kostenlos**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Beschriftet als (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Beschriftet als (autogen.ipynb)

**Erfordert ein Azure-Abonnement**:
3) Azure AI Foundry + Azure AI Agent Service. Beschriftet als (azureaiagent.ipynb)

Wir empfehlen Ihnen, alle drei Beispieltypen auszuprobieren, um herauszufinden, welcher am besten für Sie geeignet ist.

Die von Ihnen gewählte Option bestimmt, welche Einrichtungsschritte Sie unten befolgen müssen:

## Anforderungen

- Python 3.12+
  - **HINWEIS**: Falls Sie Python 3.12 nicht installiert haben, stellen Sie sicher, dass Sie es installieren. Erstellen Sie dann Ihre virtuelle Umgebung (venv) mit Python 3.12, um sicherzustellen, dass die richtigen Versionen aus der Datei requirements.txt installiert werden.
- Ein GitHub-Konto - Für den Zugriff auf den GitHub Models Marketplace
- Azure-Abonnement - Für den Zugriff auf Azure AI Foundry
- Azure AI Foundry-Konto - Für den Zugriff auf den Azure AI Agent Service

Wir haben eine `requirements.txt`-Datei im Stammverzeichnis dieses Repositorys beigefügt, die alle erforderlichen Python-Pakete enthält, um die Codebeispiele auszuführen.

Sie können diese installieren, indem Sie den folgenden Befehl in Ihrem Terminal im Stammverzeichnis des Repositorys ausführen:

```bash
pip install -r requirements.txt
```
Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

## VSCode einrichten
Stellen Sie sicher, dass Sie die richtige Python-Version in VSCode verwenden.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Einrichtung für Beispiele mit GitHub-Modellen 

### Schritt 1: Abrufen Ihres GitHub Personal Access Token (PAT)

Dieser Kurs nutzt den GitHub Models Marketplace, der kostenlosen Zugang zu großen Sprachmodellen (LLMs) bietet, die Sie zum Erstellen von KI-Agenten verwenden werden.

Um die GitHub-Modelle zu nutzen, müssen Sie ein [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) erstellen.

Dies kann durch Aufrufen Ihres GitHub-Kontos erfolgen.

Bitte befolgen Sie das [Prinzip der minimalen Rechtevergabe](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) beim Erstellen Ihres Tokens. Das bedeutet, dass Sie dem Token nur die Berechtigungen geben sollten, die es benötigt, um die Codebeispiele in diesem Kurs auszuführen.

1. Wählen Sie die Option `Fine-grained tokens` auf der linken Seite Ihres Bildschirms, indem Sie zu den **Entwicklereinstellungen** navigieren.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.de.png)

    Wählen Sie dann `Generate new token`.

    ![Token generieren](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.de.png)

2. Geben Sie einen beschreibenden Namen für Ihr Token ein, der seinen Zweck widerspiegelt, damit es später leicht zu identifizieren ist.

    🔐 Empfehlung zur Token-Dauer

    Empfohlene Dauer: 30 Tage
    Für eine sicherere Haltung können Sie eine kürzere Dauer wählen – z. B. 7 Tage 🛡️
    Dies ist eine großartige Möglichkeit, sich ein persönliches Ziel zu setzen und den Kurs abzuschließen, während Ihre Lernmotivation hoch ist 🚀.

    ![Token-Name und Ablaufdatum](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.de.png)

3. Begrenzen Sie den Umfang des Tokens auf Ihren Fork dieses Repositorys.

    ![Umfang auf Fork-Repository begrenzen](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.de.png)

4. Beschränken Sie die Berechtigungen des Tokens: Unter **Permissions** klicken Sie auf den Tab **Account** und dann auf die Schaltfläche "+ Add permissions". Es erscheint ein Dropdown-Menü. Suchen Sie nach **Models** und aktivieren Sie das Kontrollkästchen dafür.
    ![Models-Berechtigung hinzufügen](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.de.png)

5. Überprüfen Sie die erforderlichen Berechtigungen, bevor Sie das Token generieren. ![Berechtigungen überprüfen](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.de.png)

6. Bevor Sie das Token generieren, stellen Sie sicher, dass Sie bereit sind, das Token an einem sicheren Ort wie einem Passwort-Manager-Tresor zu speichern, da es nach der Erstellung nicht erneut angezeigt wird. ![Token sicher speichern](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.de.png)

Kopieren Sie Ihr neu erstelltes Token. Sie werden es nun Ihrer `.env`-Datei hinzufügen, die in diesem Kurs enthalten ist.

### Schritt 2: Erstellen Ihrer `.env`-Datei

Um Ihre `.env`-Datei zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus.

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env`-Datei in Ihrem Verzeichnis, in der Sie die Werte für die Umgebungsvariablen ausfüllen.

Nachdem Sie Ihr Token kopiert haben, öffnen Sie die `.env`-Datei in Ihrem bevorzugten Texteditor und fügen Sie Ihr Token in das Feld `GITHUB_TOKEN` ein.
![GitHub Token Feld](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.de.png)

Sie sollten nun in der Lage sein, die Codebeispiele dieses Kurses auszuführen.

## Einrichtung für Beispiele mit Azure AI Foundry und Azure AI Agent Service

### Schritt 1: Abrufen Ihres Azure-Projektendpunkts

Befolgen Sie die Schritte zur Erstellung eines Hubs und Projekts in Azure AI Foundry, die hier zu finden sind: [Hub-Ressourcenübersicht](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Sobald Sie Ihr Projekt erstellt haben, müssen Sie die Verbindungszeichenfolge für Ihr Projekt abrufen.

Dies kann durch Aufrufen der **Übersicht**-Seite Ihres Projekts im Azure AI Foundry-Portal erfolgen.

![Projekt-Verbindungszeichenfolge](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.de.png)

### Schritt 2: Erstellen Ihrer `.env`-Datei

Um Ihre `.env`-Datei zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus.

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env`-Datei in Ihrem Verzeichnis, in der Sie die Werte für die Umgebungsvariablen ausfüllen.

Nachdem Sie Ihr Token kopiert haben, öffnen Sie die `.env`-Datei in Ihrem bevorzugten Texteditor und fügen Sie Ihr Token in das Feld `PROJECT_ENDPOINT` ein.

### Schritt 3: Anmeldung bei Azure

Als Sicherheitsbest Practice verwenden wir [schlüssellose Authentifizierung](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), um sich bei Azure OpenAI mit Microsoft Entra ID zu authentifizieren.

Öffnen Sie als Nächstes ein Terminal und führen Sie `az login --use-device-code` aus, um sich bei Ihrem Azure-Konto anzumelden.

Sobald Sie sich angemeldet haben, wählen Sie Ihr Abonnement im Terminal aus.

## Zusätzliche Umgebungsvariablen - Azure Search und Azure OpenAI 

Für die Agentic RAG-Lektion - Lektion 5 - gibt es Beispiele, die Azure Search und Azure OpenAI verwenden.

Wenn Sie diese Beispiele ausführen möchten, müssen Sie die folgenden Umgebungsvariablen zu Ihrer `.env`-Datei hinzufügen:

### Übersichtsseite (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Überprüfen Sie **Projektdetails** auf der **Übersicht**-Seite Ihres Projekts.

- `AZURE_AI_PROJECT_NAME` - Schauen Sie oben auf der **Übersicht**-Seite Ihres Projekts.

- `AZURE_OPENAI_SERVICE` - Finden Sie dies im Tab **Included capabilities** für **Azure OpenAI Service** auf der **Übersicht**-Seite.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Gehen Sie zu **Projekteigenschaften** auf der **Übersicht**-Seite des **Management Centers**.

- `GLOBAL_LLM_SERVICE` - Unter **Connected resources** finden Sie den Verbindungsnamen für **Azure AI Services**. Falls nicht aufgeführt, überprüfen Sie das **Azure-Portal** unter Ihrer Ressourcengruppe nach dem Ressourcennamen der AI Services.

### Modelle + Endpunktsseite

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Wählen Sie Ihr Einbettungsmodell (z. B. `text-embedding-ada-002`) und notieren Sie den **Bereitstellungsnamen** aus den Modelldetails.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Wählen Sie Ihr Chat-Modell (z. B. `gpt-4o-mini`) und notieren Sie den **Bereitstellungsnamen** aus den Modelldetails.

### Azure-Portal

- `AZURE_OPENAI_ENDPOINT` - Suchen Sie nach **Azure AI Services**, klicken Sie darauf, gehen Sie dann zu **Ressourcenverwaltung**, **Schlüssel und Endpunkt**, scrollen Sie zu den "Azure OpenAI Endpunkten" und kopieren Sie denjenigen, der "Language APIs" sagt.

- `AZURE_OPENAI_API_KEY` - Kopieren Sie auf demselben Bildschirm SCHLÜSSEL 1 oder SCHLÜSSEL 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Finden Sie Ihre **Azure AI Search**-Ressource, klicken Sie darauf und sehen Sie **Übersicht**.

- `AZURE_SEARCH_API_KEY` - Gehen Sie dann zu **Einstellungen** und dann **Schlüssel**, um den primären oder sekundären Administratorschlüssel zu kopieren.

### Externe Webseite

- `AZURE_OPENAI_API_VERSION` - Besuchen Sie die Seite [API-Version-Lebenszyklus](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) unter **Latest GA API release**.

### Einrichtung schlüsselloser Authentifizierung

Anstatt Ihre Anmeldeinformationen fest zu codieren, verwenden wir eine schlüssellose Verbindung mit Azure OpenAI. Dazu importieren wir `DefaultAzureCredential` und rufen später die Funktion `DefaultAzureCredential` auf, um die Anmeldeinformationen zu erhalten.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Irgendwo festgefahren?

Falls Sie Probleme bei der Einrichtung haben, treten Sie unserem

## Nächste Lektion

Sie sind nun bereit, den Code für diesen Kurs auszuführen. Viel Spaß beim Lernen über die Welt der KI-Agenten! 

[Einführung in KI-Agenten und Anwendungsfälle von Agenten](../01-intro-to-ai-agents/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.