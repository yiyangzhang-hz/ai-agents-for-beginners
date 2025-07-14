<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T08:50:55+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fr"
}
-->
. Selon Wikipedia, un acteur est _le bloc de construction de base du calcul concurrent. En réponse à un message qu'il reçoit, un acteur peut : prendre des décisions locales, créer d'autres acteurs, envoyer plus de messages, et déterminer comment répondre au prochain message reçu_.

**Cas d'utilisation** : Automatisation de la génération de code, tâches d'analyse de données, et création d'agents personnalisés pour des fonctions de planification et de recherche.

Voici quelques concepts clés importants d'AutoGen :

- **Agents**. Un agent est une entité logicielle qui :
  - **Communique via des messages**, ces messages pouvant être synchrones ou asynchrones.
  - **Maintient son propre état**, qui peut être modifié par les messages entrants.
  - **Effectue des actions** en réponse aux messages reçus ou aux changements de son état. Ces actions peuvent modifier l'état de l'agent et produire des effets externes, tels que la mise à jour des journaux de messages, l'envoi de nouveaux messages, l'exécution de code ou des appels API.
    
  Voici un court extrait de code dans lequel vous créez votre propre agent avec des capacités de chat :

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
    
    Dans le code précédent, `MyAssistant` a été créé et hérite de `RoutedAgent`. Il possède un gestionnaire de messages qui affiche le contenu du message puis envoie une réponse en utilisant le délégué `AssistantAgent`. Notez particulièrement comment nous assignons à `self._delegate` une instance de `AssistantAgent`, qui est un agent préconstruit capable de gérer les complétions de chat.

    Informons maintenant AutoGen de ce type d'agent et lançons le programme :

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Dans le code précédent, les agents sont enregistrés auprès du runtime, puis un message est envoyé à l'agent, ce qui produit la sortie suivante :

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agents**. AutoGen supporte la création de plusieurs agents pouvant collaborer pour accomplir des tâches complexes. Les agents peuvent communiquer, partager des informations et coordonner leurs actions pour résoudre des problèmes plus efficacement. Pour créer un système multi-agent, vous pouvez définir différents types d'agents avec des fonctions et rôles spécialisés, tels que la récupération de données, l'analyse, la prise de décision et l'interaction utilisateur. Voyons à quoi ressemble une telle création :

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

    Dans le code précédent, nous avons un `GroupChatManager` enregistré auprès du runtime. Ce gestionnaire est responsable de la coordination des interactions entre différents types d'agents, tels que les rédacteurs, illustrateurs, éditeurs et utilisateurs.

- **Agent Runtime**. Le framework fournit un environnement d'exécution permettant la communication entre agents, gérant leurs identités et cycles de vie, et appliquant des règles de sécurité et de confidentialité. Cela signifie que vous pouvez exécuter vos agents dans un environnement sécurisé et contrôlé, garantissant qu'ils interagissent de manière sûre et efficace. Il existe deux environnements d'exécution d'intérêt :
  - **Runtime autonome**. C'est un bon choix pour les applications à processus unique où tous les agents sont implémentés dans le même langage de programmation et s'exécutent dans le même processus. Voici une illustration de son fonctionnement :

Pile applicative

    *les agents communiquent via des messages à travers le runtime, et le runtime gère le cycle de vie des agents*

  - **Runtime distribué**, adapté aux applications multi-processus où les agents peuvent être implémentés dans différents langages de programmation et s'exécuter sur différentes machines. Voici une illustration de son fonctionnement :

## Semantic Kernel + Agent Framework

Semantic Kernel est un SDK d'orchestration IA prêt pour l'entreprise. Il comprend des connecteurs AI et mémoire, ainsi qu'un Agent Framework.

Commençons par couvrir quelques composants clés :

- **Connecteurs AI** : Il s'agit d'une interface avec des services AI externes et des sources de données, utilisable à la fois en Python et en C#.

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

    Voici un exemple simple montrant comment créer un kernel et y ajouter un service de complétion de chat. Semantic Kernel établit une connexion avec un service AI externe, ici Azure OpenAI Chat Completion.

- **Plugins** : Ils encapsulent des fonctions qu'une application peut utiliser. Il existe des plugins prêts à l'emploi ainsi que des personnalisés que vous pouvez créer. Un concept lié est celui des "fonctions prompt". Au lieu de fournir des indices en langage naturel pour invoquer une fonction, vous diffusez certaines fonctions au modèle. En fonction du contexte actuel du chat, le modèle peut choisir d'appeler l'une de ces fonctions pour compléter une requête ou une interrogation. Voici un exemple :

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

    Ici, vous avez d'abord un template de prompt `skPrompt` qui laisse de la place pour que l'utilisateur saisisse du texte, `$userInput`. Ensuite, vous créez la fonction kernel `SummarizeText` puis l'importez dans le kernel avec le nom de plugin `SemanticFunctions`. Notez le nom de la fonction qui aide Semantic Kernel à comprendre ce que fait la fonction et quand elle doit être appelée.

- **Fonction native** : Il existe aussi des fonctions natives que le framework peut appeler directement pour exécuter une tâche. Voici un exemple d'une telle fonction qui récupère le contenu d'un fichier :

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

- **Mémoire** : Abstrait et simplifie la gestion du contexte pour les applications AI. L'idée avec la mémoire est que c'est quelque chose que le LLM doit connaître. Vous pouvez stocker cette information dans un magasin vectoriel qui devient une base de données en mémoire, une base vectorielle ou similaire. Voici un exemple très simplifié où des *faits* sont ajoutés à la mémoire :

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

    Ces faits sont ensuite stockés dans la collection mémoire `SummarizedAzureDocs`. C'est un exemple très simplifié, mais vous pouvez voir comment stocker des informations dans la mémoire pour que le LLM puisse les utiliser.
## Leçon précédente

[Introduction aux agents IA et cas d'utilisation des agents](../01-intro-to-ai-agents/README.md)

## Leçon suivante

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.