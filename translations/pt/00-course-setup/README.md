<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:48:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "pt"
}
-->
Deve agora ter a sua própria versão forkada deste curso no seguinte link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.pt.png)

## Executar o Código

Este curso oferece uma série de Jupyter Notebooks que pode executar para obter experiência prática na construção de Agentes de IA.

Os exemplos de código utilizam:

**Requer Conta GitHub - Gratuito**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Identificado como (semantic-kernel.ipynb)  
2) AutoGen Framework + GitHub Models Marketplace. Identificado como (autogen.ipynb)

**Requer Subscrição Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. Identificado como (azureaiagent.ipynb)

Encorajamos a experimentar os três tipos de exemplos para ver qual funciona melhor para si.

A opção que escolher determinará os passos de configuração que deverá seguir abaixo:

## Requisitos

- Python 3.12+  
  - **NOTA**: Se não tiver o Python 3.12 instalado, certifique-se de instalá-lo. Depois crie o seu ambiente virtual usando python3.12 para garantir que as versões corretas são instaladas a partir do ficheiro requirements.txt.  
- Conta GitHub - Para acesso ao GitHub Models Marketplace  
- Subscrição Azure - Para acesso ao Azure AI Foundry  
- Conta Azure AI Foundry - Para acesso ao Azure AI Agent Service  

Incluímos um ficheiro `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Pode instalá-los executando o seguinte comando no terminal, na raiz do repositório:

```bash
pip install -r requirements.txt
```  
Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configurar VSCode  
Certifique-se de que está a usar a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuração para Exemplos que Usam GitHub Models

### Passo 1: Obter o Seu Token de Acesso Pessoal (PAT) do GitHub

Atualmente, este curso utiliza o GitHub Models Marketplace para oferecer acesso gratuito a Large Language Models (LLMs) que serão usados para criar Agentes de IA.

Para aceder a este serviço, precisará de criar um Token de Acesso Pessoal no GitHub.

Isto pode ser feito na sua conta GitHub.

Selecione a opção `Fine-grained tokens` no lado esquerdo do ecrã.

Depois selecione `Generate new token`.

![Generate Token](../../../translated_images/generate-token.9748d7585dd004cb4119b5aac724baff49c3a85791701b5e8ba3274b037c5b66.pt.png)

Será solicitado que insira um nome para o seu token, selecione a data de expiração (Recomendado: 30 Dias) e selecione os escopos para o seu token (Repositórios Públicos).

É também necessário editar as permissões deste token: Permissions -> Models -> Permite acesso aos GitHub Models

Copie o seu novo token que acabou de criar. Agora irá adicioná-lo ao seu ficheiro `.env` incluído neste curso.

### Passo 2: Criar o Seu Ficheiro `.env`

Para criar o seu ficheiro `.env` execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isto irá copiar o ficheiro de exemplo e criar um `.env` no seu diretório, onde preencherá os valores das variáveis de ambiente.

Com o token copiado, abra o ficheiro `.env` no seu editor de texto preferido e cole o token no campo `GITHUB_TOKEN`.

Deverá agora conseguir executar os exemplos de código deste curso.

## Configuração para Exemplos que Usam Azure AI Foundry e Azure AI Agent Service

### Passo 1: Obter o Endpoint do Seu Projeto Azure

Siga os passos para criar um hub e projeto no Azure AI Foundry encontrados aqui: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Depois de criar o seu projeto, precisará de obter a string de ligação do seu projeto.

Isto pode ser feito na página **Overview** do seu projeto no portal Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.pt.png)

### Passo 2: Criar o Seu Ficheiro `.env`

Para criar o seu ficheiro `.env` execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isto irá copiar o ficheiro de exemplo e criar um `.env` no seu diretório, onde preencherá os valores das variáveis de ambiente.

Com o token copiado, abra o ficheiro `.env` no seu editor de texto preferido e cole o token no campo `PROJECT_ENDPOINT`.

### Passo 3: Iniciar Sessão no Azure

Como boa prática de segurança, vamos usar [autenticação sem chave](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) para autenticar no Azure OpenAI com Microsoft Entra ID. Antes de o fazer, precisará de instalar a **Azure CLI** conforme as [instruções de instalação](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) para o seu sistema operativo.

De seguida, abra um terminal e execute `az login --use-device-code` para iniciar sessão na sua conta Azure.

Depois de iniciar sessão, selecione a sua subscrição no terminal.

## Variáveis de Ambiente Adicionais - Azure Search e Azure OpenAI

Para a Aula Agentic RAG - Aula 5 - existem exemplos que usam Azure Search e Azure OpenAI.

Se quiser executar estes exemplos, terá de adicionar as seguintes variáveis de ambiente ao seu ficheiro `.env`:

### Página Overview (Projeto)

- `AZURE_SUBSCRIPTION_ID` - Verifique os **Detalhes do Projeto** na página **Overview** do seu projeto.

- `AZURE_AI_PROJECT_NAME` - Veja no topo da página **Overview** do seu projeto.

- `AZURE_OPENAI_SERVICE` - Encontre na aba **Included capabilities** para **Azure OpenAI Service** na página **Overview**.

### Centro de Gestão

- `AZURE_OPENAI_RESOURCE_GROUP` - Vá a **Propriedades do Projeto** na página **Overview** do **Centro de Gestão**.

- `GLOBAL_LLM_SERVICE` - Em **Recursos ligados**, encontre o nome da ligação **Azure AI Services**. Se não estiver listado, verifique no **portal Azure** no seu grupo de recursos pelo nome do recurso AI Services.

### Página Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecione o seu modelo de embedding (ex.: `text-embedding-ada-002`) e anote o **Nome do deployment** nos detalhes do modelo.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecione o seu modelo de chat (ex.: `gpt-4o-mini`) e anote o **Nome do deployment** nos detalhes do modelo.

### Portal Azure

- `AZURE_OPENAI_ENDPOINT` - Procure por **Azure AI services**, clique, depois vá a **Gestão de Recursos**, **Chaves e Endpoint**, desça até aos "Azure OpenAI endpoints" e copie o que diz "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na mesma página, copie a CHAVE 1 ou CHAVE 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Encontre o seu recurso **Azure AI Search**, clique e veja a **Overview**.

- `AZURE_SEARCH_API_KEY` - Depois vá a **Configurações** e depois **Chaves** para copiar a chave administrativa primária ou secundária.

### Página Externa

- `AZURE_OPENAI_API_VERSION` - Visite a página [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) em **Latest GA API release**.

### Configurar autenticação sem chave

Em vez de codificar as suas credenciais, vamos usar uma ligação sem chave com Azure OpenAI. Para isso, vamos importar `DefaultAzureCredential` e depois chamar a função `DefaultAzureCredential` para obter a credencial.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Está Preso em Algum Lado?

Se tiver algum problema a executar esta configuração, entre no nosso

ou

.

## Próxima Aula

Está agora pronto para executar o código deste curso. Divirta-se a aprender mais sobre o mundo dos Agentes de IA!

[Introdução a Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.