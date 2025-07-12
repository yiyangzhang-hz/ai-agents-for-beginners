<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:43:41+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "en"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Introduction to Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an advanced framework designed to standardize how AI models interact with client applications. MCP acts as a bridge between AI models and the applications that use them, offering a consistent interface regardless of the underlying model implementation.

Key features of MCP:

- **Standardized Communication**: MCP creates a common language for applications to communicate with AI models  
- **Enhanced Context Management**: Enables efficient transfer of contextual information to AI models  
- **Cross-platform Compatibility**: Supports multiple programming languages including C#, Java, JavaScript, Python, and TypeScript  
- **Seamless Integration**: Allows developers to easily incorporate different AI models into their applications  

MCP is especially useful in AI agent development, as it lets agents interact with various systems and data sources through a unified protocol, making them more flexible and powerful.

## Learning Objectives
- Understand what MCP is and its role in AI agent development  
- Set up and configure an MCP server for GitHub integration  
- Build a multi-agent system using MCP tools  
- Implement RAG (Retrieval Augmented Generation) with Azure Cognitive Search  

## Prerequisites
- Python 3.8+  
- Node.js 14+  
- Azure subscription  
- GitHub account  
- Basic knowledge of Semantic Kernel  

## Setup Instructions

1. **Environment Setup**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure Azure Services**  
   - Create an Azure Cognitive Search resource  
   - Set up Azure OpenAI service  
   - Configure environment variables in `.env`  

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
- GitHub Agent: Analyzes repositories  
- Hackathon Agent: Recommends projects  
- Events Agent: Suggests tech events  

### 2. Azure Integration
- Cognitive Search for indexing events  
- Azure OpenAI for agent intelligence  
- Implementation of the RAG pattern  

### 3. MCP Tools
- GitHub repository analysis  
- Code inspection  
- Metadata extraction  

## Code Walkthrough

This sample demonstrates:  
1. MCP server integration  
2. Multi-agent orchestration  
3. Azure Cognitive Search integration  
4. RAG pattern implementation  

Key features include:  
- Real-time GitHub repository analysis  
- Intelligent project recommendations  
- Event matching using Azure Search  
- Streaming responses with Chainlit  

## Running the Sample

For detailed setup instructions and more information, see the [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Start the MCP server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Launch the application:  
   ```bash
   chainlit run app.py -w
   ```

3. Test the integration:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Troubleshooting

Common issues and solutions:  
1. MCP Connection Issues  
   - Make sure the server is running  
   - Check if the port is available  
   - Verify GitHub tokens  

2. Azure Search Issues  
   - Confirm connection strings are correct  
   - Ensure the index exists  
   - Check that documents have been uploaded  

## Next Steps
- Explore additional MCP tools  
- Build custom agents  
- Improve RAG capabilities  
- Add more event sources  

## Resources
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.