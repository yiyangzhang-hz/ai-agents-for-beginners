<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:22:31+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "el"
}
-->
# Παράδειγμα Github MCP Server

## Περιγραφή

Αυτή ήταν μια επίδειξη που δημιουργήθηκε για το AI Agents Hackathon που διοργανώθηκε μέσω του Microsoft Reactor.

Το εργαλείο χρησιμοποιείται για να προτείνει έργα hackathon βασισμένα στα αποθετήρια Github ενός χρήστη.  
Αυτό γίνεται με:

1. **Github Agent** - Χρησιμοποιώντας τον Github MCP Server για την ανάκτηση αποθετηρίων και πληροφοριών σχετικά με αυτά.
2. **Hackathon Agent** - Λαμβάνει τα δεδομένα από τον Github Agent και προτείνει δημιουργικές ιδέες για έργα hackathon βασισμένες στα έργα, τις γλώσσες που χρησιμοποιεί ο χρήστης και τις κατηγορίες έργων του AI Agents hackathon.
3. **Events Agent** - Βάσει της πρότασης του hackathon agent, ο events agent προτείνει σχετικά events από τη σειρά AI Agent Hackathon.

## Εκτέλεση του κώδικα

### Μεταβλητές Περιβάλλοντος

Αυτή η επίδειξη χρησιμοποιεί το Azure Open AI Service, Semantic Kernel, τον Github MCP Server και το Azure AI Search.

Βεβαιωθείτε ότι έχετε ορίσει σωστά τις μεταβλητές περιβάλλοντος για να χρησιμοποιήσετε αυτά τα εργαλεία:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Εκκίνηση του Chainlit Server

Για να συνδεθείτε με τον MCP server, αυτή η επίδειξη χρησιμοποιεί το Chainlit ως διεπαφή συνομιλίας.

Για να εκκινήσετε τον server, χρησιμοποιήστε την παρακάτω εντολή στο τερματικό σας:

```bash
chainlit run app.py -w
```

Αυτό θα ξεκινήσει τον Chainlit server στο `localhost:8000` και θα γεμίσει το Azure AI Search Index με το περιεχόμενο του `event-descriptions.md`.

## Σύνδεση με τον MCP Server

Για να συνδεθείτε με τον Github MCP Server, επιλέξτε το εικονίδιο "πρίζας" κάτω από το πλαίσιο συνομιλίας "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.el.png)

Από εκεί, μπορείτε να κάνετε κλικ στο "Connect an MCP" για να προσθέσετε την εντολή σύνδεσης με τον Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Αντικαταστήστε το "[YOUR PERSONAL ACCESS TOKEN]" με το πραγματικό σας Personal Access Token.

Μετά τη σύνδεση, θα πρέπει να δείτε έναν αριθμό (1) δίπλα στο εικονίδιο της πρίζας για να επιβεβαιώσετε ότι η σύνδεση έγινε. Αν όχι, δοκιμάστε να επανεκκινήσετε τον chainlit server με την εντολή `chainlit run app.py -w`.

## Χρήση της Επίδειξης

Για να ξεκινήσετε τη ροή εργασίας του agent που προτείνει έργα hackathon, μπορείτε να πληκτρολογήσετε ένα μήνυμα όπως:

"Recommend hackathon projects for the Github user koreyspace"

Ο Router Agent θα αναλύσει το αίτημά σας και θα καθορίσει ποιος συνδυασμός agents (GitHub, Hackathon, και Events) είναι ο καταλληλότερος για να χειριστεί το ερώτημά σας. Οι agents συνεργάζονται για να παρέχουν ολοκληρωμένες προτάσεις βασισμένες στην ανάλυση αποθετηρίων GitHub, την ιδέα έργων και σχετικά τεχνολογικά events.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.