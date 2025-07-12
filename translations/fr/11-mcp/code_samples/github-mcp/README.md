<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:19:32+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "fr"
}
-->
# Exemple de serveur Github MCP

## Description

Il s'agit d'une démo créée pour le Hackathon AI Agents organisé par le Microsoft Reactor.

Cet outil sert à recommander des projets de hackathon en se basant sur les dépôts Github d'un utilisateur.  
Cela se fait de la manière suivante :

1. **Github Agent** - Utilise le serveur Github MCP pour récupérer les dépôts et les informations associées.  
2. **Hackathon Agent** - Prend les données du Github Agent et génère des idées créatives de projets de hackathon en fonction des projets, des langages utilisés par l'utilisateur et des thématiques du hackathon AI Agents.  
3. **Events Agent** - En se basant sur les suggestions du hackathon agent, l’Events Agent recommande des événements pertinents issus de la série AI Agent Hackathon.  

## Exécution du code

### Variables d’environnement

Cette démo utilise Azure Open AI Service, Semantic Kernel, le serveur Github MCP et Azure AI Search.

Assurez-vous d’avoir configuré correctement les variables d’environnement nécessaires pour utiliser ces outils :

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Lancement du serveur Chainlit

Pour se connecter au serveur MCP, cette démo utilise Chainlit comme interface de chat.

Pour lancer le serveur, utilisez la commande suivante dans votre terminal :

```bash
chainlit run app.py -w
```

Cela devrait démarrer votre serveur Chainlit sur `localhost:8000` et remplir votre index Azure AI Search avec le contenu de `event-descriptions.md`.

## Connexion au serveur MCP

Pour vous connecter au serveur Github MCP, cliquez sur l’icône « prise » sous la zone de saisie « Tapez votre message ici... » :

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.fr.png)

Ensuite, cliquez sur « Connect an MCP » pour ajouter la commande de connexion au serveur Github MCP :

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Remplacez "[YOUR PERSONAL ACCESS TOKEN]" par votre véritable jeton d’accès personnel.

Une fois connecté, vous devriez voir un (1) à côté de l’icône de la prise pour confirmer la connexion. Sinon, essayez de redémarrer le serveur chainlit avec `chainlit run app.py -w`.

## Utilisation de la démo

Pour lancer le workflow de recommandation de projets de hackathon, vous pouvez taper un message comme :

« Recommande des projets de hackathon pour l’utilisateur Github koreyspace »

Le Router Agent analysera votre demande et déterminera la meilleure combinaison d’agents (GitHub, Hackathon et Events) pour traiter votre requête. Les agents collaborent pour fournir des recommandations complètes basées sur l’analyse des dépôts GitHub, la génération d’idées de projets et les événements tech pertinents.

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.