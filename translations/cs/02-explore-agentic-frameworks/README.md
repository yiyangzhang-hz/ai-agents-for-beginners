<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:10:13+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "cs"
}
-->
. Podle Wikipedie je herec _základní stavební kámen souběžného výpočtu. V reakci na přijatou zprávu může herec: činit lokální rozhodnutí, vytvářet další herce, posílat další zprávy a určovat, jak reagovat na další přijatou zprávu_.

**Případy použití**: Automatizace generování kódu, úkoly analýzy dat a vytváření vlastních agentů pro plánování a výzkumné funkce.

Zde jsou některé důležité základní koncepty AutoGen:

- **Agenti**. Agent je softwarová entita, která:
  - **Komunikuje prostřednictvím zpráv**, tyto zprávy mohou být synchronní nebo asynchronní.
  - **Udržuje svůj vlastní stav**, který může být měněn příchozími zprávami.
  - **Provádí akce** v reakci na přijaté zprávy nebo změny svého stavu. Tyto akce mohou měnit stav agenta a vytvářet vnější efekty, jako je aktualizace záznamů zpráv, odesílání nových zpráv, spouštění kódu nebo volání API.
    
  Zde máte krátký ukázkový kód, ve kterém vytvoříte vlastního agenta s chatovacími schopnostmi:

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
    
    V předchozím kódu byl vytvořen `MyAssistant`, který dědí z `RoutedAgent`. Má zpracovatele zpráv, který vypisuje obsah zprávy a poté odesílá odpověď pomocí delegáta `AssistantAgent`. Zvláště si všimněte, jak přiřazujeme `self._delegate` instanci `AssistantAgent`, což je předpřipravený agent, který umí zpracovávat chatové dokončení.


    Nyní informujeme AutoGen o tomto typu agenta a spustíme program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    V předchozím kódu jsou agenti zaregistrováni v runtime a poté je agentovi odeslána zpráva, což má za následek následující výstup:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Více agentů**. AutoGen podporuje vytváření více agentů, kteří mohou spolupracovat na dosažení složitých úkolů. Agenti mohou komunikovat, sdílet informace a koordinovat své akce, aby efektivněji řešili problémy. Pro vytvoření multiagentního systému můžete definovat různé typy agentů se specializovanými funkcemi a rolemi, jako je získávání dat, analýza, rozhodování a interakce s uživatelem. Podívejme se, jak taková tvorba vypadá, abychom si to představili:

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

    V předchozím kódu máme `GroupChatManager`, který je zaregistrován v runtime. Tento manažer je zodpovědný za koordinaci interakcí mezi různými typy agentů, jako jsou spisovatelé, ilustrátoři, editoři a uživatelé.

- **Agent Runtime**. Framework poskytuje runtime prostředí, které umožňuje komunikaci mezi agenty, spravuje jejich identity a životní cykly a zajišťuje bezpečnostní a soukromé hranice. To znamená, že můžete své agenty spouštět v bezpečném a kontrolovaném prostředí, což zajišťuje, že mohou bezpečně a efektivně komunikovat. Existují dva zajímavé runtime:
  - **Samostatný runtime**. Je vhodný pro aplikace s jedním procesem, kde jsou všichni agenti implementováni ve stejném programovacím jazyce a běží ve stejném procesu. Zde je ilustrace, jak to funguje:

Aplikační zásobník

    *agenti komunikují prostřednictvím zpráv přes runtime a runtime spravuje životní cyklus agentů*

  - **Distribuovaný agent runtime** je vhodný pro aplikace s více procesy, kde agenti mohou být implementováni v různých programovacích jazycích a běží na různých strojích. Zde je ilustrace, jak to funguje:

## Semantic Kernel + Agent Framework

Semantic Kernel je podnikový AI Orchestration SDK. Skládá se z AI a paměťových konektorů spolu s Agent Frameworkem.

Nejprve si představme některé základní komponenty:

- **AI konektory**: Jedná se o rozhraní k externím AI službám a datovým zdrojům pro použití v Pythonu i C#.

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

    Zde máte jednoduchý příklad, jak vytvořit kernel a přidat službu chatového dokončení. Semantic Kernel vytváří spojení s externí AI službou, v tomto případě Azure OpenAI Chat Completion.

- **Pluginy**: Tyto zapouzdřují funkce, které může aplikace využívat. Existují hotové pluginy i vlastní, které si můžete vytvořit. Souvisejícím konceptem jsou „prompt funkce“. Místo poskytování přirozených jazykových pokynů pro volání funkcí vysíláte určité funkce do modelu. Na základě aktuálního kontextu chatu si model může vybrat, že jednu z těchto funkcí zavolá k dokončení požadavku nebo dotazu. Zde je příklad:

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

    Zde máte nejprve šablonu promptu `skPrompt`, která ponechává prostor pro uživatelský vstup `$userInput`. Poté vytvoříte kernel funkci `SummarizeText` a importujete ji do kernelu pod názvem pluginu `SemanticFunctions`. Všimněte si názvu funkce, který pomáhá Semantic Kernel pochopit, co funkce dělá a kdy by měla být volána.

- **Nativní funkce**: Existují také nativní funkce, které framework může volat přímo k vykonání úkolu. Zde je příklad takové funkce, která načítá obsah ze souboru:

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

- **Paměť**: Abstrakce a zjednodušení správy kontextu pro AI aplikace. Myšlenka paměti je, že je to něco, co by měl LLM znát. Informace můžete uložit do vektorového úložiště, které funguje jako databáze v paměti, vektorová databáze nebo podobně. Zde je příklad velmi zjednodušeného scénáře, kde jsou do paměti přidávány *fakta*:

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

    Tato fakta jsou pak uložena v paměťové kolekci `SummarizedAzureDocs`. Je to velmi zjednodušený příklad, ale můžete vidět, jak lze informace uložit do paměti, aby je LLM mohl využívat.
## Předchozí lekce

[Úvod do AI agentů a jejich použití](../01-intro-to-ai-agents/README.md)

## Následující lekce

[Pochopení agentních návrhových vzorů](../03-agentic-design-patterns/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.