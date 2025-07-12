<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:09:39+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hu"
}
-->
. A Wikipedia szerint az actor _a párhuzamos számítás alapvető építőeleme. Egy üzenetre adott válaszként az actor képes: helyi döntéseket hozni, több actort létrehozni, további üzeneteket küldeni, és meghatározni, hogyan válaszoljon a következő kapott üzenetre_.

**Használati esetek**: Kódgenerálás automatizálása, adatfeldolgozási feladatok, valamint egyedi ügynökök építése tervezési és kutatási funkciókhoz.

Íme néhány fontos alapfogalom az AutoGen-ről:

- **Ügynökök (Agents)**. Egy ügynök egy szoftver entitás, amely:
  - **Üzeneteken keresztül kommunikál**, ezek az üzenetek lehetnek szinkronok vagy aszinkronok.
  - **Fenntartja saját állapotát**, amelyet a bejövő üzenetek módosíthatnak.
  - **Műveleteket hajt végre** a kapott üzenetekre vagy állapotváltozásokra reagálva. Ezek a műveletek módosíthatják az ügynök állapotát és külső hatásokat eredményezhetnek, például üzenetnaplók frissítése, új üzenetek küldése, kód végrehajtása vagy API hívások indítása.
    
  Itt egy rövid kódrészlet, amelyben saját chat-képességekkel rendelkező ügynököt hozol létre:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Az előző kódban a `MyAssistant` létrejött és örökli a `RoutedAgent` osztályt. Van egy üzenetkezelője, amely kiírja az üzenet tartalmát, majd válaszol az `AssistantAgent` delegált segítségével. Különösen figyeld meg, hogy a `self._delegate`-nek az `AssistantAgent` példányát rendeljük, amely egy előre elkészített ügynök, képes chat befejezések kezelésére.

    Most jelezzük az AutoGen-nek ezt az ügynöktípust, és indítsuk el a programot:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Az előző kódban az ügynökök regisztrálva vannak a futtatókörnyezetben, majd egy üzenetet küldünk az ügynöknek, amely a következő kimenetet eredményezi:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Több ügynök (Multi agents)**. Az AutoGen támogatja több ügynök létrehozását, amelyek együttműködve képesek összetett feladatokat megoldani. Az ügynökök kommunikálhatnak, megoszthatják az információkat, és koordinálhatják tevékenységüket a hatékonyabb problémamegoldás érdekében. Több ügynökös rendszer létrehozásához különböző típusú, specializált funkciókkal és szerepekkel rendelkező ügynököket definiálhatsz, például adatlekérés, elemzés, döntéshozatal és felhasználói interakció. Nézzük meg, hogyan néz ki egy ilyen létrehozás:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Az előző kódban egy `GroupChatManager` van regisztrálva a futtatókörnyezetben. Ez a menedzser felelős az ügynökök közötti interakciók koordinálásáért, például írók, illusztrátorok, szerkesztők és felhasználók között.

- **Ügynök futtatókörnyezet (Agent Runtime)**. A keretrendszer biztosít egy futtatókörnyezetet, amely lehetővé teszi az ügynökök közötti kommunikációt, kezeli az identitásukat és életciklusukat, valamint érvényesíti a biztonsági és adatvédelmi határokat. Ez azt jelenti, hogy az ügynökeidet biztonságos és ellenőrzött környezetben futtathatod, biztosítva a biztonságos és hatékony interakciót. Két futtatókörnyezet érdekességként:
  - **Önálló futtatókörnyezet (Stand-alone runtime)**. Ez jó választás egyszálú alkalmazásokhoz, ahol az összes ügynök ugyanabban a programozási nyelvben van megvalósítva és ugyanabban a folyamatban fut. Íme egy ábra arról, hogyan működik:  

Alkalmazás réteg

    *az ügynökök üzeneteken keresztül kommunikálnak a futtatókörnyezeten keresztül, amely kezeli az ügynökök életciklusát*

  - **Elosztott ügynök futtatókörnyezet (Distributed agent runtime)**, amely alkalmas többfolyamatú alkalmazásokhoz, ahol az ügynökök különböző programozási nyelveken valósulhatnak meg és különböző gépeken futnak. Íme egy ábra arról, hogyan működik:  

## Semantic Kernel + Agent Framework

A Semantic Kernel egy vállalati szintű AI Orchestration SDK. Tartalmaz AI és memória csatlakozókat, valamint egy Ügynök Keretrendszert.

Először nézzük meg néhány alapvető összetevőt:

- **AI Csatlakozók (AI Connectors)**: Ez egy interfész külső AI szolgáltatásokhoz és adatforrásokhoz, amely Pythonban és C#-ban is használható.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Itt egy egyszerű példa arra, hogyan hozhatsz létre egy kernelt és adhatsz hozzá egy chat befejező szolgáltatást. A Semantic Kernel kapcsolatot létesít egy külső AI szolgáltatással, jelen esetben az Azure OpenAI Chat Completion-nel.

- **Bővítmények (Plugins)**: Ezek olyan funkciókat foglalnak magukba, amelyeket az alkalmazás használhat. Vannak kész bővítmények és egyedi, saját készítésűek is. Egy kapcsolódó fogalom a "prompt functions". Ahelyett, hogy természetes nyelvű utasításokat adnál a funkcióhíváshoz, bizonyos funkciókat közvetlenül sugárzol a modellnek. A jelenlegi chat kontextus alapján a modell eldöntheti, hogy melyik funkciót hívja meg egy kérés vagy lekérdezés teljesítéséhez. Íme egy példa:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Itt először van egy sablon prompt `skPrompt`, amely helyet hagy a felhasználói szövegbevitelnek, `$userInput`. Ezután létrehozod a kernel funkciót `SummarizeText`, majd importálod a kernelbe a `SemanticFunctions` bővítménynév alatt. Figyeld meg a funkció nevét, amely segíti a Semantic Kernel-t megérteni, mit csinál a funkció és mikor kell meghívni.

- **Natív funkció (Native function)**: Vannak natív funkciók is, amelyeket a keretrendszer közvetlenül hívhat meg a feladat végrehajtásához. Íme egy példa egy fájl tartalmának lekérésére:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Memória (Memory)**: Egyszerűsíti és absztrahálja a kontextuskezelést AI alkalmazások számára. A memória lényege, hogy ez az információ legyen ismert az LLM számára. Ezt az információt egy vektor tárolóban tárolhatod, amely lehet egy memóriában futó adatbázis, vektor adatbázis vagy hasonló. Íme egy példa egy nagyon egyszerűsített esetre, ahol *tényeket* adunk hozzá a memóriához:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    Ezeket a tényeket aztán eltároljuk a `SummarizedAzureDocs` memória gyűjteményben. Ez egy nagyon egyszerű példa, de láthatod, hogyan tárolhatsz információt a memóriában, hogy az LLM felhasználhassa.
## Előző lecke

[Bevezetés az AI ügynökökbe és az ügynökök használati eseteibe](../01-intro-to-ai-agents/README.md)

## Következő lecke

[Az ügynöki tervezési minták megértése](../03-agentic-design-patterns/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.