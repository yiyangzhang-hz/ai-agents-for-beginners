<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T17:14:15+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "fi"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.fi.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Agentic RAG

Tämä oppitunti tarjoaa kattavan yleiskatsauksen Agentic Retrieval-Augmented Generationiin (Agentic RAG), nousevaan tekoälyparadigmaan, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavat askeleensa samalla, kun ne hakevat tietoa ulkoisista lähteistä. Toisin kuin staattiset "haku ja luku" -mallit, Agentic RAG sisältää iteratiivisia kutsuja LLM:lle, joita vuorottelevat työkalujen tai toimintojen kutsut ja jäsennellyt tulosteet. Järjestelmä arvioi tuloksia, tarkentaa kyselyitä, käyttää tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu.

## Johdanto

Tässä oppitunnissa käsitellään:

- **Ymmärrä Agentic RAG:** Opi tekoälyn nousevasta paradigmasta, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavat askeleensa samalla, kun ne hakevat tietoa ulkoisista tietolähteistä.
- **Omaksu iteratiivinen Maker-Checker-tyyli:** Ymmärrä iteratiivisten LLM-kutsujen sykli, jota vuorottelevat työkalujen tai toimintojen kutsut ja jäsennellyt tulosteet, jotka on suunniteltu parantamaan tarkkuutta ja käsittelemään virheellisiä kyselyitä.
- **Tutki käytännön sovelluksia:** Tunnista tilanteet, joissa Agentic RAG loistaa, kuten tarkkuutta vaativat ympäristöt, monimutkaiset tietokantainteraktiot ja laajennetut työnkulut.

## Oppimistavoitteet

Oppitunnin jälkeen osaat/ymmärrät:

- **Agentic RAG:n ymmärtäminen:** Opi tekoälyn nousevasta paradigmasta, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavat askeleensa samalla, kun ne hakevat tietoa ulkoisista tietolähteistä.
- **Iteratiivinen Maker-Checker-tyyli:** Ymmärrä iteratiivisten LLM-kutsujen sykli, jota vuorottelevat työkalujen tai toimintojen kutsut ja jäsennellyt tulosteet, jotka on suunniteltu parantamaan tarkkuutta ja käsittelemään virheellisiä kyselyitä.
- **Päätöksenteon hallinta:** Ymmärrä järjestelmän kyky hallita omaa päättelyprosessiaan ja tehdä päätöksiä ongelmien lähestymistavasta ilman ennalta määriteltyjä polkuja.
- **Työnkulku:** Ymmärrä, miten agenttimalli päättää itsenäisesti hakea markkinatrendiraportteja, tunnistaa kilpailijatietoja, yhdistää sisäisiä myyntimittareita, synteettisesti analysoida löydöksiä ja arvioida strategiaa.
- **Iteratiiviset silmukat, työkalujen integrointi ja muisti:** Opi, miten järjestelmä hyödyntää silmukkamaista vuorovaikutusmallia, ylläpitää tilaa ja muistia vaiheiden välillä välttääkseen toistuvia silmukoita ja tehdäkseen tietoisia päätöksiä.
- **Virhetilanteiden käsittely ja itsekorjaus:** Tutki järjestelmän vahvoja itsekorjausmekanismeja, mukaan lukien iterointi ja uudelleenkysely, diagnostiikkatyökalujen käyttö ja ihmisen valvontaan turvautuminen.
- **Toimintavapauden rajat:** Ymmärrä Agentic RAG:n rajoitukset, keskittyen toimialakohtaiseen autonomiaan, infrastruktuuririippuvuuteen ja turvamekanismien kunnioittamiseen.
- **Käytännön käyttötapaukset ja arvo:** Tunnista tilanteet, joissa Agentic RAG loistaa, kuten tarkkuutta vaativat ympäristöt, monimutkaiset tietokantainteraktiot ja laajennetut työnkulut.
- **Hallinta, läpinäkyvyys ja luottamus:** Opi hallinnan ja läpinäkyvyyden tärkeydestä, mukaan lukien selitettävä päättely, puolueettomuuden hallinta ja ihmisen valvonta.

## Mikä on Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva tekoälyparadigma, jossa suuret kielimallit (LLM:t) suunnittelevat itsenäisesti seuraavat askeleensa samalla, kun ne hakevat tietoa ulkoisista lähteistä. Toisin kuin staattiset "haku ja luku" -mallit, Agentic RAG sisältää iteratiivisia kutsuja LLM:lle, joita vuorottelevat työkalujen tai toimintojen kutsut ja jäsennellyt tulosteet. Järjestelmä arvioi tuloksia, tarkentaa kyselyitä, käyttää tarvittaessa lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu. Tämä iteratiivinen "maker-checker"-tyyli parantaa tarkkuutta, käsittelee virheellisiä kyselyitä ja varmistaa korkealaatuiset tulokset.

Järjestelmä hallitsee aktiivisesti omaa päättelyprosessiaan, kirjoittaa epäonnistuneet kyselyt uudelleen, valitsee erilaisia hakutapoja ja integroi useita työkaluja—kuten vektorihaun Azure AI Searchissa, SQL-tietokantoja tai mukautettuja API-rajapintoja—ennen lopullisen vastauksen antamista. Agenttijärjestelmän erottuva piirre on sen kyky hallita omaa päättelyprosessiaan. Perinteiset RAG-toteutukset luottavat ennalta määriteltyihin polkuihin, mutta agenttijärjestelmä päättää itsenäisesti askelten järjestyksen löytämänsä tiedon laadun perusteella.

## Agentic Retrieval-Augmented Generationin (Agentic RAG) määrittely

Agentic Retrieval-Augmented Generation (Agentic RAG) on nouseva tekoälykehityksen paradigma, jossa LLM:t eivät ainoastaan hae tietoa ulkoisista tietolähteistä, vaan myös suunnittelevat itsenäisesti seuraavat askeleensa. Toisin kuin staattiset "haku ja luku" -mallit tai huolellisesti skriptatut kehotussekvenssit, Agentic RAG sisältää iteratiivisten LLM-kutsujen silmukan, jota vuorottelevat työkalujen tai toimintojen kutsut ja jäsennellyt tulosteet. Jokaisessa vaiheessa järjestelmä arvioi saatuja tuloksia, päättää, tarkentaako kyselyitä, käyttääkö lisätyökaluja ja jatkaa tätä sykliä, kunnes saavutetaan tyydyttävä ratkaisu.

Tämä iteratiivinen "maker-checker"-tyyli on suunniteltu parantamaan tarkkuutta, käsittelemään virheellisiä kyselyitä jäsenneltyihin tietokantoihin (esim. NL2SQL) ja varmistamaan tasapainoiset, korkealaatuiset tulokset. Sen sijaan, että järjestelmä luottaisi pelkästään huolellisesti suunniteltuihin kehotusketjuihin, se hallitsee aktiivisesti omaa päättelyprosessiaan. Se voi kirjoittaa epäonnistuneet kyselyt uudelleen, valita erilaisia hakutapoja ja integroida useita työkaluja—kuten vektorihaun Azure AI Searchissa, SQL-tietokantoja tai mukautettuja API-rajapintoja—ennen lopullisen vastauksen antamista. Tämä poistaa tarpeen monimutkaisille orkestrointikehyksille. Sen sijaan suhteellisen yksinkertainen silmukka "LLM-kutsu → työkalun käyttö → LLM-kutsu → …" voi tuottaa hienostuneita ja hyvin perusteltuja tuloksia.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.fi.png)

## Päättelyprosessin hallinta

Agenttijärjestelmän erottuva piirre on sen kyky hallita omaa päättelyprosessiaan. Perinteiset RAG-toteutukset luottavat usein ihmisten ennalta määrittelemään polkuun: ajatusketjuun, joka määrittelee, mitä hakea ja milloin.  
Mutta kun järjestelmä on aidosti agenttinen, se päättää sisäisesti, miten ongelmaa lähestytään. Se ei vain suorita skriptiä; se määrittää itsenäisesti askelten järjestyksen löytämänsä tiedon laadun perusteella.  
Esimerkiksi, jos sitä pyydetään luomaan tuotelanseerausstrategia, se ei luota pelkästään kehotukseen, joka määrittelee koko tutkimus- ja päätöksentekotyönkulun. Sen sijaan agenttimalli päättää itsenäisesti:

1. Hakea ajankohtaisia markkinatrendiraportteja Bing Web Groundingin avulla.
2. Tunnistaa olennaisia kilpailijatietoja Azure AI Searchin avulla.
3. Yhdistää historiallisia sisäisiä myyntimittareita Azure SQL Databasea käyttäen.
4. Synteettisesti analysoida löydökset yhtenäiseksi strategiaksi Azure OpenAI Servicen avulla.
5. Arvioida strategiaa aukkojen tai epäjohdonmukaisuuksien varalta, mikä voi johtaa uuteen hakukierrokseen.

Kaikki nämä vaiheet—kyselyiden tarkentaminen, lähteiden valinta, iterointi, kunnes vastaus on "tyydyttävä"—päätetään mallin toimesta, ei ihmisen ennalta skriptamana.

## Iteratiiviset silmukat, työkalujen integrointi ja muisti

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.fi.png)

Agenttijärjestelmä perustuu silmukkamaiseen vuorovaikutusmalliin:

- **Alustava kutsu:** Käyttäjän tavoite (eli käyttäjän kehotus) esitetään LLM:lle.
- **Työkalun käyttö:** Jos malli havaitsee puuttuvaa tietoa tai epäselviä ohjeita, se valitsee työkalun tai hakutavan—kuten vektorikantahakukyselyn (esim. Azure AI Search Hybrid -haku yksityisistä tiedoista) tai jäsennellyn SQL-kyselyn—hankkiakseen lisää kontekstia.
- **Arviointi ja tarkentaminen:** Palautetun datan tarkastelun jälkeen malli päättää, riittääkö tieto. Jos ei, se tarkentaa kyselyä, kokeilee eri työkalua tai säätää lähestymistapaansa.
- **Toista, kunnes tyytyväinen:** Tämä sykli jatkuu, kunnes malli katsoo, että sillä on tarpeeksi selkeyttä ja todisteita lopullisen, hyvin perustellun vastauksen antamiseen.
- **Muisti ja tila:** Koska järjestelmä ylläpitää tilaa ja muistia vaiheiden välillä, se voi muistaa aiemmat yritykset ja niiden tulokset, välttäen toistuvia silmukoita ja tehden tietoisempia päätöksiä edetessään.

Ajan myötä tämä luo tunteen kehittyvästä ymmärryksestä, mikä mahdollistaa mallin navigoida monimutkaisissa, monivaiheisissa tehtävissä ilman, että ihmisen tarvitsee jatkuvasti puuttua asiaan tai muokata kehotusta.

## Virhetilanteiden käsittely ja itsekorjaus

Agentic RAG:n autonomia sisältää myös vahvat itsekorjausmekanismit. Kun järjestelmä kohtaa umpikujaan johtavia tilanteita—kuten epäolennaisten dokumenttien hakemista tai virheellisiä kyselyitä—se voi:

- **Iteroida ja kysyä uudelleen:** Sen sijaan, että se palauttaisi vähäarvoisia vastauksia, malli kokeilee uusia hakustrategioita, kirjoittaa tietokantakyselyitä uudelleen tai tarkastelee vaihtoehtoisia tietojoukkoja.
- **Käyttää diagnostiikkatyökaluja:** Järjestelmä voi kutsua lisätoimintoja, jotka on suunniteltu auttamaan sen päättelyvaiheiden virheenkorjauksessa tai varmistamaan haetun datan oikeellisuus. Työkalut, kuten Azure AI Tracing, ovat tärkeitä mahdollistamaan vahvan havainnoinnin ja seurannan.
- **Turvautua ihmisen valvontaan:** Korkean riskin tai toistuvasti epäonnistuvissa tilanteissa malli voi merkitä epävarmuuden ja pyytää ihmisen ohjausta. Kun ihminen antaa korjaavaa palautetta, malli voi sisällyttää oppimansa jatkossa.

Tämä iteratiivinen ja dynaaminen lähestymistapa mahdollistaa mallin jatkuvan parantamisen, varmistaen, että se ei ole vain kertakäyttöinen järjestelmä, vaan oppii virheistään kyseisen istunnon aikana.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.fi.png)

## Toimintavapauden rajat

Vaikka Agentic RAG on autonominen tehtävänsä sisällä, se ei ole verrattavissa yleiseen tekoälyyn (Artificial General Intelligence). Sen "agenttiset" kyvyt rajoittuvat ihmisten kehittämiin työkaluihin, tietolähteisiin ja käytäntöihin. Se ei voi keksiä omia työkalujaan tai ylittää sille asetettuja toimialarajoja. Sen sijaan se loistaa dynaamisesti orkestroimalla käytettävissä olevia resursseja.  
Keskeiset erot kehittyneempiin tekoälymuotoihin ovat:

1. **Toimialakohtainen autonomia:** Agentic RAG -järjestelmät keskittyvät käyttäjän määrittämien tavoitteiden saavuttamiseen tunnetulla toimialalla, hyödyntäen strategioita, kuten kyselyiden uudelleenkirjoittamista tai työkalujen valintaa tulosten parantamiseksi.
2. **Infrastruktuuririippuvuus:** Järjestelmän kyvyt riippuvat kehittäjien integroimista työkaluista ja tiedoista. Se ei voi ylittää näitä rajoja ilman ihmisen väliintuloa.
3. **Turvamekanismien kunnioittaminen:** Eettiset ohjeet, sääntöjen noudattaminen ja liiketoimintakäytännöt ovat edelleen erittäin tärkeitä. Agentin vapaus on aina rajoitettu turvallisuusmekanismeilla ja valvontajärjestelmillä (toivottavasti?).

## Käytännön käyttötapaukset ja arvo

Agentic RAG loistaa tilanteissa, jotka vaativat iteratiivista tarkentamista ja tarkkuutta:

1. **Tarkkuutta vaativat ympäristöt:** Säädösten tarkastuksissa, sääntelyanalyysissä tai oikeudellisessa tutkimuksessa agenttimalli voi toistuvasti tarkistaa faktoja, konsultoida useita lähteitä ja kirjoittaa kyselyitä uudelleen, kunnes se tuottaa perusteellisesti tarkistetun vastauksen.
2. **Monimutkaiset tietokantainteraktiot:** Kun käsitellään jäsenneltyjä tietoja, joissa kyselyt voivat usein epäonnistua tai vaatia säätöä, järjestelmä voi itsenäisesti tarkentaa kyselyitään Azure SQL:n tai Microsoft Fabric OneLaken avulla varmistaen, että lopullinen haku vastaa käyttäjän tarkoitusta.
3. **Laajennetut työnkulut:** Pidemmät istunnot voivat kehittyä, kun uutta tietoa tulee esiin. Agentic RAG voi jatkuvasti sisällyttää uutta dataa, muuttaa strategioita ja oppia lisää ongelma-alueesta.

## Hallinta, läpinäkyvyys ja luottamus

Kun nämä järjestelmät tulevat yhä itsenäisemmiksi päättelyssään, hallinta ja läpinäkyvyys ovat ratkaisevan tärkeitä:

- **Selitettävä päättely:** Malli voi tarjota auditointipolun tekemistään kyselyistä, konsultoimistaan lähteistä ja päättelyvaiheista, jotka johtivat sen lopputulokseen. Työkalut, kuten Azure AI Content Safety ja Azure AI Tracing / GenAIOps, voivat auttaa ylläpitämään läpinäkyvyyttä ja vähentämään riskejä.
- **Puolueettomuuden hallinta ja tasapainoinen haku:** Kehittäjät voivat säätää hakustrategioita varmistaakseen, että tasapainoiset ja edustavat tietolähteet otetaan huomioon, ja säännöllisesti auditoida tuloksia puolueellisuuden tai vinoutuneiden mallien havaitsemiseksi käyttämällä mukautettuja malleja edistyneille data science -organisaatioille Azure Machine Learningin avulla.
- **Ihmisen valvonta ja sääntöjen noudattaminen:** Herkissä tehtävissä ihmisen tarkistus on edelleen välttämätöntä. Agentic RAG ei korvaa ihmisen harkintaa korkean panoksen päätöksissä—se täydentää sitä tarjoamalla perusteellisemmin tarkistettuja vaihtoehtoja.

Työkalut, jotka tarjoavat selkeän toimintarekisterin, ovat välttämättömiä. Ilman niitä monivaiheisen prosessin virheenk
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Toteuta Retrieval Augmented Generation (RAG) Azure OpenAI -palvelulla: Opi käyttämään omaa dataasi Azure OpenAI -palvelun kanssa. Tämä Microsoft Learn -moduuli tarjoaa kattavan oppaan RAG:n toteuttamiseen</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisen tekoälyn sovellusten arviointi Azure AI Foundry -palvelussa: Tämä artikkeli käsittelee mallien arviointia ja vertailua julkisesti saatavilla olevilla aineistoilla, mukaan lukien Agentic AI -sovellukset ja RAG-arkkitehtuurit</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mikä on Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Täydellinen opas agenttipohjaiseen Retrieval Augmented Generationiin – Uutisia RAG:sta</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: tehosta RAG:ia kyselymuokkauksella ja itseohjautuvilla kyselyillä! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agenttikerrosten lisääminen RAG:iin</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Tiedon avustajien tulevaisuus: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Kuinka rakentaa Agentic RAG -järjestelmiä</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Azure AI Foundry Agent Service -palvelun käyttö tekoälyagenttien skaalaamiseen</a>

### Akateemiset artikkelit

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratiivinen parantaminen itsepalautteen avulla</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Kielelliset agentit sanallisella vahvistusoppimisella</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Suuret kielimallit voivat korjata itseään työkalujen avulla</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Katsaus Agentic RAG:iin</a>

## Edellinen oppitunti

[Työkalujen käyttö -suunnittelumalli](../04-tool-use/README.md)

## Seuraava oppitunti

[Luotettavien tekoälyagenttien rakentaminen](../06-building-trustworthy-agents/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.