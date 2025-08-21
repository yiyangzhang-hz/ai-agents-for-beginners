<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8693a24942b670e3cb8def77f92513f9",
  "translation_date": "2025-08-21T12:55:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "br"
}
-->
# Configuração do Curso

## Introdução

Esta lição abordará como executar os exemplos de código deste curso.

## Clonar ou Fazer Fork deste Repositório

Para começar, clone ou faça um fork do repositório no GitHub. Isso criará sua própria versão do material do curso, permitindo que você execute, teste e ajuste o código!

Isso pode ser feito clicando no link para 

Você agora deve ter sua própria versão forkada deste curso no seguinte link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.br.png)

## Executando o Código

Este curso oferece uma série de Jupyter Notebooks que você pode executar para obter experiência prática na construção de Agentes de IA.

Os exemplos de código utilizam:

**Requer Conta no GitHub - Gratuito**:

1) Framework Semantic Kernel Agent + GitHub Models Marketplace. Identificado como (semantic-kernel.ipynb)  
2) Framework AutoGen + GitHub Models Marketplace. Identificado como (autogen.ipynb)  

**Requer Assinatura do Azure**:  
3) Azure AI Foundry + Azure AI Agent Service. Identificado como (azureaiagent.ipynb)  

Recomendamos que você experimente os três tipos de exemplos para descobrir qual funciona melhor para você.

A opção escolhida determinará quais etapas de configuração você precisará seguir abaixo:

## Requisitos

- Python 3.12+  
  - **NOTA**: Se você não tiver o Python 3.12 instalado, certifique-se de instalá-lo. Em seguida, crie seu ambiente virtual (venv) usando python3.12 para garantir que as versões corretas sejam instaladas a partir do arquivo requirements.txt.  
- Uma Conta no GitHub - Para acesso ao GitHub Models Marketplace  
- Assinatura do Azure - Para acesso ao Azure AI Foundry  
- Conta no Azure AI Foundry - Para acesso ao Azure AI Agent Service  

Incluímos um arquivo `requirements.txt` na raiz deste repositório que contém todos os pacotes Python necessários para executar os exemplos de código.

Você pode instalá-los executando o seguinte comando no terminal na raiz do repositório:

```bash
pip install -r requirements.txt
```  
Recomendamos criar um ambiente virtual Python para evitar conflitos e problemas.

## Configurar o VSCode  
Certifique-se de que está utilizando a versão correta do Python no VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Configuração para Exemplos usando Modelos do GitHub

### Passo 1: Recupere seu Token de Acesso Pessoal (PAT) do GitHub

Este curso utiliza o GitHub Models Marketplace, que oferece acesso gratuito a Modelos de Linguagem de Grande Escala (LLMs) que você usará para construir Agentes de IA.

Para usar os modelos do GitHub, você precisará criar um [Token de Acesso Pessoal do GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Isso pode ser feito acessando sua conta do GitHub.

Por favor, siga o [Princípio do Menor Privilégio](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) ao criar seu token. Isso significa que você deve conceder ao token apenas as permissões necessárias para executar os exemplos de código deste curso.

1. Selecione a opção `Fine-grained tokens` no lado esquerdo da tela, navegando até as **Configurações do Desenvolvedor**  
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.br.png)

   Em seguida, selecione `Generate new token`.  

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.br.png)

2. Insira um nome descritivo para o token que reflita seu propósito, facilitando sua identificação posteriormente.

    🔐 Recomendação de Duração do Token  

    Duração recomendada: 30 dias  
    Para uma postura mais segura, você pode optar por um período mais curto—como 7 dias 🛡️  
    É uma ótima maneira de definir uma meta pessoal e concluir o curso enquanto sua motivação está alta 🚀.  

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.br.png)

3. Limite o escopo do token ao fork deste repositório.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.br.png)

4. Restrinja as permissões do token: Em **Permissions**, clique na aba **Account** e no botão "+ Add permissions". Um menu suspenso aparecerá. Pesquise por **Models** e marque a caixa correspondente.  
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.br.png)

5. Verifique as permissões necessárias antes de gerar o token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.br.png)

6. Antes de gerar o token, certifique-se de que está pronto para armazená-lo em um local seguro, como um gerenciador de senhas, pois ele não será exibido novamente após sua criação. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.br.png)

Copie o novo token que você acabou de criar. Agora você o adicionará ao arquivo `.env` incluído neste curso.

### Passo 2: Crie seu Arquivo `.env`

Para criar o arquivo `.env`, execute o seguinte comando no terminal:

```bash
cp .env.example .env
```

Isso copiará o arquivo de exemplo e criará um `.env` no seu diretório, onde você preencherá os valores das variáveis de ambiente.

Com o token copiado, abra o arquivo `.env` no seu editor de texto favorito e cole o token no campo `GITHUB_TOKEN`.  
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.br.png)

Agora você deve conseguir executar os exemplos de código deste curso.

## Configuração para Exemplos usando Azure AI Foundry e Azure AI Agent Service

### Passo 1: Recupere o Endpoint do Projeto no Azure

Siga os passos para criar um hub e um projeto no Azure AI Foundry descritos aqui: [Visão geral dos recursos do Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Depois de criar seu projeto, você precisará recuperar a string de conexão do projeto.

Isso pode ser feito acessando a página **Overview** do seu projeto no portal do Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.br.png)

### Passo 2: Crie seu Arquivo `.env`

Para criar o arquivo `.env`, execute o seguinte comando no terminal:

```bash
cp .env.example .env
```

Isso copiará o arquivo de exemplo e criará um `.env` no seu diretório, onde você preencherá os valores das variáveis de ambiente.

Com o token copiado, abra o arquivo `.env` no seu editor de texto favorito e cole o token no campo `PROJECT_ENDPOINT`.

### Passo 3: Faça Login no Azure

Como uma prática recomendada de segurança, utilizaremos a [autenticação sem chave](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) para autenticar no Azure OpenAI com o Microsoft Entra ID.

Em seguida, abra um terminal e execute `az login --use-device-code` para fazer login na sua conta do Azure.

Depois de fazer login, selecione sua assinatura no terminal.

## Variáveis de Ambiente Adicionais - Azure Search e Azure OpenAI

Para a lição Agentic RAG - Lição 5 - há exemplos que utilizam Azure Search e Azure OpenAI.

Se você quiser executar esses exemplos, precisará adicionar as seguintes variáveis de ambiente ao seu arquivo `.env`:

### Página de Visão Geral (Projeto)

- `AZURE_SUBSCRIPTION_ID` - Verifique **Detalhes do Projeto** na página **Overview** do seu projeto.

- `AZURE_AI_PROJECT_NAME` - Veja o topo da página **Overview** do seu projeto.

- `AZURE_OPENAI_SERVICE` - Encontre isso na aba **Included capabilities** para **Azure OpenAI Service** na página **Overview**.

### Centro de Gerenciamento

- `AZURE_OPENAI_RESOURCE_GROUP` - Vá para **Propriedades do Projeto** na página **Overview** do **Centro de Gerenciamento**.

- `GLOBAL_LLM_SERVICE` - Em **Recursos Conectados**, encontre o nome da conexão **Azure AI Services**. Se não estiver listado, verifique no **portal do Azure** sob seu grupo de recursos o nome do recurso de AI Services.

### Página de Modelos + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Selecione seu modelo de embedding (por exemplo, `text-embedding-ada-002`) e anote o **Deployment name** nos detalhes do modelo.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Selecione seu modelo de chat (por exemplo, `gpt-4o-mini`) e anote o **Deployment name** nos detalhes do modelo.

### Portal do Azure

- `AZURE_OPENAI_ENDPOINT` - Procure por **Azure AI services**, clique nele, depois vá para **Gerenciamento de Recursos**, **Chaves e Endpoint**, role para baixo até "Azure OpenAI endpoints" e copie o que diz "Language APIs".

- `AZURE_OPENAI_API_KEY` - Na mesma tela, copie a CHAVE 1 ou CHAVE 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Encontre seu recurso **Azure AI Search**, clique nele e veja **Overview**.

- `AZURE_SEARCH_API_KEY` - Em seguida, vá para **Configurações** e depois **Chaves** para copiar a chave de administrador primária ou secundária.

### Página Externa

- `AZURE_OPENAI_API_VERSION` - Visite a página [Ciclo de vida da versão da API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) sob **Última versão GA da API**.

### Configurar autenticação sem chave

Em vez de codificar suas credenciais, utilizaremos uma conexão sem chave com o Azure OpenAI. Para isso, importaremos `DefaultAzureCredential` e posteriormente chamaremos a função `DefaultAzureCredential` para obter a credencial.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Com Problemas?

Se você tiver qualquer problema ao executar esta configuração, entre no nosso 

## Próxima Lição

Agora você está pronto para executar o código deste curso. Aproveite para aprender mais sobre o mundo dos Agentes de IA!

[Introdução aos Agentes de IA e Casos de Uso de Agentes](../01-intro-to-ai-agents/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.