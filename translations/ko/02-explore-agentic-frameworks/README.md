<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:56:30+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ko"
}
-->
. 위키피디아에 따르면, 액터(actor)는 _동시 계산의 기본 구성 요소입니다. 액터는 받은 메시지에 대해 다음과 같은 작업을 수행할 수 있습니다: 로컬 결정 내리기, 더 많은 액터 생성, 더 많은 메시지 전송, 그리고 다음에 받을 메시지에 어떻게 응답할지 결정하기_입니다.

**사용 사례**: 코드 생성 자동화, 데이터 분석 작업, 계획 및 연구 기능을 위한 맞춤형 에이전트 구축.

AutoGen의 중요한 핵심 개념은 다음과 같습니다:

- **에이전트(Agents)**. 에이전트는 다음과 같은 소프트웨어 엔티티입니다:
  - **메시지를 통해 통신**하며, 이 메시지는 동기식 또는 비동기식일 수 있습니다.
  - **자신만의 상태를 유지**하며, 이 상태는 들어오는 메시지에 의해 변경될 수 있습니다.
  - **받은 메시지나 상태 변화에 반응하여 동작 수행**. 이 동작은 에이전트의 상태를 변경하거나 메시지 로그 업데이트, 새 메시지 전송, 코드 실행, API 호출 등 외부 효과를 발생시킬 수 있습니다.
    
  다음은 채팅 기능을 가진 에이전트를 직접 생성하는 간단한 코드 예시입니다:

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
    
    위 코드에서 `MyAssistant`는 `RoutedAgent`를 상속받아 생성되었습니다. 메시지 핸들러는 메시지 내용을 출력한 후 `AssistantAgent` 대리자를 사용해 응답을 보냅니다. 특히 `self._delegate`에 사전 구축된 채팅 완료를 처리할 수 있는 `AssistantAgent` 인스턴스를 할당하는 부분에 주목하세요.

    이제 AutoGen에 이 에이전트 타입을 알려주고 프로그램을 시작해 봅시다:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    위 코드에서는 에이전트가 런타임에 등록되고, 에이전트에 메시지가 전송되어 다음과 같은 출력이 발생합니다:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **다중 에이전트(Multi agents)**. AutoGen은 복잡한 작업을 달성하기 위해 함께 작동할 수 있는 여러 에이전트 생성을 지원합니다. 에이전트들은 소통하고 정보를 공유하며 협력하여 문제를 더 효율적으로 해결할 수 있습니다. 다중 에이전트 시스템을 만들려면 데이터 검색, 분석, 의사결정, 사용자 상호작용 등 전문화된 기능과 역할을 가진 다양한 유형의 에이전트를 정의할 수 있습니다. 다음은 그러한 생성 예시입니다:

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

    위 코드에서는 `GroupChatManager`가 런타임에 등록되어 있습니다. 이 매니저는 작가, 일러스트레이터, 편집자, 사용자 등 다양한 유형의 에이전트 간 상호작용을 조율하는 역할을 합니다.

- **에이전트 런타임(Agent Runtime)**. 이 프레임워크는 에이전트 간 통신을 가능하게 하고, 에이전트의 신원과 수명 주기를 관리하며, 보안 및 개인정보 경계를 강제하는 런타임 환경을 제공합니다. 즉, 에이전트를 안전하고 통제된 환경에서 실행하여 안전하고 효율적으로 상호작용할 수 있도록 합니다. 관심 있는 두 가지 런타임이 있습니다:
  - **독립 실행형 런타임(Stand-alone runtime)**. 모든 에이전트가 동일한 프로그래밍 언어로 구현되고 같은 프로세스에서 실행되는 단일 프로세스 애플리케이션에 적합합니다. 작동 방식은 다음과 같습니다:

애플리케이션 스택

    *에이전트는 런타임을 통해 메시지로 통신하며, 런타임은 에이전트의 수명 주기를 관리합니다*

  - **분산 에이전트 런타임(Distributed agent runtime)**. 에이전트가 서로 다른 프로그래밍 언어로 구현되고 다른 머신에서 실행되는 다중 프로세스 애플리케이션에 적합합니다. 작동 방식은 다음과 같습니다:

## Semantic Kernel + 에이전트 프레임워크

Semantic Kernel은 엔터프라이즈급 AI 오케스트레이션 SDK입니다. AI 및 메모리 커넥터와 에이전트 프레임워크로 구성되어 있습니다.

먼저 몇 가지 핵심 구성 요소를 살펴보겠습니다:

- **AI 커넥터(AI Connectors)**: Python과 C# 모두에서 사용할 수 있는 외부 AI 서비스 및 데이터 소스와의 인터페이스입니다.

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

    여기서는 커널을 생성하고 채팅 완료 서비스를 추가하는 간단한 예시를 볼 수 있습니다. Semantic Kernel은 외부 AI 서비스, 이 경우 Azure OpenAI 채팅 완료 서비스와 연결을 만듭니다.

- **플러그인(Plugins)**: 애플리케이션에서 사용할 수 있는 기능을 캡슐화합니다. 준비된 플러그인과 직접 만들 수 있는 커스텀 플러그인이 있습니다. 관련 개념으로 "프롬프트 함수(prompt functions)"가 있습니다. 함수 호출을 위한 자연어 신호 대신 특정 함수를 모델에 브로드캐스트합니다. 현재 채팅 컨텍스트에 따라 모델이 이 함수들 중 하나를 호출해 요청이나 쿼리를 완료할 수 있습니다. 예시는 다음과 같습니다:

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

    여기서는 먼저 사용자 입력 `$userInput`을 위한 공간을 남긴 템플릿 프롬프트 `skPrompt`가 있습니다. 그 다음 `SummarizeText`라는 커널 함수를 만들고 `SemanticFunctions`라는 플러그인 이름으로 커널에 가져옵니다. 함수 이름은 Semantic Kernel이 함수의 역할과 호출 시점을 이해하는 데 도움을 줍니다.

- **네이티브 함수(Native function)**: 프레임워크가 직접 호출해 작업을 수행하는 네이티브 함수도 있습니다. 예를 들어 파일에서 내용을 가져오는 함수는 다음과 같습니다:

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

- **메모리(Memory)**: AI 앱의 컨텍스트 관리를 추상화하고 단순화합니다. 메모리는 LLM이 알아야 할 정보입니다. 이 정보를 벡터 저장소에 저장할 수 있는데, 이는 인메모리 데이터베이스나 벡터 데이터베이스와 유사합니다. 다음은 *사실(facts)*을 메모리에 추가하는 매우 단순화된 시나리오 예시입니다:

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

    이 사실들은 `SummarizedAzureDocs`라는 메모리 컬렉션에 저장됩니다. 매우 단순한 예시지만, LLM이 사용할 정보를 메모리에 저장하는 방식을 볼 수 있습니다.
## 이전 강의

[AI 에이전트 및 에이전트 사용 사례 소개](../01-intro-to-ai-agents/README.md)

## 다음 강의

[에이전틱 디자인 패턴 이해하기](../03-agentic-design-patterns/README.md)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문은 해당 언어의 원본 문서가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.