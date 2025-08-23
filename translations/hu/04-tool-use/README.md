<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d24f735b3c326b2e515f049a0330e54",
  "translation_date": "2025-08-21T13:43:05+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "hu"
}
-->
[![Hogyan tervezzünk jó mesterséges intelligencia ügynököket](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.hu.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

# Eszközhasználati tervezési minta

Az eszközök azért érdekesek, mert lehetővé teszik a mesterséges intelligencia ügynökök számára, hogy szélesebb körű képességekkel rendelkezzenek. Az ügynök korlátozott cselekvési lehetőségei helyett egy eszköz hozzáadásával most már számos különböző műveletet végezhet. Ebben a fejezetben az Eszközhasználati tervezési mintát vizsgáljuk meg, amely leírja, hogyan használhatnak az MI ügynökök specifikus eszközöket céljaik eléréséhez.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Mi az eszközhasználati tervezési minta?
- Milyen felhasználási esetekre alkalmazható?
- Milyen elemek/építőkövek szükségesek a tervezési minta megvalósításához?
- Milyen különleges szempontokat kell figyelembe venni az Eszközhasználati tervezési minta alkalmazásakor a megbízható MI ügynökök építése érdekében?

## Tanulási célok

A lecke elvégzése után képes leszel:

- Meghatározni az Eszközhasználati tervezési mintát és annak célját.
- Azonosítani azokat a felhasználási eseteket, ahol az Eszközhasználati tervezési minta alkalmazható.
- Megérteni a tervezési minta megvalósításához szükséges kulcselemeket.
- Felismerni azokat a szempontokat, amelyek biztosítják a megbízhatóságot az MI ügynökök esetében, amelyek ezt a tervezési mintát használják.

## Mi az Eszközhasználati tervezési minta?

Az **Eszközhasználati tervezési minta** arra összpontosít, hogy lehetővé tegye a nagy nyelvi modellek (LLM-ek) számára, hogy külső eszközökkel lépjenek interakcióba konkrét célok elérése érdekében. Az eszközök olyan kódok, amelyeket egy ügynök végrehajthat műveletek elvégzésére. Egy eszköz lehet egy egyszerű funkció, például egy számológép, vagy egy harmadik fél szolgáltatásának API-hívása, például részvényárfolyam-lekérdezés vagy időjárás-előrejelzés. Az MI ügynökök kontextusában az eszközöket úgy tervezték, hogy az ügynökök végrehajtsák őket **modell által generált funkcióhívások** alapján.

## Milyen felhasználási esetekre alkalmazható?

Az MI ügynökök eszközöket használhatnak összetett feladatok elvégzésére, információk lekérésére vagy döntések meghozatalára. Az eszközhasználati tervezési mintát gyakran alkalmazzák olyan helyzetekben, amelyek dinamikus interakciót igényelnek külső rendszerekkel, például adatbázisokkal, webszolgáltatásokkal vagy kódértelmezőkkel. Ez a képesség számos különböző felhasználási esetben hasznos, például:

- **Dinamikus információlekérés:** Az ügynökök külső API-kat vagy adatbázisokat kérdezhetnek le friss adatok megszerzéséhez (pl. SQLite adatbázis lekérdezése adatelemzéshez, részvényárfolyamok vagy időjárási információk lekérése).
- **Kódvégrehajtás és értelmezés:** Az ügynökök kódot vagy szkripteket futtathatnak matematikai problémák megoldására, jelentések generálására vagy szimulációk végrehajtására.
- **Munkafolyamat-automatizálás:** Ismétlődő vagy több lépésből álló munkafolyamatok automatizálása olyan eszközök integrálásával, mint feladatütemezők, e-mail szolgáltatások vagy adatfolyamok.
- **Ügyfélszolgálat:** Az ügynökök CRM rendszerekkel, jegykezelő platformokkal vagy tudásbázisokkal léphetnek interakcióba a felhasználói kérdések megoldása érdekében.
- **Tartalomgenerálás és -szerkesztés:** Az ügynökök olyan eszközöket használhatnak, mint nyelvtani ellenőrzők, szövegösszegzők vagy tartalombiztonsági értékelők, hogy segítsenek a tartalomkészítési feladatokban.

## Milyen elemek/építőkövek szükségesek az eszközhasználati tervezési minta megvalósításához?

Ezek az építőkövek lehetővé teszik az MI ügynök számára, hogy széles körű feladatokat végezzen el. Nézzük meg az Eszközhasználati tervezési minta megvalósításához szükséges kulcselemeket:

- **Funkció-/Eszközsémák:** Az elérhető eszközök részletes leírásai, beleértve a funkció nevét, célját, szükséges paramétereit és várt kimeneteit. Ezek a sémák lehetővé teszik az LLM számára, hogy megértse, milyen eszközök állnak rendelkezésre, és hogyan kell érvényes kéréseket összeállítani.
- **Funkcióvégrehajtási logika:** Szabályozza, hogy az eszközöket hogyan és mikor hívják meg a felhasználói szándék és a beszélgetési kontextus alapján. Ez magában foglalhatja a tervező modulokat, útválasztási mechanizmusokat vagy feltételes folyamatokat, amelyek dinamikusan határozzák meg az eszközhasználatot.
- **Üzenetkezelő rendszer:** Azok az összetevők, amelyek kezelik a beszélgetési folyamatot a felhasználói bemenetek, az LLM válaszai, az eszközhívások és az eszközkimenetek között.
- **Eszközintegrációs keretrendszer:** Infrastruktúra, amely összeköti az ügynököt különböző eszközökkel, legyenek azok egyszerű funkciók vagy összetett külső szolgáltatások.
- **Hibakezelés és érvényesítés:** Mechanizmusok az eszközvégrehajtás hibáinak kezelésére, a paraméterek érvényesítésére és a váratlan válaszok kezelésére.
- **Állapotkezelés:** Nyomon követi a beszélgetési kontextust, a korábbi eszközinterakciókat és a tartós adatokat, hogy biztosítsa a következetességet a többfordulós interakciók során.

Ezután részletesebben megvizsgáljuk a Funkció-/Eszközhívást.

### Funkció-/Eszközhívás

A funkcióhívás az elsődleges módja annak, hogy lehetővé tegyük a Nagy Nyelvi Modellek (LLM-ek) számára az eszközökkel való interakciót. Gyakran látni fogod, hogy a „Funkció” és az „Eszköz” kifejezéseket felcserélhetően használják, mert a „funkciók” (újrahasznosítható kódrészek) azok az „eszközök”, amelyeket az ügynökök a feladatok elvégzésére használnak. Ahhoz, hogy egy funkció kódja meghívható legyen, az LLM-nek össze kell hasonlítania a felhasználói kérést a funkció leírásával. Ehhez egy séma, amely tartalmazza az összes elérhető funkció leírását, elküldésre kerül az LLM-nek. Az LLM ezután kiválasztja a feladathoz legmegfelelőbb funkciót, és visszaadja annak nevét és argumentumait. A kiválasztott funkciót meghívják, a válaszát visszaküldik az LLM-nek, amely az információt felhasználja a felhasználói kérés megválaszolására.

A funkcióhívás megvalósításához a fejlesztőknek szükségük lesz:

1. Egy LLM modellre, amely támogatja a funkcióhívást
2. Egy sémára, amely tartalmazza a funkcióleírásokat
3. A leírt funkciók kódjára

Vegyük példaként egy város aktuális idejének lekérését:

1. **Egy funkcióhívást támogató LLM inicializálása:**

    Nem minden modell támogatja a funkcióhívást, ezért fontos ellenőrizni, hogy az általad használt LLM támogatja-e. Az <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> támogatja a funkcióhívást. Kezdhetjük az Azure OpenAI kliens inicializálásával.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Funkcióséma létrehozása:**

    Ezután definiálunk egy JSON sémát, amely tartalmazza a funkció nevét, a funkció céljának leírását, valamint a funkció paramétereinek nevét és leírását. Ezt a sémát továbbítjuk az előzőleg létrehozott kliensnek, a felhasználói kérés mellett, hogy megtaláljuk az időt San Franciscóban. Fontos megjegyezni, hogy egy **eszközhívás** az, ami visszatér, **nem** a kérdés végső válasza. Mint korábban említettük, az LLM visszaadja a feladathoz kiválasztott funkció nevét és az átadandó argumentumokat.

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
  
1. **A feladat elvégzéséhez szükséges funkciókód:**

    Most, hogy az LLM kiválasztotta, melyik funkciót kell futtatni, a feladat elvégzéséhez szükséges kódot kell megvalósítani és végrehajtani. A jelenlegi idő lekéréséhez Pythonban implementálhatjuk a kódot. Írnunk kell kódot is, amely kinyeri a választ az üzenetből, hogy megkapjuk a végső eredményt.

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

A funkcióhívás a legtöbb, ha nem az összes ügynöki eszközhasználati tervezés középpontjában áll, azonban a nulláról történő megvalósítása néha kihívást jelenthet. Ahogy azt a [2. leckében](../../../02-explore-agentic-frameworks) tanultuk, az ügynöki keretrendszerek előre elkészített építőköveket biztosítanak az eszközhasználat megvalósításához.

## Eszközhasználati példák ügynöki keretrendszerekkel

Íme néhány példa arra, hogyan valósíthatod meg az Eszközhasználati tervezési mintát különböző ügynöki keretrendszerek használatával:

### Semantic Kernel

A <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> egy nyílt forráskódú MI keretrendszer .NET, Python és Java fejlesztők számára, akik Nagy Nyelvi Modellekkel (LLM-ekkel) dolgoznak. Egyszerűsíti a funkcióhívások használatának folyamatát azáltal, hogy automatikusan leírja a funkcióidat és azok paramétereit a modell számára egy <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">szerializálás</a> nevű folyamaton keresztül. Kezeli továbbá a modell és a kód közötti kommunikációt. Az ügynöki keretrendszer, például a Semantic Kernel használatának másik előnye, hogy hozzáférést biztosít előre elkészített eszközökhöz, mint például a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> és a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

A következő diagram bemutatja a funkcióhívás folyamatát a Semantic Kernel segítségével:

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.hu.png)

A Semantic Kernelben a funkciókat/eszközöket <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugineknek</a> nevezik. Az előző példában látott `get_current_time` funkciót pluginné alakíthatjuk, ha osztállyá alakítjuk, amely tartalmazza a funkciót. Importálhatjuk a `kernel_function` dekorátort is, amely a funkció leírását veszi át. Amikor létrehozol egy kernelt a GetCurrentTimePlugin-nel, a kernel automatikusan szerializálja a funkciót és annak paramétereit, létrehozva a sémát, amelyet az LLM-nek küld.

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

Az <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> egy újabb ügynöki keretrendszer, amelyet arra terveztek, hogy lehetővé tegye a fejlesztők számára, hogy biztonságosan építsenek, telepítsenek és méretezzenek magas minőségű és bővíthető MI ügynököket anélkül, hogy az alapul szolgáló számítási és tárolási erőforrásokat kellene kezelniük. Különösen hasznos vállalati alkalmazásokhoz, mivel teljesen menedzselt szolgáltatás vállalati szintű biztonsággal.

Az LLM API-val való közvetlen fejlesztéshez képest az Azure AI Agent Service néhány előnyt kínál, többek között:

- Automatikus eszközhívás – nincs szükség az eszközhívás elemzésére, az eszköz meghívására és a válasz kezelésére; mindez most szerveroldalon történik
- Biztonságosan kezelt adatok – ahelyett, hogy saját beszélgetési állapotot kezelnél, a szálakra támaszkodhatsz, hogy tárolják az összes szükséges információt
- Előre elkészített eszközök – Eszközök, amelyeket az adataid forrásaival való interakcióhoz használhatsz, például Bing, Azure AI Search és Azure Functions.

Az Agent Service-ben elérhető eszközök két kategóriába sorolhatók:

1. Tudáseszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing kereséssel történő alapozás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fájlkeresés</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Akcióeszközök:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funkcióhívás</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kódértelmező</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI által definiált eszközök</a>
    - <a href="https://learn.microsoft.com/azure/ai-services
<a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">
Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Többügynökös Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Funkcióhívás Oktatóanyag</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Kódértelmező</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Eszközök</a>

## Előző Lecke

[Az Ügynöki Tervezési Minták Megértése](../03-agentic-design-patterns/README.md)

## Következő Lecke

[Ügynöki RAG](../05-agentic-rag/README.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.