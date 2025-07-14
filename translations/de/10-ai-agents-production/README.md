<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:34:42+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "de"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.de.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Klicken Sie auf das Bild oben, um das Video zu dieser Lektion anzusehen)_
# KI-Agenten in der Produktion

## Einführung

In dieser Lektion behandeln wir:

- Wie Sie die Bereitstellung Ihres KI-Agenten in der Produktion effektiv planen.
- Häufige Fehler und Probleme, die bei der Bereitstellung Ihres KI-Agenten in der Produktion auftreten können.
- Wie Sie Kosten kontrollieren und gleichzeitig die Leistung Ihres KI-Agenten aufrechterhalten.

## Lernziele

Nach Abschluss dieser Lektion wissen Sie, wie Sie/verstehen Sie:

- Techniken zur Verbesserung der Leistung, der Kosten und der Effektivität eines KI-Agenten-Systems in der Produktion.
- Was und wie Sie Ihre KI-Agenten bewerten können.
- Wie Sie die Kosten bei der Bereitstellung von KI-Agenten in der Produktion steuern.

Es ist wichtig, vertrauenswürdige KI-Agenten bereitzustellen. Schauen Sie sich auch die Lektion „Building Trustworthy AI Agents“ an.

## Bewertung von KI-Agenten

Vor, während und nach der Bereitstellung von KI-Agenten ist es entscheidend, ein geeignetes System zur Bewertung Ihrer KI-Agenten zu haben. So stellen Sie sicher, dass Ihr System mit Ihren und den Zielen Ihrer Nutzer übereinstimmt.

Um einen KI-Agenten zu bewerten, ist es wichtig, nicht nur die Ausgabe des Agenten, sondern auch das gesamte System, in dem Ihr KI-Agent arbeitet, zu bewerten. Dazu gehören unter anderem:

- Die ursprüngliche Modellanfrage.
- Die Fähigkeit des Agenten, die Absicht des Nutzers zu erkennen.
- Die Fähigkeit des Agenten, das richtige Werkzeug für die Aufgabe auszuwählen.
- Die Antwort des Werkzeugs auf die Anfrage des Agenten.
- Die Fähigkeit des Agenten, die Antwort des Werkzeugs zu interpretieren.
- Das Feedback des Nutzers auf die Antwort des Agenten.

So können Sie Verbesserungsmöglichkeiten modularer erkennen. Außerdem können Sie die Auswirkungen von Änderungen an Modellen, Eingabeaufforderungen, Werkzeugen und anderen Komponenten effizienter überwachen.

## Häufige Probleme und mögliche Lösungen bei KI-Agenten

| **Problem**                                    | **Mögliche Lösung**                                                                                                                                                                                                        |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| KI-Agent führt Aufgaben nicht konsistent aus   | - Verfeinern Sie die Eingabeaufforderung für den KI-Agenten; seien Sie klar in den Zielen.<br>- Prüfen Sie, ob das Aufteilen der Aufgaben in Teilaufgaben und deren Bearbeitung durch mehrere Agenten hilfreich ist.          |
| KI-Agent gerät in Endlosschleifen              | - Stellen Sie klare Abbruchbedingungen sicher, damit der Agent weiß, wann er den Prozess beenden soll.<br>- Für komplexe Aufgaben, die Planung und Schlussfolgerungen erfordern, verwenden Sie ein größeres Modell, das darauf spezialisiert ist. |
| Werkzeugaufrufe des KI-Agenten funktionieren nicht gut | - Testen und validieren Sie die Ausgabe des Werkzeugs außerhalb des Agentensystems.<br>- Verfeinern Sie die definierten Parameter, Eingabeaufforderungen und die Benennung der Werkzeuge.                                   |
| Multi-Agenten-System arbeitet nicht konsistent | - Verfeinern Sie die Eingabeaufforderungen für jeden Agenten, damit sie spezifisch und voneinander unterscheidbar sind.<br>- Bauen Sie ein hierarchisches System mit einem „Routing“- oder Steuerungsagenten auf, der bestimmt, welcher Agent der richtige ist. |

## Kostenmanagement

Hier einige Strategien, um die Kosten bei der Bereitstellung von KI-Agenten in der Produktion zu steuern:

- **Antworten zwischenspeichern** – Häufige Anfragen und Aufgaben zu identifizieren und die Antworten bereitzustellen, bevor sie durch Ihr Agentensystem laufen, ist eine gute Möglichkeit, das Volumen ähnlicher Anfragen zu reduzieren. Sie können sogar einen Ablauf implementieren, der mithilfe einfacherer KI-Modelle ermittelt, wie ähnlich eine Anfrage zu den zwischengespeicherten Anfragen ist.

- **Verwendung kleinerer Modelle** – Kleine Sprachmodelle (SLMs) können bei bestimmten agentenbasierten Anwendungsfällen gute Leistungen erbringen und die Kosten erheblich senken. Wie bereits erwähnt, ist der Aufbau eines Bewertungssystems, um die Leistung im Vergleich zu größeren Modellen zu bestimmen und zu vergleichen, der beste Weg, um zu verstehen, wie gut ein SLM in Ihrem Anwendungsfall funktioniert.

- **Einsatz eines Router-Modells** – Eine ähnliche Strategie ist die Nutzung verschiedener Modelle und Größen. Sie können ein LLM/SLM oder eine serverlose Funktion verwenden, um Anfragen je nach Komplexität an die am besten geeigneten Modelle weiterzuleiten. Dies hilft ebenfalls, Kosten zu senken und gleichzeitig die Leistung bei den richtigen Aufgaben sicherzustellen.

## Glückwunsch

Dies ist derzeit die letzte Lektion von „AI Agents for Beginners“.

Wir planen, basierend auf Feedback und Entwicklungen in dieser ständig wachsenden Branche weitere Lektionen hinzuzufügen. Schauen Sie also bald wieder vorbei.

Wenn Sie Ihr Lernen und Ihre Arbeit mit KI-Agenten fortsetzen möchten, treten Sie dem <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> bei.

Dort veranstalten wir Workshops, Community-Roundtables und „Ask me anything“-Sessions.

Außerdem haben wir eine Learn-Sammlung mit zusätzlichen Materialien, die Ihnen den Einstieg in den Aufbau von KI-Agenten in der Produktion erleichtern.

## Vorherige Lektion

[Metacognition Design Pattern](../09-metacognition/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.