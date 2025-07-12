<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:19:39+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "es"
}
-->
# Ejemplo de Servidor MCP de Github

## Descripción

Esta fue una demo creada para el AI Agents Hackathon organizado a través de Microsoft Reactor.

La herramienta se utiliza para recomendar proyectos de hackathon basados en los repositorios de Github de un usuario.  
Esto se realiza mediante:

1. **Github Agent** - Utiliza el Github MCP Server para obtener repositorios e información sobre esos repositorios.  
2. **Hackathon Agent** - Toma los datos del Github Agent y genera ideas creativas de proyectos para hackathon basándose en los proyectos, los lenguajes usados por el usuario y las categorías del AI Agents hackathon.  
3. **Events Agent** - Basándose en la sugerencia del hackathon agent, el events agent recomendará eventos relevantes de la serie AI Agent Hackathon.  

## Ejecutando el código

### Variables de Entorno

Esta demo usa Azure Open AI Service, Semantic Kernel, el Github MCP Server y Azure AI Search.

Asegúrate de tener configuradas las variables de entorno adecuadas para usar estas herramientas:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Ejecutando el Servidor Chainlit

Para conectarse al MCP server, esta demo usa Chainlit como interfaz de chat.

Para iniciar el servidor, usa el siguiente comando en tu terminal:

```bash
chainlit run app.py -w
```

Esto debería iniciar tu servidor Chainlit en `localhost:8000` y además poblar tu índice de Azure AI Search con el contenido de `event-descriptions.md`.

## Conectándose al MCP Server

Para conectarte al Github MCP Server, selecciona el ícono de "enchufe" debajo del cuadro de chat "Type your message here..":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.es.png)

Desde ahí puedes hacer clic en "Connect an MCP" para agregar el comando que conecta con el Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Reemplaza "[YOUR PERSONAL ACCESS TOKEN]" con tu token de acceso personal real.

Después de conectarte, deberías ver un (1) junto al ícono del enchufe para confirmar que está conectado. Si no, intenta reiniciar el servidor chainlit con `chainlit run app.py -w`.

## Usando la Demo

Para iniciar el flujo de trabajo del agente que recomienda proyectos para hackathon, puedes escribir un mensaje como:

"Recommend hackathon projects for the Github user koreyspace"

El Router Agent analizará tu solicitud y determinará qué combinación de agentes (GitHub, Hackathon y Events) es la más adecuada para manejar tu consulta. Los agentes trabajan juntos para ofrecer recomendaciones completas basadas en el análisis de repositorios de GitHub, generación de ideas para proyectos y eventos tecnológicos relevantes.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.