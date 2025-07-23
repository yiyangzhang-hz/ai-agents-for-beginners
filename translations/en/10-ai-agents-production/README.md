<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-23T08:04:27+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "en"
}
-->
# AI Agents in Production: Observability & Evaluation

As AI agents transition from experimental prototypes to real-world applications, understanding their behavior, monitoring their performance, and systematically evaluating their outputs becomes crucial.

## Learning Goals

After completing this lesson, you will learn how to:
- Understand the core concepts of agent observability and evaluation
- Apply techniques to improve the performance, costs, and effectiveness of agents
- Systematically evaluate your AI agents
- Manage costs when deploying AI agents to production
- Instrument agents built with AutoGen

The aim is to provide you with the knowledge to turn "black box" agents into transparent, manageable, and reliable systems.

_**Note:** Deploying safe and trustworthy AI agents is essential. Refer to the [Building Trustworthy AI Agents](./06-building-trustworthy-agents/README.md) lesson for more information._

## Traces and Spans

Observability tools like [Langfuse](https://langfuse.com/) or [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) often represent agent runs as traces and spans.

- **Trace**: Represents the entire agent task from start to finish (e.g., handling a user query).
- **Spans**: Represent individual steps within the trace (e.g., calling a language model or retrieving data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Without observability, an AI agent can feel like a "black box"—its internal state and reasoning are opaque, making it hard to diagnose issues or optimize performance. Observability transforms agents into "glass boxes," providing transparency that is essential for building trust and ensuring proper functionality.

## Why Observability Matters in Production Environments

Deploying AI agents in production environments introduces new challenges and requirements. Observability becomes a critical capability rather than a "nice-to-have":

*   **Debugging and Root-Cause Analysis**: When an agent fails or produces unexpected outputs, observability tools provide traces to identify the source of the error. This is especially important for complex agents involving multiple LLM calls, tool interactions, and conditional logic.
*   **Latency and Cost Management**: AI agents often rely on LLMs and external APIs billed per token or call. Observability enables precise tracking of these calls, helping identify operations that are slow or expensive. Teams can optimize prompts, choose more efficient models, or redesign workflows to manage costs and ensure a good user experience.
*   **Trust, Safety, and Compliance**: Observability provides an audit trail of agent actions and decisions, which is crucial for detecting and mitigating issues like prompt injection, harmful content generation, or mishandling of personally identifiable information (PII). For example, traces can help understand why an agent provided a specific response or used a particular tool.
*   **Continuous Improvement Loops**: Observability data forms the basis for iterative development. By monitoring real-world performance, teams can identify areas for improvement, gather data for fine-tuning models, and validate changes. This creates a feedback loop where production insights from online evaluation inform offline experimentation, leading to better agent performance.

## Key Metrics to Track

To monitor and understand agent behavior, various metrics and signals should be tracked. While specific metrics depend on the agent's purpose, some are universally important.

Here are common metrics monitored by observability tools:

**Latency:** How quickly does the agent respond? Long response times negatively impact user experience. Measure latency for tasks and individual steps by tracing agent runs. For example, an agent taking 20 seconds for all model calls could be sped up by using a faster model or running calls in parallel.

**Costs:** What’s the expense per agent run? AI agents rely on LLM calls billed per token or external APIs. Frequent tool usage or multiple prompts can quickly increase costs. For instance, if an agent calls an LLM five times for marginal quality improvement, assess whether the cost is justified or if fewer calls or a cheaper model could be used. Real-time monitoring can also identify unexpected spikes (e.g., bugs causing excessive API loops).

**Request Errors:** How many requests did the agent fail? This includes API errors or failed tool calls. To make the agent more robust in production, set up fallbacks or retries. For example, if LLM provider A is down, switch to LLM provider B as a backup.

**User Feedback:** Direct user evaluations provide valuable insights, such as explicit ratings (👍thumbs-up/👎down, ⭐1-5 stars) or textual comments. Consistent negative feedback signals that the agent is not performing as expected.

**Implicit User Feedback:** User behaviors offer indirect feedback even without explicit ratings. Examples include immediate question rephrasing, repeated queries, or clicking a retry button. For instance, repeated user queries indicate the agent is not meeting expectations.

**Accuracy:** How often does the agent produce correct or desirable outputs? Accuracy definitions vary (e.g., problem-solving correctness, information retrieval accuracy, user satisfaction). Start by defining success for your agent. Track accuracy via automated checks, evaluation scores, or task completion labels, such as marking traces as "succeeded" or "failed."

**Automated Evaluation Metrics:** Set up automated evaluations using tools like LLMs to score agent outputs (e.g., helpfulness, accuracy). Open-source libraries like [RAGAS](https://docs.ragas.io/) for RAG agents or [LLM Guard](https://llm-guard.com/) for detecting harmful language or prompt injection can also be used.

Combining these metrics provides the best coverage of an AI agent’s health. In this chapter's [example notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), we'll explore these metrics in real examples, but first, let's learn about a typical evaluation workflow.

## Instrument your Agent

To collect tracing data, you’ll need to instrument your code. The goal is to enable the agent code to emit traces and metrics that can be captured, processed, and visualized by an observability platform.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) is an industry standard for LLM observability, offering APIs, SDKs, and tools for generating, collecting, and exporting telemetry data.

Instrumentation libraries can wrap existing agent frameworks, making it easy to export OpenTelemetry spans to an observability tool. Below is an example of instrumenting an AutoGen agent with the [OpenLit instrumentation library](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

The [example notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) in this chapter demonstrates how to instrument your AutoGen agent.

**Manual Span Creation:** While instrumentation libraries provide a good baseline, there are cases where detailed or custom information is needed. You can manually create spans to add custom application logic or enrich spans with attributes (tags or metadata). These attributes can include business-specific data, intermediate computations, or debugging context, such as `user_id`, `session_id`, or `model_version`.

Example of creating traces and spans manually with the [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluation

Observability provides metrics, but evaluation involves analyzing that data (and performing tests) to assess how well an AI agent is performing and how it can be improved. Once you have traces and metrics, evaluation helps you judge the agent and make decisions.

Regular evaluation is essential because AI agents are often non-deterministic and can evolve (through updates or model behavior changes). Without evaluation, you wouldn’t know if your agent is performing well or has regressed.

There are two types of evaluations for AI agents: **online evaluation** and **offline evaluation**. Both are valuable and complement each other. Offline evaluation is typically the first step before deploying an agent.

### Offline Evaluation

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Offline evaluation involves testing the agent in a controlled environment using test datasets, not live user queries. Curated datasets with known expected outputs or behaviors are used to evaluate the agent.

For example, a math word-problem agent might use a [test dataset](https://huggingface.co/datasets/gsm8k) of 100 problems with known answers. Offline evaluation is often part of development and CI/CD pipelines to check improvements or prevent regressions. The benefit is **repeatability and clear accuracy metrics since ground truth is available**. Simulated user queries can also be measured against ideal answers or automated metrics.

The challenge is ensuring the test dataset is comprehensive and relevant. Agents might perform well on fixed test sets but struggle with different queries in production. Test sets should be updated with new edge cases and real-world examples. A mix of small “smoke test” cases and larger evaluation sets is useful: small sets for quick checks and larger ones for broader performance metrics.

### Online Evaluation 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Online evaluation involves testing the agent in a live, real-world environment during actual usage in production. It monitors the agent’s performance on real user interactions and continuously analyzes outcomes.

For example, success rates, user satisfaction scores, or other metrics can be tracked on live traffic. Online evaluation captures unanticipated scenarios, such as model drift or unexpected queries not covered in test data. It provides a true picture of the agent’s behavior in the wild.

Online evaluation often collects implicit and explicit user feedback and may involve shadow tests or A/B tests (comparing new and old agent versions). The challenge is obtaining reliable labels or scores for live interactions, often relying on user feedback or downstream metrics (e.g., user clicks).

### Combining the two

Online and offline evaluations complement each other. Insights from online monitoring (e.g., poor performance on new user queries) can improve offline test datasets. Conversely, agents performing well in offline tests can be confidently deployed and monitored online.

Many teams adopt a loop:

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Common Issues

When deploying AI agents to production, you may encounter challenges. Here are common issues and potential solutions:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Refine the prompt given to the AI Agent; be clear on objectives.<br>- Consider dividing tasks into subtasks handled by multiple agents. |
| AI Agent running into continuous loops  | - Define clear termination conditions so the Agent knows when to stop.<br>- For complex tasks requiring reasoning and planning, use a larger model specialized for reasoning. |
| AI Agent tool calls are not performing well   | - Test and validate the tool's output outside of the agent system. |

- Refine the defined parameters, prompts, and naming of tools.  |
| Multi-Agent system not performing consistently | - Adjust the prompts given to each agent to ensure they are clear and distinct from one another.<br>- Create a hierarchical system using a "routing" or controller agent to decide which agent is the most suitable. |

Many of these issues can be identified more effectively with proper observability in place. The traces and metrics we discussed earlier help pinpoint exactly where problems occur in the agent workflow, making debugging and optimization much more efficient.

## Managing Costs

Here are some strategies to control the costs of deploying AI agents in production:

**Using Smaller Models:** Small Language Models (SLMs) can perform well for certain agent-based use cases and significantly reduce costs. As mentioned earlier, building an evaluation system to compare performance against larger models is the best way to understand how well an SLM will work for your specific use case. Consider using SLMs for simpler tasks like intent classification or parameter extraction, while reserving larger models for more complex reasoning.

**Using a Router Model:** Another approach is to use a variety of models with different sizes. You can use an LLM/SLM or serverless function to route requests based on complexity to the most suitable models. This strategy helps reduce costs while ensuring optimal performance for the right tasks. For example, route simple queries to smaller, faster models, and reserve expensive large models for tasks requiring complex reasoning.

**Caching Responses:** Identifying common requests and tasks and providing pre-generated responses before they go through your agent system is an effective way to reduce the volume of similar requests. You can even implement a process to determine how similar a request is to your cached responses using simpler AI models. This approach can significantly lower costs for frequently asked questions or repetitive workflows.

## Let's see how this works in practice

In the [example notebook for this section](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), we’ll explore examples of how observability tools can be used to monitor and evaluate our agent.

## Previous Lesson

[Metacognition Design Pattern](../09-metacognition/README.md)

## Next Lesson

[MCP](../11-mcp/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.