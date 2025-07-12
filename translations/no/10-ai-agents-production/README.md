<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:39:40+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "no"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.no.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_
# AI-agenter i produksjon

## Introduksjon

Denne leksjonen vil dekke:

- Hvordan planlegge utrullingen av din AI-agent til produksjon på en effektiv måte.
- Vanlige feil og utfordringer du kan møte når du deployerer AI-agenten din i produksjon.
- Hvordan håndtere kostnader samtidig som du opprettholder ytelsen til AI-agenten din.

## Læringsmål

Etter å ha fullført denne leksjonen vil du vite hvordan du kan/forstå:

- Teknikker for å forbedre ytelsen, kostnadene og effektiviteten til et produksjonssystem med AI-agenter.
- Hva og hvordan du kan evaluere AI-agentene dine.
- Hvordan kontrollere kostnader ved utrulling av AI-agenter i produksjon.

Det er viktig å deployere AI-agenter som er pålitelige. Ta også en titt på leksjonen "Building Trustworthy AI Agents".

## Evaluering av AI-agenter

Før, under og etter utrulling av AI-agenter er det avgjørende å ha et godt system for å evaluere AI-agentene dine. Dette sikrer at systemet ditt er i tråd med dine og brukernes mål.

For å evaluere en AI-agent er det viktig å kunne vurdere ikke bare agentens output, men også hele systemet som AI-agenten opererer i. Dette inkluderer, men er ikke begrenset til:

- Den opprinnelige modellforespørselen.
- Agentens evne til å identifisere brukerens intensjon.
- Agentens evne til å finne riktig verktøy for å utføre oppgaven.
- Verktøyets respons på agentens forespørsel.
- Agentens evne til å tolke verktøyets respons.
- Brukerens tilbakemelding på agentens respons.

Dette gjør det mulig å identifisere forbedringsområder på en mer modulær måte. Du kan deretter overvåke effekten av endringer i modeller, prompts, verktøy og andre komponenter mer effektivt.

## Vanlige problemer og mulige løsninger med AI-agenter

| **Problem**                                    | **Mulig løsning**                                                                                                                                                                                                         |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI-agenten utfører ikke oppgaver konsekvent    | - Forbedre prompten som gis til AI-agenten; vær tydelig på målene.<br>- Identifiser hvor det kan hjelpe å dele opp oppgaver i deloppgaver som håndteres av flere agenter.                                                    |
| AI-agenten havner i kontinuerlige løkker       | - Sørg for klare avslutningsbetingelser slik at agenten vet når prosessen skal stoppe.<br>- For komplekse oppgaver som krever resonnement og planlegging, bruk en større modell som er spesialisert på slike oppgaver.       |
| AI-agentens verktøysanrop fungerer ikke godt   | - Test og valider verktøyets output utenfor agentsystemet.<br>- Forbedre definerte parametere, prompts og navngivning av verktøy.                                                                                          |
| Multi-agent systemet fungerer ikke konsekvent  | - Forbedre promptene til hver agent slik at de er spesifikke og tydelig forskjellige.<br>- Bygg et hierarkisk system med en "routing"- eller kontrollagent som avgjør hvilken agent som er riktig for oppgaven.              |

## Kostnadshåndtering

Her er noen strategier for å håndtere kostnadene ved å deployere AI-agenter i produksjon:

- **Caching av svar** – Identifisere vanlige forespørsler og oppgaver og levere svarene før de går gjennom agentsystemet ditt er en god måte å redusere volumet av like forespørsler på. Du kan til og med implementere en flyt for å vurdere hvor lik en forespørsel er til dine cachede svar ved hjelp av enklere AI-modeller.

- **Bruke mindre modeller** – Små språkmodeller (SLM) kan fungere godt for visse agentbrukstilfeller og vil redusere kostnadene betydelig. Som nevnt tidligere er det beste å bygge et evalueringssystem for å måle og sammenligne ytelsen mot større modeller for å forstå hvor godt en SLM vil fungere i ditt brukstilfelle.

- **Bruke en router-modell** – En lignende strategi er å bruke en variasjon av modeller og størrelser. Du kan bruke en LLM/SLM eller en serverløs funksjon for å rute forespørsler basert på kompleksitet til de mest passende modellene. Dette vil også bidra til å redusere kostnader samtidig som ytelsen sikres på riktige oppgaver.

## Gratulerer

Dette er for øyeblikket den siste leksjonen i "AI Agents for Beginners".

Vi planlegger å fortsette å legge til leksjoner basert på tilbakemeldinger og endringer i denne stadig voksende industrien, så stikk gjerne innom igjen i nær fremtid.

Hvis du ønsker å fortsette læringen og byggingen med AI-agenter, bli med i <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Der arrangerer vi workshops, community roundtables og "ask me anything"-økter.

Vi har også en Learn-samling med ekstra materiale som kan hjelpe deg i gang med å bygge AI-agenter i produksjon.

## Forrige leksjon

[Metacognition Design Pattern](../09-metacognition/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.