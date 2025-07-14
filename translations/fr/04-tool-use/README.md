<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "88258b03f2893aa2e69eb8fb24baabbc",
  "translation_date": "2025-07-12T09:22:03+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "fr"
}
-->
[![Comment concevoir de bons agents IA](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.fr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Cliquez sur l’image ci-dessus pour visionner la vidéo de cette leçon)_

# Modèle de conception d’utilisation d’outils

Les outils sont intéressants car ils permettent aux agents IA d’avoir un éventail plus large de capacités. Au lieu que l’agent dispose d’un ensemble limité d’actions, l’ajout d’un outil lui permet désormais d’exécuter une grande variété d’actions. Dans ce chapitre, nous allons explorer le modèle de conception d’utilisation d’outils, qui décrit comment les agents IA peuvent utiliser des outils spécifiques pour atteindre leurs objectifs.

## Introduction

Dans cette leçon, nous cherchons à répondre aux questions suivantes :

- Qu’est-ce que le modèle de conception d’utilisation d’outils ?
- Dans quels cas d’usage peut-il être appliqué ?
- Quels sont les éléments/blocs de construction nécessaires pour implémenter ce modèle ?
- Quelles sont les considérations particulières pour utiliser ce modèle afin de créer des agents IA fiables ?

## Objectifs d’apprentissage

À l’issue de cette leçon, vous serez capable de :

- Définir le modèle de conception d’utilisation d’outils et son objectif.
- Identifier les cas d’usage où ce modèle est applicable.
- Comprendre les éléments clés nécessaires à son implémentation.
- Reconnaître les considérations pour garantir la fiabilité des agents IA utilisant ce modèle.

## Qu’est-ce que le modèle de conception d’utilisation d’outils ?

Le **modèle de conception d’utilisation d’outils** vise à donner aux LLM la capacité d’interagir avec des outils externes pour atteindre des objectifs spécifiques. Les outils sont des codes exécutables par un agent pour réaliser des actions. Un outil peut être une fonction simple comme une calculatrice, ou un appel API vers un service tiers, par exemple pour consulter le cours d’une action ou la météo. Dans le contexte des agents IA, les outils sont conçus pour être exécutés en réponse à des **appels de fonction générés par le modèle**.

## Dans quels cas d’usage peut-il être appliqué ?

Les agents IA peuvent exploiter des outils pour accomplir des tâches complexes, récupérer des informations ou prendre des décisions. Le modèle d’utilisation d’outils est souvent utilisé dans des scénarios nécessitant une interaction dynamique avec des systèmes externes, tels que des bases de données, des services web ou des interprètes de code. Cette capacité est utile pour plusieurs cas d’usage, notamment :

- **Récupération dynamique d’informations :** Les agents peuvent interroger des API externes ou des bases de données pour obtenir des données à jour (par exemple, interroger une base SQLite pour une analyse de données, récupérer des cours boursiers ou des prévisions météo).
- **Exécution et interprétation de code :** Les agents peuvent exécuter du code ou des scripts pour résoudre des problèmes mathématiques, générer des rapports ou réaliser des simulations.
- **Automatisation de flux de travail :** Automatiser des processus répétitifs ou multi-étapes en intégrant des outils comme des planificateurs de tâches, des services de messagerie ou des pipelines de données.
- **Support client :** Les agents peuvent interagir avec des systèmes CRM, des plateformes de tickets ou des bases de connaissances pour répondre aux demandes des utilisateurs.
- **Génération et édition de contenu :** Les agents peuvent utiliser des outils comme des correcteurs grammaticaux, des résumeurs de texte ou des évaluateurs de sécurité de contenu pour aider à la création de contenu.

## Quels sont les éléments/blocs de construction nécessaires pour implémenter le modèle d’utilisation d’outils ?

Ces blocs de construction permettent à l’agent IA d’exécuter une large gamme de tâches. Voici les éléments clés nécessaires pour implémenter le modèle d’utilisation d’outils :

- **Schémas de fonctions/outils** : Définitions détaillées des outils disponibles, incluant le nom de la fonction, son objectif, les paramètres requis et les résultats attendus. Ces schémas permettent au LLM de comprendre quels outils sont disponibles et comment formuler des requêtes valides.

- **Logique d’exécution des fonctions** : Gère comment et quand les outils sont invoqués en fonction de l’intention de l’utilisateur et du contexte de la conversation. Cela peut inclure des modules de planification, des mécanismes de routage ou des flux conditionnels qui déterminent dynamiquement l’utilisation des outils.

- **Système de gestion des messages** : Composants qui gèrent le flux conversationnel entre les entrées utilisateur, les réponses du LLM, les appels aux outils et les résultats retournés.

- **Cadre d’intégration des outils** : Infrastructure qui connecte l’agent aux différents outils, qu’il s’agisse de fonctions simples ou de services externes complexes.

- **Gestion des erreurs et validation** : Mécanismes pour gérer les échecs d’exécution des outils, valider les paramètres et traiter les réponses inattendues.

- **Gestion de l’état** : Suit le contexte de la conversation, les interactions précédentes avec les outils et les données persistantes pour assurer la cohérence sur plusieurs échanges.

Passons maintenant à un examen plus détaillé de l’appel de fonctions/outils.

### Appel de fonctions/outils

L’appel de fonctions est le principal moyen permettant aux Large Language Models (LLM) d’interagir avec des outils. Vous verrez souvent les termes « fonction » et « outil » utilisés de manière interchangeable, car les « fonctions » (blocs de code réutilisables) sont les « outils » que les agents utilisent pour accomplir des tâches. Pour qu’un code de fonction soit invoqué, un LLM doit comparer la requête de l’utilisateur avec la description des fonctions. Pour cela, un schéma contenant les descriptions de toutes les fonctions disponibles est envoyé au LLM. Le LLM sélectionne alors la fonction la plus appropriée pour la tâche et retourne son nom ainsi que ses arguments. La fonction sélectionnée est invoquée, sa réponse est renvoyée au LLM, qui utilise cette information pour répondre à la requête de l’utilisateur.

Pour que les développeurs puissent implémenter l’appel de fonctions pour les agents, il faut :

1. Un modèle LLM qui supporte l’appel de fonctions
2. Un schéma contenant les descriptions des fonctions
3. Le code de chaque fonction décrite

Prenons l’exemple de l’obtention de l’heure actuelle dans une ville pour illustrer :

1. **Initialiser un LLM qui supporte l’appel de fonctions :**

    Tous les modèles ne supportent pas l’appel de fonctions, il est donc important de vérifier que le LLM utilisé le fait. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> supporte l’appel de fonctions. Nous pouvons commencer par initialiser le client Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Créer un schéma de fonction :**

    Ensuite, nous définirons un schéma JSON contenant le nom de la fonction, la description de ce qu’elle fait, ainsi que les noms et descriptions des paramètres. Nous passerons ensuite ce schéma au client créé précédemment, avec la requête utilisateur pour obtenir l’heure à San Francisco. Il est important de noter qu’un **appel d’outil** est ce qui est retourné, **pas** la réponse finale à la question. Comme mentionné plus tôt, le LLM retourne le nom de la fonction sélectionnée pour la tâche, ainsi que les arguments qui lui seront passés.

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Le code de la fonction nécessaire pour réaliser la tâche :**

    Maintenant que le LLM a choisi la fonction à exécuter, le code qui réalise la tâche doit être implémenté et exécuté. Nous pouvons écrire le code pour obtenir l’heure actuelle en Python. Il faudra aussi écrire le code pour extraire le nom et les arguments de la réponse afin d’obtenir le résultat final.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

    ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

    ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

L’appel de fonctions est au cœur de la plupart, sinon de tous, les modèles d’utilisation d’outils pour agents, mais l’implémenter de zéro peut parfois être complexe. Comme nous l’avons vu dans [Leçon 2](../../../02-explore-agentic-frameworks), les frameworks agentiques nous fournissent des blocs de construction préfabriqués pour implémenter l’utilisation d’outils.

## Exemples d’utilisation d’outils avec des frameworks agentiques

Voici quelques exemples d’implémentation du modèle d’utilisation d’outils avec différents frameworks agentiques :

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> est un framework IA open source pour les développeurs .NET, Python et Java travaillant avec des Large Language Models (LLM). Il simplifie l’utilisation de l’appel de fonctions en décrivant automatiquement vos fonctions et leurs paramètres au modèle via un processus appelé <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">sérialisation</a>. Il gère également la communication bidirectionnelle entre le modèle et votre code. Un autre avantage d’utiliser un framework agentique comme Semantic Kernel est qu’il permet d’accéder à des outils préconstruits comme <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> et <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Le schéma suivant illustre le processus d’appel de fonctions avec Semantic Kernel :

![appel de fonction](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.fr.png)

Dans Semantic Kernel, les fonctions/outils sont appelés <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Nous pouvons transformer la fonction `get_current_time` vue précédemment en plugin en la convertissant en classe contenant la fonction. Nous pouvons aussi importer le décorateur `kernel_function`, qui prend en paramètre la description de la fonction. Lorsque vous créez un kernel avec GetCurrentTimePlugin, le kernel sérialise automatiquement la fonction et ses paramètres, créant ainsi le schéma à envoyer au LLM.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> est un framework agentique récent conçu pour permettre aux développeurs de créer, déployer et faire évoluer des agents IA de haute qualité et extensibles, sans avoir à gérer les ressources de calcul et de stockage sous-jacentes. Il est particulièrement adapté aux applications d’entreprise car il s’agit d’un service entièrement managé avec une sécurité de niveau entreprise.

Comparé au développement direct avec l’API LLM, Azure AI Agent Service offre plusieurs avantages, notamment :

- Appel automatique des outils – plus besoin d’analyser un appel d’outil, d’invoquer l’outil et de gérer la réponse ; tout cela est désormais pris en charge côté serveur
- Gestion sécurisée des données – au lieu de gérer vous-même l’état de la conversation, vous pouvez vous appuyer sur les threads pour stocker toutes les informations nécessaires
- Outils prêts à l’emploi – des outils pour interagir avec vos sources de données, comme Bing, Azure AI Search et Azure Functions.

Les outils disponibles dans Azure AI Agent Service se divisent en deux catégories :

1. Outils de connaissance :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Intégration avec Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Outils d’action :
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Appel de fonctions</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Outils définis par OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Le Agent Service nous permet d’utiliser ces outils ensemble sous forme de `toolset`. Il utilise également des `threads` qui conservent l’historique des messages d’une conversation donnée.

Imaginez que vous êtes un commercial chez Contoso. Vous souhaitez développer un agent conversationnel capable de répondre aux questions sur vos données de vente.

L’image suivante illustre comment vous pourriez utiliser Azure AI Agent Service pour analyser vos données de vente :

![Agentic Service en action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.fr.jpg)

Pour utiliser ces outils avec le service, nous pouvons créer un client et définir un outil ou un ensemble d’outils. Pour implémenter cela concrètement, nous pouvons utiliser le code Python suivant. Le LLM pourra examiner le toolset et décider d’utiliser la fonction créée par l’utilisateur, `fetch_sales_data_using_sqlite_query`, ou l’interpréteur de code préconstruit selon la requête de l’utilisateur.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Quelles sont les considérations particulières pour utiliser le modèle d’utilisation d’outils afin de créer des agents IA fiables ?

Une préoccupation courante concernant le SQL généré dynamiquement par les LLM est la sécurité, notamment le risque d’injection SQL ou d’actions malveillantes, comme la suppression ou la modification de la base de données. Bien que ces préoccupations soient légitimes, elles peuvent être efficacement atténuées en configurant correctement les permissions d’accès à la base de données. Pour la plupart des bases, cela consiste à configurer la base en lecture seule. Pour des services de bases de données comme PostgreSQL ou Azure SQL, l’application doit se voir attribuer un rôle en lecture seule (SELECT).

Exécuter l’application dans un environnement sécurisé renforce encore la protection. Dans les scénarios d’entreprise, les données sont généralement extraites et transformées depuis les systèmes opérationnels vers une base de données ou un entrepôt de données en lecture seule avec un schéma adapté à l’utilisateur. Cette approche garantit que les données sont sécurisées, optimisées pour la performance et l’accessibilité, et que l’application dispose d’un accès restreint en lecture seule.

## Ressources supplémentaires

-
<a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">
Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Atelier Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutoriel sur l’Appel de Fonction dans Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpréteur de Code Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Outils Autogen</a>

## Leçon précédente

[Comprendre les modèles de conception agentique](../03-agentic-design-patterns/README.md)

## Leçon suivante

[Agentic RAG](../05-agentic-rag/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.