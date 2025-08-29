<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-29T20:24:50+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "cs"
}
-->
[![Jak navrhnout dobré AI agenty](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.cs.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Vzor návrhu použití nástrojů

Nástroje jsou zajímavé, protože umožňují AI agentům mít širší škálu schopností. Místo toho, aby agent měl omezenou sadu akcí, které může provádět, přidáním nástroje může nyní vykonávat širokou škálu úkolů. V této kapitole se podíváme na vzor návrhu použití nástrojů, který popisuje, jak mohou AI agenti používat specifické nástroje k dosažení svých cílů.

## Úvod

V této lekci se snažíme odpovědět na následující otázky:

- Co je vzor návrhu použití nástrojů?
- Na jaké případy použití jej lze aplikovat?
- Jaké prvky/stavební bloky jsou potřebné k implementaci tohoto vzoru návrhu?
- Jaké jsou zvláštní úvahy při použití vzoru návrhu použití nástrojů k vytvoření důvěryhodných AI agentů?

## Cíle učení

Po dokončení této lekce budete schopni:

- Definovat vzor návrhu použití nástrojů a jeho účel.
- Identifikovat případy použití, kde je tento vzor návrhu použitelný.
- Pochopit klíčové prvky potřebné k implementaci tohoto vzoru návrhu.
- Rozpoznat úvahy pro zajištění důvěryhodnosti AI agentů využívajících tento vzor návrhu.

## Co je vzor návrhu použití nástrojů?

**Vzor návrhu použití nástrojů** se zaměřuje na to, jak dát LLM schopnost interagovat s externími nástroji k dosažení specifických cílů. Nástroje jsou kód, který může agent vykonat k provedení akcí. Nástroj může být jednoduchá funkce, jako je kalkulačka, nebo API volání na službu třetí strany, například pro vyhledání cen akcií nebo předpovědi počasí. V kontextu AI agentů jsou nástroje navrženy tak, aby je agenti mohli vykonávat v reakci na **modelově generované volání funkcí**.

## Na jaké případy použití jej lze aplikovat?

AI agenti mohou využívat nástroje k dokončení složitých úkolů, získávání informací nebo rozhodování. Vzor návrhu použití nástrojů se často používá ve scénářích vyžadujících dynamickou interakci s externími systémy, jako jsou databáze, webové služby nebo interprety kódu. Tato schopnost je užitečná pro řadu různých případů použití, včetně:

- **Dynamické získávání informací:** Agenti mohou dotazovat externí API nebo databáze pro získání aktuálních dat (např. dotazování SQLite databáze pro analýzu dat, získávání cen akcií nebo informací o počasí).
- **Spouštění a interpretace kódu:** Agenti mohou spouštět kód nebo skripty k řešení matematických problémů, generování reportů nebo provádění simulací.
- **Automatizace pracovních postupů:** Automatizace opakujících se nebo vícekrokových pracovních postupů integrací nástrojů, jako jsou plánovače úkolů, e-mailové služby nebo datové pipeline.
- **Zákaznická podpora:** Agenti mohou interagovat s CRM systémy, platformami pro správu tiketů nebo znalostními databázemi k řešení dotazů uživatelů.
- **Generování a úprava obsahu:** Agenti mohou využívat nástroje, jako jsou kontrolory gramatiky, sumarizátory textu nebo hodnotitelé bezpečnosti obsahu, k asistenci při tvorbě obsahu.

## Jaké prvky/stavební bloky jsou potřebné k implementaci vzoru návrhu použití nástrojů?

Tyto stavební bloky umožňují AI agentovi vykonávat širokou škálu úkolů. Podívejme se na klíčové prvky potřebné k implementaci vzoru návrhu použití nástrojů:

- **Schémata funkcí/nástrojů:** Podrobné definice dostupných nástrojů, včetně názvu funkce, účelu, požadovaných parametrů a očekávaných výstupů. Tato schémata umožňují LLM pochopit, jaké nástroje jsou k dispozici a jak vytvořit platné požadavky.
- **Logika vykonávání funkcí:** Řídí, jak a kdy jsou nástroje vyvolávány na základě záměru uživatele a kontextu konverzace. To může zahrnovat plánovací moduly, směrovací mechanismy nebo podmíněné toky, které dynamicky určují použití nástrojů.
- **Systém zpracování zpráv:** Komponenty, které spravují tok konverzace mezi vstupy uživatele, odpověďmi LLM, voláními nástrojů a výstupy nástrojů.
- **Rámec pro integraci nástrojů:** Infrastruktura, která propojuje agenta s různými nástroji, ať už jsou to jednoduché funkce nebo složité externí služby.
- **Zpracování chyb a validace:** Mechanismy pro řešení selhání při vykonávání nástrojů, validaci parametrů a správu neočekávaných odpovědí.
- **Správa stavu:** Sleduje kontext konverzace, předchozí interakce s nástroji a perzistentní data, aby byla zajištěna konzistence při vícekrokových interakcích.

Dále se podíváme na volání funkcí/nástrojů podrobněji.

### Volání funkcí/nástrojů

Volání funkcí je primární způsob, jak umožnit velkým jazykovým modelům (LLMs) interagovat s nástroji. Často se setkáte s tím, že se termíny "funkce" a "nástroje" používají zaměnitelně, protože "funkce" (bloky znovupoužitelného kódu) jsou "nástroje", které agenti používají k provádění úkolů. Aby mohl být kód funkce vyvolán, musí LLM porovnat požadavek uživatele s popisem funkce. K tomu je LLM odesláno schéma obsahující popisy všech dostupných funkcí. LLM poté vybere nejvhodnější funkci pro daný úkol a vrátí její název a argumenty. Vybraná funkce je vyvolána, její odpověď je odeslána zpět LLM, které použije informace k odpovědi na požadavek uživatele.

Pro implementaci volání funkcí pro agenty budou vývojáři potřebovat:

1. LLM model, který podporuje volání funkcí
2. Schéma obsahující popisy funkcí
3. Kód pro každou popsanou funkci

Pojďme si to ilustrovat na příkladu získání aktuálního času ve městě:

1. **Inicializace LLM, které podporuje volání funkcí:**

    Ne všechny modely podporují volání funkcí, proto je důležité ověřit, že LLM, které používáte, tuto funkci má. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> podporuje volání funkcí. Můžeme začít inicializací klienta Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Vytvoření schématu funkce:**

    Dále definujeme JSON schéma, které obsahuje název funkce, popis toho, co funkce dělá, a názvy a popisy parametrů funkce. Toto schéma poté předáme klientovi vytvořenému dříve spolu s požadavkem uživatele na zjištění času v San Franciscu. Důležité je si uvědomit, že je vráceno **volání nástroje**, **ne** konečná odpověď na otázku. Jak bylo zmíněno dříve, LLM vrací název funkce, kterou vybralo pro úkol, a argumenty, které budou předány.

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
  
1. **Kód funkce potřebný k provedení úkolu:**

    Nyní, když LLM vybralo, která funkce má být spuštěna, je třeba implementovat a vykonat kód, který úkol provede. Můžeme implementovat kód pro získání aktuálního času v Pythonu. Také musíme napsat kód pro extrakci názvu a argumentů z `response_message`, abychom získali konečný výsledek.

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

Volání funkcí je jádrem většiny, ne-li všech návrhů použití nástrojů agentů, avšak jeho implementace od nuly může být někdy náročná. Jak jsme se naučili v [Lekci 2](../../../02-explore-agentic-frameworks), agentické rámce nám poskytují předpřipravené stavební bloky pro implementaci použití nástrojů.

## Příklady použití nástrojů s agentickými rámci

Zde jsou některé příklady, jak můžete implementovat vzor návrhu použití nástrojů pomocí různých agentických rámců:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> je open-source AI rámec pro vývojáře v .NET, Pythonu a Javě, kteří pracují s velkými jazykovými modely (LLMs). Zjednodušuje proces použití volání funkcí tím, že automaticky popisuje vaše funkce a jejich parametry modelu prostřednictvím procesu nazývaného <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializace</a>. Také spravuje komunikaci mezi modelem a vaším kódem. Další výhodou použití agentického rámce, jako je Semantic Kernel, je to, že vám umožňuje přístup k předpřipraveným nástrojům, jako je <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> a <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Následující diagram ilustruje proces volání funkcí pomocí Semantic Kernel:

![volání funkcí](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.cs.png)

V Semantic Kernel se funkce/nástroje nazývají <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Pluginy</a>. Můžeme převést funkci `get_current_time`, kterou jsme viděli dříve, na plugin tím, že ji přeměníme na třídu s touto funkcí uvnitř. Můžeme také importovat dekorátor `kernel_function`, který přijímá popis funkce. Když poté vytvoříte kernel s pluginem GetCurrentTimePlugin, kernel automaticky serializuje funkci a její parametry, čímž vytvoří schéma k odeslání LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> je novější agentický rámec navržený tak, aby umožnil vývojářům bezpečně vytvářet, nasazovat a škálovat vysoce kvalitní a rozšiřitelné AI agenty bez nutnosti spravovat podkladové výpočetní a úložné zdroje. Je obzvláště užitečný pro podnikové aplikace, protože se jedná o plně spravovanou službu s podnikovou úrovní zabezpečení.

Ve srovnání s vývojem přímo s LLM API poskytuje Azure AI Agent Service některé výhody, včetně:

- Automatické volání nástrojů – není třeba analyzovat volání nástroje, vyvolávat nástroj a zpracovávat odpověď; vše je nyní prováděno na straně serveru.
- Bezpečně spravovaná data – místo správy vlastního stavu konverzace se můžete spolehnout na vlákna, která uchovávají všechny potřebné informace.
- Předpřipravené nástroje – Nástroje, které můžete použít k interakci s vašimi datovými zdroji, jako jsou Bing, Azure AI Search a Azure Functions.

Nástroje dostupné v Azure AI Agent Service lze rozdělit do dvou kategorií:

1. Nástroje pro znalosti:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding s Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Nástroje pro akce:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Volání funkcí</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Nástroje definované OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service nám umožňuje používat tyto nástroje společně jako `toolset`. Také využívá `threads`, které sledují historii zpráv z konkrétní konverzace.

Představte si, že jste obchodní zástupce ve společnosti Contoso. Chcete vyvinout konverzačního agenta, který dokáže odpovídat na otázky týkající se vašich obchodních dat.

Následující obrázek ilustruje, jak byste mohli použít Azure AI Agent Service k analýze vašich obchodních dat:

![Agentic Service v akci](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.cs.jpg)

Pro použití některého z těchto nástrojů se službou můžeme vytvořit klienta a definovat nástroj nebo sadu nástrojů. Pro praktickou implementaci můžeme použít následující Python kód. LLM bude schopno podívat se na sadu nástrojů a rozhodnout, zda použít uživatelem vytvořenou funkci `fetch_sales_data_using_sqlite_query`, nebo předpřipravený Code Interpreter v závislosti na požadavku uživatele.

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

## Jaké jsou zvláštní úvahy při použití vzoru návrhu použití nástrojů k vytvoření důvěryhodných AI agentů?

Běžnou obavou u SQL dynamicky generovaného LLM je bezpečnost, zejména riziko SQL injekce nebo škodlivých akcí, jako je odstranění nebo manipulace s databází. I když jsou tyto obavy oprávněné, lze je efektivně zmírnit správnou konfigurací oprávnění k přístupu do databáze. U většiny databází to zahrnuje konfiguraci databáze jako pouze pro čtení. U databázových služeb, jako je PostgreSQL nebo Azure SQL, by aplikaci měla být přiřazena role pouze pro čtení (SELECT).

Provozování aplikace v zabezpečeném prostředí dále zvyšuje ochranu. V podnikových scénářích jsou data obvykle extrahována a transformována z operačních systémů do databáze pouze pro čtení nebo datového skladu s uživatelsky přívětivým schématem. Tento přístup zajišťuje, že data jsou bezpečná, optimalizovaná pro výkon a přístupnost, a že aplikace má omezený přístup pouze pro čtení.

### Máte další otázky ohledně vzoru návrhu použití nástrojů?
Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na své otázky týkající se AI agentů.

## Další zdroje

## Předchozí lekce

[Porozumění agentickým návrhovým vzorům](../03-agentic-design-patterns/README.md)

## Další lekce

[Agentický RAG](../05-agentic-rag/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.