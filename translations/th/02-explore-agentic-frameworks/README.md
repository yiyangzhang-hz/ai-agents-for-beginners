<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:03:25+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "th"
}
-->
. ตามที่วิกิพีเดียกล่าวไว้ actor คือ _หน่วยพื้นฐานของการคำนวณแบบพร้อมกัน (concurrent computation) ซึ่งเมื่อได้รับข้อความ actor สามารถ: ตัดสินใจภายใน, สร้าง actor เพิ่มเติม, ส่งข้อความเพิ่มเติม และกำหนดวิธีตอบสนองต่อข้อความถัดไปที่ได้รับ_

**กรณีการใช้งาน**: การสร้างโค้ดอัตโนมัติ, งานวิเคราะห์ข้อมูล และการสร้างเอเจนต์เฉพาะสำหรับการวางแผนและฟังก์ชันการวิจัย

นี่คือแนวคิดหลักสำคัญของ AutoGen:

- **Agents**. เอเจนต์คือเอนทิตีซอฟต์แวร์ที่:
  - **สื่อสารผ่านข้อความ** ซึ่งข้อความเหล่านี้อาจเป็นแบบ synchronous หรือ asynchronous
  - **รักษาสถานะของตัวเอง** ซึ่งสามารถถูกแก้ไขโดยข้อความที่เข้ามา
  - **ดำเนินการ** เพื่อตอบสนองต่อข้อความที่ได้รับหรือการเปลี่ยนแปลงสถานะ การดำเนินการเหล่านี้อาจเปลี่ยนแปลงสถานะของเอเจนต์และสร้างผลกระทบภายนอก เช่น การอัปเดตบันทึกข้อความ ส่งข้อความใหม่ รันโค้ด หรือเรียก API

  นี่คือตัวอย่างโค้ดสั้น ๆ ที่คุณสร้างเอเจนต์ของคุณเองที่มีความสามารถในการแชท:

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
    
    ในโค้ดข้างต้น `MyAssistant` ถูกสร้างขึ้นและสืบทอดมาจาก `RoutedAgent` มีตัวจัดการข้อความที่พิมพ์เนื้อหาของข้อความและส่งการตอบกลับโดยใช้ตัวแทน `AssistantAgent` โปรดสังเกตเป็นพิเศษว่าเราได้กำหนด `self._delegate` ให้เป็นอินสแตนซ์ของ `AssistantAgent` ซึ่งเป็นเอเจนต์ที่สร้างไว้ล่วงหน้าที่สามารถจัดการการแชทได้

    ต่อไปเราจะให้ AutoGen รู้จักประเภทเอเจนต์นี้และเริ่มโปรแกรม:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    ในโค้ดข้างต้น เอเจนต์ถูกลงทะเบียนกับ runtime จากนั้นส่งข้อความไปยังเอเจนต์ซึ่งส่งผลลัพธ์ดังนี้:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen รองรับการสร้างเอเจนต์หลายตัวที่สามารถทำงานร่วมกันเพื่อบรรลุภารกิจที่ซับซ้อน เอเจนต์สามารถสื่อสาร แบ่งปันข้อมูล และประสานงานการทำงานเพื่อแก้ปัญหาได้อย่างมีประสิทธิภาพมากขึ้น ในการสร้างระบบหลายเอเจนต์ คุณสามารถกำหนดประเภทเอเจนต์ที่มีฟังก์ชันและบทบาทเฉพาะ เช่น การดึงข้อมูล การวิเคราะห์ การตัดสินใจ และการโต้ตอบกับผู้ใช้ มาดูตัวอย่างการสร้างแบบนี้กัน:

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

    ในโค้ดข้างต้น เรามี `GroupChatManager` ที่ลงทะเบียนกับ runtime ผู้จัดการนี้รับผิดชอบในการประสานงานการโต้ตอบระหว่างเอเจนต์ประเภทต่าง ๆ เช่น นักเขียน นักวาดภาพ บรรณาธิการ และผู้ใช้

- **Agent Runtime**. เฟรมเวิร์กมีสภาพแวดล้อม runtime ที่ช่วยให้เอเจนต์สื่อสารกัน จัดการตัวตนและวงจรชีวิตของเอเจนต์ รวมถึงบังคับใช้ขอบเขตความปลอดภัยและความเป็นส่วนตัว ซึ่งหมายความว่าคุณสามารถรันเอเจนต์ของคุณในสภาพแวดล้อมที่ปลอดภัยและควบคุมได้ เพื่อให้พวกเขาสามารถโต้ตอบได้อย่างปลอดภัยและมีประสิทธิภาพ มี runtime สองแบบที่น่าสนใจ:
  - **Stand-alone runtime** เหมาะสำหรับแอปพลิเคชันแบบกระบวนการเดียวที่เอเจนต์ทั้งหมดถูกพัฒนาในภาษาโปรแกรมเดียวกันและรันในกระบวนการเดียว นี่คือตัวอย่างภาพรวมการทำงาน:

สแต็กแอปพลิเคชัน

    *เอเจนต์สื่อสารผ่านข้อความผ่าน runtime และ runtime จัดการวงจรชีวิตของเอเจนต์*

  - **Distributed agent runtime** เหมาะสำหรับแอปพลิเคชันแบบหลายกระบวนการที่เอเจนต์อาจถูกพัฒนาในภาษาต่าง ๆ และรันบนเครื่องต่าง ๆ นี่คือตัวอย่างภาพรวมการทำงาน:

## Semantic Kernel + Agent Framework

Semantic Kernel คือ SDK สำหรับการประสานงาน AI ที่พร้อมใช้งานในองค์กร ประกอบด้วยตัวเชื่อมต่อ AI และหน่วยความจำ พร้อมกับ Agent Framework

เรามาเริ่มต้นด้วยส่วนประกอบหลักบางอย่าง:

- **AI Connectors**: เป็นอินเทอร์เฟซกับบริการ AI ภายนอกและแหล่งข้อมูลสำหรับใช้งานทั้งใน Python และ C#

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

    นี่คือตัวอย่างง่าย ๆ ของการสร้าง kernel และเพิ่มบริการ chat completion Semantic Kernel สร้างการเชื่อมต่อกับบริการ AI ภายนอก ในกรณีนี้คือ Azure OpenAI Chat Completion

- **Plugins**: เป็นการรวบรวมฟังก์ชันที่แอปพลิเคชันสามารถใช้ได้ มีทั้งปลั๊กอินที่สร้างไว้ล่วงหน้าและปลั๊กอินที่คุณสร้างเอง แนวคิดที่เกี่ยวข้องคือ "prompt functions" แทนที่จะให้คำสั่งเป็นภาษาธรรมชาติสำหรับเรียกใช้ฟังก์ชัน คุณจะเผยแพร่ฟังก์ชันบางอย่างไปยังโมเดล โดยโมเดลอาจเลือกเรียกใช้ฟังก์ชันเหล่านี้ตามบริบทการแชทปัจจุบันเพื่อทำคำขอหรือสอบถามให้เสร็จสมบูรณ์ นี่คือตัวอย่าง:

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

    ที่นี่ คุณมีเทมเพลต prompt `skPrompt` ที่เว้นที่ว่างให้ผู้ใช้ป้อนข้อความ `$userInput` จากนั้นคุณสร้างฟังก์ชัน kernel ชื่อ `SummarizeText` และนำเข้าฟังก์ชันนี้ใน kernel ภายใต้ชื่อปลั๊กอิน `SemanticFunctions` โปรดสังเกตชื่อฟังก์ชันที่ช่วยให้ Semantic Kernel เข้าใจว่าฟังก์ชันทำอะไรและควรเรียกเมื่อใด

- **Native function**: ยังมีฟังก์ชันเนทีฟที่เฟรมเวิร์กสามารถเรียกใช้โดยตรงเพื่อดำเนินงาน ตัวอย่างเช่น ฟังก์ชันที่ดึงเนื้อหาจากไฟล์:

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

- **Memory**: เป็นการสรุปและทำให้การจัดการบริบทสำหรับแอป AI ง่ายขึ้น แนวคิดของ memory คือข้อมูลนี้เป็นสิ่งที่ LLM ควรรู้ คุณสามารถเก็บข้อมูลนี้ใน vector store ซึ่งอาจเป็นฐานข้อมูลในหน่วยความจำหรือฐานข้อมูลเวกเตอร์หรือคล้ายกัน นี่คือตัวอย่างสถานการณ์ง่าย ๆ ที่เพิ่ม *facts* ลงใน memory:

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

    ข้อเท็จจริงเหล่านี้จะถูกเก็บในคอลเลกชัน memory ชื่อ `SummarizedAzureDocs` นี่คือตัวอย่างที่เรียบง่ายมาก แต่คุณจะเห็นว่าคุณสามารถเก็บข้อมูลใน memory เพื่อให้ LLM ใช้งานได้อย่างไร
## บทเรียนก่อนหน้า

[แนะนำเกี่ยวกับ AI Agents และกรณีการใช้งาน Agent](../01-intro-to-ai-agents/README.md)

## บทเรียนถัดไป

[ทำความเข้าใจรูปแบบการออกแบบ Agentic](../03-agentic-design-patterns/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้