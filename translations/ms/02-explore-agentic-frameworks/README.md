<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:07:52+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ms"
}
-->
. Menurut Wikipedia, pelakon adalah _blok binaan asas pengiraan serentak. Sebagai tindak balas kepada mesej yang diterimanya, pelakon boleh: membuat keputusan tempatan, mencipta lebih banyak pelakon, menghantar lebih banyak mesej, dan menentukan bagaimana untuk bertindak balas kepada mesej seterusnya yang diterima_.

**Kes Penggunaan**: Automasi penjanaan kod, tugas analisis data, dan membina ejen tersuai untuk fungsi perancangan dan penyelidikan.

Berikut adalah beberapa konsep teras penting AutoGen:

- **Ejen**. Ejen adalah entiti perisian yang:
  - **Berkomunikasi melalui mesej**, mesej ini boleh bersifat segerak atau tak segerak.
  - **Mengekalkan keadaan sendiri**, yang boleh diubah oleh mesej yang diterima.
  - **Melaksanakan tindakan** sebagai tindak balas kepada mesej yang diterima atau perubahan dalam keadaannya. Tindakan ini mungkin mengubah keadaan ejen dan menghasilkan kesan luaran, seperti mengemas kini log mesej, menghantar mesej baru, melaksanakan kod, atau membuat panggilan API.
    
  Di sini anda mempunyai petikan kod ringkas di mana anda mencipta ejen anda sendiri dengan keupayaan Chat:

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
    
    Dalam kod sebelum ini, `MyAssistant` telah dicipta dan mewarisi dari `RoutedAgent`. Ia mempunyai pengendali mesej yang mencetak kandungan mesej dan kemudian menghantar respons menggunakan delegasi `AssistantAgent`. Perhatikan khusus bagaimana kami menetapkan kepada `self._delegate` satu contoh `AssistantAgent` yang merupakan ejen pra-bina yang boleh mengendalikan penyempurnaan chat.

    Mari kita beritahu AutoGen tentang jenis ejen ini dan mulakan program seterusnya:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Dalam kod sebelum ini, ejen didaftarkan dengan runtime dan kemudian mesej dihantar kepada ejen menghasilkan output berikut:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi ejen**. AutoGen menyokong penciptaan pelbagai ejen yang boleh bekerjasama untuk mencapai tugas yang kompleks. Ejen boleh berkomunikasi, berkongsi maklumat, dan menyelaraskan tindakan mereka untuk menyelesaikan masalah dengan lebih cekap. Untuk mencipta sistem multi-ejen, anda boleh mentakrifkan jenis ejen yang berbeza dengan fungsi dan peranan khusus, seperti pengambilan data, analisis, pembuatan keputusan, dan interaksi pengguna. Mari lihat bagaimana penciptaan sebegini kelihatan supaya kita dapat gambaran mengenainya:

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

    Dalam kod sebelum ini, kami mempunyai `GroupChatManager` yang didaftarkan dengan runtime. Pengurus ini bertanggungjawab untuk menyelaraskan interaksi antara jenis ejen yang berbeza, seperti penulis, pelukis, editor, dan pengguna.

- **Runtime Ejen**. Rangka kerja menyediakan persekitaran runtime, membolehkan komunikasi antara ejen, mengurus identiti dan kitar hayat mereka, serta menguatkuasakan sempadan keselamatan dan privasi. Ini bermakna anda boleh menjalankan ejen anda dalam persekitaran yang selamat dan terkawal, memastikan mereka boleh berinteraksi dengan selamat dan cekap. Terdapat dua runtime yang menarik:
  - **Runtime berdiri sendiri**. Ini adalah pilihan yang baik untuk aplikasi proses tunggal di mana semua ejen dilaksanakan dalam bahasa pengaturcaraan yang sama dan dijalankan dalam proses yang sama. Berikut adalah ilustrasi bagaimana ia berfungsi:

Timbunan aplikasi

    *ejen berkomunikasi melalui mesej melalui runtime, dan runtime mengurus kitar hayat ejen*

  - **Runtime ejen teragih**, sesuai untuk aplikasi berbilang proses di mana ejen mungkin dilaksanakan dalam bahasa pengaturcaraan yang berbeza dan dijalankan pada mesin yang berbeza. Berikut adalah ilustrasi bagaimana ia berfungsi:

## Semantic Kernel + Rangka Kerja Ejen

Semantic Kernel adalah SDK Orkestrasi AI yang sedia untuk perusahaan. Ia terdiri daripada penyambung AI dan memori, bersama dengan Rangka Kerja Ejen.

Mari kita mulakan dengan beberapa komponen teras:

- **Penyambung AI**: Ini adalah antara muka dengan perkhidmatan AI luaran dan sumber data untuk digunakan dalam Python dan C#.

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

    Di sini anda mempunyai contoh mudah bagaimana anda boleh mencipta kernel dan menambah perkhidmatan penyempurnaan chat. Semantic Kernel mencipta sambungan ke perkhidmatan AI luaran, dalam kes ini, Azure OpenAI Chat Completion.

- **Plugin**: Ini merangkumi fungsi yang boleh digunakan oleh aplikasi. Terdapat plugin sedia ada dan juga yang boleh anda cipta sendiri. Konsep berkaitan ialah "fungsi prompt." Daripada memberikan isyarat bahasa semula jadi untuk panggilan fungsi, anda menyiarkan fungsi tertentu kepada model. Berdasarkan konteks chat semasa, model mungkin memilih untuk memanggil salah satu fungsi ini untuk melengkapkan permintaan atau pertanyaan. Berikut adalah contoh:

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

    Di sini, anda mula-mula mempunyai templat prompt `skPrompt` yang membenarkan ruang untuk pengguna memasukkan teks, `$userInput`. Kemudian anda mencipta fungsi kernel `SummarizeText` dan mengimportnya ke dalam kernel dengan nama plugin `SemanticFunctions`. Perhatikan nama fungsi yang membantu Semantic Kernel memahami apa fungsi itu lakukan dan bila ia harus dipanggil.

- **Fungsi asli**: Terdapat juga fungsi asli yang boleh dipanggil terus oleh rangka kerja untuk melaksanakan tugas. Berikut adalah contoh fungsi yang mengambil kandungan dari fail:

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

- **Memori**: Mengabstrak dan memudahkan pengurusan konteks untuk aplikasi AI. Idea dengan memori ialah ini adalah sesuatu yang LLM harus tahu. Anda boleh menyimpan maklumat ini dalam stor vektor yang akhirnya menjadi pangkalan data dalam memori atau pangkalan data vektor atau yang serupa. Berikut adalah contoh senario yang sangat ringkas di mana *fakta* ditambah ke dalam memori:

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

    Fakta-fakta ini kemudian disimpan dalam koleksi memori `SummarizedAzureDocs`. Ini adalah contoh yang sangat ringkas, tetapi anda boleh lihat bagaimana anda boleh menyimpan maklumat dalam memori untuk digunakan oleh LLM.
## Pelajaran Sebelumnya

[Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen](../01-intro-to-ai-agents/README.md)

## Pelajaran Seterusnya

[Memahami Corak Reka Bentuk Agentic](../03-agentic-design-patterns/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.