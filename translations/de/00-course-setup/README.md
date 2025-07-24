<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:08:11+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Kursvorbereitung

## Einführung

In dieser Lektion erfahren Sie, wie Sie die Codebeispiele dieses Kurses ausführen können.

## Dieses Repository klonen oder forken

Um zu beginnen, klonen oder forken Sie bitte das GitHub-Repository. Dadurch erstellen Sie Ihre eigene Version des Kursmaterials, sodass Sie den Code ausführen, testen und anpassen können!

Dies kann durch Klicken auf den Link zu Ihrem eigenen geforkten Repository erfolgen:

![Geforktes Repository](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.de.png)

## Den Code ausführen

Dieser Kurs bietet eine Reihe von Jupyter Notebooks, die Sie ausführen können, um praktische Erfahrungen beim Erstellen von KI-Agenten zu sammeln.

Die Codebeispiele verwenden entweder:

**Erfordert ein kostenloses GitHub-Konto**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Gekennzeichnet als (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Gekennzeichnet als (autogen.ipynb)  

**Erfordert ein Azure-Abonnement**:  
3) Azure AI Foundry + Azure AI Agent Service. Gekennzeichnet als (azureaiagent.ipynb)  

Wir empfehlen Ihnen, alle drei Arten von Beispielen auszuprobieren, um herauszufinden, welche für Sie am besten geeignet ist.

Die von Ihnen gewählte Option bestimmt, welche Einrichtungsschritte Sie im Folgenden ausführen müssen:

## Anforderungen

- Python 3.12+  
  - **HINWEIS**: Falls Python 3.12 nicht installiert ist, stellen Sie sicher, dass Sie es installieren. Erstellen Sie dann Ihre virtuelle Umgebung (venv) mit Python 3.12, um sicherzustellen, dass die richtigen Versionen aus der Datei `requirements.txt` installiert werden.
- Ein GitHub-Konto – für den Zugriff auf den GitHub Models Marketplace
- Ein Azure-Abonnement – für den Zugriff auf Azure AI Foundry
- Ein Azure AI Foundry-Konto – für den Zugriff auf den Azure AI Agent Service

Wir haben eine Datei `requirements.txt` im Stammverzeichnis dieses Repositories bereitgestellt, die alle erforderlichen Python-Pakete enthält, um die Codebeispiele auszuführen.

Sie können diese Pakete installieren, indem Sie den folgenden Befehl im Terminal im Stammverzeichnis des Repositories ausführen:

```bash
pip install -r requirements.txt
```

Wir empfehlen, eine Python-virtuelle Umgebung zu erstellen, um Konflikte und Probleme zu vermeiden.

## VSCode einrichten

Stellen Sie sicher, dass Sie die richtige Python-Version in VSCode verwenden.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Einrichtung für Beispiele mit GitHub-Modellen

### Schritt 1: Abrufen Ihres GitHub Personal Access Token (PAT)

Dieser Kurs nutzt den GitHub Models Marketplace, der kostenlosen Zugriff auf Large Language Models (LLMs) bietet, die Sie zum Erstellen von KI-Agenten verwenden werden.

Um die GitHub-Modelle zu nutzen, müssen Sie ein [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) erstellen.

Dies kann in Ihrem GitHub-Konto erfolgen.

Bitte befolgen Sie das [Prinzip der minimalen Rechtevergabe](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely), wenn Sie Ihr Token erstellen. Das bedeutet, dass Sie dem Token nur die Berechtigungen geben, die es benötigt, um die Codebeispiele in diesem Kurs auszuführen.

1. Wählen Sie auf der linken Seite Ihrer Bildschirmansicht die Option `Fine-grained tokens`.

    Wählen Sie dann `Generate new token`.

    ![Token generieren](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.de.png)

1. Geben Sie einen beschreibenden Namen für Ihr Token ein, der seinen Zweck widerspiegelt, damit es später leicht zu identifizieren ist. Legen Sie ein Ablaufdatum fest (empfohlen: 30 Tage; Sie können auch eine kürzere Dauer wie 7 Tage wählen, wenn Sie eine sicherere Vorgehensweise bevorzugen).

    ![Token-Name und Ablaufdatum](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.de.png)

1. Beschränken Sie den Geltungsbereich des Tokens auf Ihren Fork dieses Repositories.

    ![Geltungsbereich auf Fork-Repository beschränken](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.de.png)

1. Beschränken Sie die Berechtigungen des Tokens: Unter **Permissions** aktivieren Sie **Account Permissions**, navigieren zu **Models** und aktivieren nur den erforderlichen Lesezugriff für GitHub-Modelle.

    ![Kontoberechtigungen](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.de.png)

    ![Modelle Lesezugriff](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.de.png)

Kopieren Sie Ihr neu erstelltes Token. Sie werden es nun in Ihre `.env`-Datei einfügen, die in diesem Kurs enthalten ist.

### Schritt 2: Erstellen Ihrer `.env`-Datei

Um Ihre `.env`-Datei zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env`-Datei in Ihrem Verzeichnis, in der Sie die Werte für die Umgebungsvariablen eintragen.

Öffnen Sie die `.env`-Datei in Ihrem bevorzugten Texteditor und fügen Sie Ihr kopiertes Token in das Feld `GITHUB_TOKEN` ein.

Sie sollten nun in der Lage sein, die Codebeispiele dieses Kurses auszuführen.

## Einrichtung für Beispiele mit Azure AI Foundry und Azure AI Agent Service

### Schritt 1: Abrufen Ihres Azure-Projektendpunkts

Befolgen Sie die Schritte zur Erstellung eines Hubs und Projekts in Azure AI Foundry, die hier beschrieben sind: [Hub-Ressourcenübersicht](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources).

Sobald Sie Ihr Projekt erstellt haben, müssen Sie die Verbindungszeichenfolge für Ihr Projekt abrufen.

Dies kann auf der **Übersichtsseite** Ihres Projekts im Azure AI Foundry-Portal erfolgen.

![Projekt-Verbindungszeichenfolge](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.de.png)

### Schritt 2: Erstellen Ihrer `.env`-Datei

Um Ihre `.env`-Datei zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
cp .env.example .env
```

Dies kopiert die Beispieldatei und erstellt eine `.env`-Datei in Ihrem Verzeichnis, in der Sie die Werte für die Umgebungsvariablen eintragen.

Öffnen Sie die `.env`-Datei in Ihrem bevorzugten Texteditor und fügen Sie Ihr kopiertes Token in das Feld `PROJECT_ENDPOINT` ein.

### Schritt 3: Anmeldung bei Azure

Als Sicherheitsbest-Practice verwenden wir [schlüssellose Authentifizierung](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst), um uns bei Azure OpenAI mit Microsoft Entra ID zu authentifizieren.

Öffnen Sie ein Terminal und führen Sie `az login --use-device-code` aus, um sich bei Ihrem Azure-Konto anzumelden.

Nach der Anmeldung wählen Sie Ihr Abonnement im Terminal aus.

## Zusätzliche Umgebungsvariablen – Azure Search und Azure OpenAI

Für die Agentic RAG-Lektion – Lektion 5 – gibt es Beispiele, die Azure Search und Azure OpenAI verwenden.

Wenn Sie diese Beispiele ausführen möchten, müssen Sie die folgenden Umgebungsvariablen zu Ihrer `.env`-Datei hinzufügen:

### Übersichtsseite (Projekt)

- `AZURE_SUBSCRIPTION_ID` – Überprüfen Sie **Projektdetails** auf der **Übersichtsseite** Ihres Projekts.
- `AZURE_AI_PROJECT_NAME` – Schauen Sie oben auf der **Übersichtsseite** Ihres Projekts.
- `AZURE_OPENAI_SERVICE` – Finden Sie dies im Tab **Eingeschlossene Funktionen** für **Azure OpenAI Service** auf der **Übersichtsseite**.

### Verwaltungszentrum

- `AZURE_OPENAI_RESOURCE_GROUP` – Gehen Sie zu **Projekteigenschaften** auf der **Übersichtsseite** des **Verwaltungszentrums**.
- `GLOBAL_LLM_SERVICE` – Unter **Verbundene Ressourcen** finden Sie den **Azure AI Services** Verbindungsnamen. Falls nicht aufgeführt, überprüfen Sie das **Azure-Portal** unter Ihrer Ressourcengruppe nach dem Namen der AI Services-Ressource.

### Modelle + Endpunkte-Seite

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` – Wählen Sie Ihr Einbettungsmodell (z. B. `text-embedding-ada-002`) und notieren Sie den **Bereitstellungsnamen** aus den Modelldetails.
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` – Wählen Sie Ihr Chat-Modell (z. B. `gpt-4o-mini`) und notieren Sie den **Bereitstellungsnamen** aus den Modelldetails.

### Azure-Portal

- `AZURE_OPENAI_ENDPOINT` – Suchen Sie nach **Azure AI Services**, klicken Sie darauf, gehen Sie zu **Ressourcenverwaltung**, **Schlüssel und Endpunkt**, scrollen Sie zu den "Azure OpenAI-Endpunkten" und kopieren Sie den, der "Language APIs" sagt.
- `AZURE_OPENAI_API_KEY` – Kopieren Sie auf demselben Bildschirm SCHLÜSSEL 1 oder SCHLÜSSEL 2.
- `AZURE_SEARCH_SERVICE_ENDPOINT` – Finden Sie Ihre **Azure AI Search**-Ressource, klicken Sie darauf und sehen Sie **Übersicht**.
- `AZURE_SEARCH_API_KEY` – Gehen Sie dann zu **Einstellungen** und dann **Schlüssel**, um den primären oder sekundären Administratorschlüssel zu kopieren.

### Externe Webseite

- `AZURE_OPENAI_API_VERSION` – Besuchen Sie die Seite [API-Version-Lebenszyklus](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) unter **Neueste GA-API-Version**.

### Schlüssellose Authentifizierung einrichten

Anstatt Ihre Anmeldedaten fest zu codieren, verwenden wir eine schlüssellose Verbindung mit Azure OpenAI. Dazu importieren wir `DefaultAzureCredential` und rufen später die Funktion `DefaultAzureCredential` auf, um die Anmeldedaten abzurufen.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Irgendwo festgefahren?

Falls Sie Probleme bei der Einrichtung haben, treten Sie unserer...

## Nächste Lektion

Sie sind nun bereit, den Code für diesen Kurs auszuführen. Viel Spaß beim Lernen über die Welt der KI-Agenten!

[Einführung in KI-Agenten und Anwendungsfälle](../01-intro-to-ai-agents/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.