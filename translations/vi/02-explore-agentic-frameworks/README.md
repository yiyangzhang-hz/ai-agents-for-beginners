<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:06:57+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "vi"
}
-->
. Theo Wikipedia, một actor là _khối xây dựng cơ bản của tính toán đồng thời. Đáp lại một tin nhắn mà nó nhận được, một actor có thể: đưa ra quyết định cục bộ, tạo thêm các actor khác, gửi thêm tin nhắn, và xác định cách phản hồi tin nhắn tiếp theo nhận được_.

**Trường hợp sử dụng**: Tự động tạo mã, các tác vụ phân tích dữ liệu, và xây dựng các agent tùy chỉnh cho các chức năng lập kế hoạch và nghiên cứu.

Dưới đây là một số khái niệm cốt lõi quan trọng của AutoGen:

- **Agents**. Một agent là một thực thể phần mềm mà:
  - **Giao tiếp qua tin nhắn**, các tin nhắn này có thể đồng bộ hoặc bất đồng bộ.
  - **Duy trì trạng thái riêng của nó**, trạng thái này có thể được thay đổi bởi các tin nhắn đến.
  - **Thực hiện các hành động** để phản hồi các tin nhắn nhận được hoặc thay đổi trạng thái của nó. Các hành động này có thể thay đổi trạng thái của agent và tạo ra các hiệu ứng bên ngoài, như cập nhật nhật ký tin nhắn, gửi tin nhắn mới, thực thi mã, hoặc gọi API.
    
  Dưới đây là đoạn mã ngắn trong đó bạn tạo một agent của riêng mình với khả năng Chat:

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
    
    Trong đoạn mã trên, `MyAssistant` được tạo ra và kế thừa từ `RoutedAgent`. Nó có một trình xử lý tin nhắn in ra nội dung của tin nhắn và sau đó gửi phản hồi sử dụng đại biểu `AssistantAgent`. Đặc biệt lưu ý cách chúng ta gán cho `self._delegate` một thể hiện của `AssistantAgent`, đây là một agent được xây dựng sẵn có thể xử lý các hoàn thành chat.

    Bây giờ hãy cho AutoGen biết về loại agent này và khởi chạy chương trình:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Trong đoạn mã trên, các agent được đăng ký với runtime và sau đó một tin nhắn được gửi đến agent, kết quả là đầu ra sau:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen hỗ trợ tạo nhiều agent có thể làm việc cùng nhau để hoàn thành các tác vụ phức tạp. Các agent có thể giao tiếp, chia sẻ thông tin và phối hợp hành động để giải quyết vấn đề hiệu quả hơn. Để tạo hệ thống đa agent, bạn có thể định nghĩa các loại agent khác nhau với các chức năng và vai trò chuyên biệt, như truy xuất dữ liệu, phân tích, ra quyết định và tương tác với người dùng. Hãy xem cách tạo một hệ thống như vậy:

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

    Trong đoạn mã trên, chúng ta có một `GroupChatManager` được đăng ký với runtime. Quản lý này chịu trách nhiệm điều phối các tương tác giữa các loại agent khác nhau, như người viết, họa sĩ minh họa, biên tập viên và người dùng.

- **Agent Runtime**. Framework cung cấp một môi trường runtime, cho phép giao tiếp giữa các agent, quản lý danh tính và vòng đời của chúng, đồng thời đảm bảo các ranh giới bảo mật và quyền riêng tư. Điều này có nghĩa là bạn có thể chạy các agent của mình trong một môi trường an toàn và được kiểm soát, đảm bảo chúng có thể tương tác một cách an toàn và hiệu quả. Có hai loại runtime đáng chú ý:
  - **Standalone runtime**. Đây là lựa chọn tốt cho các ứng dụng đơn tiến trình, nơi tất cả các agent được triển khai trong cùng một ngôn ngữ lập trình và chạy trong cùng một tiến trình. Dưới đây là minh họa cách nó hoạt động:

Application stack

    *các agent giao tiếp qua tin nhắn thông qua runtime, và runtime quản lý vòng đời của các agent*

  - **Distributed agent runtime**, phù hợp cho các ứng dụng đa tiến trình, nơi các agent có thể được triển khai bằng các ngôn ngữ lập trình khác nhau và chạy trên các máy khác nhau. Dưới đây là minh họa cách nó hoạt động:

## Semantic Kernel + Agent Framework

Semantic Kernel là một SDK điều phối AI sẵn sàng cho doanh nghiệp. Nó bao gồm các kết nối AI và bộ nhớ, cùng với một Agent Framework.

Trước tiên, hãy tìm hiểu một số thành phần cốt lõi:

- **AI Connectors**: Đây là giao diện với các dịch vụ AI bên ngoài và nguồn dữ liệu để sử dụng trong cả Python và C#.

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

    Đây là ví dụ đơn giản về cách bạn có thể tạo một kernel và thêm dịch vụ hoàn thành chat. Semantic Kernel tạo kết nối với dịch vụ AI bên ngoài, trong trường hợp này là Azure OpenAI Chat Completion.

- **Plugins**: Chúng đóng gói các hàm mà ứng dụng có thể sử dụng. Có cả plugin có sẵn và plugin tùy chỉnh mà bạn có thể tạo. Một khái niệm liên quan là "prompt functions". Thay vì cung cấp các gợi ý ngôn ngữ tự nhiên để gọi hàm, bạn phát sóng một số hàm nhất định tới mô hình. Dựa trên ngữ cảnh chat hiện tại, mô hình có thể chọn gọi một trong các hàm này để hoàn thành yêu cầu hoặc truy vấn. Đây là ví dụ:

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

    Ở đây, bạn có một mẫu prompt `skPrompt` để người dùng nhập văn bản, `$userInput`. Sau đó bạn tạo hàm kernel `SummarizeText` và nhập nó vào kernel với tên plugin `SemanticFunctions`. Lưu ý tên hàm giúp Semantic Kernel hiểu chức năng của hàm và khi nào nên gọi nó.

- **Native function**: Cũng có các hàm gốc mà framework có thể gọi trực tiếp để thực hiện tác vụ. Đây là ví dụ về hàm lấy nội dung từ một file:

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

- **Memory**: Trừu tượng hóa và đơn giản hóa quản lý ngữ cảnh cho các ứng dụng AI. Ý tưởng về memory là đây là thông tin mà LLM nên biết. Bạn có thể lưu trữ thông tin này trong một kho vector, cuối cùng trở thành cơ sở dữ liệu trong bộ nhớ hoặc cơ sở dữ liệu vector hoặc tương tự. Đây là ví dụ về một kịch bản rất đơn giản, nơi các *facts* được thêm vào memory:

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

    Các facts này sau đó được lưu trong bộ nhớ `SummarizedAzureDocs`. Đây là ví dụ rất đơn giản, nhưng bạn có thể thấy cách lưu trữ thông tin trong memory để LLM sử dụng.
## Bài học trước

[Giới thiệu về AI Agents và các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

## Bài học tiếp theo

[Hiểu về các mẫu thiết kế Agentic](../03-agentic-design-patterns/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.