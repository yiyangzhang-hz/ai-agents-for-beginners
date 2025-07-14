<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:55:59+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ja"
}
-->
. Wikipediaによると、アクターは「並行計算の基本的な構成要素であり、受け取ったメッセージに応じて、ローカルでの意思決定、さらなるアクターの生成、メッセージの送信、次に受け取るメッセージへの応答方法の決定ができる」とされています。

**ユースケース**：コード生成の自動化、データ分析タスク、計画や研究機能のためのカスタムエージェントの構築。

AutoGenの重要なコアコンセプトをいくつか紹介します：

- **エージェント**。エージェントは以下の特徴を持つソフトウェアエンティティです：
  - **メッセージを介して通信**し、これらのメッセージは同期的または非同期的であることがあります。
  - **自身の状態を保持**し、受信したメッセージによって状態が変更されることがあります。
  - **受信したメッセージや状態の変化に応じてアクションを実行**します。これらのアクションはエージェントの状態を変更したり、メッセージログの更新、新しいメッセージの送信、コードの実行、APIコールなどの外部効果を生み出すことがあります。

  以下はチャット機能を持つ独自のエージェントを作成する短いコードスニペットです：

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
    
    上記のコードでは、`MyAssistant`が`RoutedAgent`を継承して作成されています。メッセージハンドラーはメッセージの内容を表示し、その後`AssistantAgent`デリゲートを使って応答を送信します。特に、`self._delegate`にチャット完了を処理できる事前構築済みのエージェントである`AssistantAgent`のインスタンスを割り当てている点に注目してください。

    次に、このエージェントタイプをAutoGenに登録し、プログラムを開始します：

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    上記のコードでは、エージェントがランタイムに登録され、その後エージェントにメッセージが送信され、以下のような出力が得られます：

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **マルチエージェント**。AutoGenは複数のエージェントが協力して複雑なタスクを達成できるようにサポートします。エージェントは通信し、情報を共有し、行動を調整して問題をより効率的に解決します。マルチエージェントシステムを作成するには、データ取得、分析、意思決定、ユーザーインタラクションなど、専門的な機能や役割を持つ異なるタイプのエージェントを定義します。以下はその例です：

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

    上記のコードでは、`GroupChatManager`がランタイムに登録されています。このマネージャーは、ライター、イラストレーター、編集者、ユーザーなど異なるタイプのエージェント間のやり取りを調整する役割を持っています。

- **エージェントランタイム**。フレームワークはエージェント間の通信を可能にし、エージェントの識別子やライフサイクルを管理し、セキュリティとプライバシーの境界を強制するランタイム環境を提供します。これにより、エージェントを安全かつ制御された環境で実行し、効率的かつ安全に相互作用させることができます。注目すべきランタイムは以下の2つです：
  - **スタンドアロンランタイム**。すべてのエージェントが同じプログラミング言語で実装され、同一プロセス内で動作する単一プロセスアプリケーションに適しています。動作イメージは以下の通りです：

アプリケーションスタック

    *エージェントはランタイムを介してメッセージで通信し、ランタイムがエージェントのライフサイクルを管理します*

  - **分散エージェントランタイム**。異なるプログラミング言語で実装され、異なるマシン上で動作するマルチプロセスアプリケーションに適しています。動作イメージは以下の通りです：

## Semantic Kernel + Agent Framework

Semantic Kernelはエンタープライズ対応のAIオーケストレーションSDKです。AIコネクターとメモリコネクター、そしてエージェントフレームワークで構成されています。

まずはコアコンポーネントを紹介します：

- **AIコネクター**：PythonとC#の両方で使用可能な外部AIサービスやデータソースとのインターフェースです。

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

    ここでは、カーネルを作成し、チャット完了サービスを追加する簡単な例を示しています。Semantic Kernelは外部AIサービス、ここではAzure OpenAIのチャット完了サービスへの接続を作成します。

- **プラグイン**：アプリケーションが利用できる関数をカプセル化します。既製のプラグインもあれば、カスタムで作成することも可能です。関連する概念に「プロンプト関数」があります。これは関数呼び出しのために自然言語のキューを提供する代わりに、特定の関数をモデルにブロードキャストします。現在のチャットコンテキストに基づき、モデルはこれらの関数のいずれかを呼び出してリクエストやクエリを完了させることがあります。例を示します：

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

    ここでは、まずテンプレートプロンプト`skPrompt`があり、ユーザーが入力するテキスト`$userInput`のためのスペースを空けています。次にカーネル関数`SummarizeText`を作成し、プラグイン名`SemanticFunctions`でカーネルにインポートしています。関数名はSemantic Kernelが関数の役割と呼び出しタイミングを理解するのに役立ちます。

- **ネイティブ関数**：フレームワークが直接呼び出してタスクを実行するネイティブ関数もあります。以下はファイルから内容を取得する例です：

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

- **メモリ**：AIアプリのコンテキスト管理を抽象化し簡素化します。メモリの考え方は、LLMが知っておくべき情報を保存することです。情報はベクターストアに保存され、これはインメモリデータベースやベクターデータベースなどになります。以下は非常に単純化したシナリオで、*facts*をメモリに追加する例です：

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

    これらのfactsはメモリコレクション`SummarizedAzureDocs`に保存されます。非常に簡単な例ですが、LLMが利用できるように情報をメモリに保存する方法がわかります。
## 前のレッスン

[AIエージェントとエージェントのユースケースの紹介](../01-intro-to-ai-agents/README.md)

## 次のレッスン

[エージェント設計パターンの理解](../03-agentic-design-patterns/README.md)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。