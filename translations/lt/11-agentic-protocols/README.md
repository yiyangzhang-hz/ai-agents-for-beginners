<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T09:31:34+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "lt"
}
-->
# Naudojant Agentinius Protokolus (MCP, A2A ir NLWeb)

[![Agentiniai Protokolai](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.lt.png)](https://youtu.be/X-Dh9R3Opn8)

Didėjant dirbtinio intelekto agentų naudojimui, auga ir poreikis protokolams, kurie užtikrintų standartizaciją, saugumą ir skatintų atvirą inovaciją. Šioje pamokoje aptarsime tris protokolus, kurie siekia patenkinti šį poreikį – Modelio Konteksto Protokolą (MCP), Agentas Agentui (A2A) ir Natūralios Kalbos Tinklą (NLWeb).

## Įvadas

Šioje pamokoje aptarsime:

• Kaip **MCP** leidžia DI agentams pasiekti išorinius įrankius ir duomenis, kad atliktų vartotojo užduotis.

• Kaip **A2A** suteikia galimybę skirtingiems DI agentams bendrauti ir bendradarbiauti.

• Kaip **NLWeb** suteikia natūralios kalbos sąsajas bet kuriai svetainei, leidžiant DI agentams atrasti ir sąveikauti su turiniu.

## Mokymosi Tikslai

• **Atpažinti** pagrindinę MCP, A2A ir NLWeb paskirtį bei naudą DI agentų kontekste.

• **Paaiškinti**, kaip kiekvienas protokolas palengvina bendravimą ir sąveiką tarp LLM, įrankių ir kitų agentų.

• **Suprasti**, kokius unikalius vaidmenis kiekvienas protokolas atlieka kuriant sudėtingas agentines sistemas.

## Modelio Konteksto Protokolas

**Modelio Konteksto Protokolas (MCP)** yra atviras standartas, kuris suteikia standartizuotą būdą programoms pateikti kontekstą ir įrankius LLM. Tai leidžia sukurti „universalų adapterį“, kuris užtikrina nuoseklų ryšį su įvairiais duomenų šaltiniais ir įrankiais, kuriuos gali naudoti DI agentai.

Pažvelkime į MCP komponentus, naudą lyginant su tiesioginiu API naudojimu, ir pavyzdį, kaip DI agentai gali naudoti MCP serverį.

### MCP Pagrindiniai Komponentai

MCP veikia pagal **kliento-serverio architektūrą**, o pagrindiniai komponentai yra:

• **Hostai** – tai LLM programos (pavyzdžiui, kodo redaktorius kaip VSCode), kurios inicijuoja ryšius su MCP serveriu.

• **Klientai** – tai komponentai hosto programoje, kurie palaiko vienas su vienu ryšius su serveriais.

• **Serveriai** – tai lengvos programos, kurios teikia specifines galimybes.

Protokole yra trys pagrindiniai MCP serverio gebėjimai:

• **Įrankiai**: Tai yra atskiros funkcijos ar veiksmai, kuriuos DI agentas gali iškviesti, kad atliktų užduotį. Pavyzdžiui, orų tarnyba gali pateikti „gauti orų prognozę“ įrankį, o e. prekybos serveris – „pirkti produktą“ įrankį. MCP serveriai pateikia kiekvieno įrankio pavadinimą, aprašymą ir įvesties/išvesties schemą savo galimybių sąraše.

• **Ištekliai**: Tai yra tik skaitymui skirti duomenų elementai ar dokumentai, kuriuos MCP serveris gali pateikti, o klientai gali juos gauti pagal poreikį. Pavyzdžiai: failų turinys, duomenų bazės įrašai ar žurnalo failai. Ištekliai gali būti tekstiniai (pvz., kodas ar JSON) arba dvejetainiai (pvz., vaizdai ar PDF).

• **Šablonai**: Tai yra iš anksto paruošti šablonai, kurie pateikia siūlomus raginimus, leidžiančius vykdyti sudėtingesnius darbo procesus.

### MCP Nauda

MCP suteikia reikšmingų privalumų DI agentams:

• **Dinaminis Įrankių Aptikimas**: Agentai gali dinamiškai gauti serverio pateiktą įrankių sąrašą su jų aprašymais. Tai skiriasi nuo tradicinių API, kurios dažnai reikalauja statinio kodavimo integracijoms, o bet kokie API pakeitimai reikalauja kodo atnaujinimų. MCP siūlo „integruoti vieną kartą“ metodą, kuris užtikrina didesnį lankstumą.

• **Suderinamumas su Skirtingais LLM**: MCP veikia su įvairiais LLM, suteikdamas galimybę keisti pagrindinius modelius, siekiant geresnio našumo.

• **Standartizuotas Saugumas**: MCP apima standartizuotą autentifikavimo metodą, kuris palengvina mastelio didinimą, kai reikia pridėti prieigą prie papildomų MCP serverių. Tai paprasčiau nei valdyti skirtingus raktus ir autentifikavimo tipus tradicinėms API.

### MCP Pavyzdys

![MCP Diagrama](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.lt.png)

Įsivaizduokite, kad vartotojas nori užsisakyti skrydį naudodamas DI asistentą, kuris veikia su MCP.

1. **Ryšys**: DI asistentas (MCP klientas) prisijungia prie MCP serverio, kurį teikia oro linijos.

2. **Įrankių Aptikimas**: Klientas klausia oro linijų MCP serverio: „Kokius įrankius turite?“ Serveris atsako su įrankiais, tokiais kaip „ieškoti skrydžių“ ir „užsakyti skrydžius“.

3. **Įrankio Iškvietimas**: Tada jūs prašote DI asistento: „Prašau surasti skrydį iš Portlando į Honolulu.“ DI asistentas, naudodamas savo LLM, nustato, kad reikia iškviesti „ieškoti skrydžių“ įrankį ir perduoda atitinkamus parametrus (išvykimo vietą, paskirties vietą) MCP serveriui.

4. **Vykdymas ir Atsakymas**: MCP serveris, veikiantis kaip tarpininkas, atlieka faktinį kvietimą į oro linijų vidinę užsakymo API. Jis gauna skrydžio informaciją (pvz., JSON duomenis) ir siunčia ją atgal DI asistentui.

5. **Tolesnė Sąveika**: DI asistentas pateikia skrydžio pasirinkimus. Kai pasirenkate skrydį, asistentas gali iškviesti „užsakyti skrydį“ įrankį tame pačiame MCP serveryje, užbaigdamas užsakymą.

## Agentas Agentui Protokolas (A2A)

Nors MCP orientuojasi į LLM ir įrankių sujungimą, **Agentas Agentui (A2A) protokolas** žengia dar toliau, suteikdamas galimybę skirtingiems DI agentams bendrauti ir bendradarbiauti. A2A jungia DI agentus iš skirtingų organizacijų, aplinkų ir technologijų, kad jie galėtų atlikti bendrą užduotį.

Aptarsime A2A komponentus, naudą ir pavyzdį, kaip jis galėtų būti pritaikytas mūsų kelionių programoje.

### A2A Pagrindiniai Komponentai

A2A orientuojasi į agentų bendravimą ir jų bendrą darbą, siekiant atlikti vartotojo užduotį. Kiekvienas protokolo komponentas prisideda prie šio tikslo:

#### Agentų Kortelė

Panašiai kaip MCP serveris pateikia įrankių sąrašą, Agentų Kortelė turi:

- Agentų pavadinimą.  
- **Bendros užduočių aprašymą**, kurias jis atlieka.  
- **Specifinių įgūdžių sąrašą** su aprašymais, padedančiais kitiems agentams (ar net žmonėms) suprasti, kada ir kodėl reikėtų kreiptis į šį agentą.  
- **Dabartinį agento URL adresą**.  
- **Versiją** ir **galimybes**, tokias kaip atsakymų transliavimas ir pranešimų siuntimas.  

#### Agentų Vykdytojas

Agentų Vykdytojas yra atsakingas už **vartotojo pokalbio konteksto perdavimą nuotoliniam agentui**, kad šis suprastų, kokią užduotį reikia atlikti. 

#### Artefaktas

Kai nuotolinis agentas užbaigia užduotį, jo darbo rezultatas pateikiamas kaip artefaktas. Artefaktas **apima atliktos užduoties rezultatą**, **aprašymą**, kas buvo atlikta, ir **tekstinį kontekstą**, kuris perduodamas per protokolą.

#### Įvykių Eilė

Šis komponentas naudojamas **atnaujinimų valdymui ir pranešimų perdavimui**. Tai ypač svarbu gamyboje, kad agentų ryšys nebūtų nutrauktas prieš užduoties užbaigimą, ypač kai užduotys užtrunka ilgiau.

### A2A Nauda

• **Pagerintas Bendradarbiavimas**: Leidžia agentams iš skirtingų tiekėjų ir platformų sąveikauti, dalintis kontekstu ir dirbti kartu, užtikrinant sklandžią automatizaciją tarp tradiciškai atskirtų sistemų.

• **Modelių Pasirinkimo Lankstumas**: Kiekvienas A2A agentas gali pasirinkti, kurį LLM naudoti, optimizuojant ar pritaikant modelius pagal poreikius.

• **Integruotas Autentifikavimas**: Autentifikavimas yra tiesiogiai integruotas į A2A protokolą, užtikrinant tvirtą saugumo sistemą agentų sąveikai.

### A2A Pavyzdys

![A2A Diagrama](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.lt.png)

Išplėskime mūsų kelionių užsakymo scenarijų, bet šį kartą naudodami A2A.

1. **Vartotojo Užklausa Multi-Agentui**: Vartotojas bendrauja su „Kelionių Agentu“ (A2A klientu/agentu), pavyzdžiui, sakydamas: „Prašau užsakyti visą kelionę į Honolulu kitai savaitei, įskaitant skrydžius, viešbutį ir automobilio nuomą.“

2. **Kelionių Agento Orkestracija**: Kelionių Agentas gauna šį sudėtingą prašymą. Jis naudoja savo LLM, kad suprastų užduotį ir nustatytų, jog reikia bendrauti su kitais specializuotais agentais.

3. **Tarpagentinė Komunikacija**: Kelionių Agentas naudoja A2A protokolą, kad prisijungtų prie kitų agentų, tokių kaip „Oro Linijų Agentas“, „Viešbučių Agentas“ ir „Automobilių Nuomos Agentas“, kuriuos sukūrė skirtingos įmonės.

4. **Deleguotas Užduočių Vykdymas**: Kelionių Agentas siunčia specifines užduotis šiems specializuotiems agentams (pvz., „Raskite skrydžius į Honolulu“, „Užsakykite viešbutį“, „Išnuomokite automobilį“). Kiekvienas iš šių specializuotų agentų, naudodamas savo LLM ir vidinius įrankius (kurie gali būti MCP serveriai), atlieka savo užduotį.

5. **Apibendrintas Atsakymas**: Kai visi agentai užbaigia savo užduotis, Kelionių Agentas sujungia rezultatus (skrydžio detales, viešbučio patvirtinimą, automobilio nuomos užsakymą) ir pateikia išsamų atsakymą vartotojui.

## Natūralios Kalbos Tinklas (NLWeb)

Svetainės jau seniai yra pagrindinis būdas vartotojams pasiekti informaciją ir duomenis internete.

Pažvelkime į skirtingus NLWeb komponentus, NLWeb naudą ir pavyzdį, kaip NLWeb veikia mūsų kelionių programoje.

### NLWeb Komponentai

- **NLWeb Programa (Pagrindinis Paslaugos Kodas)**: Sistema, kuri apdoroja natūralios kalbos klausimus. Ji jungia skirtingas platformos dalis, kad sukurtų atsakymus. Galite tai įsivaizduoti kaip **variklį, kuris valdo svetainės natūralios kalbos funkcijas**.

- **NLWeb Protokolas**: Tai yra **pagrindinių taisyklių rinkinys natūralios kalbos sąveikai** su svetaine. Jis grąžina atsakymus JSON formatu (dažnai naudojant Schema.org). Jo tikslas – sukurti paprastą pagrindą „DI Tinklui“, panašiai kaip HTML leido dalintis dokumentais internete.

- **MCP Serveris (Modelio Konteksto Protokolo Galutinis Taškas)**: Kiekviena NLWeb sąranka taip pat veikia kaip **MCP serveris**. Tai reiškia, kad ji gali **dalintis įrankiais (pvz., „klausti“ metodu) ir duomenimis** su kitomis DI sistemomis.

- **Įterpimo Modeliai**: Šie modeliai naudojami **svetainės turiniui paversti skaitiniais atvaizdais, vadinamais vektoriais** (įterpimais). Šie vektoriai užfiksuoja prasmę taip, kad kompiuteriai galėtų juos palyginti ir ieškoti.

- **Vektorių Duomenų Bazė (Paieškos Mechanizmas)**: Ši duomenų bazė **saugo svetainės turinio įterpimus**. Kai kas nors užduoda klausimą, NLWeb tikrina vektorių duomenų bazę, kad greitai rastų tinkamiausią informaciją.

### NLWeb Pavyzdys

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.lt.png)

Apsvarstykime mūsų kelionių užsakymo svetainę, bet šį kartą ji veikia su NLWeb.

1. **Duomenų Įkėlimas**: Kelionių svetainės esami produktų katalogai (pvz., skrydžių sąrašai, viešbučių aprašymai, kelionių paketai) yra suformatuoti naudojant Schema.org arba įkelti per RSS srautus. NLWeb įrankiai įkelia šiuos struktūrizuotus duomenis, sukuria įterpimus ir saugo juos vietinėje arba nuotolinėje vektorių duomenų bazėje.

2. **Natūralios Kalbos Užklausa (Žmogus)**: Vartotojas apsilanko svetainėje ir, užuot naršęs meniu, įveda į pokalbių sąsają: „Raskite šeimai draugišką viešbutį Honolulu su baseinu kitai savaitei“.

3. **NLWeb Apdorojimas**: NLWeb programa gauna šią užklausą. Ji siunčia užklausą LLM, kad suprastų, ir tuo pačiu metu ieško savo vektorių duomenų bazėje tinkamų viešbučių sąrašų.

4. **Tikslūs Rezultatai**: LLM padeda interpretuoti paieškos rezultatus iš duomenų bazės, nustatyti geriausius atitikmenis pagal „šeimai draugiškas“, „baseinas“ ir „Honolulu“ kriterijus, o tada suformuoja natūralios kalbos atsakymą.

5. **DI Agento Sąveika**: Kadangi NLWeb veikia kaip MCP serveris, išorinis DI kelionių agentas taip pat galėtų prisijungti prie šios svetainės NLWeb instancijos. DI agentas galėtų naudoti `klausti` MCP metodą, kad tiesiogiai užduotų klausimą svetainei.

### Turite Daugiau Klausimų apie MCP/A2A/NLWeb?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiaisiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo DI agentų klausimus.

## Ištekliai

- [MCP Pradedantiesiems](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [NLWeb Saugykla](https://github.com/nlweb-ai/NLWeb)  
- [Semantic Kernel Vadovai](https://learn.microsoft.com/semantic-kernel/)  

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipiame dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudotis profesionalių vertėjų paslaugomis. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus aiškinimus, kylančius dėl šio vertimo naudojimo.