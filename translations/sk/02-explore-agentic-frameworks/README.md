<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:10:59+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sk"
}
-->
. Podľa Wikipédie je herec _základným stavebným prvkom súbežného výpočtu. V reakcii na prijatú správu môže herec: robiť lokálne rozhodnutia, vytvárať ďalších hercov, posielať ďalšie správy a rozhodovať, ako reagovať na ďalšiu prijatú správu_.

**Použitie**: Automatizácia generovania kódu, úlohy analýzy dát a tvorba vlastných agentov pre plánovanie a výskumné funkcie.

Tu sú niektoré dôležité základné koncepty AutoGen:

- **Agenti**. Agent je softvérová entita, ktorá:
  - **Komunikuje prostredníctvom správ**, ktoré môžu byť synchronné alebo asynchrónne.
  - **Udržiava svoj vlastný stav**, ktorý môže byť modifikovaný prichádzajúcimi správami.
  - **Vykonáva akcie** v reakcii na prijaté správy alebo zmeny svojho stavu. Tieto akcie môžu meniť stav agenta a vytvárať vonkajšie efekty, ako napríklad aktualizáciu záznamov správ, posielanie nových správ, vykonávanie kódu alebo volanie API.
    
  Tu máte krátky ukážkový kód, v ktorom vytvoríte vlastného agenta s chatovacími schopnosťami:

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
    
    V predchádzajúcom kóde bol vytvorený `MyAssistant`, ktorý dedí od `RoutedAgent`. Má spracovateľa správ, ktorý vypisuje obsah správy a potom posiela odpoveď pomocou delegáta `AssistantAgent`. Zvlášť si všimnite, ako priraďujeme do `self._delegate` inštanciu `AssistantAgent`, čo je predpripravený agent schopný spracovať chatové dokončenia.

    Teraz necháme AutoGen vedieť o tomto type agenta a spustíme program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    V predchádzajúcom kóde sú agenti zaregistrovaní v runtime a potom je agentovi odoslaná správa, čo vedie k nasledujúcemu výstupu:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Viac agentov**. AutoGen podporuje vytváranie viacerých agentov, ktorí môžu spolupracovať na dosiahnutí zložitých úloh. Agenti môžu komunikovať, zdieľať informácie a koordinovať svoje akcie, aby efektívnejšie riešili problémy. Na vytvorenie multi-agentného systému môžete definovať rôzne typy agentov so špecializovanými funkciami a úlohami, ako je získavanie dát, analýza, rozhodovanie a interakcia s používateľom. Pozrime sa, ako takáto tvorba vyzerá:

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

    V predchádzajúcom kóde máme `GroupChatManager`, ktorý je zaregistrovaný v runtime. Tento manažér je zodpovedný za koordináciu interakcií medzi rôznymi typmi agentov, ako sú spisovatelia, ilustrátori, redaktori a používatelia.

- **Agent Runtime**. Framework poskytuje runtime prostredie, ktoré umožňuje komunikáciu medzi agentmi, spravuje ich identity a životný cyklus a zabezpečuje bezpečnostné a súkromné hranice. To znamená, že môžete spúšťať svojich agentov v bezpečnom a kontrolovanom prostredí, čím sa zabezpečí ich bezpečná a efektívna interakcia. Existujú dva zaujímavé runtime:
  - **Samostatný runtime**. Je vhodný pre aplikácie s jedným procesom, kde všetci agenti sú implementovaní v rovnakom programovacom jazyku a bežia v rovnakom procese. Tu je ilustrácia, ako to funguje:

Aplikačný stack

    *agenti komunikujú prostredníctvom správ cez runtime a runtime spravuje životný cyklus agentov*

  - **Distribuovaný agent runtime** je vhodný pre viacprocesové aplikácie, kde agenti môžu byť implementovaní v rôznych programovacích jazykoch a bežať na rôznych strojoch. Tu je ilustrácia, ako to funguje:

## Semantic Kernel + Agent Framework

Semantic Kernel je podnikový AI Orchestration SDK. Skladá sa z AI a pamäťových konektorov spolu s Agent Frameworkom.

Najprv si prejdime niektoré základné komponenty:

- **AI konektory**: Toto je rozhranie k externým AI službám a dátovým zdrojom, použiteľné v Pythone aj C#.

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

    Tu máte jednoduchý príklad, ako vytvoriť kernel a pridať službu chat completions. Semantic Kernel vytvára spojenie s externou AI službou, v tomto prípade Azure OpenAI Chat Completion.

- **Pluginy**: Tieto zahŕňajú funkcie, ktoré môže aplikácia používať. Existujú hotové pluginy aj vlastné, ktoré si môžete vytvoriť. Súvisiacim konceptom sú "prompt functions". Namiesto poskytovania prirodzených jazykových pokynov na vyvolanie funkcie, vysielate určité funkcie do modelu. Na základe aktuálneho kontextu chatu si model môže vybrať, že zavolá jednu z týchto funkcií na dokončenie požiadavky alebo dotazu. Tu je príklad:

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

    Tu najprv máte šablónu promptu `skPrompt`, ktorá ponecháva miesto pre vstup používateľa `$userInput`. Potom vytvoríte kernel funkciu `SummarizeText` a importujete ju do kernelu s názvom pluginu `SemanticFunctions`. Všimnite si názov funkcie, ktorý pomáha Semantic Kernel pochopiť, čo funkcia robí a kedy by mala byť volaná.

- **Nativna funkcia**: Existujú aj natívne funkcie, ktoré framework môže volať priamo na vykonanie úlohy. Tu je príklad takejto funkcie, ktorá načítava obsah zo súboru:

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

- **Pamäť**: Abstrahuje a zjednodušuje správu kontextu pre AI aplikácie. Myšlienka pamäte je, že ide o informácie, ktoré by mal LLM poznať. Môžete tieto informácie ukladať do vektorového úložiska, ktoré môže byť databázou v pamäti, vektorovou databázou alebo podobne. Tu je príklad veľmi zjednodušeného scenára, kde sa do pamäte pridávajú *fakty*:

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

    Tieto fakty sú potom uložené v pamäťovej kolekcii `SummarizedAzureDocs`. Toto je veľmi zjednodušený príklad, ale vidíte, ako môžete ukladať informácie do pamäte, aby ich LLM mohol použiť.
## Predchádzajúca lekcia

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

## Nasledujúca lekcia

[Pochopenie agentových dizajnových vzorov](../03-agentic-design-patterns/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.