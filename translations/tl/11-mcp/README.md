<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:49:45+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "tl"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Introduction to Model Context Protocol (MCP)

Ang Model Context Protocol (MCP) ay isang makabagong framework na idinisenyo upang gawing pare-pareho ang ugnayan sa pagitan ng mga AI model at mga client application. Ang MCP ay nagsisilbing tulay sa pagitan ng mga AI model at ng mga application na gumagamit nito, na nagbibigay ng isang pare-parehong interface kahit ano pa man ang implementasyon ng model.

Mga pangunahing aspeto ng MCP:

- **Standardized Communication**: Nagbibigay ang MCP ng isang karaniwang wika para sa komunikasyon ng mga application sa AI models
- **Enhanced Context Management**: Pinapadali ang epektibong pagpapasa ng kontekstwal na impormasyon sa mga AI model
- **Cross-platform Compatibility**: Gumagana ito sa iba't ibang programming languages tulad ng C#, Java, JavaScript, Python, at TypeScript
- **Seamless Integration**: Pinapadali ng MCP sa mga developer ang pag-integrate ng iba't ibang AI model sa kanilang mga application

Napakahalaga ng MCP sa pag-develop ng AI agent dahil pinapayagan nito ang mga agent na makipag-ugnayan sa iba't ibang sistema at pinanggagalingan ng data gamit ang isang pinag-isang protocol, kaya mas nagiging flexible at malakas ang mga agent.

## Learning Objectives
- Maunawaan kung ano ang MCP at ang papel nito sa pag-develop ng AI agent
- Mag-set up at mag-configure ng MCP server para sa GitHub integration
- Gumawa ng multi-agent system gamit ang mga MCP tools
- Mag-implement ng RAG (Retrieval Augmented Generation) gamit ang Azure Cognitive Search

## Prerequisites
- Python 3.8+
- Node.js 14+
- Azure subscription
- GitHub account
- Pangunahing kaalaman sa Semantic Kernel

## Setup Instructions

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Azure Services**
   - Gumawa ng Azure Cognitive Search resource
   - I-set up ang Azure OpenAI service
   - I-configure ang mga environment variables sa `.env`

3. **MCP Server Setup**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Project Structure

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

## Core Components

### 1. Multi-Agent System
- GitHub Agent: Pagsusuri ng repositoryo
- Hackathon Agent: Mga rekomendasyon para sa proyekto
- Events Agent: Mga suhestiyon para sa tech events

### 2. Azure Integration
- Cognitive Search para sa pag-index ng mga event
- Azure OpenAI para sa katalinuhan ng agent
- Pag-implement ng RAG pattern

### 3. MCP Tools
- Pagsusuri ng GitHub repository
- Pag-inspeksyon ng code
- Pagkuha ng metadata

## Code Walkthrough

Ipinapakita ng sample ang:
1. Integrasyon ng MCP server
2. Orkestrasyon ng multi-agent
3. Integrasyon ng Azure Cognitive Search
4. Pag-implement ng RAG pattern

Mga pangunahing tampok:
- Real-time na pagsusuri ng GitHub repository
- Matalinong mga rekomendasyon para sa proyekto
- Pagtutugma ng event gamit ang Azure Search
- Streaming na mga tugon gamit ang Chainlit

## Running the Sample

Para sa detalyadong mga tagubilin sa setup at karagdagang impormasyon, tingnan ang [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Simulan ang MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Ilunsad ang application:
   ```bash
   chainlit run app.py -w
   ```

3. Subukan ang integrasyon:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Troubleshooting

Mga karaniwang isyu at solusyon:
1. MCP Connection Issues
   - Siguraduhing tumatakbo ang server
   - Suriin ang availability ng port
   - Kumpirmahin ang mga GitHub token

2. Azure Search Issues
   - I-validate ang connection strings
   - Suriin kung umiiral ang index
   - Kumpirmahin ang pag-upload ng dokumento

## Next Steps
- Tuklasin ang iba pang MCP tools
- Mag-implement ng custom agents
- Palawakin ang kakayahan ng RAG
- Magdagdag ng mas maraming pinanggagalingan ng event

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.