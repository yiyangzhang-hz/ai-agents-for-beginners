<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:07:24+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "id"
}
-->
. Menurut Wikipedia, aktor adalah _blok bangunan dasar dari komputasi konkuren. Sebagai respons terhadap pesan yang diterimanya, seorang aktor dapat: membuat keputusan lokal, membuat lebih banyak aktor, mengirim lebih banyak pesan, dan menentukan bagaimana merespons pesan berikutnya yang diterima_.

**Kasus Penggunaan**: Mengotomatisasi pembuatan kode, tugas analisis data, dan membangun agen khusus untuk fungsi perencanaan dan riset.

Berikut beberapa konsep inti penting dari AutoGen:

- **Agen**. Agen adalah entitas perangkat lunak yang:
  - **Berkomunikasi melalui pesan**, pesan ini bisa bersifat sinkron atau asinkron.
  - **Mempertahankan statusnya sendiri**, yang dapat diubah oleh pesan yang masuk.
  - **Melakukan tindakan** sebagai respons terhadap pesan yang diterima atau perubahan statusnya. Tindakan ini dapat mengubah status agen dan menghasilkan efek eksternal, seperti memperbarui log pesan, mengirim pesan baru, menjalankan kode, atau melakukan panggilan API.
    
  Berikut adalah potongan kode singkat di mana Anda membuat agen sendiri dengan kemampuan Chat:

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
    
    Dalam kode sebelumnya, `MyAssistant` telah dibuat dan mewarisi dari `RoutedAgent`. Ia memiliki pengelola pesan yang mencetak isi pesan dan kemudian mengirim respons menggunakan delegasi `AssistantAgent`. Perhatikan khususnya bagaimana kita menetapkan ke `self._delegate` sebuah instance dari `AssistantAgent` yang merupakan agen bawaan yang dapat menangani penyelesaian chat.

    Mari beri tahu AutoGen tentang tipe agen ini dan jalankan program berikutnya:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Dalam kode sebelumnya, agen-agen didaftarkan ke runtime dan kemudian sebuah pesan dikirim ke agen yang menghasilkan output berikut:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agen**. AutoGen mendukung pembuatan beberapa agen yang dapat bekerja sama untuk menyelesaikan tugas kompleks. Agen dapat berkomunikasi, berbagi informasi, dan mengoordinasikan tindakan mereka untuk memecahkan masalah dengan lebih efisien. Untuk membuat sistem multi-agen, Anda dapat mendefinisikan berbagai tipe agen dengan fungsi dan peran khusus, seperti pengambilan data, analisis, pengambilan keputusan, dan interaksi pengguna. Mari kita lihat bagaimana pembuatan seperti ini terlihat agar kita bisa memahami:

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

    Dalam kode sebelumnya, kita memiliki `GroupChatManager` yang didaftarkan ke runtime. Manajer ini bertanggung jawab mengoordinasikan interaksi antara berbagai tipe agen, seperti penulis, ilustrator, editor, dan pengguna.

- **Agent Runtime**. Framework menyediakan lingkungan runtime, memungkinkan komunikasi antar agen, mengelola identitas dan siklus hidup mereka, serta menegakkan batas keamanan dan privasi. Ini berarti Anda dapat menjalankan agen Anda dalam lingkungan yang aman dan terkendali, memastikan mereka dapat berinteraksi dengan aman dan efisien. Ada dua runtime yang perlu diperhatikan:
  - **Runtime mandiri**. Ini adalah pilihan yang baik untuk aplikasi satu proses di mana semua agen diimplementasikan dalam bahasa pemrograman yang sama dan berjalan dalam proses yang sama. Berikut ilustrasi cara kerjanya:

Tumpukan aplikasi

    *agen berkomunikasi melalui pesan lewat runtime, dan runtime mengelola siklus hidup agen*

  - **Runtime agen terdistribusi**, cocok untuk aplikasi multi-proses di mana agen dapat diimplementasikan dalam bahasa pemrograman berbeda dan berjalan di mesin yang berbeda. Berikut ilustrasi cara kerjanya:

## Semantic Kernel + Agent Framework

Semantic Kernel adalah SDK Orkestrasi AI siap pakai untuk perusahaan. Ini terdiri dari konektor AI dan memori, bersama dengan Agent Framework.

Mari kita bahas beberapa komponen inti terlebih dahulu:

- **AI Connectors**: Ini adalah antarmuka dengan layanan AI eksternal dan sumber data untuk digunakan di Python dan C#.

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

    Di sini Anda memiliki contoh sederhana bagaimana membuat kernel dan menambahkan layanan penyelesaian chat. Semantic Kernel membuat koneksi ke layanan AI eksternal, dalam hal ini Azure OpenAI Chat Completion.

- **Plugins**: Ini mengenkapsulasi fungsi yang dapat digunakan aplikasi. Ada plugin siap pakai dan juga yang bisa Anda buat sendiri. Konsep terkait adalah "fungsi prompt." Alih-alih memberikan petunjuk bahasa alami untuk pemanggilan fungsi, Anda menyiarkan fungsi tertentu ke model. Berdasarkan konteks chat saat ini, model dapat memilih untuk memanggil salah satu fungsi ini untuk menyelesaikan permintaan atau kueri. Berikut contohnya:

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

    Di sini, Anda pertama memiliki template prompt `skPrompt` yang menyediakan ruang bagi pengguna untuk memasukkan teks, `$userInput`. Kemudian Anda membuat fungsi kernel `SummarizeText` dan mengimpornya ke kernel dengan nama plugin `SemanticFunctions`. Perhatikan nama fungsi yang membantu Semantic Kernel memahami apa fungsi tersebut dan kapan harus dipanggil.

- **Native function**: Ada juga fungsi native yang dapat dipanggil langsung oleh framework untuk menjalankan tugas. Berikut contoh fungsi yang mengambil konten dari sebuah file:

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

- **Memory**: Mengabstraksi dan menyederhanakan manajemen konteks untuk aplikasi AI. Ide dari memori adalah ini sesuatu yang harus diketahui oleh LLM. Anda dapat menyimpan informasi ini dalam vector store yang pada akhirnya menjadi database in-memory atau database vektor atau sejenisnya. Berikut contoh skenario sangat sederhana di mana *fakta* ditambahkan ke memori:

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

    Fakta-fakta ini kemudian disimpan dalam koleksi memori `SummarizedAzureDocs`. Ini contoh yang sangat sederhana, tapi Anda bisa melihat bagaimana Anda dapat menyimpan informasi dalam memori untuk digunakan oleh LLM.
## Pelajaran Sebelumnya

[Pengantar Agen AI dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

## Pelajaran Berikutnya

[Memahami Pola Desain Agenik](../03-agentic-design-patterns/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.