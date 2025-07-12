<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:42:43+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "hr"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.hr.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_
# AI Agent u produkciji

## Uvod

Ova lekcija će obuhvatiti:

- Kako učinkovito planirati implementaciju vašeg AI Agenta u produkciju.
- Uobičajene pogreške i probleme na koje možete naići prilikom implementacije AI Agenta u produkciju.
- Kako upravljati troškovima, a pritom održavati performanse vašeg AI Agenta.

## Ciljevi učenja

Nakon završetka ove lekcije, znat ćete kako/razumjeti:

- Tehnike za poboljšanje performansi, troškova i učinkovitosti sustava AI Agenta u produkciji.
- Što i kako evaluirati kod vaših AI Agenata.
- Kako kontrolirati troškove prilikom implementacije AI Agenata u produkciju.

Važno je implementirati AI Agente kojima se može vjerovati. Pogledajte i lekciju "Building Trustworthy AI Agents".

## Evaluacija AI Agenata

Prije, tijekom i nakon implementacije AI Agenata, ključno je imati odgovarajući sustav za evaluaciju vaših AI Agenata. To će osigurati da je vaš sustav usklađen s vašim i ciljevima korisnika.

Za evaluaciju AI Agenta važno je moći procijeniti ne samo izlaz agenta, već i cijeli sustav u kojem vaš AI Agent djeluje. To uključuje, ali nije ograničeno na:

- Početni zahtjev modelu.
- Sposobnost agenta da prepozna namjeru korisnika.
- Sposobnost agenta da odabere pravi alat za izvršenje zadatka.
- Odgovor alata na zahtjev agenta.
- Sposobnost agenta da interpretira odgovor alata.
- Povratne informacije korisnika na odgovor agenta.

Ovo vam omogućuje da modularnije identificirate područja za poboljšanje. Zatim možete učinkovitije pratiti učinke promjena u modelima, promptovima, alatima i drugim komponentama.

## Uobičajeni problemi i moguća rješenja s AI Agentima

| **Problem**                                    | **Moguće rješenje**                                                                                                                                                                                                        |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AI Agent ne izvršava zadatke dosljedno        | - Doradite prompt koji dajete AI Agentu; budite jasni u ciljevima.<br>- Identificirajte gdje podjela zadataka na podzadatke i njihovo rješavanje od strane više agenata može pomoći.                                         |
| AI Agent ulazi u beskonačne petlje             | - Osigurajte jasne uvjete za prekid kako bi agent znao kada zaustaviti proces.<br>- Za složene zadatke koji zahtijevaju rezoniranje i planiranje, koristite veći model specijaliziran za takve zadatke.                    |
| Pozivi alata AI Agenta ne funkcioniraju dobro  | - Testirajte i validirajte izlaz alata izvan sustava agenta.<br>- Doradite definirane parametre, promptove i nazive alata.                                                                                                |
| Sustav s više agenata ne radi dosljedno        | - Doradite promptove za svakog agenta kako bi bili specifični i različiti.<br>- Izgradite hijerarhijski sustav koristeći "routing" ili kontrolnog agenta koji određuje koji je agent prikladan.                             |

## Upravljanje troškovima

Evo nekoliko strategija za upravljanje troškovima implementacije AI Agenata u produkciju:

- **Keširanje odgovora** - Prepoznavanje čestih zahtjeva i zadataka te pružanje odgovora prije nego što prođu kroz vaš agentski sustav dobar je način za smanjenje volumena sličnih zahtjeva. Možete čak implementirati tok za procjenu sličnosti zahtjeva s keširanim odgovorima koristeći jednostavnije AI modele.

- **Korištenje manjih modela** - Mali jezični modeli (SLM) mogu dobro funkcionirati u određenim agentskim slučajevima i značajno smanjiti troškove. Kao što je ranije spomenuto, izgradnja sustava za evaluaciju koji uspoređuje performanse s većim modelima najbolji je način da procijenite koliko će SLM dobro raditi u vašem slučaju.

- **Korištenje router modela** - Slična strategija je korištenje različitih modela i veličina. Možete koristiti LLM/SLM ili serverless funkciju za usmjeravanje zahtjeva prema složenosti na najprikladnije modele. To također pomaže u smanjenju troškova, a istovremeno osigurava performanse na pravim zadacima.

## Čestitamo

Ovo je trenutno zadnja lekcija iz serije "AI Agents for Beginners".

Planiramo nastaviti dodavati lekcije na temelju povratnih informacija i promjena u ovoj brzo rastućoj industriji, stoga nam se ponovno pridružite uskoro.

Ako želite nastaviti s učenjem i izgradnjom AI Agenata, pridružite se <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Tamo organiziramo radionice, okrugle stolove zajednice i sesije "pitaj me bilo što".

Također imamo Learn kolekciju dodatnih materijala koji vam mogu pomoći da započnete s izgradnjom AI Agenata u produkciji.

## Prethodna lekcija

[Metacognition Design Pattern](../09-metacognition/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.