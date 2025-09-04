<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T07:20:01+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "en"
}
-->
# Using Agentic Protocols (MCP, A2A, and NLWeb)

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.en.png)](https://youtu.be/X-Dh9R3Opn8)

As AI agents become more prevalent, the need for protocols that ensure standardization, security, and foster open innovation grows. In this lesson, we’ll explore three protocols designed to address these needs: Model Context Protocol (MCP), Agent-to-Agent (A2A), and Natural Language Web (NLWeb).

## Introduction

In this lesson, we’ll discuss:

• How **MCP** enables AI agents to access external tools and data to complete user tasks.

• How **A2A** facilitates communication and collaboration between different AI agents.

• How **NLWeb** introduces natural language interfaces to websites, allowing AI agents to discover and interact with content.

## Learning Goals

• **Understand** the primary purpose and advantages of MCP, A2A, and NLWeb in the context of AI agents.

• **Describe** how each protocol supports communication and interaction between LLMs, tools, and other agents.

• **Differentiate** the unique roles each protocol plays in building complex agentic systems.

## Model Context Protocol

The **Model Context Protocol (MCP)** is an open standard that provides a consistent way for applications to supply context and tools to LLMs. It acts as a "universal adapter," enabling AI agents to connect to various data sources and tools in a standardized manner.

Let’s examine the components of MCP, its advantages over direct API usage, and an example of how AI agents might utilize an MCP server.

### MCP Core Components

MCP operates on a **client-server architecture**, with the following key components:

• **Hosts**: LLM applications (e.g., a code editor like VSCode) that initiate connections to an MCP server.

• **Clients**: Components within the host application that maintain one-to-one connections with servers.

• **Servers**: Lightweight programs that expose specific capabilities.

The protocol includes three core primitives that define the capabilities of an MCP server:

• **Tools**: These are specific actions or functions an AI agent can invoke to perform tasks. For instance, a weather service might offer a "get weather" tool, or an e-commerce server might provide a "purchase product" tool. MCP servers list each tool’s name, description, and input/output schema in their capabilities.

• **Resources**: These are read-only data items or documents that an MCP server can provide, which clients can retrieve as needed. Examples include file contents, database records, or log files. Resources can be text-based (e.g., code or JSON) or binary (e.g., images or PDFs).

• **Prompts**: These are predefined templates that suggest prompts, enabling more complex workflows.

### Benefits of MCP

MCP offers several advantages for AI agents:

• **Dynamic Tool Discovery**: Agents can dynamically retrieve a list of available tools from a server, along with descriptions of their functions. Unlike traditional APIs, which often require static coding for integrations (and updates when APIs change), MCP allows for an "integrate once" approach, enhancing adaptability.

• **Interoperability Across LLMs**: MCP works with different LLMs, providing flexibility to switch models for better performance evaluation.

• **Standardized Security**: MCP includes a unified authentication method, simplifying scalability when adding access to additional MCP servers. This eliminates the need to manage multiple keys and authentication types for various APIs.

### MCP Example

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.en.png)

Imagine a user wants to book a flight using an AI assistant powered by MCP.

1. **Connection**: The AI assistant (the MCP client) connects to an MCP server provided by an airline.

2. **Tool Discovery**: The client queries the airline’s MCP server: "What tools do you have available?" The server responds with tools like "search flights" and "book flights."

3. **Tool Invocation**: The user asks the AI assistant, "Please search for a flight from Portland to Honolulu." The AI assistant identifies the need to call the "search flights" tool and sends the relevant parameters (origin, destination) to the MCP server.

4. **Execution and Response**: The MCP server, acting as a wrapper, makes the actual call to the airline’s internal booking API. It retrieves the flight information (e.g., JSON data) and sends it back to the AI assistant.

5. **Further Interaction**: The AI assistant presents the flight options. Once the user selects a flight, the assistant might invoke the "book flight" tool on the same MCP server to complete the booking.

## Agent-to-Agent Protocol (A2A)

While MCP focuses on connecting LLMs to tools, the **Agent-to-Agent (A2A) protocol** goes further by enabling communication and collaboration between different AI agents. A2A connects AI agents across various organizations, environments, and tech stacks to accomplish shared tasks.

We’ll explore the components and benefits of A2A, along with an example of its application in our travel scenario.

### A2A Core Components

A2A facilitates communication between agents, enabling them to collaborate on subtasks. Each component of the protocol plays a role in this process:

#### Agent Card

Similar to an MCP server’s tool list, an Agent Card includes:

- The agent’s **name**.
- A **description of its general tasks**.
- A **list of specific skills** with descriptions to help other agents (or humans) understand when and why to call that agent.
- The agent’s **current endpoint URL**.
- The agent’s **version** and **capabilities**, such as streaming responses and push notifications.

#### Agent Executor

The Agent Executor is responsible for **passing the user’s context to the remote agent**, enabling the remote agent to understand the task at hand. In an A2A server, the agent uses its own LLM to interpret incoming requests and execute tasks using its internal tools.

#### Artifact

Once a remote agent completes a task, it produces an artifact. An artifact includes the **result of the agent’s work**, a **description of what was completed**, and the **text context** sent through the protocol. After the artifact is delivered, the connection with the remote agent is closed until needed again.

#### Event Queue

This component manages **updates and message passing**. It ensures that connections between agents remain open until tasks are completed, which is especially important for longer-running processes in production environments.

### Benefits of A2A

• **Enhanced Collaboration**: A2A enables agents from different vendors and platforms to interact, share context, and collaborate, streamlining automation across traditionally disconnected systems.

• **Model Selection Flexibility**: Each A2A agent can choose its own LLM to handle requests, allowing for optimized or fine-tuned models per agent, unlike scenarios where a single LLM is used.

• **Integrated Authentication**: A2A includes built-in authentication, providing a secure framework for agent interactions.

### A2A Example

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.en.png)

Let’s revisit our travel booking scenario, this time using A2A.

1. **User Request to Multi-Agent**: A user interacts with a "Travel Agent" A2A client/agent, requesting, "Please book an entire trip to Honolulu for next week, including flights, a hotel, and a rental car."

2. **Orchestration by Travel Agent**: The Travel Agent processes the request, using its LLM to determine that it needs to collaborate with other specialized agents.

3. **Inter-Agent Communication**: The Travel Agent uses the A2A protocol to connect with downstream agents, such as an "Airline Agent," a "Hotel Agent," and a "Car Rental Agent," each developed by different companies.

4. **Delegated Task Execution**: The Travel Agent assigns specific tasks to these agents (e.g., "Find flights to Honolulu," "Book a hotel," "Rent a car"). Each agent, using its own LLM and tools (possibly MCP servers), completes its part of the booking.

5. **Consolidated Response**: Once all agents finish their tasks, the Travel Agent compiles the results (flight details, hotel confirmation, car rental booking) and provides a comprehensive response to the user.

## Natural Language Web (NLWeb)

Websites have long been the primary way for users to access information and data online.

Let’s explore the components of NLWeb, its benefits, and an example of how it works in our travel application.

### Components of NLWeb

- **NLWeb Application (Core Service Code)**: The system that processes natural language queries, connecting different platform components to generate responses. Think of it as the **engine powering natural language features** on a website.

- **NLWeb Protocol**: A **basic set of rules for natural language interaction** with a website, returning responses in JSON format (often using Schema.org). It provides a simple foundation for the “AI Web,” similar to how HTML enabled document sharing online.

- **MCP Server (Model Context Protocol Endpoint)**: Each NLWeb setup also functions as an **MCP server**, sharing tools (e.g., an “ask” method) and data with other AI systems. This allows the website’s content and capabilities to integrate into the broader “agent ecosystem.”

- **Embedding Models**: These models **convert website content into numerical representations (embeddings)**, capturing meaning for comparison and search. The embeddings are stored in a specialized database, and users can select their preferred embedding model.

- **Vector Database (Retrieval Mechanism)**: This database **stores embeddings of website content**. When a query is made, NLWeb searches the database to find the most relevant information, ranking results by similarity. NLWeb supports various vector storage systems, such as Qdrant, Snowflake, Milvus, Azure AI Search, and Elasticsearch.

### NLWeb by Example

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.en.png)

Consider our travel booking website, now powered by NLWeb.

1. **Data Ingestion**: The website’s product catalogs (e.g., flight listings, hotel descriptions, tour packages) are formatted using Schema.org or loaded via RSS feeds. NLWeb ingests this structured data, creates embeddings, and stores them in a vector database.

2. **Natural Language Query (Human)**: A user visits the website and types into a chat interface: "Find me a family-friendly hotel in Honolulu with a pool for next week."

3. **NLWeb Processing**: NLWeb processes the query, sending it to an LLM for interpretation while simultaneously searching the vector database for relevant hotel listings.

4. **Accurate Results**: The LLM interprets the search results, identifies the best matches based on the user’s criteria, and formats a natural language response. The response references actual hotels from the website’s catalog, avoiding fabricated information.

5. **AI Agent Interaction**: Since NLWeb functions as an MCP server, an external AI travel agent could connect to the website’s NLWeb instance. For example, the agent might use the `ask` MCP method to query the site directly: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. NLWeb would process the query, leveraging its database, and return a structured JSON response.

### Got More Questions about MCP/A2A/NLWeb?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI agent questions answered.

## Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.