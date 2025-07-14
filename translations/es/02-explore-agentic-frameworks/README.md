<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:51:23+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "es"
}
-->
. Según Wikipedia, un actor es _el bloque básico de la computación concurrente. En respuesta a un mensaje que recibe, un actor puede: tomar decisiones locales, crear más actores, enviar más mensajes y determinar cómo responder al siguiente mensaje recibido_.

**Casos de uso**: Automatización de generación de código, tareas de análisis de datos y creación de agentes personalizados para funciones de planificación e investigación.

Aquí algunos conceptos clave importantes de AutoGen:

- **Agentes**. Un agente es una entidad de software que:
  - **Se comunica mediante mensajes**, estos mensajes pueden ser síncronos o asíncronos.
  - **Mantiene su propio estado**, que puede ser modificado por mensajes entrantes.
  - **Realiza acciones** en respuesta a mensajes recibidos o cambios en su estado. Estas acciones pueden modificar el estado del agente y producir efectos externos, como actualizar registros de mensajes, enviar nuevos mensajes, ejecutar código o hacer llamadas a APIs.
    
  Aquí tienes un fragmento de código corto en el que creas tu propio agente con capacidades de chat:

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
    
    En el código anterior, `MyAssistant` ha sido creado y hereda de `RoutedAgent`. Tiene un manejador de mensajes que imprime el contenido del mensaje y luego envía una respuesta usando el delegado `AssistantAgent`. Observa especialmente cómo asignamos a `self._delegate` una instancia de `AssistantAgent`, que es un agente preconstruido que puede manejar completaciones de chat.

    Ahora informemos a AutoGen sobre este tipo de agente y ejecutemos el programa:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    En el código anterior, los agentes se registran en el runtime y luego se envía un mensaje al agente, resultando en la siguiente salida:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agentes**. AutoGen soporta la creación de múltiples agentes que pueden trabajar juntos para lograr tareas complejas. Los agentes pueden comunicarse, compartir información y coordinar sus acciones para resolver problemas de manera más eficiente. Para crear un sistema multiagente, puedes definir diferentes tipos de agentes con funciones y roles especializados, como recuperación de datos, análisis, toma de decisiones e interacción con usuarios. Veamos cómo se ve una creación así para que te hagas una idea:

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

    En el código anterior tenemos un `GroupChatManager` que está registrado en el runtime. Este gestor es responsable de coordinar las interacciones entre diferentes tipos de agentes, como escritores, ilustradores, editores y usuarios.

- **Agent Runtime**. El framework proporciona un entorno de ejecución que permite la comunicación entre agentes, gestiona sus identidades y ciclos de vida, y aplica límites de seguridad y privacidad. Esto significa que puedes ejecutar tus agentes en un entorno seguro y controlado, asegurando que puedan interactuar de forma segura y eficiente. Hay dos runtimes de interés:
  - **Runtime independiente**. Es una buena opción para aplicaciones de un solo proceso donde todos los agentes están implementados en el mismo lenguaje de programación y se ejecutan en el mismo proceso. Aquí tienes una ilustración de cómo funciona:

Pila de aplicación

    *los agentes se comunican mediante mensajes a través del runtime, y el runtime gestiona el ciclo de vida de los agentes*

  - **Runtime distribuido**, es adecuado para aplicaciones multiproceso donde los agentes pueden estar implementados en diferentes lenguajes de programación y ejecutarse en distintas máquinas. Aquí tienes una ilustración de cómo funciona:

## Semantic Kernel + Agent Framework

Semantic Kernel es un SDK de orquestación de IA listo para empresas. Consiste en conectores de IA y memoria, junto con un Agent Framework.

Primero cubramos algunos componentes clave:

- **Conectores de IA**: Esta es una interfaz con servicios externos de IA y fuentes de datos para uso tanto en Python como en C#.

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

    Aquí tienes un ejemplo simple de cómo puedes crear un kernel y agregar un servicio de completación de chat. Semantic Kernel crea una conexión con un servicio externo de IA, en este caso, Azure OpenAI Chat Completion.

- **Plugins**: Estos encapsulan funciones que una aplicación puede usar. Hay plugins ya hechos y otros personalizados que puedes crear. Un concepto relacionado es el de "funciones prompt". En lugar de proporcionar indicaciones en lenguaje natural para invocar funciones, transmites ciertas funciones al modelo. Basado en el contexto actual del chat, el modelo puede elegir llamar a una de estas funciones para completar una solicitud o consulta. Aquí tienes un ejemplo:

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

    Aquí, primero tienes una plantilla de prompt `skPrompt` que deja espacio para que el usuario ingrese texto, `$userInput`. Luego creas la función del kernel `SummarizeText` y la importas al kernel con el nombre de plugin `SemanticFunctions`. Observa el nombre de la función que ayuda a Semantic Kernel a entender qué hace la función y cuándo debe ser llamada.

- **Función nativa**: También hay funciones nativas que el framework puede llamar directamente para realizar la tarea. Aquí un ejemplo de una función que recupera el contenido de un archivo:

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

- **Memoria**: Abstrae y simplifica la gestión del contexto para aplicaciones de IA. La idea con la memoria es que esto es algo que el LLM debería conocer. Puedes almacenar esta información en un vector store que termina siendo una base de datos en memoria o una base de datos vectorial o similar. Aquí un ejemplo de un escenario muy simplificado donde se agregan *hechos* a la memoria:

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

    Estos hechos se almacenan luego en la colección de memoria `SummarizedAzureDocs`. Este es un ejemplo muy simplificado, pero puedes ver cómo puedes almacenar información en la memoria para que el LLM la use.
## Lección Anterior

[Introducción a los Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

## Próxima Lección

[Comprendiendo los Patrones de Diseño Agéntico](../03-agentic-design-patterns/README.md)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.