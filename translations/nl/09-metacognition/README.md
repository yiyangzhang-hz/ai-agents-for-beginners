<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8cbf460468c802c7994aa62e0e0779c9",
  "translation_date": "2025-07-12T12:52:34+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "nl"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.nl.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_
# Metacognitie in AI-agenten

## Introductie

Welkom bij de les over metacognitie in AI-agenten! Dit hoofdstuk is bedoeld voor beginners die nieuwsgierig zijn naar hoe AI-agenten kunnen nadenken over hun eigen denkprocessen. Aan het einde van deze les begrijp je de belangrijkste concepten en ben je uitgerust met praktische voorbeelden om metacognitie toe te passen in het ontwerp van AI-agenten.

## Leerdoelen

Na het voltooien van deze les kun je:

1. De gevolgen van redeneer-lussen in agentdefinities begrijpen.
2. Plannings- en evaluatietechnieken gebruiken om zelfcorrigerende agenten te ondersteunen.
3. Je eigen agenten creëren die code kunnen manipuleren om taken uit te voeren.

## Introductie tot Metacognitie

Metacognitie verwijst naar de hogere-orde cognitieve processen waarbij je nadenkt over je eigen denken. Voor AI-agenten betekent dit dat ze hun acties kunnen evalueren en aanpassen op basis van zelfbewustzijn en eerdere ervaringen. Metacognitie, of "nadenken over nadenken," is een belangrijk concept bij de ontwikkeling van agentische AI-systemen. Het houdt in dat AI-systemen zich bewust zijn van hun eigen interne processen en in staat zijn hun gedrag te monitoren, reguleren en aanpassen. Net zoals wij dat doen wanneer we de sfeer peilen of een probleem bekijken. Dit zelfbewustzijn helpt AI-systemen betere beslissingen te nemen, fouten te herkennen en hun prestaties in de loop van de tijd te verbeteren – wat weer terugkoppelt naar de Turing-test en het debat over of AI de macht zal overnemen.

In de context van agentische AI-systemen kan metacognitie helpen bij het aanpakken van verschillende uitdagingen, zoals:
- Transparantie: Zorgen dat AI-systemen hun redeneringen en beslissingen kunnen uitleggen.
- Redeneren: Het vermogen van AI-systemen verbeteren om informatie te synthetiseren en weloverwogen beslissingen te nemen.
- Aanpassing: AI-systemen in staat stellen zich aan te passen aan nieuwe omgevingen en veranderende omstandigheden.
- Waarneming: De nauwkeurigheid van AI-systemen verbeteren bij het herkennen en interpreteren van data uit hun omgeving.

### Wat is Metacognitie?

Metacognitie, of "nadenken over nadenken," is een hogere-orde cognitief proces dat zelfbewustzijn en zelfregulatie van de eigen cognitieve processen omvat. In de wereld van AI stelt metacognitie agenten in staat hun strategieën en acties te evalueren en aan te passen, wat leidt tot verbeterde probleemoplossing en besluitvorming. Door metacognitie te begrijpen, kun je AI-agenten ontwerpen die niet alleen intelligenter zijn, maar ook flexibeler en efficiënter. Bij echte metacognitie zie je dat de AI expliciet nadenkt over haar eigen redeneerproces.

Voorbeeld: “Ik heb goedkopere vluchten gekozen omdat… misschien mis ik directe vluchten, dus ik controleer het nog eens.”  
Bijhouden hoe of waarom een bepaalde route is gekozen.  
- Opmerken dat er fouten zijn gemaakt omdat te veel werd vertrouwd op gebruikersvoorkeuren van de vorige keer, en daarom wordt de besluitvormingsstrategie aangepast, niet alleen de uiteindelijke aanbeveling.  
- Patronen diagnosticeren zoals: “Telkens als ik zie dat de gebruiker ‘te druk’ noemt, moet ik niet alleen bepaalde attracties schrappen, maar ook reflecteren dat mijn methode om ‘topattracties’ te kiezen gebrekkig is als ik altijd op populariteit rangschik.”

### Belang van Metacognitie in AI-agenten

Metacognitie speelt een cruciale rol in het ontwerp van AI-agenten om verschillende redenen:

![Importance of Metacognition](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.nl.png)

- Zelfreflectie: Agenten kunnen hun eigen prestaties beoordelen en verbeterpunten identificeren.
- Aanpassingsvermogen: Agenten kunnen hun strategieën aanpassen op basis van eerdere ervaringen en veranderende omgevingen.
- Foutcorrectie: Agenten kunnen zelfstandig fouten detecteren en corrigeren, wat leidt tot nauwkeurigere resultaten.
- Middelenbeheer: Agenten kunnen het gebruik van middelen, zoals tijd en rekenkracht, optimaliseren door hun acties te plannen en te evalueren.

## Componenten van een AI-agent

Voordat we ingaan op metacognitieve processen, is het belangrijk de basiscomponenten van een AI-agent te begrijpen. Een AI-agent bestaat doorgaans uit:

- Persona: De persoonlijkheid en kenmerken van de agent, die bepalen hoe deze met gebruikers omgaat.
- Tools: De mogelijkheden en functies die de agent kan uitvoeren.
- Vaardigheden: De kennis en expertise die de agent bezit.

Deze componenten werken samen om een "expertiseenheid" te vormen die specifieke taken kan uitvoeren.

**Voorbeeld**:  
Denk aan een reisagent, een agent die niet alleen je vakantie plant, maar ook zijn route aanpast op basis van realtime data en eerdere ervaringen van klanten.

### Voorbeeld: Metacognitie in een Reisagentdienst

Stel je voor dat je een reisagentdienst ontwerpt die wordt aangedreven door AI. Deze agent, "Travel Agent," helpt gebruikers bij het plannen van hun vakanties. Om metacognitie te integreren, moet Travel Agent zijn acties evalueren en aanpassen op basis van zelfbewustzijn en eerdere ervaringen. Zo kan metacognitie een rol spelen:

#### Huidige Taak

De huidige taak is om een gebruiker te helpen een reis naar Parijs te plannen.

#### Stappen om de Taak te Voltooien

1. **Verzamelen van Gebruikersvoorkeuren**: Vraag de gebruiker naar reisdata, budget, interesses (bijv. musea, gastronomie, winkelen) en specifieke wensen.
2. **Informatie Opzoeken**: Zoek naar vluchtopties, accommodaties, attracties en restaurants die passen bij de voorkeuren van de gebruiker.
3. **Aanbevelingen Genereren**: Bied een gepersonaliseerd reisschema aan met vluchtgegevens, hotelreserveringen en voorgestelde activiteiten.
4. **Aanpassen op Basis van Feedback**: Vraag de gebruiker om feedback op de aanbevelingen en pas deze waar nodig aan.

#### Benodigde Middelen

- Toegang tot databases voor vlucht- en hotelboekingen.
- Informatie over Parijse attracties en restaurants.
- Gebruikersfeedback van eerdere interacties.

#### Ervaring en Zelfreflectie

Travel Agent gebruikt metacognitie om zijn prestaties te evalueren en te leren van eerdere ervaringen. Bijvoorbeeld:

1. **Analyseren van Gebruikersfeedback**: Travel Agent bekijkt de feedback om te bepalen welke aanbevelingen goed werden ontvangen en welke niet. Op basis daarvan past hij toekomstige suggesties aan.
2. **Aanpassingsvermogen**: Als een gebruiker eerder heeft aangegeven drukke plekken te vermijden, zal Travel Agent in de toekomst populaire toeristische plekken tijdens piekuren vermijden.
3. **Foutcorrectie**: Als Travel Agent in het verleden een fout maakte, zoals het aanbevelen van een hotel dat volgeboekt was, leert hij om beschikbaarheid strenger te controleren voordat hij aanbevelingen doet.

#### Praktisch Voorbeeld voor Ontwikkelaars

Hier is een vereenvoudigd voorbeeld van hoe de code van Travel Agent eruit zou kunnen zien met metacognitie:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Waarom Metacognitie Belangrijk Is

- **Zelfreflectie**: Agenten kunnen hun prestaties analyseren en verbeterpunten identificeren.
- **Aanpassingsvermogen**: Agenten kunnen strategieën aanpassen op basis van feedback en veranderende omstandigheden.
- **Foutcorrectie**: Agenten kunnen zelfstandig fouten detecteren en corrigeren.
- **Middelenbeheer**: Agenten kunnen het gebruik van middelen zoals tijd en rekenkracht optimaliseren.

Door metacognitie te integreren kan Travel Agent meer gepersonaliseerde en nauwkeurige reisaanbevelingen geven, wat de gebruikerservaring aanzienlijk verbetert.

---

## 2. Planning in Agenten

Planning is een cruciaal onderdeel van het gedrag van AI-agenten. Het omvat het uitstippelen van de stappen die nodig zijn om een doel te bereiken, rekening houdend met de huidige situatie, beschikbare middelen en mogelijke obstakels.

### Elementen van Planning

- **Huidige Taak**: Definieer de taak duidelijk.
- **Stappen om de Taak te Voltooien**: Verdeel de taak in beheersbare stappen.
- **Benodigde Middelen**: Identificeer de benodigde middelen.
- **Ervaring**: Gebruik eerdere ervaringen om de planning te ondersteunen.

**Voorbeeld**:  
Hier zijn de stappen die Travel Agent moet nemen om een gebruiker effectief te helpen bij het plannen van een reis:

### Stappen voor Travel Agent

1. **Verzamelen van Gebruikersvoorkeuren**  
   - Vraag de gebruiker naar details over reisdata, budget, interesses en specifieke wensen.  
   - Voorbeelden: "Wanneer wil je reizen?" "Wat is je budget?" "Welke activiteiten vind je leuk tijdens je vakantie?"

2. **Informatie Opzoeken**  
   - Zoek naar relevante reisopties op basis van de voorkeuren van de gebruiker.  
   - **Vluchten**: Zoek beschikbare vluchten binnen het budget en de gewenste reisdata.  
   - **Accommodaties**: Vind hotels of huurwoningen die passen bij de voorkeuren qua locatie, prijs en voorzieningen.  
   - **Attracties en Restaurants**: Identificeer populaire attracties, activiteiten en eetgelegenheden die aansluiten bij de interesses van de gebruiker.

3. **Aanbevelingen Genereren**  
   - Stel de verzamelde informatie samen in een gepersonaliseerd reisschema.  
   - Geef details zoals vluchtopties, hotelreserveringen en voorgestelde activiteiten, afgestemd op de voorkeuren van de gebruiker.

4. **Reisschema Presenteren aan Gebruiker**  
   - Deel het voorgestelde reisschema met de gebruiker ter beoordeling.  
   - Voorbeeld: "Hier is een voorgesteld reisschema voor je trip naar Parijs. Het bevat vluchtgegevens, hotelboekingen en een lijst met aanbevolen activiteiten en restaurants. Wat vind je ervan?"

5. **Feedback Verzamelen**  
   - Vraag de gebruiker om feedback op het voorgestelde reisschema.  
   - Voorbeelden: "Vind je de vluchtopties goed?" "Is het hotel geschikt voor je?" "Wil je nog activiteiten toevoegen of verwijderen?"

6. **Aanpassen op Basis van Feedback**  
   - Pas het reisschema aan op basis van de feedback van de gebruiker.  
   - Breng de nodige wijzigingen aan in vlucht-, accommodatie- en activiteit-aanbevelingen om beter aan te sluiten bij de voorkeuren.

7. **Definitieve Bevestiging**  
   - Presenteer het bijgewerkte reisschema aan de gebruiker voor definitieve goedkeuring.  
   - Voorbeeld: "Ik heb de aanpassingen doorgevoerd op basis van je feedback. Hier is het bijgewerkte reisschema. Is alles naar wens?"

8. **Boeken en Bevestigen**  
   - Zodra de gebruiker akkoord gaat, regel je de boekingen van vluchten, accommodaties en eventuele vooraf geplande activiteiten.  
   - Stuur bevestigingsgegevens naar de gebruiker.

9. **Voortdurende Ondersteuning Bieden**  
   - Blijf beschikbaar om de gebruiker te helpen met wijzigingen of extra verzoeken voor en tijdens de reis.  
   - Voorbeeld: "Als je tijdens je reis nog hulp nodig hebt, kun je altijd contact met me opnemen!"

### Voorbeeldinteractie

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Corrective RAG-systeem

Laten we eerst het verschil begrijpen tussen RAG Tool en Pre-emptive Context Load.

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.nl.png)

### Retrieval-Augmented Generation (RAG)

RAG combineert een retrievalsysteem met een generatief model. Wanneer er een vraag wordt gesteld, haalt het retrievalsysteem relevante documenten of data op uit een externe bron, en deze opgehaalde informatie wordt gebruikt om de input voor het generatieve model aan te vullen. Dit helpt het model om nauwkeurigere en contextueel relevantere antwoorden te genereren.

In een RAG-systeem haalt de agent relevante informatie op uit een kennisbank en gebruikt deze om passende antwoorden of acties te genereren.

### Corrective RAG-benadering

De Corrective RAG-benadering richt zich op het gebruik van RAG-technieken om fouten te corrigeren en de nauwkeurigheid van AI-agenten te verbeteren. Dit omvat:

1. **Prompting-techniek**: Het gebruik van specifieke prompts om de agent te sturen bij het ophalen van relevante informatie.  
2. **Tool**: Het implementeren van algoritmen en mechanismen die de agent in staat stellen de relevantie van de opgehaalde informatie te beoordelen en nauwkeurige antwoorden te genereren.  
3. **Evaluatie**: Het continu beoordelen van de prestaties van de agent en het aanbrengen van aanpassingen om de nauwkeurigheid en efficiëntie te verbeteren.

#### Voorbeeld: Corrective RAG in een Zoekagent

Denk aan een zoekagent die informatie van het web haalt om vragen van gebruikers te beantwoorden. De Corrective RAG-benadering kan bestaan uit:

1. **Prompting-techniek**: Zoekopdrachten formuleren op basis van de input van de gebruiker.  
2. **Tool**: Gebruik maken van natuurlijke taalverwerking en machine learning-algoritmen om zoekresultaten te rangschikken en te filteren.  
3. **Evaluatie**: Gebruikersfeedback analyseren om onnauwkeurigheden in de opgehaalde informatie te identificeren en te corrigeren.

### Corrective RAG in Travel Agent

Corrective RAG (Retrieval-Augmented Generation) verbetert het vermogen van een AI om informatie op te halen en te genereren, terwijl het eventuele onnauwkeurigheden corrigeert. Laten we bekijken hoe Travel Agent de Corrective RAG-benadering kan gebruiken om nauwkeurigere en relevantere reisaanbevelingen te geven.

Dit omvat:

- **Prompting-techniek:** Gebruik van specifieke prompts om de agent te sturen bij het ophalen van relevante informatie.  
- **Tool:** Implementatie van algoritmen en mechanismen die de agent in staat stellen de relevantie van de opgehaalde informatie te beoordelen en nauwkeurige antwoorden te genereren.  
- **Evaluatie:** Continu de prestaties van de agent beoordelen en aanpassingen maken om de nauwkeurigheid en efficiëntie te verbeteren.

#### Stappen voor het Implementeren van Corrective RAG in Travel Agent

1. **Eerste Gebruikersinteractie**  
   - Travel Agent verzamelt de eerste voorkeuren van de gebruiker, zoals bestemming, reisdata, budget en interesses.  
   - Voorbeeld:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Informatie Ophalen**  
   - Travel Agent haalt informatie op over vluchten, accommodaties, attracties en restaurants op basis van de voorkeuren van de gebruiker.  
   - Voorbeeld:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Genereren van Initiële Aanbevelingen**  
   - Travel Agent gebruikt de opgehaalde informatie om een gepersonaliseerd reisschema te maken.  
   - Voorbeeld:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Verzamelen van Gebruikersfeedback**  
   - Travel Agent vraagt de gebruiker om feedback op de initiële aanbevelingen.  
   - Voorbeeld:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Corrective RAG-proces**  
   - **Prompting-techniek**: Travel Agent formuleert nieuwe zoekopdrachten op basis van de feedback van de gebruiker.  
     - Voorbeeld:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Tool**: Travel Agent gebruikt algoritmen om nieuwe zoekresultaten te rangschikken en te filteren, met nadruk op relevantie op basis van gebruikersfeedback.  
     - Voorbeeld:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluatie**: Travel Agent beoordeelt continu de relevantie en nauwkeurigheid van zijn aanbevelingen door gebruikersfeedback te analyseren en waar nodig aanpassingen te maken.  
     - Voorbeeld:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktisch Voorbeeld

Hier is een vereenvoudigd Python-codevoorbeeld waarin de Corrective RAG-benadering in Travel Agent wordt geïntegreerd:
### Pre-emptive Context Load

Pre-emptive Context Load houdt in dat relevante context of achtergrondinformatie in het model wordt geladen voordat een vraag wordt verwerkt. Dit betekent dat het model vanaf het begin toegang heeft tot deze informatie, wat kan helpen om beter geïnformeerde antwoorden te genereren zonder tijdens het proces extra gegevens te hoeven ophalen.

Hier is een vereenvoudigd voorbeeld van hoe een pre-emptive context load eruit zou kunnen zien voor een reisagent-applicatie in Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Uitleg

1. **Initialisatie (`__init__` methode)**: De `TravelAgent`-klasse laadt vooraf een woordenboek met informatie over populaire bestemmingen zoals Parijs, Tokio, New York en Sydney. Dit woordenboek bevat details zoals het land, de valuta, de taal en belangrijke bezienswaardigheden per bestemming.

2. **Informatie ophalen (`get_destination_info` methode)**: Wanneer een gebruiker een specifieke bestemming opvraagt, haalt de `get_destination_info`-methode de relevante informatie op uit het vooraf geladen contextwoordenboek.

Door de context vooraf te laden, kan de reisagent-applicatie snel reageren op gebruikersvragen zonder deze informatie in real-time van een externe bron te hoeven ophalen. Dit maakt de applicatie efficiënter en responsiever.

### Bootstrapping van het Plan met een Doel voordat je Itereert

Bootstrapping van een plan met een doel betekent dat je begint met een duidelijk doel of gewenste uitkomst voor ogen. Door dit doel vooraf te definiëren, kan het model dit als leidraad gebruiken tijdens het iteratieve proces. Dit helpt ervoor te zorgen dat elke iteratie dichter bij het gewenste resultaat komt, waardoor het proces efficiënter en gerichter wordt.

Hier is een voorbeeld van hoe je een reisplan kunt bootstrapten met een doel voordat je gaat itereren voor een reisagent in Python:

### Scenario

Een reisagent wil een op maat gemaakte vakantie plannen voor een klant. Het doel is om een reisroute te creëren die de tevredenheid van de klant maximaliseert op basis van hun voorkeuren en budget.

### Stappen

1. Definieer de voorkeuren en het budget van de klant.
2. Bootstrap het initiële plan op basis van deze voorkeuren.
3. Itereer om het plan te verfijnen, waarbij geoptimaliseerd wordt voor de tevredenheid van de klant.

#### Python Code

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Uitleg Code

1. **Initialisatie (`__init__` methode)**: De `TravelAgent`-klasse wordt geïnitialiseerd met een lijst van potentiële bestemmingen, elk met eigenschappen zoals naam, kosten en type activiteit.

2. **Bootstrappen van het Plan (`bootstrap_plan` methode)**: Deze methode maakt een eerste reisplan op basis van de voorkeuren en het budget van de klant. Het doorloopt de lijst met bestemmingen en voegt deze toe aan het plan als ze overeenkomen met de voorkeuren van de klant en binnen het budget passen.

3. **Voorkeuren Matchen (`match_preferences` methode)**: Deze methode controleert of een bestemming overeenkomt met de voorkeuren van de klant.

4. **Itereren van het Plan (`iterate_plan` methode)**: Deze methode verfijnt het initiële plan door te proberen elke bestemming in het plan te vervangen door een betere match, rekening houdend met de voorkeuren van de klant en budgetbeperkingen.

5. **Kosten Berekenen (`calculate_cost` methode)**: Deze methode berekent de totale kosten van het huidige plan, inclusief een mogelijke nieuwe bestemming.

#### Voorbeeld Gebruik

- **Initieel Plan**: De reisagent maakt een eerste plan op basis van de voorkeuren van de klant voor sightseeing en een budget van $2000.
- **Verfijnd Plan**: De reisagent iterereert het plan en optimaliseert dit voor de voorkeuren en het budget van de klant.

Door het plan te bootstrapten met een duidelijk doel (bijvoorbeeld het maximaliseren van klanttevredenheid) en te itereren om het plan te verfijnen, kan de reisagent een op maat gemaakte en geoptimaliseerde reisroute voor de klant creëren. Deze aanpak zorgt ervoor dat het reisplan vanaf het begin aansluit bij de voorkeuren en het budget van de klant en verbetert met elke iteratie.

### Gebruikmaken van LLM voor Herordenen en Scoren

Grote taalmodellen (LLM's) kunnen worden ingezet voor het herordenen en scoren door de relevantie en kwaliteit van opgehaalde documenten of gegenereerde antwoorden te evalueren. Zo werkt het:

**Ophalen:** De eerste stap haalt een set kandidaat-documenten of antwoorden op basis van de vraag.

**Herordenen:** Het LLM beoordeelt deze kandidaten en herordent ze op basis van relevantie en kwaliteit. Deze stap zorgt ervoor dat de meest relevante en kwalitatieve informatie als eerste wordt getoond.

**Scoren:** Het LLM kent scores toe aan elke kandidaat, die hun relevantie en kwaliteit weerspiegelen. Dit helpt bij het selecteren van het beste antwoord of document voor de gebruiker.

Door LLM's te gebruiken voor herordenen en scoren kan het systeem nauwkeurigere en contextueel relevantere informatie bieden, wat de algehele gebruikerservaring verbetert.

Hier is een voorbeeld van hoe een reisagent een Large Language Model (LLM) kan gebruiken voor het herordenen en scoren van reisbestemmingen op basis van gebruikersvoorkeuren in Python:

#### Scenario - Reizen op basis van Voorkeuren

Een reisagent wil de beste reisbestemmingen aanbevelen aan een klant op basis van diens voorkeuren. Het LLM helpt bij het herordenen en scoren van de bestemmingen om de meest relevante opties te presenteren.

#### Stappen:

1. Verzamel de voorkeuren van de gebruiker.
2. Haal een lijst met potentiële reisbestemmingen op.
3. Gebruik het LLM om de bestemmingen te herordenen en te scoren op basis van de voorkeuren van de gebruiker.

Hier zie je hoe je het vorige voorbeeld kunt aanpassen om Azure OpenAI Services te gebruiken:

#### Vereisten

1. Je hebt een Azure-abonnement nodig.
2. Maak een Azure OpenAI-resource aan en verkrijg je API-sleutel.

#### Voorbeeld Python Code

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Uitleg Code - Preference Booker

1. **Initialisatie**: De `TravelAgent`-klasse wordt geïnitialiseerd met een lijst van potentiële reisbestemmingen, elk met eigenschappen zoals naam en beschrijving.

2. **Aanbevelingen Ophalen (`get_recommendations` methode)**: Deze methode genereert een prompt voor de Azure OpenAI-service op basis van de voorkeuren van de gebruiker en doet een HTTP POST-verzoek naar de Azure OpenAI API om herordende en gescoorde bestemmingen te verkrijgen.

3. **Prompt Genereren (`generate_prompt` methode)**: Deze methode stelt een prompt op voor Azure OpenAI, inclusief de voorkeuren van de gebruiker en de lijst met bestemmingen. De prompt stuurt het model aan om de bestemmingen te herordenen en te scoren op basis van de opgegeven voorkeuren.

4. **API-aanroep**: De `requests`-bibliotheek wordt gebruikt om een HTTP POST-verzoek te doen naar de Azure OpenAI API-endpoint. De respons bevat de herordende en gescoorde bestemmingen.

5. **Voorbeeld Gebruik**: De reisagent verzamelt gebruikersvoorkeuren (bijvoorbeeld interesse in sightseeing en diverse cultuur) en gebruikt de Azure OpenAI-service om herordende en gescoorde aanbevelingen voor reisbestemmingen te krijgen.

Zorg ervoor dat je `your_azure_openai_api_key` vervangt door je eigen Azure OpenAI API-sleutel en `https://your-endpoint.com/...` door de daadwerkelijke endpoint-URL van je Azure OpenAI-implementatie.

Door het LLM te gebruiken voor herordenen en scoren kan de reisagent meer gepersonaliseerde en relevante reisaanbevelingen aan klanten geven, wat hun algehele ervaring verbetert.

### RAG: Prompting Techniek versus Tool

Retrieval-Augmented Generation (RAG) kan zowel een prompting techniek als een tool zijn bij de ontwikkeling van AI-agenten. Het begrijpen van het verschil tussen beide kan je helpen RAG effectiever in je projecten te gebruiken.

#### RAG als Prompting Techniek

**Wat is het?**

- Als prompting techniek houdt RAG in dat je specifieke vragen of prompts formuleert om relevante informatie op te halen uit een grote verzameling of database. Deze informatie wordt vervolgens gebruikt om antwoorden of acties te genereren.

**Hoe werkt het:**

1. **Prompts formuleren**: Maak goed gestructureerde prompts of vragen op basis van de taak of de input van de gebruiker.
2. **Informatie ophalen**: Gebruik de prompts om relevante data te zoeken in een bestaande kennisbank of dataset.
3. **Antwoord genereren**: Combineer de opgehaalde informatie met generatieve AI-modellen om een uitgebreid en coherent antwoord te produceren.

**Voorbeeld bij Reisagent**:

- Gebruikersinput: "Ik wil musea bezoeken in Parijs."
- Prompt: "Vind de beste musea in Parijs."
- Opgehaalde informatie: Details over het Louvre, Musée d'Orsay, enzovoort.
- Gegeneerd antwoord: "Hier zijn enkele topmusea in Parijs: Louvre, Musée d'Orsay en Centre Pompidou."

#### RAG als Tool

**Wat is het?**

- Als tool is RAG een geïntegreerd systeem dat het ophalen en genereren automatiseert, waardoor ontwikkelaars complexe AI-functionaliteiten kunnen implementeren zonder voor elke vraag handmatig prompts te hoeven maken.

**Hoe werkt het:**

1. **Integratie**: Embed RAG in de architectuur van de AI-agent, zodat het automatisch het ophalen en genereren afhandelt.
2. **Automatisering**: De tool beheert het hele proces, van het ontvangen van gebruikersinput tot het genereren van het uiteindelijke antwoord, zonder expliciete prompts voor elke stap.
3. **Efficiëntie**: Verbetert de prestaties van de agent door het ophalen en genereren te stroomlijnen, wat snellere en nauwkeurigere antwoorden mogelijk maakt.

**Voorbeeld bij Reisagent**:

- Gebruikersinput: "Ik wil musea bezoeken in Parijs."
- RAG Tool: Haalt automatisch informatie over musea op en genereert een antwoord.
- Gegeneerd antwoord: "Hier zijn enkele topmusea in Parijs: Louvre, Musée d'Orsay en Centre Pompidou."

### Vergelijking

| Aspect                 | Prompting Techniek                                        | Tool                                                  |
|------------------------|----------------------------------------------------------|-------------------------------------------------------|
| **Handmatig vs Automatisch** | Handmatig formuleren van prompts voor elke vraag.       | Geautomatiseerd proces voor ophalen en genereren.     |
| **Controle**            | Biedt meer controle over het ophaalproces.               | Stroomlijnt en automatiseert ophalen en genereren.    |
| **Flexibiliteit**       | Laat aangepaste prompts toe op basis van specifieke behoeften. | Efficiënter voor grootschalige implementaties.        |
| **Complexiteit**        | Vereist het maken en aanpassen van prompts.               | Makkelijker te integreren in de architectuur van een AI-agent. |

### Praktische Voorbeelden

**Prompting Techniek Voorbeeld:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Tool Voorbeeld:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Relevantie Evalueren

Het evalueren van relevantie is een cruciaal onderdeel van de prestaties van een AI-agent. Het zorgt ervoor dat de informatie die de agent ophaalt en genereert passend, accuraat en nuttig is voor de gebruiker. Laten we bekijken hoe je relevantie kunt evalueren in AI-agenten, inclusief praktische voorbeelden en technieken.

#### Belangrijke Concepten bij het Evalueren van Relevantie

1. **Contextbewustzijn**:
   - De agent moet de context van de vraag van de gebruiker begrijpen om relevante informatie op te halen en te genereren.
   - Voorbeeld: Als een gebruiker vraagt naar "beste restaurants in Parijs", moet de agent rekening houden met voorkeuren zoals type keuken en budget.

2. **Nauwkeurigheid**:
   - De informatie die de agent geeft moet feitelijk correct en actueel zijn.
   - Voorbeeld: Aanbevelen van momenteel geopende restaurants met goede recensies in plaats van verouderde of gesloten opties.

3. **Gebruikersintentie**:
   - De agent moet de intentie van de gebruiker achter de vraag afleiden om de meest relevante informatie te bieden.
   - Voorbeeld: Als een gebruiker vraagt naar "budgetvriendelijke hotels", moet de agent betaalbare opties prioriteren.

4. **Feedback Loop**:
   - Het continu verzamelen en analyseren van gebruikersfeedback helpt de agent om het evaluatieproces van relevantie te verbeteren.
   - Voorbeeld: Gebruikersbeoordelingen en feedback op eerdere aanbevelingen verwerken om toekomstige antwoorden te verbeteren.

#### Praktische Technieken voor het Evalueren van Relevantie

1. **Relevantie Scoring**:
   - Ken een relevantiescore toe aan elk opgehaald item op basis van hoe goed het aansluit bij de vraag en voorkeuren van de gebruiker.
   - Voorbeeld:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filteren en Rangschikken**:
   - Filter irrelevante items eruit en rangschik de overgebleven items op basis van hun relevantiescores.
   - Voorbeeld:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Natural Language Processing (NLP)**:
   - Gebruik NLP-technieken om de vraag van de gebruiker te begrijpen en relevante informatie op te halen.
   - Voorbeeld:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integratie van Gebruikersfeedback**:
   - Verzamel feedback over de gegeven aanbevelingen en gebruik deze om toekomstige relevantie-evaluaties aan te passen.
   - Voorbeeld:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Voorbeeld: Relevantie Evalueren in Travel Agent

Hier is een praktisch voorbeeld van hoe Travel Agent de relevantie van reisaanbevelingen kan evalueren:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Zoeken met Intentie

Zoeken met intentie betekent dat je het onderliggende doel of de reden achter de vraag van een gebruiker begrijpt en interpreteert om de meest relevante en bruikbare informatie op te halen en te genereren. Deze aanpak gaat verder dan alleen het matchen van zoekwoorden en richt zich op het begrijpen van de werkelijke behoeften en context van de gebruiker.

#### Belangrijke Concepten bij Zoeken met Intentie

1. **Begrijpen van Gebruikersintentie**:
   - Gebruikersintentie kan worden onderverdeeld in drie hoofdtypen: informatief, navigerend en transactioneel.
     - **Informatieve Intentie**: De gebruiker zoekt informatie over een onderwerp (bijv. "Wat zijn de beste musea in Parijs?").
     - **Navigerende Intentie**: De gebruiker wil naar een specifieke website of pagina navigeren (bijv. "Officiële website Louvre Museum").
     - **Transactionele Intentie**: De gebruiker wil een transactie uitvoeren, zoals een vlucht boeken of een aankoop doen (bijv. "Boek een vlucht naar Parijs").

2. **Contextbewustzijn**:
   - Het analyseren van de context van de vraag helpt om de intentie nauwkeurig te identificeren. Dit omvat eerdere interacties, gebruikersvoorkeuren en specifieke details van de huidige vraag.

3. **Natural Language Processing (NLP)**:
   - NLP-technieken worden ingezet om de natuurlijke taalvragen van gebruikers te begrijpen en te interpreteren. Dit omvat taken zoals entiteitsherkenning, sentimentanalyse en query parsing.

4. **Personalisatie**:
   - Het personaliseren van zoekresultaten op basis van de geschiedenis, voorkeuren en feedback van de gebruiker verhoogt de relevantie van de opgehaalde informatie.
#### Praktisch Voorbeeld: Zoeken met Intentie in Travel Agent

Laten we Travel Agent als voorbeeld nemen om te zien hoe zoeken met intentie geïmplementeerd kan worden.

1. **Verzamelen van Gebruikersvoorkeuren**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Begrijpen van de Intentie van de Gebruiker**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Contextbewustzijn**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Zoeken en Personaliseren van Resultaten**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Voorbeeldgebruik**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Code Genereren als Hulpmiddel

Code genererende agents gebruiken AI-modellen om code te schrijven en uit te voeren, waarmee ze complexe problemen oplossen en taken automatiseren.

### Code Genererende Agents

Code genererende agents maken gebruik van generatieve AI-modellen om code te schrijven en uit te voeren. Deze agents kunnen complexe problemen oplossen, taken automatiseren en waardevolle inzichten bieden door code te genereren en uit te voeren in verschillende programmeertalen.

#### Praktische Toepassingen

1. **Geautomatiseerde Codegeneratie**: Genereer codefragmenten voor specifieke taken, zoals data-analyse, webscraping of machine learning.
2. **SQL als RAG**: Gebruik SQL-queries om data uit databases op te halen en te manipuleren.
3. **Probleemoplossing**: Maak en voer code uit om specifieke problemen op te lossen, zoals het optimaliseren van algoritmes of het analyseren van data.

#### Voorbeeld: Code Genererende Agent voor Data-analyse

Stel je voor dat je een code genererende agent ontwerpt. Zo zou het kunnen werken:

1. **Taak**: Analyseer een dataset om trends en patronen te identificeren.
2. **Stappen**:
   - Laad de dataset in een data-analysetool.
   - Genereer SQL-queries om de data te filteren en te aggregeren.
   - Voer de queries uit en haal de resultaten op.
   - Gebruik de resultaten om visualisaties en inzichten te genereren.
3. **Benodigde Middelen**: Toegang tot de dataset, data-analysetools en SQL-mogelijkheden.
4. **Ervaring**: Gebruik eerdere analyse-resultaten om de nauwkeurigheid en relevantie van toekomstige analyses te verbeteren.

### Voorbeeld: Code Genererende Agent voor Travel Agent

In dit voorbeeld ontwerpen we een code genererende agent, Travel Agent, die gebruikers helpt bij het plannen van hun reis door code te genereren en uit te voeren. Deze agent kan taken uitvoeren zoals het ophalen van reismogelijkheden, filteren van resultaten en het samenstellen van een reisplan met behulp van generatieve AI.

#### Overzicht van de Code Genererende Agent

1. **Verzamelen van Gebruikersvoorkeuren**: Verzamelt gebruikersinput zoals bestemming, reisdata, budget en interesses.
2. **Code Genereren om Data op te Halen**: Genereert codefragmenten om gegevens over vluchten, hotels en attracties op te halen.
3. **Uitvoeren van de Gegeneerde Code**: Voert de gegenereerde code uit om realtime informatie op te halen.
4. **Reisplan Genereren**: Stelt de opgehaalde data samen tot een gepersonaliseerd reisplan.
5. **Aanpassen op Basis van Feedback**: Ontvangt gebruikersfeedback en genereert indien nodig nieuwe code om de resultaten te verfijnen.

#### Stapsgewijze Implementatie

1. **Verzamelen van Gebruikersvoorkeuren**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Code Genereren om Data op te Halen**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Uitvoeren van de Gegeneerde Code**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Reisplan Genereren**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Aanpassen op Basis van Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Gebruik maken van omgevingsbewustzijn en redeneren

Op basis van het schema van de tabel kan het genereren van queries worden verbeterd door gebruik te maken van omgevingsbewustzijn en redeneren.

Hier is een voorbeeld van hoe dit kan worden gedaan:

1. **Begrijpen van het Schema**: Het systeem begrijpt het schema van de tabel en gebruikt deze informatie om de querygeneratie te onderbouwen.
2. **Aanpassen op Basis van Feedback**: Het systeem past gebruikersvoorkeuren aan op basis van feedback en redeneert over welke velden in het schema bijgewerkt moeten worden.
3. **Genereren en Uitvoeren van Queries**: Het systeem genereert en voert queries uit om bijgewerkte vlucht- en hotelgegevens op te halen op basis van de nieuwe voorkeuren.

Hier is een bijgewerkt Python-codevoorbeeld dat deze concepten verwerkt:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Uitleg - Boeken op Basis van Feedback

1. **Schema Bewustzijn**: De `schema` dictionary definieert hoe voorkeuren aangepast moeten worden op basis van feedback. Het bevat velden zoals `favorites` en `avoid`, met bijbehorende aanpassingen.
2. **Voorkeuren Aanpassen (`adjust_based_on_feedback` methode)**: Deze methode past voorkeuren aan op basis van gebruikersfeedback en het schema.
3. **Omgevingsgebaseerde Aanpassingen (`adjust_based_on_environment` methode)**: Deze methode personaliseert de aanpassingen op basis van het schema en de feedback.
4. **Genereren en Uitvoeren van Queries**: Het systeem genereert code om bijgewerkte vlucht- en hotelgegevens op te halen op basis van de aangepaste voorkeuren en simuleert de uitvoering van deze queries.
5. **Reisplan Genereren**: Het systeem maakt een bijgewerkt reisplan op basis van de nieuwe vlucht-, hotel- en attractiegegevens.

Door het systeem omgevingsbewust te maken en te laten redeneren op basis van het schema, kan het nauwkeurigere en relevantere queries genereren, wat leidt tot betere reisaanbevelingen en een meer gepersonaliseerde gebruikerservaring.

### SQL gebruiken als Retrieval-Augmented Generation (RAG) techniek

SQL (Structured Query Language) is een krachtig hulpmiddel voor het werken met databases. Wanneer SQL wordt gebruikt als onderdeel van een Retrieval-Augmented Generation (RAG) aanpak, kan het relevante data uit databases ophalen om AI-agents te informeren en te helpen bij het genereren van antwoorden of acties. Laten we bekijken hoe SQL als RAG-techniek kan worden ingezet in de context van Travel Agent.

#### Belangrijke Concepten

1. **Interactie met Databases**:
   - SQL wordt gebruikt om databases te bevragen, relevante informatie op te halen en data te manipuleren.
   - Voorbeeld: Het ophalen van vluchtgegevens, hotelinformatie en attracties uit een reisdatabase.

2. **Integratie met RAG**:
   - SQL-queries worden gegenereerd op basis van gebruikersinput en voorkeuren.
   - De opgehaalde data wordt vervolgens gebruikt om gepersonaliseerde aanbevelingen of acties te genereren.

3. **Dynamische Querygeneratie**:
   - De AI-agent genereert dynamische SQL-queries op basis van de context en de behoeften van de gebruiker.
   - Voorbeeld: SQL-queries aanpassen om resultaten te filteren op budget, data en interesses.

#### Toepassingen

- **Geautomatiseerde Codegeneratie**: Genereer codefragmenten voor specifieke taken.
- **SQL als RAG**: Gebruik SQL-queries om data te manipuleren.
- **Probleemoplossing**: Maak en voer code uit om problemen op te lossen.

**Voorbeeld**:  
Een data-analyse agent:

1. **Taak**: Analyseer een dataset om trends te vinden.  
2. **Stappen**:  
   - Laad de dataset.  
   - Genereer SQL-queries om data te filteren.  
   - Voer queries uit en haal resultaten op.  
   - Genereer visualisaties en inzichten.  
3. **Middelen**: Toegang tot dataset, SQL-mogelijkheden.  
4. **Ervaring**: Gebruik eerdere resultaten om toekomstige analyses te verbeteren.

#### Praktisch Voorbeeld: SQL gebruiken in Travel Agent

1. **Verzamelen van Gebruikersvoorkeuren**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL Queries Genereren**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL Queries Uitvoeren**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Aanbevelingen Genereren**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Voorbeeld SQL Queries

1. **Vlucht Query**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Hotel Query**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Attractie Query**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Door SQL te gebruiken als onderdeel van de Retrieval-Augmented Generation (RAG) techniek, kunnen AI-agents zoals Travel Agent dynamisch relevante data ophalen en gebruiken om nauwkeurige en gepersonaliseerde aanbevelingen te doen.

### Voorbeeld van Metacognitie

Om een implementatie van metacognitie te demonstreren, laten we een eenvoudige agent maken die *reflecteert op zijn besluitvormingsproces* terwijl hij een probleem oplost. In dit voorbeeld bouwen we een systeem waarin een agent probeert de keuze van een hotel te optimaliseren, maar vervolgens zijn eigen redenering evalueert en zijn strategie aanpast wanneer hij fouten of suboptimale keuzes maakt.

We simuleren dit met een basisvoorbeeld waarbij de agent hotels selecteert op basis van een combinatie van prijs en kwaliteit, maar hij "reflecteert" op zijn beslissingen en past zich daarop aan.

#### Hoe dit metacognitie illustreert:

1. **Initiële Beslissing**: De agent kiest het goedkoopste hotel, zonder rekening te houden met de kwaliteit.
2. **Reflectie en Evaluatie**: Na de eerste keuze controleert de agent of het hotel een "slechte" keuze was aan de hand van gebruikersfeedback. Als blijkt dat de kwaliteit te laag was, reflecteert hij op zijn redenering.
3. **Strategie Aanpassen**: De agent past zijn strategie aan op basis van zijn reflectie en schakelt van "goedkoopste" naar "hoogste_kwaliteit", waardoor zijn besluitvorming in toekomstige rondes verbetert.

Hier is een voorbeeld:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Metacognitieve Vermogens van Agents

Het belangrijkste hier is het vermogen van de agent om:
- Zijn eerdere keuzes en besluitvormingsproces te evalueren.
- Zijn strategie aan te passen op basis van die reflectie, oftewel metacognitie in actie.

Dit is een eenvoudige vorm van metacognitie waarbij het systeem zijn redeneringsproces kan aanpassen op basis van interne feedback.

### Conclusie

Metacognitie is een krachtig hulpmiddel dat de mogelijkheden van AI-agents aanzienlijk kan verbeteren. Door metacognitieve processen te integreren, kun je agents ontwerpen die intelligenter, flexibeler en efficiënter zijn. Gebruik de aanvullende bronnen om de fascinerende wereld van metacognitie in AI-agents verder te verkennen.

## Vorige Les

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Volgende Les

[AI Agents in Production](../10-ai-agents-production/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.