<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:59:15+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pa"
}
-->
. ਵਿਖਿਆਪਨ ਅਨੁਸਾਰ, ਇੱਕ ਐਕਟਰ _ਸਮਕਾਲੀ ਗਣਨਾ ਦਾ ਮੂਲ ਭਾਗ ਹੈ। ਜਦੋਂ ਇਹ ਕਿਸੇ ਸੁਨੇਹੇ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ, ਤਾਂ ਇਹ: ਸਥਾਨਕ ਫੈਸਲੇ ਕਰ ਸਕਦਾ ਹੈ, ਹੋਰ ਐਕਟਰ ਬਣਾਉਂਦਾ ਹੈ, ਹੋਰ ਸੁਨੇਹੇ ਭੇਜਦਾ ਹੈ, ਅਤੇ ਅਗਲੇ ਪ੍ਰਾਪਤ ਹੋਣ ਵਾਲੇ ਸੁਨੇਹੇ ਦਾ ਜਵਾਬ ਕਿਵੇਂ ਦੇਣਾ ਹੈ ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ_।

**ਵਰਤੋਂ ਦੇ ਕੇਸ**: ਕੋਡ ਜਨਰੇਸ਼ਨ ਨੂੰ ਆਟੋਮੇਟ ਕਰਨ, ਡਾਟਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕਾਰਜਾਂ ਨੂੰ ਕਰਨ ਅਤੇ ਯੋਜਨਾ ਬਣਾਉਣ ਅਤੇ ਖੋਜ ਕਾਰਜਾਂ ਲਈ ਕਸਟਮ ਏਜੰਟ ਬਣਾਉਣ।

ਇੱਥੇ AutoGen ਦੇ ਕੁਝ ਮਹੱਤਵਪੂਰਨ ਮੁੱਖ ਸੰਕਲਪ ਹਨ:

- **ਏਜੰਟ**। ਇੱਕ ਏਜੰਟ ਇੱਕ ਸਾਫਟਵੇਅਰ ਇਕਾਈ ਹੈ ਜੋ:
  - **ਸੁਨੇਹਿਆਂ ਰਾਹੀਂ ਸੰਚਾਰ ਕਰਦਾ ਹੈ**, ਇਹ ਸੁਨੇਹੇ ਸਮਕਾਲੀ ਜਾਂ ਅਸਮਕਾਲੀ ਹੋ ਸਕਦੇ ਹਨ।
  - **ਆਪਣੀ ਸਥਿਤੀ ਨੂੰ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ**, ਜਿਸ ਨੂੰ ਆਉਣ ਵਾਲੇ ਸੁਨੇਹਿਆਂ ਦੁਆਰਾ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ।
  - **ਪ੍ਰਾਪਤ ਸੁਨੇਹਿਆਂ ਜਾਂ ਆਪਣੀ ਸਥਿਤੀ ਵਿੱਚ ਬਦਲਾਅ ਦੇ ਜਵਾਬ ਵਿੱਚ ਕਾਰਵਾਈ ਕਰਦਾ ਹੈ।** ਇਹ ਕਾਰਵਾਈਆਂ ਏਜੰਟ ਦੀ ਸਥਿਤੀ ਨੂੰ ਬਦਲ ਸਕਦੀਆਂ ਹਨ ਅਤੇ ਬਾਹਰੀ ਪ੍ਰਭਾਵ ਪੈਦਾ ਕਰ ਸਕਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਕਿ ਸੁਨੇਹਾ ਲਾਗਜ਼ ਨੂੰ ਅਪਡੇਟ ਕਰਨਾ, ਨਵੇਂ ਸੁਨੇਹੇ ਭੇਜਣਾ, ਕੋਡ ਚਲਾਉਣਾ ਜਾਂ API ਕਾਲ ਕਰਨਾ।
    
  ਇੱਥੇ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਛੋਟਾ ਕੋਡ ਸਨਿੱਪੇਟ ਹੈ ਜਿਸ ਵਿੱਚ ਤੁਸੀਂ ਚੈਟ ਸਮਰੱਥਾਵਾਂ ਵਾਲਾ ਆਪਣਾ ਏਜੰਟ ਬਣਾਉਂਦੇ ਹੋ:

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
    
    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ, `MyAssistant` ਬਣਾਇਆ ਗਿਆ ਹੈ ਅਤੇ `RoutedAgent` ਤੋਂ ਵਿਰਾਸਤ ਵਿੱਚ ਮਿਲਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਇੱਕ ਸੁਨੇਹਾ ਹੈਂਡਲਰ ਹੈ ਜੋ ਸੁਨੇਹੇ ਦੀ ਸਮੱਗਰੀ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ `AssistantAgent` ਡੈਲੀਗੇਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਵਾਬ ਭੇਜਦਾ ਹੈ। ਖਾਸ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਅਸੀਂ `self._delegate` ਨੂੰ `AssistantAgent` ਦਾ ਇੱਕ ਉਦਾਹਰਨ ਸੌਂਪਦੇ ਹਾਂ ਜੋ ਇੱਕ ਪ੍ਰੀ-ਬਿਲਟ ਏਜੰਟ ਹੈ ਜੋ ਚੈਟ ਪੂਰਨਤਾ ਨੂੰ ਸੰਭਾਲ ਸਕਦਾ ਹੈ।

    ਆਓ AutoGen ਨੂੰ ਇਸ ਏਜੰਟ ਕਿਸਮ ਬਾਰੇ ਦੱਸਦੇ ਹਾਂ ਅਤੇ ਅਗਲਾ ਪ੍ਰੋਗਰਾਮ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਏਜੰਟਾਂ ਨੂੰ ਰਨਟਾਈਮ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਫਿਰ ਏਜੰਟ ਨੂੰ ਇੱਕ ਸੁਨੇਹਾ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ ਜਿਸ ਦਾ ਨਤੀਜਾ ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਹੈ:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **ਮਲਟੀ ਏਜੰਟ**। AutoGen ਕਈ ਏਜੰਟਾਂ ਦੀ ਰਚਨਾ ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ ਜੋ ਮਿਲ ਕੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਜਟਿਲ ਕਾਰਜਾਂ ਨੂੰ ਪੂਰਾ ਕੀਤਾ ਜਾ ਸਕੇ। ਏਜੰਟ ਸੰਚਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਾਣਕਾਰੀ ਸਾਂਝੀ ਕਰ ਸਕਦੇ ਹਨ, ਅਤੇ ਆਪਣੇ ਕਾਰਜਾਂ ਨੂੰ ਸਹਿਯੋਗ ਨਾਲ ਨਿਭਾ ਸਕਦੇ ਹਨ ਤਾਂ ਜੋ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਜ਼ਿਆਦਾ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਹੱਲ ਕੀਤਾ ਜਾ ਸਕੇ। ਮਲਟੀ-ਏਜੰਟ ਸਿਸਟਮ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਏਜੰਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰ ਸਕਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਦੇ ਵਿਸ਼ੇਸ਼ ਕਾਰਜ ਅਤੇ ਭੂਮਿਕਾਵਾਂ ਹੁੰਦੀਆਂ ਹਨ, ਜਿਵੇਂ ਡਾਟਾ ਪ੍ਰਾਪਤੀ, ਵਿਸ਼ਲੇਸ਼ਣ, ਫੈਸਲਾ-ਲੈਣਾ, ਅਤੇ ਉਪਭੋਗਤਾ ਇੰਟਰੈਕਸ਼ਨ। ਆਓ ਵੇਖੀਏ ਕਿ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਰਚਨਾ ਕਿਵੇਂ ਦਿਸਦੀ ਹੈ:

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

    ਪਿਛਲੇ ਕੋਡ ਵਿੱਚ ਸਾਡੇ ਕੋਲ ਇੱਕ `GroupChatManager` ਹੈ ਜੋ ਰਨਟਾਈਮ ਨਾਲ ਰਜਿਸਟਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਇਹ ਮੈਨੇਜਰ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਏਜੰਟਾਂ, ਜਿਵੇਂ ਲੇਖਕਾਂ, ਚਿੱਤਰਕਾਰਾਂ, ਸੰਪਾਦਕਾਂ ਅਤੇ ਉਪਭੋਗਤਾਵਾਂ ਦੇ ਵਿਚਕਾਰ ਇੰਟਰੈਕਸ਼ਨਾਂ ਦਾ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ।

- **ਏਜੰਟ ਰਨਟਾਈਮ**। ਫਰੇਮਵਰਕ ਇੱਕ ਰਨਟਾਈਮ ਵਾਤਾਵਰਣ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਏਜੰਟਾਂ ਵਿਚਕਾਰ ਸੰਚਾਰ ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ, ਉਨ੍ਹਾਂ ਦੀਆਂ ਪਹਿਚਾਣਾਂ ਅਤੇ ਜੀਵਨਚੱਕਰਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰਦਾ ਹੈ, ਅਤੇ ਸੁਰੱਖਿਆ ਅਤੇ ਗੋਪਨੀਯਤਾ ਦੀਆਂ ਸੀਮਾਵਾਂ ਲਾਗੂ ਕਰਦਾ ਹੈ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਏਜੰਟਾਂ ਨੂੰ ਇੱਕ ਸੁਰੱਖਿਅਤ ਅਤੇ ਨਿਯੰਤਰਿਤ ਵਾਤਾਵਰਣ ਵਿੱਚ ਚਲਾ ਸਕਦੇ ਹੋ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦੇ ਹੋਏ ਕਿ ਉਹ ਸੁਰੱਖਿਅਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਢੰਗ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਸਕਦੇ ਹਨ। ਦੋ ਰਨਟਾਈਮ ਹਨ ਜੋ ਦਿਲਚਸਪੀ ਦੇ ਹਨ:
  - **ਸਟੈਂਡ-ਅਲੋਨ ਰਨਟਾਈਮ**। ਇਹ ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੈ ਇਕ-ਪ੍ਰਕਿਰਿਆ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਜਿੱਥੇ ਸਾਰੇ ਏਜੰਟ ਇੱਕੋ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾ ਵਿੱਚ ਲਾਗੂ ਕੀਤੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਇੱਕੋ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਚਲਦੇ ਹਨ। ਇਹ ਹੈ ਕਿ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ:  

ਐਪਲੀਕੇਸ਼ਨ ਸਟੈਕ

    *ਏਜੰਟ ਸੁਨੇਹਿਆਂ ਰਾਹੀਂ ਰਨਟਾਈਮ ਨਾਲ ਸੰਚਾਰ ਕਰਦੇ ਹਨ, ਅਤੇ ਰਨਟਾਈਮ ਏਜੰਟਾਂ ਦੇ ਜੀਵਨਚੱਕਰ ਦਾ ਪ੍ਰਬੰਧ ਕਰਦਾ ਹੈ*

  - **ਵੰਡਿਆ ਹੋਇਆ ਏਜੰਟ ਰਨਟਾਈਮ**, ਇਹ ਬਹੁ-ਪ੍ਰਕਿਰਿਆ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਉਚਿਤ ਹੈ ਜਿੱਥੇ ਏਜੰਟ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਲਾਗੂ ਹੋ ਸਕਦੇ ਹਨ ਅਤੇ ਵੱਖ-ਵੱਖ ਮਸ਼ੀਨਾਂ 'ਤੇ ਚੱਲ ਰਹੇ ਹੋ ਸਕਦੇ ਹਨ। ਇਹ ਹੈ ਕਿ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ:  

## Semantic Kernel + Agent Framework

Semantic Kernel ਇੱਕ ਉਦਯੋਗ-ਤਿਆਰ AI ਓਰਕੇਸਟ੍ਰੇਸ਼ਨ SDK ਹੈ। ਇਹ AI ਅਤੇ ਮੈਮੋਰੀ ਕਨੈਕਟਰਾਂ ਦੇ ਨਾਲ-ਨਾਲ ਇੱਕ ਏਜੰਟ ਫਰੇਮਵਰਕ 'ਤੇ مشتمل ਹੈ।

ਆਓ ਪਹਿਲਾਂ ਕੁਝ ਮੁੱਖ ਭਾਗਾਂ ਨੂੰ ਕਵਰ ਕਰੀਏ:

- **AI ਕਨੈਕਟਰ**: ਇਹ ਬਾਹਰੀ AI ਸੇਵਾਵਾਂ ਅਤੇ ਡਾਟਾ ਸਰੋਤਾਂ ਨਾਲ ਇੰਟਰਫੇਸ ਹੈ ਜੋ Python ਅਤੇ C# ਦੋਹਾਂ ਵਿੱਚ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

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

    ਇੱਥੇ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਸਧਾਰਣ ਉਦਾਹਰਨ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਇੱਕ kernel ਬਣਾਉਂਦੇ ਹੋ ਅਤੇ ਚੈਟ ਪੂਰਨਤਾ ਸੇਵਾ ਜੋੜਦੇ ਹੋ। Semantic Kernel ਇੱਕ ਬਾਹਰੀ AI ਸੇਵਾ ਨਾਲ ਕਨੈਕਸ਼ਨ ਬਣਾਉਂਦਾ ਹੈ, ਇਸ ਮਾਮਲੇ ਵਿੱਚ Azure OpenAI Chat Completion।

- **ਪਲੱਗਇਨ**: ਇਹ ਉਹ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਸਮੇਟਦੇ ਹਨ ਜੋ ਇੱਕ ਐਪਲੀਕੇਸ਼ਨ ਵਰਤ ਸਕਦੀ ਹੈ। ਤਿਆਰ-ਮੁਕੰਮਲ ਪਲੱਗਇਨ ਅਤੇ ਕਸਟਮ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ। ਇੱਕ ਸੰਬੰਧਿਤ ਸੰਕਲਪ "prompt functions" ਹੈ। ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੇ ਇਸ਼ਾਰਿਆਂ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਕੁਝ ਫੰਕਸ਼ਨਾਂ ਨੂੰ ਮਾਡਲ ਨੂੰ ਪ੍ਰਸਾਰਿਤ ਕਰਦੇ ਹੋ। ਮੌਜੂਦਾ ਚੈਟ ਸੰਦਰਭ ਦੇ ਆਧਾਰ 'ਤੇ, ਮਾਡਲ ਇਹਨਾਂ ਵਿੱਚੋਂ ਕਿਸੇ ਇੱਕ ਫੰਕਸ਼ਨ ਨੂੰ ਕਾਲ ਕਰ ਸਕਦਾ ਹੈ ਤਾਂ ਜੋ ਬੇਨਤੀ ਜਾਂ ਪੁੱਛਗਿੱਛ ਪੂਰੀ ਕੀਤੀ ਜਾ ਸਕੇ। ਇੱਥੇ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

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

    ਇੱਥੇ, ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਇੱਕ ਟੈਮਪਲੇਟ ਪ੍ਰਾਂਪਟ `skPrompt` ਹੈ ਜੋ ਉਪਭੋਗਤਾ ਲਈ ਟੈਕਸਟ ਇਨਪੁੱਟ `$userInput` ਲਈ ਜਗ੍ਹਾ ਛੱਡਦਾ ਹੈ। ਫਿਰ ਤੁਸੀਂ kernel ਫੰਕਸ਼ਨ `SummarizeText` ਬਣਾਉਂਦੇ ਹੋ ਅਤੇ ਇਸਨੂੰ `SemanticFunctions` ਨਾਮ ਦੇ ਪਲੱਗਇਨ ਨਾਲ kernel ਵਿੱਚ ਆਯਾਤ ਕਰਦੇ ਹੋ। ਫੰਕਸ਼ਨ ਦੇ ਨਾਮ 'ਤੇ ਧਿਆਨ ਦਿਓ ਜੋ Semantic Kernel ਨੂੰ ਸਮਝਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ ਕਿ ਫੰਕਸ਼ਨ ਕੀ ਕਰਦਾ ਹੈ ਅਤੇ ਕਦੋਂ ਕਾਲ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

- **ਦੇਸੀ ਫੰਕਸ਼ਨ**: ਫਰੇਮਵਰਕ ਕੋਲ ਐਸੇ ਦੇਸੀ ਫੰਕਸ਼ਨ ਵੀ ਹਨ ਜੋ ਸਿੱਧਾ ਕਾਰਜ ਕਰਨ ਲਈ ਕਾਲ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਇੱਥੇ ਇੱਕ ਉਦਾਹਰਨ ਹੈ ਜੋ ਫਾਇਲ ਤੋਂ ਸਮੱਗਰੀ ਪ੍ਰਾਪਤ ਕਰਦਾ ਹੈ:

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

- **ਮੈਮੋਰੀ**: AI ਐਪਸ ਲਈ ਸੰਦਰਭ ਪ੍ਰਬੰਧਨ ਨੂੰ ਸਰਲ ਅਤੇ ਅਸਾਨ ਬਣਾਉਂਦਾ ਹੈ। ਮੈਮੋਰੀ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਹ ਕੁਝ ਐਸਾ ਹੈ ਜੋ LLM ਨੂੰ ਜਾਣਨਾ ਚਾਹੀਦਾ ਹੈ। ਤੁਸੀਂ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਇੱਕ ਵੈਕਟਰ ਸਟੋਰ ਵਿੱਚ ਸਟੋਰ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਇੱਕ ਇਨ-ਮੈਮੋਰੀ ਡੇਟਾਬੇਸ ਜਾਂ ਵੈਕਟਰ ਡੇਟਾਬੇਸ ਜਾਂ ਇਸਦੇ ਸਮਾਨ ਹੁੰਦਾ ਹੈ। ਇੱਥੇ ਇੱਕ ਬਹੁਤ ਹੀ ਸਧਾਰਣ ਉਦਾਹਰਨ ਹੈ ਜਿੱਥੇ *ਤੱਥ* ਮੈਮੋਰੀ ਵਿੱਚ ਜੋੜੇ ਜਾਂਦੇ ਹਨ:

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

    ਇਹ ਤੱਥ ਫਿਰ ਮੈਮੋਰੀ ਕਲੈਕਸ਼ਨ `SummarizedAzureDocs` ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਬਹੁਤ ਹੀ ਸਧਾਰਣ ਉਦਾਹਰਨ ਹੈ, ਪਰ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਜਾਣਕਾਰੀ ਨੂੰ ਮੈਮੋਰੀ ਵਿੱਚ ਸਟੋਰ ਕਰ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ LLM ਇਸਦਾ ਉਪਯੋਗ ਕਰ ਸਕੇ।
## ਪਿਛਲਾ ਪਾਠ

[AI ਏਜੰਟਸ ਅਤੇ ਏਜੰਟ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਦਾ ਪਰਚਿਆ](../01-intro-to-ai-agents/README.md)

## ਅਗਲਾ ਪਾਠ

[ਏਜੰਟਿਕ ਡਿਜ਼ਾਈਨ ਪੈਟਰਨਾਂ ਨੂੰ ਸਮਝਣਾ](../03-agentic-design-patterns/README.md)

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।