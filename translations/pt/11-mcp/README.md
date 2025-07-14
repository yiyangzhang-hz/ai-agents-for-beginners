<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:47:00+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "pt"
}
-->
# Aula 11: Integração do Protocolo de Contexto do Modelo (MCP)

## Introdução ao Protocolo de Contexto do Modelo (MCP)

O Protocolo de Contexto do Modelo (MCP) é uma estrutura inovadora criada para padronizar as interações entre modelos de IA e aplicações cliente. O MCP funciona como uma ponte entre os modelos de IA e as aplicações que os utilizam, oferecendo uma interface consistente independentemente da implementação subjacente do modelo.

Aspectos principais do MCP:

- **Comunicação Padronizada**: O MCP estabelece uma linguagem comum para as aplicações comunicarem com os modelos de IA
- **Gestão de Contexto Aprimorada**: Permite a passagem eficiente de informação contextual para os modelos de IA
- **Compatibilidade Multiplataforma**: Funciona em várias linguagens de programação, incluindo C#, Java, JavaScript, Python e TypeScript
- **Integração Simplificada**: Permite aos programadores integrar facilmente diferentes modelos de IA nas suas aplicações

O MCP é especialmente valioso no desenvolvimento de agentes de IA, pois permite que os agentes interajam com vários sistemas e fontes de dados através de um protocolo unificado, tornando-os mais flexíveis e poderosos.

## Objetivos de Aprendizagem
- Compreender o que é o MCP e o seu papel no desenvolvimento de agentes de IA
- Configurar e preparar um servidor MCP para integração com o GitHub
- Construir um sistema multi-agente usando as ferramentas MCP
- Implementar RAG (Retrieval Augmented Generation) com o Azure Cognitive Search

## Pré-requisitos
- Python 3.8+
- Node.js 14+
- Subscrição Azure
- Conta GitHub
- Conhecimentos básicos de Semantic Kernel

## Instruções de Configuração

1. **Configuração do Ambiente**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurar Serviços Azure**
   - Criar um recurso Azure Cognitive Search
   - Configurar o serviço Azure OpenAI
   - Definir variáveis de ambiente no ficheiro `.env`

3. **Configuração do Servidor MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Estrutura do Projeto

```
11-mcp/
├── code_samples/
│   └── github-mcp/
│       ├── app.py              # Main application
│       ├── event-descriptions.md  # Event data
│       └── MCP_SETUP.md        # Setup guide
├── README.md
└── requirements.txt
```

## Componentes Principais

### 1. Sistema Multi-Agente
- Agente GitHub: Análise de repositórios
- Agente Hackathon: Recomendações de projetos
- Agente de Eventos: Sugestões de eventos tecnológicos

### 2. Integração Azure
- Cognitive Search para indexação de eventos
- Azure OpenAI para inteligência dos agentes
- Implementação do padrão RAG

### 3. Ferramentas MCP
- Análise de repositórios GitHub
- Inspeção de código
- Extração de metadados

## Análise do Código

O exemplo demonstra:
1. Integração do servidor MCP
2. Orquestração multi-agente
3. Integração com Azure Cognitive Search
4. Implementação do padrão RAG

Funcionalidades principais:
- Análise em tempo real de repositórios GitHub
- Recomendações inteligentes de projetos
- Correspondência de eventos usando Azure Search
- Respostas em streaming com Chainlit

## Executar o Exemplo

Para instruções detalhadas de configuração e mais informações, consulte o [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Inicie o servidor MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lance a aplicação:
   ```bash
   chainlit run app.py -w
   ```

3. Teste a integração:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Resolução de Problemas

Problemas comuns e soluções:
1. Problemas de Conexão MCP
   - Verifique se o servidor está a correr
   - Confirme a disponibilidade da porta
   - Confirme os tokens GitHub

2. Problemas com Azure Search
   - Valide as strings de conexão
   - Verifique a existência do índice
   - Confirme o upload dos documentos

## Próximos Passos
- Explorar ferramentas MCP adicionais
- Implementar agentes personalizados
- Melhorar as capacidades RAG
- Adicionar mais fontes de eventos

## Recursos
- [MCP para Iniciantes](https://aka.ms/mcp-for-beginners)  
- [Documentação MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Documentação Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Guias Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.