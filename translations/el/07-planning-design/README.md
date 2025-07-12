<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:41:32+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "el"
}
-->
για μια γρήγορη επισκόπηση.

Το παρακάτω απόσπασμα Python δείχνει έναν απλό πράκτορα σχεδιασμού που διασπά έναν στόχο σε υποεργασίες και δημιουργεί ένα δομημένο σχέδιο:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.azure import AzureAIChatCompletionClient
from azure.core.credentials import AzureKeyCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

client = AzureAIChatCompletionClient(
    model="gpt-4o-mini",
    endpoint="https://models.inference.ai.azure.com",
    # To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
    # Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    model_info={
        "json_output": False,
        "function_calling": True,
        "vision": True,
        "family": "unknown",
    },
)

# Define the user message
messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
                      Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(
        content="Create a travel plan for a family of 2 kids from Singapore to Melboune", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": 'json_object'})

response_content: Optional[str] = response.content if isinstance(
    response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string" )

pprint(json.loads(response_content))

# # Ensure the response content is a valid JSON string before loading it
# response_content: Optional[str] = response.content if isinstance(
#     response.content, str) else None
# if response_content is None:
#     raise ValueError("Response content is not a valid JSON string")

# # Print the response content after loading it as JSON
# pprint(json.loads(response_content))

# Validate the response content with the MathReasoning model
# TravelPlan.model_validate(json.loads(response_content))
```

### Πράκτορας Σχεδιασμού με Ορχήστρωση Πολλαπλών Πρακτόρων

Σε αυτό το παράδειγμα, ένας Semantic Router Agent λαμβάνει ένα αίτημα χρήστη (π.χ., "Χρειάζομαι ένα σχέδιο ξενοδοχείου για το ταξίδι μου.").

Ο σχεδιαστής στη συνέχεια:

* Λαμβάνει το Σχέδιο Ξενοδοχείου: Ο σχεδιαστής παίρνει το μήνυμα του χρήστη και, βασιζόμενος σε ένα σύστημα προτροπής (που περιλαμβάνει λεπτομέρειες για τους διαθέσιμους πράκτορες), δημιουργεί ένα δομημένο ταξιδιωτικό σχέδιο.
* Καταγράφει τους Πράκτορες και τα Εργαλεία τους: Το μητρώο πρακτόρων κρατά μια λίστα πρακτόρων (π.χ., για πτήσεις, ξενοδοχεία, ενοικίαση αυτοκινήτου και δραστηριότητες) μαζί με τις λειτουργίες ή τα εργαλεία που προσφέρουν.
* Δρομολογεί το Σχέδιο στους Αντίστοιχους Πράκτορες: Ανάλογα με τον αριθμό των υποεργασιών, ο σχεδιαστής είτε στέλνει το μήνυμα απευθείας σε έναν αφιερωμένο πράκτορα (για σενάρια με μία εργασία) είτε συντονίζει μέσω ενός διαχειριστή ομαδικής συνομιλίας για συνεργασία πολλαπλών πρακτόρων.
* Συνοψίζει το Αποτέλεσμα: Τέλος, ο σχεδιαστής συνοψίζει το παραγόμενο σχέδιο για σαφήνεια.
Το παρακάτω δείγμα κώδικα Python απεικονίζει αυτά τα βήματα:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Travel SubTask Model

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # we want to assign the task to the agent

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient

# Create the client with type-checked environment variables

client = AzureOpenAIChatCompletionClient(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)

from pprint import pprint

# Define the user message

messages = [
    SystemMessage(content="""You are an planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
]

response = await client.create(messages=messages, extra_create_args={"response_format": TravelPlan})

# Ensure the response content is a valid JSON string before loading it

response_content: Optional[str] = response.content if isinstance(response.content, str) else None
if response_content is None:
    raise ValueError("Response content is not a valid JSON string")

# Print the response content after loading it as JSON

pprint(json.loads(response_content))
```

Ακολουθεί η έξοδος από τον προηγούμενο κώδικα και μπορείτε στη συνέχεια να χρησιμοποιήσετε αυτή τη δομημένη έξοδο για να δρομολογήσετε στον `assigned_agent` και να συνοψίσετε το ταξιδιωτικό σχέδιο στον τελικό χρήστη.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Ένα παράδειγμα σημειωματάριου με το προηγούμενο δείγμα κώδικα είναι διαθέσιμο [εδώ](../../../07-planning-design/07-autogen.ipynb).

### Επαναληπτικός Σχεδιασμός

Ορισμένες εργασίες απαιτούν αλληλεπίδραση ή επανασχεδιασμό, όπου το αποτέλεσμα μιας υποεργασίας επηρεάζει την επόμενη. Για παράδειγμα, αν ο πράκτορας ανακαλύψει ένα απρόσμενο μορφότυπο δεδομένων κατά την κράτηση πτήσεων, μπορεί να χρειαστεί να προσαρμόσει τη στρατηγική του πριν προχωρήσει στις κρατήσεις ξενοδοχείων.

Επιπλέον, η ανατροφοδότηση του χρήστη (π.χ. ένας άνθρωπος που αποφασίζει ότι προτιμά μια νωρίτερη πτήση) μπορεί να ενεργοποιήσει μερικό επανασχεδιασμό. Αυτή η δυναμική, επαναληπτική προσέγγιση διασφαλίζει ότι η τελική λύση ευθυγραμμίζεται με τους πραγματικούς περιορισμούς και τις εξελισσόμενες προτιμήσεις του χρήστη.

π.χ. δείγμα κώδικα

```python
from autogen_core.models import UserMessage, SystemMessage, AssistantMessage
#.. same as previous code and pass on the user history, current plan
messages = [
    SystemMessage(content="""You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests""", source="system"),
    UserMessage(content="Create a travel plan for a family of 2 kids from Singapore to Melbourne", source="user"),
    AssistantMessage(content=f"Previous travel plan - {TravelPlan}", source="assistant")
]
# .. re-plan and send the tasks to respective agents
```

Για πιο ολοκληρωμένο σχεδιασμό, ρίξτε μια ματιά στο Magnetic One

για την επίλυση σύνθετων εργασιών.

## Περίληψη

Σε αυτό το άρθρο εξετάσαμε ένα παράδειγμα για το πώς μπορούμε να δημιουργήσουμε έναν σχεδιαστή που μπορεί δυναμικά να επιλέγει τους διαθέσιμους ορισμένους πράκτορες. Η έξοδος του Σχεδιαστή διασπά τις εργασίες και αναθέτει τους πράκτορες ώστε να εκτελεστούν. Υποτίθεται ότι οι πράκτορες έχουν πρόσβαση στις λειτουργίες/εργαλεία που απαιτούνται για την εκτέλεση της εργασίας. Επιπλέον των πρακτόρων, μπορείτε να συμπεριλάβετε και άλλα μοτίβα όπως reflection, summarizer, και round robin chat για περαιτέρω προσαρμογή.

## Πρόσθετοι Πόροι

* AutoGen Magnetic One - Ένα γενικευμένο σύστημα πολλαπλών πρακτόρων για την επίλυση σύνθετων εργασιών που έχει επιτύχει εντυπωσιακά αποτελέσματα σε πολλαπλά απαιτητικά benchmarks πρακτόρων. Αναφορά:

. Σε αυτή την υλοποίηση, ο ορχηστρωτής δημιουργεί ένα σχέδιο ειδικό για την εργασία και αναθέτει αυτές τις εργασίες στους διαθέσιμους πράκτορες. Επιπλέον του σχεδιασμού, ο ορχηστρωτής χρησιμοποιεί και έναν μηχανισμό παρακολούθησης για να ελέγχει την πρόοδο της εργασίας και να επανασχεδιάζει όταν απαιτείται.

## Προηγούμενο Μάθημα

[Κατασκευή Αξιόπιστων Πρακτόρων Τεχνητής Νοημοσύνης](../06-building-trustworthy-agents/README.md)

## Επόμενο Μάθημα

[Μοτίβο Σχεδιασμού Πολλαπλών Πρακτόρων](../08-multi-agent/README.md)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.