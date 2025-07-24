<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c6a79c8f2b56a80370ff7e447765524f",
  "translation_date": "2025-07-23T08:06:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "es"
}
-->
# Configuración del Curso

## Introducción

Esta lección cubrirá cómo ejecutar los ejemplos de código de este curso.

## Clonar o Hacer Fork de este Repositorio

Para comenzar, por favor clona o haz un fork del repositorio de GitHub. Esto te permitirá tener tu propia versión del material del curso para que puedas ejecutar, probar y modificar el código.

Esto se puede hacer haciendo clic en el enlace a

Deberías tener ahora tu propia versión del curso en el siguiente enlace:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.es.png)

## Ejecutar el Código

Este curso ofrece una serie de Jupyter Notebooks que puedes ejecutar para obtener experiencia práctica construyendo Agentes de IA.

Los ejemplos de código utilizan:

**Requiere una cuenta de GitHub - Gratis**:

1) Framework Semantic Kernel Agent + GitHub Models Marketplace. Etiquetado como (semantic-kernel.ipynb)
2) Framework AutoGen + GitHub Models Marketplace. Etiquetado como (autogen.ipynb)

**Requiere una suscripción a Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Etiquetado como (azureaiagent.ipynb)

Te animamos a probar los tres tipos de ejemplos para ver cuál funciona mejor para ti.

La opción que elijas determinará los pasos de configuración que debes seguir a continuación:

## Requisitos

- Python 3.12+
  - **NOTE**: Si no tienes Python 3.12 instalado, asegúrate de instalarlo. Luego crea tu entorno virtual usando python3.12 para garantizar que se instalen las versiones correctas desde el archivo requirements.txt.
- Una cuenta de GitHub - Para acceder al GitHub Models Marketplace
- Suscripción a Azure - Para acceder a Azure AI Foundry
- Cuenta de Azure AI Foundry - Para acceder al Azure AI Agent Service

Hemos incluido un archivo `requirements.txt` en la raíz de este repositorio que contiene todos los paquetes de Python necesarios para ejecutar los ejemplos de código.

Puedes instalarlos ejecutando el siguiente comando en tu terminal en la raíz del repositorio:

```bash
pip install -r requirements.txt
```
Recomendamos crear un entorno virtual de Python para evitar conflictos y problemas.

## Configurar VSCode
Asegúrate de estar utilizando la versión correcta de Python en VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuración para Ejemplos usando GitHub Models 

### Paso 1: Obtener tu Token de Acceso Personal (PAT) de GitHub

Este curso utiliza el GitHub Models Marketplace, que proporciona acceso gratuito a Modelos de Lenguaje Extenso (LLMs) que usarás para construir Agentes de IA.

Para usar los modelos de GitHub, necesitarás crear un [Token de Acceso Personal de GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Esto se puede hacer accediendo a tu

Cuenta de GitHub.

Por favor, sigue el [Principio de Menor Privilegio](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) al crear tu token. Esto significa que solo debes otorgar al token los permisos necesarios para ejecutar los ejemplos de código de este curso.

1. Selecciona la opción `Fine-grained tokens` en el lado izquierdo de tu pantalla.

    Luego selecciona `Generate new token`.

    ![Generate Token](../../../translated_images/generate-new-token.8772e24e8e2e067f2e6742500eaf68bb5c5f8999537bd79a040d2ecc09c7fdcb.es.png)

1. Ingresa un nombre descriptivo para tu token que refleje su propósito, facilitando su identificación más adelante. Establece una fecha de expiración (recomendado: 30 días; puedes elegir un período más corto como 7 días si prefieres una postura más segura).

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.es.png)

1. Limita el alcance del token a tu fork de este repositorio.

    ![Limit scope to fork repository](../../../translated_images/select-fork-repository.4497f6bb05ccd6b474ed134493a815fc34f94f89db2b1630c494adff7b5b558a.es.png)

1. Restringe los permisos del token: Bajo **Permissions**, activa **Account Permissions**, navega a **Models** y habilita solo el acceso de lectura necesario para los modelos de GitHub.

    ![Account Permissions](../../../translated_images/account-permissions.de1806fad33a72c6194d2688cf2c10f2adb9ff7a5c1041a2329cbef46bffbba0.es.png)

    ![Models Read Access](../../../translated_images/models-read-access.c00bc44e28c40450a85542e19f8e8c68284c71861c076b7dbc078b4c7e51faa6.es.png)

Copia tu nuevo token que acabas de crear. Ahora lo agregarás a tu archivo `.env` incluido en este curso.

### Paso 2: Crear tu archivo `.env`

Para crear tu archivo `.env`, ejecuta el siguiente comando en tu terminal.

```bash
cp .env.example .env
```

Esto copiará el archivo de ejemplo y creará un `.env` en tu directorio donde llenarás los valores de las variables de entorno.

Con tu token copiado, abre el archivo `.env` en tu editor de texto favorito y pega tu token en el campo `GITHUB_TOKEN`.

Ahora deberías poder ejecutar los ejemplos de código de este curso.

## Configuración para Ejemplos usando Azure AI Foundry y Azure AI Agent Service

### Paso 1: Obtener tu Endpoint de Proyecto de Azure

Sigue los pasos para crear un hub y proyecto en Azure AI Foundry que se encuentran aquí: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Una vez que hayas creado tu proyecto, necesitarás obtener la cadena de conexión para tu proyecto.

Esto se puede hacer accediendo a la página **Overview** de tu proyecto en el portal de Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.es.png)

### Paso 2: Crear tu archivo `.env`

Para crear tu archivo `.env`, ejecuta el siguiente comando en tu terminal.

```bash
cp .env.example .env
```

Esto copiará el archivo de ejemplo y creará un `.env` en tu directorio donde llenarás los valores de las variables de entorno.

Con tu token copiado, abre el archivo `.env` en tu editor de texto favorito y pega tu token en el campo `PROJECT_ENDPOINT`.

### Paso 3: Iniciar sesión en Azure

Como una práctica de seguridad, utilizaremos [autenticación sin claves](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) para autenticarnos en Azure OpenAI con Microsoft Entra ID.

A continuación, abre un terminal y ejecuta `az login --use-device-code` para iniciar sesión en tu cuenta de Azure.

Una vez que hayas iniciado sesión, selecciona tu suscripción en el terminal.

## Variables de Entorno Adicionales - Azure Search y Azure OpenAI 

Para la lección Agentic RAG - Lección 5 - hay ejemplos que utilizan Azure Search y Azure OpenAI.

Si deseas ejecutar estos ejemplos, necesitarás agregar las siguientes variables de entorno a tu archivo `.env`:

### Página de Resumen (Proyecto)

- `AZURE_SUBSCRIPTION_ID` - Revisa **Project details** en la página **Overview** de tu proyecto.

- `AZURE_AI_PROJECT_NAME` - Mira la parte superior de la página **Overview** de tu proyecto.

- `AZURE_OPENAI_SERVICE` - Encuentra esto en la pestaña **Included capabilities** para **Azure OpenAI Service** en la página **Overview**.

### Centro de Gestión

- `AZURE_OPENAI_RESOURCE_GROUP` - Ve a **Project properties** en la página **Overview** del **Management Center**.

- `GLOBAL_LLM_SERVICE` - Bajo **Connected resources**, encuentra el nombre de conexión de **Azure AI Services**. Si no está listado, revisa el **Azure portal** bajo tu grupo de recursos para el nombre del recurso de AI Services.

### Página de Modelos + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecciona tu modelo de embedding (por ejemplo, `text-embedding-ada-002`) y toma nota del **Deployment name** de los detalles del modelo.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecciona tu modelo de chat (por ejemplo, `gpt-4o-mini`) y toma nota del **Deployment name** de los detalles del modelo.

### Portal de Azure

- `AZURE_OPENAI_ENDPOINT` - Busca **Azure AI services**, haz clic en él, luego ve a **Resource Management**, **Keys and Endpoint**, desplázate hacia abajo hasta los "Azure OpenAI endpoints" y copia el que dice "Language APIs".

- `AZURE_OPENAI_API_KEY` - Desde la misma pantalla, copia KEY 1 o KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Encuentra tu recurso **Azure AI Search**, haz clic en él y ve a **Overview**.

- `AZURE_SEARCH_API_KEY` - Luego ve a **Settings** y luego a **Keys** para copiar la clave de administrador primaria o secundaria.

### Página Externa

- `AZURE_OPENAI_API_VERSION` - Visita la página [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) bajo **Latest GA API release**.

### Configurar autenticación sin claves

En lugar de codificar tus credenciales, utilizaremos una conexión sin claves con Azure OpenAI. Para hacerlo, importaremos `DefaultAzureCredential` y luego llamaremos a la función `DefaultAzureCredential` para obtener la credencial.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ¿Atascado en algún lugar?

Si tienes algún problema ejecutando esta configuración, únete a nuestro

## Próxima Lección

Ahora estás listo para ejecutar el código de este curso. ¡Feliz aprendizaje sobre el mundo de los Agentes de IA!

[Introducción a los Agentes de IA y Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.