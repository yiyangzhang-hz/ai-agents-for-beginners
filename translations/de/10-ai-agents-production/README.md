<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-23T08:08:42+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "de"
}
-->
# KI-Agenten in der Produktion: Beobachtbarkeit & Bewertung

Wenn KI-Agenten von experimentellen Prototypen zu realen Anwendungen übergehen, wird die Fähigkeit, ihr Verhalten zu verstehen, ihre Leistung zu überwachen und ihre Ergebnisse systematisch zu bewerten, entscheidend.

## Lernziele

Nach Abschluss dieser Lektion werden Sie wissen/verstehen:
- Grundkonzepte der Beobachtbarkeit und Bewertung von Agenten
- Techniken zur Verbesserung der Leistung, Kosten und Effektivität von Agenten
- Was und wie Sie Ihre KI-Agenten systematisch bewerten können
- Wie Sie die Kosten bei der Bereitstellung von KI-Agenten in der Produktion kontrollieren können
- Wie Sie Agenten, die mit AutoGen erstellt wurden, instrumentieren können

Das Ziel ist, Sie mit dem Wissen auszustatten, um Ihre "Black-Box"-Agenten in transparente, handhabbare und zuverlässige Systeme zu verwandeln.

_**Hinweis:** Es ist wichtig, KI-Agenten bereitzustellen, die sicher und vertrauenswürdig sind. Sehen Sie sich die Lektion [Vertrauenswürdige KI-Agenten erstellen](./06-building-trustworthy-agents/README.md) an._

## Traces und Spans

Beobachtungswerkzeuge wie [Langfuse](https://langfuse.com/) oder [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) stellen Agentenläufe normalerweise als Traces und Spans dar.

- **Trace** repräsentiert eine vollständige Agentenaufgabe von Anfang bis Ende (z. B. die Bearbeitung einer Benutzeranfrage).
- **Spans** sind einzelne Schritte innerhalb des Traces (z. B. der Aufruf eines Sprachmodells oder das Abrufen von Daten).

![Trace-Baum in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Ohne Beobachtbarkeit kann sich ein KI-Agent wie eine "Black Box" anfühlen – sein interner Zustand und seine Argumentation sind undurchsichtig, was es schwierig macht, Probleme zu diagnostizieren oder die Leistung zu optimieren. Mit Beobachtbarkeit werden Agenten zu "Glasboxen", die Transparenz bieten, die entscheidend ist, um Vertrauen aufzubauen und sicherzustellen, dass sie wie beabsichtigt funktionieren.

## Warum Beobachtbarkeit in Produktionsumgebungen wichtig ist

Die Einführung von KI-Agenten in Produktionsumgebungen bringt neue Herausforderungen und Anforderungen mit sich. Beobachtbarkeit ist nicht mehr nur ein "Nice-to-have", sondern eine kritische Fähigkeit:

*   **Fehlerbehebung und Ursachenanalyse**: Wenn ein Agent fehlschlägt oder eine unerwartete Ausgabe erzeugt, liefern Beobachtungswerkzeuge die Traces, die benötigt werden, um die Fehlerquelle zu identifizieren. Dies ist besonders wichtig bei komplexen Agenten, die mehrere LLM-Aufrufe, Werkzeuginteraktionen und bedingte Logik umfassen können.
*   **Latenz- und Kostenmanagement**: KI-Agenten verlassen sich oft auf LLMs und andere externe APIs, die pro Token oder pro Aufruf abgerechnet werden. Beobachtbarkeit ermöglicht eine präzise Verfolgung dieser Aufrufe, um Operationen zu identifizieren, die übermäßig langsam oder teuer sind. Dies hilft Teams, Prompts zu optimieren, effizientere Modelle auszuwählen oder Workflows neu zu gestalten, um Betriebskosten zu verwalten und eine gute Benutzererfahrung zu gewährleisten.
*   **Vertrauen, Sicherheit und Compliance**: In vielen Anwendungen ist es wichtig sicherzustellen, dass Agenten sicher und ethisch handeln. Beobachtbarkeit bietet eine Prüfspur der Aktionen und Entscheidungen des Agenten. Dies kann verwendet werden, um Probleme wie Prompt Injection, die Generierung schädlicher Inhalte oder den unsachgemäßen Umgang mit personenbezogenen Daten (PII) zu erkennen und zu beheben. Beispielsweise können Sie Traces überprüfen, um zu verstehen, warum ein Agent eine bestimmte Antwort gegeben oder ein bestimmtes Werkzeug verwendet hat.
*   **Kontinuierliche Verbesserungszyklen**: Beobachtungsdaten sind die Grundlage eines iterativen Entwicklungsprozesses. Durch die Überwachung der Leistung von Agenten in der realen Welt können Teams Verbesserungsbereiche identifizieren, Daten für die Feinabstimmung von Modellen sammeln und die Auswirkungen von Änderungen validieren. Dies schafft eine Feedback-Schleife, bei der Produktionsinformationen aus der Online-Bewertung Offline-Experimente und -Verfeinerungen informieren, was zu einer schrittweisen Verbesserung der Agentenleistung führt.

## Wichtige Metriken, die verfolgt werden sollten

Um das Verhalten von Agenten zu überwachen und zu verstehen, sollten eine Reihe von Metriken und Signalen verfolgt werden. Während die spezifischen Metriken je nach Zweck des Agenten variieren können, sind einige universell wichtig.

Hier sind einige der häufigsten Metriken, die von Beobachtungswerkzeugen überwacht werden:

**Latenz:** Wie schnell reagiert der Agent? Lange Wartezeiten wirken sich negativ auf die Benutzererfahrung aus. Sie sollten die Latenz für Aufgaben und einzelne Schritte durch die Verfolgung von Agentenläufen messen. Beispielsweise könnte ein Agent, der 20 Sekunden für alle Modellaufrufe benötigt, durch die Verwendung eines schnelleren Modells oder durch paralleles Ausführen von Modellaufrufen beschleunigt werden.

**Kosten:** Was sind die Kosten pro Agentenlauf? KI-Agenten verlassen sich auf LLM-Aufrufe, die pro Token oder externe APIs abgerechnet werden. Häufige Werkzeugnutzung oder mehrere Prompts können die Kosten schnell erhöhen. Beispielsweise, wenn ein Agent ein LLM fünfmal aufruft, um eine marginale Qualitätsverbesserung zu erzielen, müssen Sie beurteilen, ob die Kosten gerechtfertigt sind oder ob Sie die Anzahl der Aufrufe reduzieren oder ein günstigeres Modell verwenden könnten. Echtzeitüberwachung kann auch unerwartete Spitzen identifizieren (z. B. Fehler, die übermäßige API-Schleifen verursachen).

**Anfragefehler:** Wie viele Anfragen hat der Agent nicht erfolgreich bearbeitet? Dies kann API-Fehler oder fehlgeschlagene Werkzeugaufrufe umfassen. Um Ihren Agenten in der Produktion robuster gegen diese zu machen, können Sie Fallbacks oder Wiederholungen einrichten. Z. B. wenn Anbieter A für LLMs ausfällt, wechseln Sie zu Anbieter B als Backup.

**Benutzerfeedback:** Die Implementierung direkter Benutzerbewertungen liefert wertvolle Einblicke. Dies kann explizite Bewertungen (👍Daumen hoch/👎runter, ⭐1-5 Sterne) oder Textkommentare umfassen. Konsistentes negatives Feedback sollte Sie alarmieren, da dies ein Zeichen dafür ist, dass der Agent nicht wie erwartet funktioniert.

**Implizites Benutzerfeedback:** Benutzerverhalten liefert indirektes Feedback, auch ohne explizite Bewertungen. Dies kann das sofortige Umformulieren von Fragen, wiederholte Anfragen oder das Klicken auf eine Wiederholungsschaltfläche umfassen. Z. B. wenn Sie sehen, dass Benutzer wiederholt dieselbe Frage stellen, ist dies ein Zeichen dafür, dass der Agent nicht wie erwartet funktioniert.

**Genauigkeit:** Wie oft erzeugt der Agent korrekte oder wünschenswerte Ergebnisse? Genauigkeitsdefinitionen variieren (z. B. Problemlösungsgenauigkeit, Informationsabrufgenauigkeit, Benutzerzufriedenheit). Der erste Schritt besteht darin, zu definieren, wie Erfolg für Ihren Agenten aussieht. Sie können die Genauigkeit über automatisierte Prüfungen, Bewertungsscores oder Aufgabenabschlusskennzeichnungen verfolgen. Beispielsweise können Traces als "erfolgreich" oder "fehlgeschlagen" markiert werden.

**Automatisierte Bewertungsmetriken:** Sie können auch automatisierte Bewertungen einrichten. Beispielsweise können Sie ein LLM verwenden, um die Ausgabe des Agenten zu bewerten, z. B. ob sie hilfreich, genau oder nicht ist. Es gibt auch mehrere Open-Source-Bibliotheken, die Ihnen helfen, verschiedene Aspekte des Agenten zu bewerten. Z. B. [RAGAS](https://docs.ragas.io/) für RAG-Agenten oder [LLM Guard](https://llm-guard.com/), um schädliche Sprache oder Prompt Injection zu erkennen.

In der Praxis bietet eine Kombination dieser Metriken die beste Abdeckung der Gesundheit eines KI-Agenten. Im [Beispiel-Notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) dieses Kapitels zeigen wir Ihnen, wie diese Metriken in realen Beispielen aussehen, aber zuerst lernen wir, wie ein typischer Bewertungsworkflow aussieht.

## Instrumentieren Sie Ihren Agenten

Um Tracing-Daten zu sammeln, müssen Sie Ihren Code instrumentieren. Ziel ist es, den Agenten-Code so zu instrumentieren, dass Traces und Metriken ausgegeben werden, die von einer Beobachtungsplattform erfasst, verarbeitet und visualisiert werden können.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) hat sich als Industriestandard für LLM-Beobachtbarkeit etabliert. Es bietet eine Reihe von APIs, SDKs und Tools zum Generieren, Sammeln und Exportieren von Telemetriedaten.

Es gibt viele Instrumentierungsbibliotheken, die bestehende Agenten-Frameworks umschließen und das Exportieren von OpenTelemetry-Spans zu einem Beobachtungswerkzeug erleichtern. Unten finden Sie ein Beispiel zur Instrumentierung eines AutoGen-Agenten mit der [OpenLit-Instrumentierungsbibliothek](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

Das [Beispiel-Notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) in diesem Kapitel zeigt, wie Sie Ihren AutoGen-Agenten instrumentieren können.

**Manuelle Span-Erstellung:** Während Instrumentierungsbibliotheken eine gute Grundlage bieten, gibt es oft Fälle, in denen detailliertere oder benutzerdefinierte Informationen benötigt werden. Sie können Spans manuell erstellen, um benutzerdefinierte Anwendungslogik hinzuzufügen. Noch wichtiger ist, dass sie automatisch oder manuell erstellte Spans mit benutzerdefinierten Attributen (auch bekannt als Tags oder Metadaten) anreichern können. Diese Attribute können geschäftsspezifische Daten, Zwischenberechnungen oder jeden Kontext umfassen, der für Debugging oder Analyse nützlich sein könnte, wie `user_id`, `session_id` oder `model_version`.

Beispiel zur manuellen Erstellung von Traces und Spans mit dem [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agentenbewertung

Beobachtbarkeit liefert uns Metriken, aber die Bewertung ist der Prozess der Analyse dieser Daten (und Durchführung von Tests), um festzustellen, wie gut ein KI-Agent funktioniert und wie er verbessert werden kann. Mit anderen Worten, sobald Sie diese Traces und Metriken haben, wie nutzen Sie sie, um den Agenten zu beurteilen und Entscheidungen zu treffen?

Regelmäßige Bewertung ist wichtig, da KI-Agenten oft nicht-deterministisch sind und sich entwickeln können (durch Updates oder driftendes Modellverhalten) – ohne Bewertung würden Sie nicht wissen, ob Ihr "intelligenter Agent" tatsächlich seine Aufgabe gut erfüllt oder ob er sich verschlechtert hat.

Es gibt zwei Kategorien von Bewertungen für KI-Agenten: **Online-Bewertung** und **Offline-Bewertung**. Beide sind wertvoll und ergänzen sich gegenseitig. Normalerweise beginnen wir mit der Offline-Bewertung, da dies der Mindestschritt ist, bevor ein Agent bereitgestellt wird.

### Offline-Bewertung

![Datensatz-Elemente in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Dies beinhaltet die Bewertung des Agenten in einer kontrollierten Umgebung, typischerweise mit Testdatensätzen, nicht mit Live-Benutzeranfragen. Sie verwenden kuratierte Datensätze, bei denen Sie wissen, was die erwartete Ausgabe oder das korrekte Verhalten ist, und führen dann Ihren Agenten darauf aus.

Beispielsweise, wenn Sie einen Agenten für mathematische Textaufgaben erstellt haben, könnten Sie einen [Testdatensatz](https://huggingface.co/datasets/gsm8k) mit 100 Problemen und bekannten Antworten haben. Offline-Bewertung wird oft während der Entwicklung durchgeführt (und kann Teil von CI/CD-Pipelines sein), um Verbesserungen zu überprüfen oder Regressionen zu verhindern. Der Vorteil ist, dass sie **wiederholbar ist und Sie klare Genauigkeitsmetriken erhalten können, da Sie eine Ground Truth haben**. Sie könnten auch Benutzeranfragen simulieren und die Antworten des Agenten mit idealen Antworten vergleichen oder automatisierte Metriken wie oben beschrieben verwenden.

Die Hauptherausforderung bei der Offline-Bewertung besteht darin, sicherzustellen, dass Ihr Testdatensatz umfassend und relevant bleibt – der Agent könnte auf einem festen Testdatensatz gut abschneiden, aber sehr unterschiedliche Anfragen in der Produktion begegnen. Daher sollten Sie Testdatensätze mit neuen Randfällen und Beispielen aktualisieren, die reale Szenarien widerspiegeln​. Eine Mischung aus kleinen "Smoke-Test"-Fällen und größeren Bewertungssätzen ist nützlich: kleine Sätze für schnelle Überprüfungen und größere für umfassendere Leistungsmetriken​.

### Online-Bewertung

![Übersicht über Beobachtungsmetriken](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Dies bezieht sich auf die Bewertung des Agenten in einer Live-Umgebung, d. h. während der tatsächlichen Nutzung in der Produktion. Online-Bewertung beinhaltet die kontinuierliche Überwachung der Leistung des Agenten bei realen Benutzerinteraktionen und die Analyse der Ergebnisse.

Beispielsweise könnten Sie Erfolgsraten, Benutzerzufriedenheitsbewertungen oder andere Metriken im Live-Verkehr verfolgen. Der Vorteil der Online-Bewertung ist, dass sie **Dinge erfasst, die Sie in einer Laboreinstellung möglicherweise nicht vorhersehen** – Sie können Modelldrift im Laufe der Zeit beobachten (wenn die Effektivität des Agenten abnimmt, während sich Eingabemuster ändern) und unerwartete Anfragen oder Situationen erfassen, die nicht in Ihren Testdaten enthalten waren​. Sie bietet ein echtes Bild davon, wie sich der Agent in der Praxis verhält.

Online-Bewertung beinhaltet oft das Sammeln von implizitem und explizitem Benutzerfeedback, wie besprochen, und möglicherweise das Durchführen von Shadow-Tests oder A/B-Tests (bei denen eine neue Version des Agenten parallel läuft, um mit der alten verglichen zu werden). Die Herausforderung besteht darin, zuverlässige Labels oder Bewertungen für Live-Interaktionen zu erhalten – Sie könnten sich auf Benutzerfeedback oder nachgelagerte Metriken verlassen (z. B. ob der Benutzer auf das Ergebnis geklickt hat).

### Kombination der beiden

Online- und Offline-Bewertungen schließen sich nicht gegenseitig aus; sie ergänzen sich stark. Erkenntnisse aus der Online-Überwachung (z. B. neue Arten von Benutzeranfragen, bei denen der Agent schlecht abschneidet) können verwendet werden, um Offline-Testdatensätze zu erweitern und zu verbessern. Umgekehrt können Agenten, die in Offline-Tests gut abschneiden, dann sicherer bereitgestellt und online überwacht werden.

Tatsächlich übernehmen viele Teams eine Schleife:

_offline bewerten -> bereitstellen -> online überwachen -> neue Fehlerfälle sammeln -> zum Offline-Datensatz hinzufügen -> Agenten verfeinern -> wiederholen_.

## Häufige Probleme

Wenn Sie KI-Agenten in der Produktion bereitstellen, können verschiedene Herausforderungen auftreten. Hier sind einige häufige Probleme und mögliche Lösungen:

| **Problem**    | **Mögliche Lösung**   |
| ------------- | ------------------ |
| KI-Agent führt Aufgaben nicht konsistent aus | - Verfeinern Sie den Prompt, der dem KI-Agenten gegeben wird; seien Sie klar in den Zielen.<br>- Identifizieren Sie, wo das Aufteilen der Aufgaben in Unteraufgaben und deren Bearbeitung durch mehrere Agenten helfen kann. |
| KI-Agent gerät in kontinuierliche Schleifen  | - Stellen Sie sicher, dass Sie klare Beendigungsbedingungen haben, damit der Agent weiß, wann der Prozess beendet werden soll.<br>- Für komplexe Aufgaben, die Argumentation und Planung erfordern, verwenden Sie ein größeres Modell, das auf Argumentationsaufgaben spezialisiert ist. |
| Werkzeugaufrufe des KI-Agenten funktionieren nicht gut   | - Testen und validieren Sie die Ausgabe des Werkzeugs außerhalb des Agentensystems. |

- Verfeinern Sie die definierten Parameter, Eingabeaufforderungen und die Benennung der Tools.  |
| Multi-Agenten-System funktioniert nicht konsistent | - Verfeinern Sie die Eingabeaufforderungen für jeden Agenten, um sicherzustellen, dass sie spezifisch und voneinander unterscheidbar sind.<br>- Erstellen Sie ein hierarchisches System mit einem "Routing"- oder Steuerungsagenten, der bestimmt, welcher Agent der richtige ist. |

Viele dieser Probleme können effektiver erkannt werden, wenn eine Beobachtbarkeit implementiert ist. Die zuvor besprochenen Traces und Metriken helfen dabei, genau zu bestimmen, wo im Workflow des Agenten Probleme auftreten, was das Debugging und die Optimierung erheblich effizienter macht.

## Kostenmanagement

Hier sind einige Strategien, um die Kosten für den Einsatz von KI-Agenten in der Produktion zu verwalten:

**Verwendung kleinerer Modelle:** Kleine Sprachmodelle (Small Language Models, SLMs) können bei bestimmten agentischen Anwendungsfällen gut abschneiden und die Kosten erheblich senken. Wie bereits erwähnt, ist der Aufbau eines Bewertungssystems, um die Leistung im Vergleich zu größeren Modellen zu bestimmen und zu vergleichen, der beste Weg, um zu verstehen, wie gut ein SLM für Ihren Anwendungsfall geeignet ist. Ziehen Sie in Betracht, SLMs für einfachere Aufgaben wie Intent-Klassifikation oder Parameterextraktion zu verwenden, während größere Modelle für komplexes Denken reserviert bleiben.

**Verwendung eines Router-Modells:** Eine ähnliche Strategie besteht darin, eine Vielfalt von Modellen und Größen zu nutzen. Sie können ein LLM/SLM oder eine serverlose Funktion verwenden, um Anfragen basierend auf ihrer Komplexität an die am besten geeigneten Modelle weiterzuleiten. Dies hilft nicht nur, die Kosten zu senken, sondern stellt auch sicher, dass die Leistung für die richtigen Aufgaben gewährleistet ist. Beispielsweise können einfache Anfragen an kleinere, schnellere Modelle weitergeleitet werden, während teure große Modelle nur für komplexe Denkaufgaben verwendet werden.

**Caching von Antworten:** Das Identifizieren häufiger Anfragen und Aufgaben und das Bereitstellen der Antworten, bevor sie durch Ihr agentisches System laufen, ist eine gute Möglichkeit, das Volumen ähnlicher Anfragen zu reduzieren. Sie können sogar einen Ablauf implementieren, um zu erkennen, wie ähnlich eine Anfrage den gecachten Anfragen ist, indem Sie einfachere KI-Modelle verwenden. Diese Strategie kann die Kosten für häufig gestellte Fragen oder gängige Workflows erheblich senken.

## Schauen wir uns an, wie das in der Praxis funktioniert

Im [Beispiel-Notebook dieses Abschnitts](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) sehen wir Beispiele dafür, wie wir Beobachtungstools nutzen können, um unseren Agenten zu überwachen und zu bewerten.

## Vorherige Lektion

[Metakognitions-Designmuster](../09-metacognition/README.md)

## Nächste Lektion

[MCP](../11-mcp/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.