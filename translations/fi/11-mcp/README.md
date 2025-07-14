<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:44+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "fi"
}
-->
# Oppitunti 11: Model Context Protocol (MCP) -integraatio

## Johdanto Model Context Protocoliin (MCP)

Model Context Protocol (MCP) on huippuluokan kehys, joka on suunniteltu vakioimaan vuorovaikutus AI-mallien ja asiakasohjelmien välillä. MCP toimii siltana AI-mallien ja niitä käyttävien sovellusten välillä tarjoten yhtenäisen rajapinnan riippumatta mallin toteutuksesta.

MCP:n keskeiset ominaisuudet:

- **Vakiomuotoinen viestintä**: MCP luo yhteisen kielen sovelluksille kommunikoida AI-mallien kanssa
- **Parannettu kontekstinhallinta**: Mahdollistaa tehokkaan kontekstuaalisen tiedon välittämisen AI-malleille
- **Monialustainen yhteensopivuus**: Toimii useilla ohjelmointikielillä, kuten C#, Java, JavaScript, Python ja TypeScript
- **Saumaton integraatio**: Mahdollistaa kehittäjille erilaisten AI-mallien helpon liittämisen sovelluksiin

MCP on erityisen hyödyllinen AI-agenttien kehityksessä, sillä se mahdollistaa agenttien vuorovaikutuksen eri järjestelmien ja tietolähteiden kanssa yhtenäisen protokollan kautta, tehden agenteista joustavampia ja tehokkaampia.

## Oppimistavoitteet
- Ymmärtää, mitä MCP on ja sen rooli AI-agenttien kehityksessä
- Asentaa ja konfiguroida MCP-palvelin GitHub-integraatiota varten
- Rakentaa monen agentin järjestelmä MCP-työkaluilla
- Toteuttaa RAG (Retrieval Augmented Generation) Azure Cognitive Searchin avulla

## Esivaatimukset
- Python 3.8+
- Node.js 14+
- Azure-tilaus
- GitHub-tili
- Perustiedot Semantic Kernelistä

## Asennusohjeet

1. **Ympäristön asennus**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure-palveluiden konfigurointi**
   - Luo Azure Cognitive Search -resurssi
   - Ota käyttöön Azure OpenAI -palvelu
   - Määritä ympäristömuuttujat `.env`-tiedostoon

3. **MCP-palvelimen asennus**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Projektin rakenne

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Keskeiset komponentit

### 1. Monen agentin järjestelmä
- GitHub Agentti: Repositorion analysointi
- Hackathon Agentti: Projektisuositukset
- Events Agentti: Teknologiatapahtumien ehdotukset

### 2. Azure-integraatio
- Cognitive Search tapahtumien indeksointiin
- Azure OpenAI agenttien älykkyyteen
- RAG-mallin toteutus

### 3. MCP-työkalut
- GitHub-repositorion analyysi
- Koodin tarkastus
- Metatietojen poiminta

## Koodin läpikäynti

Esimerkki havainnollistaa:
1. MCP-palvelimen integroinnin
2. Monen agentin orkestroinnin
3. Azure Cognitive Search -integraation
4. RAG-mallin toteutuksen

Tärkeimmät ominaisuudet:
- Reaaliaikainen GitHub-repositorion analyysi
- Älykkäät projektisuositukset
- Tapahtumien yhdistäminen Azure Searchin avulla
- Vastauksien suoratoisto Chainlitillä

## Esimerkin suorittaminen

Yksityiskohtaiset asennusohjeet ja lisätiedot löytyvät [Github MCP Server Example README](./code_samples/github-mcp/README.md) -tiedostosta.

1. Käynnistä MCP-palvelin:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Käynnistä sovellus:
   ```bash
   chainlit run app.py -w
   ```

3. Testaa integraatio:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Vianetsintä

Yleisiä ongelmia ja ratkaisuja:
1. MCP-yhteysongelmat
   - Varmista, että palvelin on käynnissä
   - Tarkista portin saatavuus
   - Vahvista GitHub-tokenit

2. Azure Search -ongelmat
   - Tarkista yhteysmerkkijonot
   - Varmista indeksin olemassaolo
   - Tarkista dokumenttien lataus

## Seuraavat askeleet
- Tutustu lisä-MCP-työkaluihin
- Toteuta omia agentteja
- Paranna RAG-ominaisuuksia
- Lisää lisää tapahtumalähteitä

## Resurssit
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.