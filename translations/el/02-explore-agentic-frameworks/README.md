<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-12T09:02:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "el"
}
-->
. Σύμφωνα με τη Wikipedia, ένας actor είναι _η βασική μονάδα του ταυτόχρονου υπολογισμού. Σε απάντηση σε ένα μήνυμα που λαμβάνει, ένας actor μπορεί: να παίρνει τοπικές αποφάσεις, να δημιουργεί περισσότερους actors, να στέλνει περισσότερα μηνύματα και να καθορίζει πώς θα απαντήσει στο επόμενο μήνυμα που θα λάβει_.

**Περίπτωσεις χρήσης**: Αυτοματοποίηση δημιουργίας κώδικα, εργασίες ανάλυσης δεδομένων και κατασκευή προσαρμοσμένων agents για λειτουργίες σχεδιασμού και έρευνας.

Ακολουθούν μερικές βασικές έννοιες του AutoGen:

- **Agents**. Ένας agent είναι μια οντότητα λογισμικού που:
  - **Επικοινωνεί μέσω μηνυμάτων**, τα οποία μπορεί να είναι συγχρονισμένα ή ασύγχρονα.
  - **Διατηρεί την δική του κατάσταση**, η οποία μπορεί να τροποποιηθεί από εισερχόμενα μηνύματα.
  - **Εκτελεί ενέργειες** ως απάντηση σε ληφθέντα μηνύματα ή αλλαγές στην κατάστασή του. Αυτές οι ενέργειες μπορεί να τροποποιήσουν την κατάσταση του agent και να παράγουν εξωτερικά αποτελέσματα, όπως ενημέρωση αρχείων καταγραφής μηνυμάτων, αποστολή νέων μηνυμάτων, εκτέλεση κώδικα ή κλήσεις API.
    
  Εδώ έχετε ένα σύντομο απόσπασμα κώδικα όπου δημιουργείτε τον δικό σας agent με δυνατότητες συνομιλίας:

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
    
    Στον προηγούμενο κώδικα, το `MyAssistant` έχει δημιουργηθεί και κληρονομεί από το `RoutedAgent`. Διαθέτει έναν χειριστή μηνυμάτων που εκτυπώνει το περιεχόμενο του μηνύματος και στη συνέχεια στέλνει μια απάντηση χρησιμοποιώντας τον αντιπρόσωπο `AssistantAgent`. Ιδιαίτερα σημειώστε πώς αναθέτουμε στο `self._delegate` ένα στιγμιότυπο του `AssistantAgent`, που είναι ένας προ-κατασκευασμένος agent που μπορεί να χειριστεί ολοκληρώσεις συνομιλίας.

    Ας ενημερώσουμε το AutoGen για αυτόν τον τύπο agent και να ξεκινήσουμε το πρόγραμμα:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Στον προηγούμενο κώδικα, οι agents καταχωρούνται στο runtime και στη συνέχεια αποστέλλεται ένα μήνυμα στον agent, με αποτέλεσμα την ακόλουθη έξοδο:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Πολλαπλοί agents**. Το AutoGen υποστηρίζει τη δημιουργία πολλαπλών agents που μπορούν να συνεργαστούν για την επίτευξη σύνθετων εργασιών. Οι agents μπορούν να επικοινωνούν, να μοιράζονται πληροφορίες και να συντονίζουν τις ενέργειές τους για να λύσουν προβλήματα πιο αποτελεσματικά. Για να δημιουργήσετε ένα σύστημα πολλαπλών agents, μπορείτε να ορίσετε διαφορετικούς τύπους agents με εξειδικευμένες λειτουργίες και ρόλους, όπως ανάκτηση δεδομένων, ανάλυση, λήψη αποφάσεων και αλληλεπίδραση με τον χρήστη. Ας δούμε πώς μοιάζει μια τέτοια δημιουργία για να κατανοήσουμε καλύτερα:

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

    Στον προηγούμενο κώδικα έχουμε έναν `GroupChatManager` που είναι καταχωρημένος στο runtime. Αυτός ο διαχειριστής είναι υπεύθυνος για το συντονισμό των αλληλεπιδράσεων μεταξύ διαφορετικών τύπων agents, όπως συγγραφείς, εικονογράφους, επιμελητές και χρήστες.

- **Agent Runtime**. Το πλαίσιο παρέχει ένα περιβάλλον εκτέλεσης, επιτρέποντας την επικοινωνία μεταξύ των agents, διαχειρίζεται τις ταυτότητες και τον κύκλο ζωής τους, και επιβάλλει όρια ασφαλείας και ιδιωτικότητας. Αυτό σημαίνει ότι μπορείτε να εκτελείτε τους agents σας σε ένα ασφαλές και ελεγχόμενο περιβάλλον, διασφαλίζοντας ότι μπορούν να αλληλεπιδρούν με ασφάλεια και αποδοτικότητα. Υπάρχουν δύο περιβάλλοντα εκτέλεσης που αξίζει να αναφέρουμε:
  - **Αυτόνομο runtime**. Είναι μια καλή επιλογή για εφαρμογές μονής διεργασίας όπου όλοι οι agents υλοποιούνται στην ίδια γλώσσα προγραμματισμού και εκτελούνται στην ίδια διεργασία. Ακολουθεί μια απεικόνιση του πώς λειτουργεί:  

Στοίβα εφαρμογής

    *οι agents επικοινωνούν μέσω μηνυμάτων μέσω του runtime, και το runtime διαχειρίζεται τον κύκλο ζωής των agents*

  - **Κατανεμημένο runtime agent**, κατάλληλο για εφαρμογές πολλαπλών διεργασιών όπου οι agents μπορεί να υλοποιούνται σε διαφορετικές γλώσσες προγραμματισμού και να εκτελούνται σε διαφορετικές μηχανές. Ακολουθεί μια απεικόνιση του πώς λειτουργεί:  

## Semantic Kernel + Agent Framework

Το Semantic Kernel είναι ένα έτοιμο για επιχειρήσεις SDK ορχήστρωσης AI. Αποτελείται από συνδέσμους AI και μνήμης, μαζί με ένα Πλαίσιο Agent.

Ας καλύψουμε πρώτα μερικά βασικά στοιχεία:

- **AI Connectors**: Πρόκειται για μια διεπαφή με εξωτερικές υπηρεσίες AI και πηγές δεδομένων για χρήση τόσο σε Python όσο και σε C#.

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

    Εδώ έχετε ένα απλό παράδειγμα για το πώς μπορείτε να δημιουργήσετε έναν kernel και να προσθέσετε μια υπηρεσία ολοκλήρωσης συνομιλίας. Το Semantic Kernel δημιουργεί μια σύνδεση με μια εξωτερική υπηρεσία AI, σε αυτή την περίπτωση, την Azure OpenAI Chat Completion.

- **Plugins**: Αυτά ενσωματώνουν λειτουργίες που μπορεί να χρησιμοποιήσει μια εφαρμογή. Υπάρχουν έτοιμα plugins αλλά και προσαρμοσμένα που μπορείτε να δημιουργήσετε. Μια σχετική έννοια είναι οι "λειτουργίες prompt". Αντί να παρέχετε φυσικές γλωσσικές εντολές για την κλήση λειτουργιών, μεταδίδετε ορισμένες λειτουργίες στο μοντέλο. Βάσει του τρέχοντος πλαισίου συνομιλίας, το μοντέλο μπορεί να επιλέξει να καλέσει μία από αυτές τις λειτουργίες για να ολοκληρώσει ένα αίτημα ή ερώτημα. Να ένα παράδειγμα:

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

    Εδώ, έχετε πρώτα ένα πρότυπο prompt `skPrompt` που αφήνει χώρο για την είσοδο κειμένου από τον χρήστη, `$userInput`. Στη συνέχεια, δημιουργείτε τη λειτουργία kernel `SummarizeText` και την εισάγετε στον kernel με το όνομα plugin `SemanticFunctions`. Σημειώστε το όνομα της λειτουργίας που βοηθά το Semantic Kernel να καταλάβει τι κάνει η λειτουργία και πότε πρέπει να κληθεί.

- **Native function**: Υπάρχουν επίσης εγγενείς λειτουργίες που το πλαίσιο μπορεί να καλέσει απευθείας για να εκτελέσει την εργασία. Να ένα παράδειγμα μιας τέτοιας λειτουργίας που ανακτά το περιεχόμενο από ένα αρχείο:

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

- **Memory**: Αφαιρεί και απλοποιεί τη διαχείριση του πλαισίου για εφαρμογές AI. Η ιδέα με τη μνήμη είναι ότι πρόκειται για κάτι που το LLM πρέπει να γνωρίζει. Μπορείτε να αποθηκεύσετε αυτές τις πληροφορίες σε μια βάση δεδομένων διανυσμάτων, που καταλήγει να είναι μια βάση δεδομένων στη μνήμη ή μια βάση διανυσμάτων ή παρόμοια. Να ένα παράδειγμα ενός πολύ απλοποιημένου σεναρίου όπου *γεγονότα* προστίθενται στη μνήμη:

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

    Αυτά τα γεγονότα αποθηκεύονται στη συλλογή μνήμης `SummarizedAzureDocs`. Πρόκειται για ένα πολύ απλοποιημένο παράδειγμα, αλλά μπορείτε να δείτε πώς μπορείτε να αποθηκεύσετε πληροφορίες στη μνήμη για να τις χρησιμοποιήσει το LLM.
## Προηγούμενο Μάθημα

[Εισαγωγή στους AI Agents και Περιπτώσεις Χρήσης Agent](../01-intro-to-ai-agents/README.md)

## Επόμενο Μάθημα

[Κατανόηση των Agentic Design Patterns](../03-agentic-design-patterns/README.md)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.