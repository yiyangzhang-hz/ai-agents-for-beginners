<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c55b973b1562abf5aadf6a4028265ac5",
  "translation_date": "2025-08-29T12:48:05+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Configuração do Curso

## Introdução

Esta lição abordará como executar os exemplos de código deste curso.

## Junte-se a Outros Alunos e Obtenha Ajuda

Antes de começar a clonar seu repositório, junte-se ao [canal Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord) para obter ajuda com a configuração, tirar dúvidas sobre o curso ou se conectar com outros alunos.

## Clone ou Faça um Fork deste Repositório

Para começar, clone ou faça um fork do repositório GitHub. Isso criará sua própria versão do material do curso para que você possa executar, testar e ajustar o código!

Isso pode ser feito clicando no link para 

Você deve agora ter sua própria versão forkada deste curso no seguinte link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.br.png)

## Executando o Código

Este curso oferece uma série de Jupyter Notebooks que você pode executar para obter experiência prática na construção de Agentes de IA.

Os exemplos de código utilizam:

**Requer Conta no GitHub - Gratuito**:

1) Framework Semantic Kernel Agent + GitHub Models Marketplace. Identificado como (semantic-kernel.ipynb)
2) Framework AutoGen + GitHub Models Marketplace. Identificado como (autogen.ipynb)

**Requer Assinatura do Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Identificado como (azureaiagent.ipynb)

Recomendamos que você experimente os três tipos de exemplos para ver qual funciona melhor para você.

A opção que você escolher determinará quais etapas de configuração você precisará seguir abaixo:

## Requisitos

- Python 3.12+
  - **NOTE**: Se você não tiver o Python 3.12 instalado, certifique-se de instalá-lo. Em seguida, crie seu venv usando python3.12 para garantir que as versões corretas sejam instaladas a partir do arquivo requirements.txt.
- Uma Conta no GitHub - Para acesso ao GitHub Models Marketplace
- Assinatura do Azure - Para acesso ao Azure AI Foundry
- Conta do Azure AI Foundry - Para acesso ao Azure AI Agent Service

Incluímos um arquivo `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Você pode instalá-los executando o seguinte comando no terminal na raiz do repositório:

```bash
pip install -r requirements.txt
```
Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configuração do VSCode
Certifique-se de que está usando a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuração para Exemplos usando Modelos do GitHub 

### Etapa 1: Recupere Seu Token de Acesso Pessoal (PAT) do GitHub

Este curso utiliza o GitHub Models Marketplace, fornecendo acesso gratuito a Modelos de Linguagem Grande (LLMs) que você usará para construir Agentes de IA.

Para usar os Modelos do GitHub, você precisará criar um [Token de Acesso Pessoal do GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Isso pode ser feito acessando sua conta do GitHub.

Por favor, siga o [Princípio do Menor Privilégio](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ao criar seu token. Isso significa que você deve conceder ao token apenas as permissões necessárias para executar os exemplos de código deste curso.

1. Selecione a opção `Fine-grained tokens` no lado esquerdo da tela, navegando até **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.br.png)

    Em seguida, selecione `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.br.png)

2. Insira um nome descritivo para seu token que reflita seu propósito, facilitando sua identificação posteriormente.

    🔐 Recomendação de Duração do Token

    Duração recomendada: 30 dias  
    Para uma postura mais segura, você pode optar por um período mais curto—como 7 dias 🛡️  
    É uma ótima maneira de definir uma meta pessoal e concluir o curso enquanto sua motivação está alta 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.br.png)

3. Limite o escopo do token ao seu fork deste repositório.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.br.png)

4. Restrinja as permissões do token: Sob **Permissions**, clique na aba **Account** e no botão "+ Add permissions". Um menu suspenso aparecerá. Procure por **Models** e marque a caixa correspondente.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.br.png)

5. Verifique as permissões necessárias antes de gerar o token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.br.png)

6. Antes de gerar o token, certifique-se de que está pronto para armazená-lo em um local seguro, como um cofre de gerenciador de senhas, pois ele não será exibido novamente após sua criação. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.br.png)

Copie seu novo token que acabou de criar. Agora você o adicionará ao arquivo `.env` incluído neste curso.

### Etapa 2: Crie Seu Arquivo `.env`

Para criar seu arquivo `.env`, execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isso copiará o arquivo de exemplo e criará um `.env` em seu diretório, onde você preencherá os valores das variáveis de ambiente.

Com seu token copiado, abra o arquivo `.env` em seu editor de texto favorito e cole seu token no campo `GITHUB_TOKEN`.  
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.br.png)

Agora você deve conseguir executar os exemplos de código deste curso.

## Configuração para Exemplos usando Azure AI Foundry e Azure AI Agent Service

### Etapa 1: Recupere Seu Endpoint de Projeto do Azure

Siga os passos para criar um hub e projeto no Azure AI Foundry encontrados aqui: [Visão geral de recursos do Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Depois de criar seu projeto, você precisará recuperar a string de conexão para seu projeto.

Isso pode ser feito acessando a página **Overview** do seu projeto no portal Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.br.png)

### Etapa 2: Crie Seu Arquivo `.env`

Para criar seu arquivo `.env`, execute o seguinte comando no terminal.

```bash
cp .env.example .env
```

Isso copiará o arquivo de exemplo e criará um `.env` em seu diretório, onde você preencherá os valores das variáveis de ambiente.

Com seu token copiado, abra o arquivo `.env` em seu editor de texto favorito e cole seu token no campo `PROJECT_ENDPOINT`.

### Etapa 3: Faça Login no Azure

Como prática recomendada de segurança, usaremos [autenticação sem chave](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) para autenticar no Azure OpenAI com Microsoft Entra ID.

Em seguida, abra um terminal e execute `az login --use-device-code` para fazer login em sua conta do Azure.

Depois de fazer login, selecione sua assinatura no terminal.

## Variáveis de Ambiente Adicionais - Azure Search e Azure OpenAI 

Para a lição Agentic RAG - Lição 5 - há exemplos que utilizam Azure Search e Azure OpenAI.

Se você quiser executar esses exemplos, precisará adicionar as seguintes variáveis de ambiente ao seu arquivo `.env`:

### Página de Visão Geral (Projeto)

- `AZURE_SUBSCRIPTION_ID` - Verifique **Project details** na página **Overview** do seu projeto.

- `AZURE_AI_PROJECT_NAME` - Veja no topo da página **Overview** do seu projeto.

- `AZURE_OPENAI_SERVICE` - Encontre isso na aba **Included capabilities** para **Azure OpenAI Service** na página **Overview**.

### Centro de Gerenciamento

- `AZURE_OPENAI_RESOURCE_GROUP` - Vá para **Project properties** na página **Overview** do **Management Center**.

- `GLOBAL_LLM_SERVICE` - Sob **Connected resources**, encontre o nome da conexão **Azure AI Services**. Se não estiver listado, verifique o **portal do Azure** em seu grupo de recursos para o nome do recurso AI Services.

### Página de Modelos + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecione seu modelo de embedding (por exemplo, `text-embedding-ada-002`) e anote o **Deployment name** nos detalhes do modelo.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecione seu modelo de chat (por exemplo, `gpt-4o-mini`) e anote o **Deployment name** nos detalhes do modelo.

### Portal do Azure

- `AZURE_OPENAI_ENDPOINT` - Procure por **Azure AI services**, clique nele, vá para **Resource Management**, **Keys and Endpoint**, role para baixo até "Azure OpenAI endpoints" e copie o que diz "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na mesma tela, copie a CHAVE 1 ou CHAVE 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Encontre seu recurso **Azure AI Search**, clique nele e veja **Overview**.

- `AZURE_SEARCH_API_KEY` - Em seguida, vá para **Settings** e depois **Keys** para copiar a chave de administrador primária ou secundária.

### Página Externa

- `AZURE_OPENAI_API_VERSION` - Visite a página [ciclo de vida da versão da API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sob **Latest GA API release**.

### Configuração de autenticação sem chave

Em vez de codificar suas credenciais, usaremos uma conexão sem chave com Azure OpenAI. Para isso, importaremos `DefaultAzureCredential` e posteriormente chamaremos a função `DefaultAzureCredential` para obter a credencial.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Com Problemas?

Se você tiver algum problema ao executar esta configuração, entre em nosso 

## Próxima Lição

Agora você está pronto para executar o código deste curso. Aproveite para aprender mais sobre o mundo dos Agentes de IA!

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.