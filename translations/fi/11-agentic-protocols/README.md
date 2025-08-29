<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6600bebb86f72f3f62a9163fcce9566",
  "translation_date": "2025-08-29T18:23:04+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "fi"
}
-->
# Agenttisten protokollien käyttö (MCP, A2A ja NLWeb)

[![Agenttiset protokollat](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.fi.png)](https://youtu.be/X-Dh9R3Opn8)

Kun tekoälyagenttien käyttö kasvaa, myös tarve protokollille, jotka varmistavat standardoinnin, turvallisuuden ja avoimen innovaation tukemisen, lisääntyy. Tässä oppitunnissa käsittelemme kolmea protokollaa, jotka pyrkivät vastaamaan tähän tarpeeseen: Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Johdanto

Tässä oppitunnissa käsitellään:

• Kuinka **MCP** mahdollistaa tekoälyagenttien pääsyn ulkoisiin työkaluihin ja tietoihin käyttäjän tehtävien suorittamiseksi.

• Kuinka **A2A** mahdollistaa viestinnän ja yhteistyön eri tekoälyagenttien välillä.

• Kuinka **NLWeb** tuo luonnollisen kielen käyttöliittymät mille tahansa verkkosivustolle, mahdollistaen tekoälyagenttien sisällön löytämisen ja vuorovaikutuksen sen kanssa.

## Oppimistavoitteet

• **Tunnistaa** MCP:n, A2A:n ja NLWebin keskeinen tarkoitus ja hyödyt tekoälyagenttien kontekstissa.

• **Selittää**, kuinka kukin protokolla helpottaa viestintää ja vuorovaikutusta LLM:ien, työkalujen ja muiden agenttien välillä.

• **Tunnistaa** kunkin protokollan erityiset roolit monimutkaisten agenttijärjestelmien rakentamisessa.

## Model Context Protocol

**Model Context Protocol (MCP)** on avoin standardi, joka tarjoaa yhtenäisen tavan sovelluksille tarjota konteksti ja työkalut LLM:ille. Tämä mahdollistaa "universaalin sovittimen" eri tietolähteille ja työkaluille, joihin tekoälyagentit voivat yhdistyä johdonmukaisella tavalla.

Tarkastellaan MCP:n komponentteja, sen etuja verrattuna suoraan API-käyttöön ja esimerkkiä siitä, kuinka tekoälyagentit voivat käyttää MCP-palvelinta.

### MCP:n keskeiset komponentit

MCP toimii **asiakas-palvelin-arkkitehtuurilla**, ja sen keskeiset komponentit ovat:

• **Isännät** ovat LLM-sovelluksia (esimerkiksi koodieditori kuten VSCode), jotka aloittavat yhteydet MCP-palvelimeen.

• **Asiakkaat** ovat isäntäsovelluksen sisäisiä komponentteja, jotka ylläpitävät yksi-yhteen-yhteyksiä palvelimiin.

• **Palvelimet** ovat kevyitä ohjelmia, jotka tarjoavat tiettyjä toimintoja.

Protokollaan sisältyy kolme keskeistä perusominaisuutta, jotka ovat MCP-palvelimen kyvykkyyksiä:

• **Työkalut**: Nämä ovat yksittäisiä toimintoja tai tehtäviä, joita tekoälyagentti voi kutsua suorittaakseen toiminnon. Esimerkiksi säätietopalvelu voi tarjota "hae sää" -työkalun, tai verkkokauppapalvelin voi tarjota "osta tuote" -työkalun. MCP-palvelimet ilmoittavat kunkin työkalun nimen, kuvauksen ja syöte/tuloste-skeeman kyvykkyysluettelossaan.

• **Resurssit**: Nämä ovat vain luku -tyyppisiä tietoja tai asiakirjoja, joita MCP-palvelin voi tarjota, ja asiakkaat voivat noutaa ne tarvittaessa. Esimerkkejä ovat tiedostojen sisältö, tietokantatiedot tai lokitiedostot. Resurssit voivat olla tekstiä (kuten koodia tai JSON-tiedostoja) tai binäärimuotoisia (kuten kuvia tai PDF-tiedostoja).

• **Kehoitteet**: Nämä ovat ennalta määriteltyjä malleja, jotka tarjoavat ehdotettuja kehoitteita, mahdollistaen monimutkaisempia työnkulkuja.

### MCP:n edut

MCP tarjoaa merkittäviä etuja tekoälyagenteille:

• **Dynaaminen työkalujen löytäminen**: Agentit voivat dynaamisesti vastaanottaa luettelon käytettävissä olevista työkaluista palvelimelta sekä kuvaukset niiden toiminnasta. Tämä eroaa perinteisistä API:ista, jotka usein vaativat staattista koodausta integraatioihin, mikä tarkoittaa, että API-muutokset edellyttävät koodipäivityksiä. MCP tarjoaa "integroi kerran" -lähestymistavan, mikä lisää mukautuvuutta.

• **Yhteensopivuus eri LLM:ien välillä**: MCP toimii eri LLM:ien kanssa, tarjoten joustavuutta vaihtaa ydintä malleihin paremman suorituskyvyn arvioimiseksi.

• **Standardoitu turvallisuus**: MCP sisältää standardoidun todennusmenetelmän, mikä parantaa skaalautuvuutta lisättäessä pääsyä muihin MCP-palvelimiin. Tämä on yksinkertaisempaa kuin hallita eri avaimia ja todennustyyppejä eri perinteisille API:ille.

### MCP-esimerkki

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.fi.png)

Kuvitellaan, että käyttäjä haluaa varata lennon tekoälyavustajan avulla, joka käyttää MCP:tä.

1. **Yhteys**: Tekoälyavustaja (MCP-asiakas) yhdistyy lentoyhtiön tarjoamaan MCP-palvelimeen.

2. **Työkalujen löytäminen**: Asiakas kysyy lentoyhtiön MCP-palvelimelta: "Mitä työkaluja sinulla on käytettävissä?" Palvelin vastaa työkaluilla, kuten "etsi lentoja" ja "varaa lentoja".

3. **Työkalun kutsuminen**: Käyttäjä pyytää tekoälyavustajaa: "Etsi lento Portlandista Honoluluun." Tekoälyavustaja, käyttäen LLM:äänsä, tunnistaa, että sen täytyy kutsua "etsi lentoja" -työkalu ja välittää asiaankuuluvat parametrit (lähtöpaikka, määränpää) MCP-palvelimelle.

4. **Suoritus ja vastaus**: MCP-palvelin, joka toimii kääreenä, tekee varsinaisen kutsun lentoyhtiön sisäiseen varaus-API:iin. Se vastaanottaa lentotiedot (esim. JSON-muodossa) ja lähettää ne takaisin tekoälyavustajalle.

5. **Jatkovuorovaikutus**: Tekoälyavustaja esittää lentovaihtoehdot. Kun käyttäjä valitsee lennon, avustaja voi kutsua "varaa lento" -työkalun samalta MCP-palvelimelta, viimeistellen varauksen.

## Agent-to-Agent Protocol (A2A)

Kun MCP keskittyy LLM:ien yhdistämiseen työkaluihin, **Agent-to-Agent (A2A) -protokolla** vie tämän askeleen pidemmälle mahdollistamalla viestinnän ja yhteistyön eri tekoälyagenttien välillä. A2A yhdistää tekoälyagentit eri organisaatioiden, ympäristöjen ja teknologiapinojen välillä suorittamaan yhteistä tehtävää.

Tarkastelemme A2A:n komponentteja ja etuja sekä esimerkkiä siitä, kuinka sitä voitaisiin soveltaa matkailusovelluksessamme.

### A2A:n keskeiset komponentit

A2A keskittyy mahdollistamaan agenttien välisen viestinnän ja niiden yhteistyön käyttäjän alitehtävän suorittamiseksi. Jokainen protokollan komponentti edistää tätä:

#### Agenttikortti

Samoin kuin MCP-palvelin jakaa luettelon työkaluista, agenttikortti sisältää:
    ◦ Agentin nimen.  
    ◦ **Kuvauksen yleisistä tehtävistä**, joita se suorittaa.  
    ◦ **Luettelon erityisistä taidoista** kuvauksineen, jotka auttavat muita agentteja (tai jopa ihmiskäyttäjiä) ymmärtämään, milloin ja miksi he haluaisivat kutsua kyseistä agenttia.  
    ◦ Agentin **nykyisen päätepisteen URL-osoitteen**.  
    ◦ Agentin **version** ja **kyvykkyydet**, kuten suoratoistovastaukset ja push-ilmoitukset.  

#### Agentin suorittaja

Agentin suorittaja vastaa **käyttäjän keskustelun kontekstin välittämisestä etäagentille**, jotta etäagentti ymmärtää, mikä tehtävä on suoritettava. A2A-palvelimessa agentti käyttää omaa LLM:äänsä tulkitsemaan saapuvat pyynnöt ja suorittamaan tehtäviä omilla sisäisillä työkaluillaan.

#### Artefakti

Kun etäagentti on suorittanut pyydetyn tehtävän, sen työn tulos luodaan artefaktina. Artefakti **sisältää agentin työn tuloksen**, **kuvauksen suoritetusta tehtävästä** ja **tekstikontekstin**, joka lähetetään protokollan kautta. Kun artefakti on lähetetty, yhteys etäagenttiin suljetaan, kunnes sitä tarvitaan uudelleen.

#### Tapahtumajono

Tätä komponenttia käytetään **päivitysten käsittelyyn ja viestien välittämiseen**. Se on erityisen tärkeä tuotantoympäristöissä agenttijärjestelmille, jotta agenttien välinen yhteys ei sulkeudu ennen tehtävän valmistumista, erityisesti kun tehtävän suorittaminen voi kestää pidemmän aikaa.

### A2A:n edut

• **Parannettu yhteistyö**: Mahdollistaa eri toimittajien ja alustojen agenttien vuorovaikutuksen, kontekstin jakamisen ja yhteistyön, helpottaen saumattoman automaation perinteisesti erillisten järjestelmien välillä.

• **Mallin valinnan joustavuus**: Jokainen A2A-agentti voi päättää, mitä LLM:ää se käyttää pyyntöjensä käsittelyyn, mahdollistaen optimoidut tai hienosäädetyt mallit agenttia kohden, toisin kuin yksittäinen LLM-yhteys joissakin MCP-skenaarioissa.

• **Sisäänrakennettu todennus**: Todennus on integroitu suoraan A2A-protokollaan, tarjoten vahvan turvallisuuskehyksen agenttien väliselle vuorovaikutukselle.

### A2A-esimerkki

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.fi.png)

Laajennetaan matkavarauksen skenaariota, mutta tällä kertaa käytetään A2A:ta.

1. **Käyttäjän pyyntö monitoimiagentille**: Käyttäjä on vuorovaikutuksessa "Matka-agentti" A2A-asiakas/agentin kanssa, esimerkiksi sanomalla: "Varaa koko matka Honoluluun ensi viikolle, mukaan lukien lennot, hotelli ja vuokra-auto."

2. **Matka-agentin orkestrointi**: Matka-agentti vastaanottaa tämän monimutkaisen pyynnön. Se käyttää LLM:äänsä päättelyyn tehtävästä ja määrittää, että sen täytyy olla vuorovaikutuksessa muiden erikoistuneiden agenttien kanssa.

3. **Agenttien välinen viestintä**: Matka-agentti käyttää A2A-protokollaa yhdistyäkseen alaspäin oleviin agentteihin, kuten "Lentoyhtiöagentti", "Hotelliagentti" ja "Autovuokraamoagentti", jotka on luotu eri yritysten toimesta.

4. **Tehtävien delegointi**: Matka-agentti lähettää erityisiä tehtäviä näille erikoistuneille agenteille (esim. "Etsi lentoja Honoluluun", "Varaa hotelli", "Vuokraa auto"). Jokainen näistä erikoistuneista agenteista, jotka käyttävät omia LLM:äänsä ja omia työkalujaan (jotka voivat olla MCP-palvelimia), suorittaa oman osuutensa varauksesta.

5. **Koottu vastaus**: Kun kaikki alaspäin olevat agentit ovat suorittaneet tehtävänsä, matka-agentti kokoaa tulokset (lentotiedot, hotellivahvistus, autonvuokraus) ja lähettää kattavan, keskustelutyylisen vastauksen takaisin käyttäjälle.

## Natural Language Web (NLWeb)

Verkkosivustot ovat pitkään olleet ensisijainen tapa käyttäjille päästä käsiksi tietoon ja dataan internetissä.

Tarkastellaan NLWebin eri komponentteja, sen etuja ja esimerkkiä siitä, kuinka NLWeb toimii matkailusovelluksessamme.

### NLWebin komponentit

- **NLWeb-sovellus (ydinpalvelukoodi)**: Järjestelmä, joka käsittelee luonnollisen kielen kysymyksiä. Se yhdistää alustan eri osat luodakseen vastauksia. Voit ajatella sitä verkkosivuston luonnollisen kielen ominaisuuksien **moottorina**.

- **NLWeb-protokolla**: Tämä on **perussääntöjen joukko luonnollisen kielen vuorovaikutukselle** verkkosivuston kanssa. Se lähettää vastaukset JSON-muodossa (usein käyttäen Schema.orgia). Sen tarkoitus on luoda yksinkertainen perusta "tekoälyverkolle", samalla tavalla kuin HTML mahdollisti asiakirjojen jakamisen verkossa.

- **MCP-palvelin (Model Context Protocol -päätepiste)**: Jokainen NLWeb-asennus toimii myös **MCP-palvelimena**. Tämä tarkoittaa, että se voi **jakaa työkaluja (kuten "kysy"-menetelmä) ja dataa** muiden tekoälyjärjestelmien kanssa. Käytännössä tämä tekee verkkosivuston sisällöstä ja kyvyistä käytettävissä olevan tekoälyagenteille, mahdollistaen sivuston osaksi laajempaa "agenttiekosysteemiä".

- **Upotusmallit**: Näitä malleja käytetään **muuntamaan verkkosivuston sisältö numeerisiksi esityksiksi, joita kutsutaan vektoreiksi** (upotukset). Nämä vektorit tallentavat merkityksen tavalla, jota tietokoneet voivat verrata ja hakea. Ne tallennetaan erityiseen tietokantaan, ja käyttäjät voivat valita, mitä upotusmallia he haluavat käyttää.

- **Vektoripohjainen tietokanta (hakumekanismi)**: Tämä tietokanta **tallentaa verkkosivuston sisällön upotukset**. Kun joku esittää kysymyksen, NLWeb tarkistaa vektoripohjaisen tietokannan löytääkseen nopeasti merkityksellisimmät tiedot. Se antaa nopean luettelon mahdollisista vastauksista, jotka on järjestetty samankaltaisuuden mukaan. NLWeb toimii eri vektorivarastojärjestelmien kanssa, kuten Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb-esimerkki

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.fi.png)

Kuvitellaan matkailusivustoamme uudelleen, mutta tällä kertaa se on NLWebin tukema.

1. **Datan syöttö**: Matkailusivuston olemassa olevat tuotekatalogit (esim. lentoluettelot, hotellikuvaukset, matkailupaketit) muotoillaan Schema.orgin avulla tai ladataan RSS-syötteiden kautta. NLWebin työkalut syöttävät tämän rakenteellisen datan, luovat upotukset ja tallentavat ne paikalliseen tai etävektoritietokantaan.

2. **Luonnollisen kielen kysely (ihminen)**: Käyttäjä vierailee verkkosivustolla ja kirjoittaa chat-käyttöliittymään: "Etsi perheystävällinen hotelli Honolulusta, jossa on uima-allas ensi viikolle."

3. **NLWebin käsittely**: NLWeb-sovellus vastaanottaa tämän kyselyn. Se lähettää kyselyn LLM:lle ymmärtämistä varten ja etsii samanaikaisesti vektoripohjaisesta tietokannastaan merkityksellisiä hotelliluetteloita.

4. **Tarkat tulokset**: LLM auttaa tulkitsemaan tietokannan hakutuloksia, tunnistamaan parhaat osumat "perheystävällinen", "uima-allas" ja "Honolulu" -kriteerien perusteella ja muotoilemaan luonnollisen kielen vastauksen. Tärkeää on, että vastaus viittaa verkkosivuston todellisiin hotelleihin, välttäen keksittyä tietoa.

5. **Tekoälyagentin vuorovaikutus**: Koska NLWeb toimii MCP-palvelimena, ulkoinen tekoälymatka-agentti voisi myös yhdistyä tämän verkkosivuston NLWeb-instanssiin. Tekoälyagentti voisi sitten käyttää `ask`-MCP-menetelmää kysyäkseen verkkosivustolta suoraan: `ask("Onko Honolulun alueella vegaaniravintoloita, joita hotelli suosittelee?")`. NLWeb-instanssi käsittelisi tämän, hyödyntäen tietokantaansa ravintolatiedoista (jos ladattu), ja palauttaisi rakenteellisen JSON-vastauksen.

### Onko sinulla lisää kysymyksiä MCP:stä, A2A:sta tai NLWebistä?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.