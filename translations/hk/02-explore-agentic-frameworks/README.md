<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:55:02+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hk"
}
-->
。根據維基百科，actor 是「並行計算的基本構建塊。當收到訊息時，actor 可以：做出本地決策、創建更多 actors、發送更多訊息，並決定如何回應下一個收到的訊息」。

**使用案例**：自動化代碼生成、數據分析任務，以及為規劃和研究功能構建自訂代理。

以下是 AutoGen 的一些重要核心概念：

- **Agents（代理）**。代理是一種軟件實體，具有以下特性：
  - **通過訊息進行通訊**，這些訊息可以是同步或非同步的。
  - **維護自己的狀態**，該狀態可被傳入的訊息修改。
  - **根據收到的訊息或狀態變化執行動作**。這些動作可能會修改代理的狀態並產生外部效果，例如更新訊息日誌、發送新訊息、執行代碼或調用 API。
    
  這裡有一段簡短的程式碼片段，展示如何創建具有聊天功能的自訂代理：

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
    
    在上述程式碼中，`MyAssistant` 被創建並繼承自 `RoutedAgent`。它有一個訊息處理器，會列印訊息內容，然後使用 `AssistantAgent` 委派發送回應。特別注意我們如何將 `self._delegate` 指派為 `AssistantAgent` 的實例，這是一個可處理聊天完成的預建代理。

    接著讓 AutoGen 知道這個代理類型並啟動程式：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    在上述程式碼中，代理被註冊到執行時，然後向代理發送訊息，結果輸出如下：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **多代理（Multi agents）**。AutoGen 支援創建多個代理協同工作以完成複雜任務。代理可以通訊、共享資訊並協調行動以更有效地解決問題。要建立多代理系統，可以定義具有專門功能和角色的不同類型代理，例如資料檢索、分析、決策和用戶互動。以下展示這樣的創建範例：

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

    在上述程式碼中，我們有一個 `GroupChatManager`，它被註冊到執行時。此管理器負責協調不同類型代理之間的互動，如作家、插畫師、編輯和用戶。

- **代理執行時（Agent Runtime）**。框架提供執行時環境，促進代理間通訊，管理其身份和生命週期，並強制執行安全與隱私邊界。這意味著你可以在安全且受控的環境中運行代理，確保它們能安全且高效地互動。有兩種執行時值得關注：
  - **獨立執行時（Stand-alone runtime）**。適合單進程應用，所有代理使用相同程式語言並在同一進程中運行。以下是其運作示意：

應用堆疊

    *代理透過執行時以訊息通訊，執行時管理代理的生命週期*

  - **分散式代理執行時（Distributed agent runtime）**，適合多進程應用，代理可能使用不同程式語言並運行於不同機器。以下是其運作示意：

## Semantic Kernel + Agent Framework

Semantic Kernel 是一個企業級 AI 編排 SDK。它包含 AI 和記憶體連接器，以及一個代理框架。

先介紹一些核心組件：

- **AI Connectors（AI 連接器）**：這是與外部 AI 服務和資料來源的介面，支援 Python 和 C#。

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

    這裡有一個簡單範例，展示如何建立 kernel 並新增聊天完成服務。Semantic Kernel 會建立與外部 AI 服務的連接，此例中為 Azure OpenAI 聊天完成。

- **Plugins（插件）**：封裝應用可使用的函式。既有現成插件，也可自訂。相關概念是「prompt functions（提示函式）」。不再用自然語言提示呼叫函式，而是向模型廣播某些函式。根據當前聊天上下文，模型可能選擇呼叫其中一個函式以完成請求或查詢。範例如下：

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

    這裡先有一個模板提示 `skPrompt`，留空讓用戶輸入文字 `$userInput`。接著建立 kernel 函式 `SummarizeText`，並以插件名稱 `SemanticFunctions` 匯入 kernel。注意函式名稱有助 Semantic Kernel 理解該函式的功能及何時呼叫。

- **Native function（原生函式）**：框架也能直接呼叫原生函式來執行任務。以下範例示範從檔案讀取內容的函式：

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

- **Memory（記憶體）**：抽象並簡化 AI 應用的上下文管理。記憶體的概念是讓 LLM 知道某些資訊。你可以將這些資訊存入向量庫，這通常是記憶體資料庫、向量資料庫或類似系統。以下是一個非常簡化的範例，將「事實」加入記憶體：

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

    這些事實隨後被存入記憶體集合 `SummarizedAzureDocs`。這是個非常簡化的例子，但你可以看到如何將資訊存入記憶體供 LLM 使用。
## 上一課

[AI 代理及代理使用案例介紹](../01-intro-to-ai-agents/README.md)

## 下一課

[理解代理設計模式](../03-agentic-design-patterns/README.md)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。