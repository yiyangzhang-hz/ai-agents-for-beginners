<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T17:13:16+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "fi"
}
-->
[![Miten suunnitella hyviä tekoälyagentteja](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.fi.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Työkalujen käyttö -suunnittelumalli

Työkalut ovat mielenkiintoisia, koska ne laajentavat tekoälyagenttien kyvykkyyksiä. Sen sijaan, että agentilla olisi vain rajallinen joukko toimintoja, työkalun lisääminen mahdollistaa huomattavasti laajemman toimintavalikoiman. Tässä luvussa tarkastelemme Työkalujen käyttö -suunnittelumallia, joka kuvaa, miten tekoälyagentit voivat käyttää tiettyjä työkaluja saavuttaakseen tavoitteensa.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Mikä on työkalujen käyttö -suunnittelumalli?
- Mihin käyttötapauksiin sitä voidaan soveltaa?
- Mitkä ovat suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?
- Mitä erityisiä huomioita on otettava huomioon, kun rakennetaan luotettavia tekoälyagentteja käyttäen tätä suunnittelumallia?

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Määritellä Työkalujen käyttö -suunnittelumallin ja sen tarkoituksen.
- Tunnistaa käyttötapaukset, joissa suunnittelumalli on sovellettavissa.
- Ymmärtää suunnittelumallin toteuttamiseen tarvittavat keskeiset elementit.
- Tunnistaa huomioitavat asiat luotettavuuden varmistamiseksi tekoälyagenteissa, jotka käyttävät tätä suunnittelumallia.

## Mikä on Työkalujen käyttö -suunnittelumalli?

**Työkalujen käyttö -suunnittelumalli** keskittyy antamaan suurille kielimalleille (LLM) kyvyn käyttää ulkoisia työkaluja saavuttaakseen tiettyjä tavoitteita. Työkalut ovat koodia, jonka agentti voi suorittaa toimintoja varten. Työkalu voi olla yksinkertainen funktio, kuten laskin, tai API-kutsu kolmannen osapuolen palveluun, kuten osakekurssien tarkistus tai säätiedot. Tekoälyagenttien kontekstissa työkalut on suunniteltu suoritettaviksi agenttien toimesta vastauksena **mallin generoimiin funktiokutsuihin**.

## Mihin käyttötapauksiin sitä voidaan soveltaa?

Tekoälyagentit voivat hyödyntää työkaluja suorittaakseen monimutkaisia tehtäviä, hakeakseen tietoa tai tehdäkseen päätöksiä. Työkalujen käyttö -suunnittelumallia käytetään usein tilanteissa, joissa tarvitaan dynaamista vuorovaikutusta ulkoisten järjestelmien, kuten tietokantojen, verkkopalveluiden tai koodintulkitsijoiden, kanssa. Tämä kyky on hyödyllinen monissa eri käyttötapauksissa, kuten:

- **Dynaaminen tiedonhaku:** Agentit voivat kysellä ulkoisia API-rajapintoja tai tietokantoja saadakseen ajankohtaista tietoa (esim. SQLite-tietokannan kyselyt data-analyysia varten, osakekurssien tai säätietojen haku).
- **Koodin suorittaminen ja tulkinta:** Agentit voivat suorittaa koodia tai skriptejä ratkaistakseen matemaattisia ongelmia, luodakseen raportteja tai suorittaakseen simulaatioita.
- **Työnkulkujen automatisointi:** Toistuvien tai monivaiheisten työnkulkujen automatisointi integroimalla työkaluja, kuten tehtäväajastimia, sähköpostipalveluita tai dataputkia.
- **Asiakastuki:** Agentit voivat olla vuorovaikutuksessa CRM-järjestelmien, tikettialustojen tai tietokantojen kanssa ratkaistakseen käyttäjien kysymyksiä.
- **Sisällön luominen ja muokkaus:** Agentit voivat hyödyntää työkaluja, kuten kieliopin tarkistajia, tekstin tiivistäjiä tai sisällön turvallisuusarvioijia, avustaakseen sisällöntuotantotehtävissä.

## Mitkä ovat suunnittelumallin toteuttamiseen tarvittavat elementit/rakennuspalikat?

Nämä rakennuspalikat mahdollistavat tekoälyagentin suorittaa laajan valikoiman tehtäviä. Tarkastellaan keskeisiä elementtejä, joita tarvitaan Työkalujen käyttö -suunnittelumallin toteuttamiseen:

- **Funktio-/työkaluskeemat:** Yksityiskohtaiset määritelmät käytettävissä olevista työkaluista, mukaan lukien funktion nimi, tarkoitus, vaaditut parametrit ja odotetut tulosteet. Näiden skeemojen avulla LLM ymmärtää, mitä työkaluja on saatavilla ja miten rakentaa kelvollisia pyyntöjä.
- **Funktion suorituslogiikka:** Määrittää, miten ja milloin työkaluja kutsutaan käyttäjän tarkoituksen ja keskustelukontekstin perusteella. Tämä voi sisältää suunnittelumoduuleja, reititysmekanismeja tai ehdollisia virtauksia, jotka määrittävät työkalujen käytön dynaamisesti.
- **Viestien käsittelyjärjestelmä:** Komponentit, jotka hallitsevat keskustelun kulkua käyttäjän syötteiden, LLM:n vastausten, työkalukutsujen ja työkalujen tulosteiden välillä.
- **Työkalujen integrointikehys:** Infrastruktuuri, joka yhdistää agentin erilaisiin työkaluihin, olivatpa ne yksinkertaisia funktioita tai monimutkaisia ulkoisia palveluita.
- **Virheenkäsittely ja validointi:** Mekanismit työkalujen suoritusvirheiden käsittelyyn, parametrien validointiin ja odottamattomien vastausten hallintaan.
- **Tilanhallinta:** Seuraa keskustelukontekstia, aiempia työkaluvuorovaikutuksia ja pysyvää dataa varmistaakseen johdonmukaisuuden monivaiheisissa vuorovaikutuksissa.

Seuraavaksi tarkastelemme funktio-/työkalukutsuja tarkemmin.

### Funktio-/työkalukutsut

Funktiokutsut ovat ensisijainen tapa, jolla suuret kielimallit (LLM) voivat olla vuorovaikutuksessa työkalujen kanssa. Usein termejä "Funktio" ja "Työkalu" käytetään keskenään, koska "funktiot" (uudelleenkäytettävän koodin lohkot) ovat agenttien "työkaluja" tehtävien suorittamiseen. Jotta funktion koodi voidaan suorittaa, LLM:n on verrattava käyttäjän pyyntöä funktion kuvaukseen. Tätä varten LLM:lle lähetetään skeema, joka sisältää kaikkien käytettävissä olevien funktioiden kuvaukset. LLM valitsee tehtävään sopivimman funktion ja palauttaa sen nimen ja argumentit. Valittu funktio suoritetaan, sen vastaus lähetetään takaisin LLM:lle, joka käyttää tietoa vastatakseen käyttäjän pyyntöön.

Kehittäjien on toteutettava funktiokutsut seuraavasti:

1. LLM-malli, joka tukee funktiokutsuja
2. Funktioiden kuvaukset sisältävä skeema
3. Jokaisen kuvatun funktion koodi

Käytetään esimerkkinä nykyisen ajan hakemista kaupungissa:

1. **Alusta LLM, joka tukee funktiokutsuja:**

   Kaikki mallit eivät tue funktiokutsuja, joten on tärkeää varmistaa, että käyttämäsi LLM tukee niitä.  
   <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> tukee funktiokutsuja. Voimme aloittaa Azure OpenAI -asiakkaan alustamisella.

   ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Luo funktioskeema:**

   Seuraavaksi määritämme JSON-skeeman, joka sisältää funktion nimen, kuvauksen funktion toiminnasta sekä parametrien nimet ja kuvaukset.  
   Tämän skeeman avulla voimme lähettää käyttäjän pyynnön löytää aika San Franciscossa. On tärkeää huomata, että palautettu tulos on **työkalukutsu**, **ei** lopullinen vastaus kysymykseen. Kuten aiemmin mainittiin, LLM palauttaa tehtävään valitun funktion nimen ja sille välitettävät argumentit.

   ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
   ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

   ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Tehtävän suorittamiseen tarvittava funktiokoodi:**

   Nyt kun LLM on valinnut suoritettavan funktion, tehtävän suorittamiseen tarvittava koodi on toteutettava ja suoritettava.  
   Voimme toteuttaa koodin nykyisen ajan hakemiseksi Pythonilla. Meidän on myös kirjoitettava koodi, joka poimii nimen ja argumentit response_message:sta saadaksemme lopullisen tuloksen.

   ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

   ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

   ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktiokutsut ovat keskeinen osa useimpia, ellei kaikkia, agenttien työkalujen käyttöön liittyviä suunnitelmia, mutta niiden toteuttaminen alusta alkaen voi joskus olla haastavaa.  
Kuten opimme [Oppitunnilla 2](../../../02-explore-agentic-frameworks), agenttikehykset tarjoavat meille valmiita rakennuspalikoita työkalujen käytön toteuttamiseen.

## Työkalujen käyttö esimerkkejä agenttikehysten avulla

Tässä on joitakin esimerkkejä siitä, miten voit toteuttaa Työkalujen käyttö -suunnittelumallin eri agenttikehysten avulla:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> on avoimen lähdekoodin tekoälykehys .NET-, Python- ja Java-kehittäjille, jotka työskentelevät suurten kielimallien (LLM) kanssa. Se yksinkertaistaa funktiokutsujen käyttöä kuvaamalla automaattisesti funktiosi ja niiden parametrit mallille prosessissa, jota kutsutaan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisoinniksi</a>. Lisäksi se hallitsee mallin ja koodisi välistä viestintää. Toinen etu agenttikehyksen, kuten Semantic Kernelin, käytössä on, että se mahdollistaa valmiiden työkalujen, kuten <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> ja <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>, käytön.

Seuraava kaavio havainnollistaa funktiokutsujen prosessia Semantic Kernelin avulla:

![funktiokutsut](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.fi.png)

Semantic Kernelissä funktioita/työkaluja kutsutaan <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugineiksi</a>. Voimme muuntaa aiemmin näkemämme `get_current_time`-funktion pluginiksi muuttamalla sen luokaksi, joka sisältää funktion. Voimme myös tuoda `kernel_function`-koristelijan, joka ottaa funktion kuvauksen. Kun luot ytimen GetCurrentTimePluginin kanssa, ydin serialisoi automaattisesti funktion ja sen parametrit, luoden skeeman lähetettäväksi LLM:lle prosessin aikana.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> on uudempi agenttikehys, joka on suunniteltu auttamaan kehittäjiä rakentamaan, ottamaan käyttöön ja skaalaamaan korkealaatuisia ja laajennettavia tekoälyagentteja turvallisesti ilman, että heidän tarvitsee hallita taustalla olevia laskenta- ja tallennusresursseja. Se on erityisen hyödyllinen yrityssovelluksissa, koska se on täysin hallinnoitu palvelu, jossa on yritystason tietoturva.

Verrattuna suoraan LLM-rajapinnan käyttöön Azure AI Agent Service tarjoaa joitakin etuja, kuten:

- Automaattinen työkalujen kutsuminen – ei tarvetta parsia työkalukutsua, kutsua työkalua ja käsitellä vastausta; kaikki tämä tehdään nyt palvelinpuolella.
- Turvallisesti hallinnoitu data – sen sijaan, että hallitsisit omaa keskustelutilaasi, voit luottaa säikeisiin tallentaaksesi kaiken tarvitsemasi tiedon.
- Valmiit työkalut – Työkalut, joita voit käyttää vuorovaikutuksessa tietolähteidesi kanssa, kuten Bing, Azure AI Search ja Azure Functions.

Azure AI Agent Servicen työkalut voidaan jakaa kahteen kategoriaan:

1. Tietotyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing-hakuun perustuva tiedonhaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Tiedostohaku</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Toimintatyökalut:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktiokutsut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Koodintulkitsija</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI:n määrittelemät työkalut</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service mahdollistaa näiden työkalujen käytön yhdessä `toolset`-kokonaisuutena. Se hyödyntää myös `threads`-ominaisuutta, joka seuraa tietyn keskustelun viestihistoriaa.

Kuvittele, että olet myyntiedustaja yrityksessä nimeltä Contoso. Haluat kehittää keskusteluagentin, joka voi vastata kysymyksiin myyntidatastasi.

Seuraava kuva havainnollistaa, miten voisit käyttää Azure AI Agent Serviceä analysoidaksesi myyntidataa:

![Agent Service toiminnassa](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.fi.jpg)

Näiden työkalujen käyttöön palvelun kanssa voimme luoda asiakkaan ja määritellä työkalun tai työkalukokonaisuuden. Käytännön toteutuksessa voimme käyttää seuraavaa Python-koodia. LLM pystyy tarkastelemaan työkalukokonaisuutta ja päättämään, käytetäänkö käyttäjän luomaa funktiota, `fetch_sales_data_using_sqlite_query`, vai valmista koodintulkitsijaa käyttäjän pyynnön perusteella.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Mitä erityisiä huomioita on otettava huomioon, kun rakennetaan luotettavia tekoälyagentteja käyttäen Työkalujen käyttö -suunnittelumallia?

Yksi yleinen huolenaihe LLM:ien dynaamisesti generoimassa SQL-koodissa on turvallisuus, erityisesti SQL-injektioiden tai haitallisten toimien, kuten tietokannan poistamisen tai manipuloinnin, riski. Vaikka nämä huolenaiheet ovat perusteltuja, ne voidaan tehokkaasti minimoida määrittämällä tietokannan käyttöoikeudet asianmukaisesti. Useimmissa tietokannoissa tämä tarkoittaa tietokannan määrittämistä vain luku -tilaan. Tietokantapalveluissa, kuten PostgreSQL tai Azure SQL, sovellukselle tulisi määrittää vain lukuoikeudet (SELECT).

Sovelluksen suorittaminen turvallisessa ympäristössä parantaa suojaa entisestään. Yritysympäristöissä data yleensä siirretään ja muokataan operatiivisista järjestelmistä vain luku -tietokantaan tai tietovarastoon, jossa on käyttäjäystävällinen skeema. Tämä lähestymistapa varmistaa, että data on turvallista, optimoitua suorituskyvyn ja saavutettavuuden kannalta, ja että sovelluksella on rajoitettu, vain luku -pääsy.

### Onko sinulla lisää kys
Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord), jossa voit tavata muita oppijoita, osallistua toimistotunteihin ja saada vastauksia AI Agents -kysymyksiisi.

## Lisäresurssit

## Edellinen oppitunti

[Ymmärrä agenttisuunnittelumallit](../03-agentic-design-patterns/README.md)

## Seuraava oppitunti

[Agentic RAG](../05-agentic-rag/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.