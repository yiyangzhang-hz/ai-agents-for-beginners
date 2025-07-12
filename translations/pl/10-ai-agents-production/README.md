<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:38:22+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "pl"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.pl.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_
# AI Agents w produkcji

## Wprowadzenie

W tej lekcji omówimy:

- Jak skutecznie zaplanować wdrożenie swojego AI Agenta do produkcji.
- Typowe błędy i problemy, które mogą wystąpić podczas wdrażania AI Agenta do produkcji.
- Jak zarządzać kosztami, jednocześnie utrzymując wydajność AI Agenta.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił/zrozumiesz:

- Techniki poprawy wydajności, kosztów i efektywności systemu AI Agenta w produkcji.
- Co i jak oceniać w swoich AI Agentach.
- Jak kontrolować koszty podczas wdrażania AI Agentów do produkcji.

Ważne jest, aby wdrażać AI Agentów, którym można zaufać. Sprawdź również lekcję „Building Trustworthy AI Agents”.

## Ocena AI Agentów

Przed, w trakcie i po wdrożeniu AI Agentów kluczowe jest posiadanie odpowiedniego systemu do ich oceny. Zapewni to, że Twój system będzie zgodny z Twoimi oraz celami użytkowników.

Aby ocenić AI Agenta, ważne jest, aby móc ocenić nie tylko wynik agenta, ale także cały system, w którym działa Twój AI Agent. Obejmuje to między innymi:

- Początkowe zapytanie do modelu.
- Zdolność agenta do rozpoznania intencji użytkownika.
- Zdolność agenta do wyboru odpowiedniego narzędzia do wykonania zadania.
- Odpowiedź narzędzia na zapytanie agenta.
- Zdolność agenta do interpretacji odpowiedzi narzędzia.
- Informacje zwrotne użytkownika dotyczące odpowiedzi agenta.

Dzięki temu możesz zidentyfikować obszary wymagające poprawy w bardziej modułowy sposób. Następnie możesz monitorować wpływ zmian w modelach, promptach, narzędziach i innych komponentach z większą efektywnością.

## Typowe problemy i możliwe rozwiązania z AI Agentami

| **Problem**                                    | **Możliwe rozwiązanie**                                                                                                                                                                                                    |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI Agent nie wykonuje zadań konsekwentnie      | - Doprecyzuj prompt przekazywany do AI Agenta; jasno określ cele.<br>- Zidentyfikuj, gdzie podział zadań na podzadania i obsługa ich przez wielu agentów może pomóc.                                                        |
| AI Agent wpada w ciągłe pętle                   | - Upewnij się, że masz jasne warunki zakończenia, aby Agent wiedział, kiedy przerwać proces.<br>- W przypadku złożonych zadań wymagających rozumowania i planowania, użyj większego modelu specjalizującego się w takich zadaniach. |
| Wywołania narzędzi AI Agenta nie działają dobrze | - Przetestuj i zweryfikuj wyniki narzędzia poza systemem agenta.<br>- Doprecyzuj parametry, prompt i nazewnictwo narzędzi.                                                                                                   |
| System Multi-Agent nie działa spójnie           | - Doprecyzuj prompt dla każdego agenta, aby były specyficzne i różniły się od siebie.<br>- Zbuduj system hierarchiczny z użyciem agenta „routingowego” lub kontrolera, który zdecyduje, który agent jest odpowiedni.          |

## Zarządzanie kosztami

Oto kilka strategii zarządzania kosztami wdrażania AI Agentów do produkcji:

- **Buforowanie odpowiedzi** – Identyfikowanie często powtarzających się zapytań i zadań oraz dostarczanie odpowiedzi zanim trafią do systemu agentowego to dobry sposób na zmniejszenie liczby podobnych zapytań. Możesz nawet wdrożyć mechanizm oceniający podobieństwo zapytania do buforowanych odpowiedzi, korzystając z prostszych modeli AI.

- **Używanie mniejszych modeli** – Małe modele językowe (SLM) mogą dobrze sprawdzać się w niektórych zastosowaniach agentowych i znacznie obniżyć koszty. Jak wspomniano wcześniej, budowa systemu oceny pozwalającego porównać wydajność z większymi modelami to najlepszy sposób, by ocenić, jak dobrze SLM sprawdzi się w Twoim przypadku.

- **Używanie modelu routera** – Podobną strategią jest stosowanie różnorodnych modeli i ich rozmiarów. Możesz użyć LLM/SLM lub funkcji serverless do kierowania zapytań na podstawie ich złożoności do najlepiej dopasowanych modeli. To również pomaga obniżyć koszty, jednocześnie zapewniając wydajność tam, gdzie jest potrzebna.

## Gratulacje

To obecnie ostatnia lekcja z serii „AI Agents for Beginners”.

Planujemy kontynuować dodawanie lekcji na podstawie opinii i zmian w tej dynamicznie rozwijającej się branży, więc zaglądaj do nas ponownie w niedalekiej przyszłości.

Jeśli chcesz kontynuować naukę i rozwijanie AI Agentów, dołącz do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Organizujemy tam warsztaty, spotkania społecznościowe i sesje „ask me anything”.

Mamy też kolekcję Learn z dodatkowymi materiałami, które pomogą Ci zacząć budować AI Agentów w produkcji.

## Poprzednia lekcja

[Metacognition Design Pattern](../09-metacognition/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.