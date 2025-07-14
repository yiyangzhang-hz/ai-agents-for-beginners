<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f57852cac3a86c4a5ef47f793cc12178",
  "translation_date": "2025-07-12T10:26:13+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "br"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.br.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_

# Construindo Agentes de IA Confiáveis

## Introdução

Nesta aula, abordaremos:

- Como construir e implantar Agentes de IA seguros e eficazes
- Considerações importantes de segurança ao desenvolver Agentes de IA
- Como manter a privacidade dos dados e dos usuários ao desenvolver Agentes de IA

## Objetivos de Aprendizagem

Após concluir esta aula, você saberá como:

- Identificar e mitigar riscos ao criar Agentes de IA
- Implementar medidas de segurança para garantir que dados e acessos sejam gerenciados adequadamente
- Criar Agentes de IA que preservem a privacidade dos dados e ofereçam uma experiência de usuário de qualidade

## Segurança

Vamos começar analisando como construir aplicações agentivas seguras. Segurança significa que o agente de IA atua conforme o esperado. Como desenvolvedores de aplicações agentivas, dispomos de métodos e ferramentas para maximizar a segurança:

### Construindo uma Estrutura de Mensagem do Sistema

Se você já desenvolveu uma aplicação de IA usando Large Language Models (LLMs), sabe a importância de criar um prompt ou mensagem de sistema robusta. Esses prompts estabelecem as regras meta, instruções e diretrizes sobre como o LLM interagirá com o usuário e os dados.

Para Agentes de IA, o prompt do sistema é ainda mais importante, pois eles precisarão de instruções altamente específicas para executar as tarefas que projetamos para eles.

Para criar prompts de sistema escaláveis, podemos usar uma estrutura de mensagem do sistema para construir um ou mais agentes em nossa aplicação:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.br.png)

#### Passo 1: Criar uma Mensagem Meta do Sistema

O meta prompt será usado por um LLM para gerar os prompts do sistema para os agentes que criarmos. Projetamos isso como um modelo para que possamos criar múltiplos agentes de forma eficiente, se necessário.

Aqui está um exemplo de mensagem meta do sistema que forneceríamos ao LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Passo 2: Criar um prompt básico

O próximo passo é criar um prompt básico para descrever o Agente de IA. Você deve incluir o papel do agente, as tarefas que ele realizará e quaisquer outras responsabilidades.

Aqui está um exemplo:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Passo 3: Fornecer a Mensagem Básica do Sistema ao LLM

Agora podemos otimizar essa mensagem do sistema fornecendo a mensagem meta do sistema como a mensagem do sistema e nossa mensagem básica.

Isso produzirá uma mensagem do sistema melhor projetada para guiar nossos agentes de IA:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Passo 4: Iterar e Melhorar

O valor dessa estrutura de mensagem do sistema é permitir escalar a criação de mensagens do sistema para múltiplos agentes com mais facilidade, além de melhorar suas mensagens ao longo do tempo. É raro que uma mensagem do sistema funcione perfeitamente na primeira tentativa para todo o seu caso de uso. Poder fazer pequenos ajustes e melhorias alterando a mensagem básica e executando-a pelo sistema permitirá comparar e avaliar os resultados.

## Entendendo as Ameaças

Para construir agentes de IA confiáveis, é importante entender e mitigar os riscos e ameaças ao seu agente de IA. Vamos analisar algumas das diferentes ameaças aos agentes de IA e como você pode planejar e se preparar melhor para elas.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.br.png)

### Tarefa e Instrução

**Descrição:** Atacantes tentam alterar as instruções ou objetivos do agente de IA por meio de prompts ou manipulação das entradas.

**Mitigação:** Execute verificações de validação e filtros de entrada para detectar prompts potencialmente perigosos antes que sejam processados pelo Agente de IA. Como esses ataques geralmente exigem interação frequente com o agente, limitar o número de interações em uma conversa é outra forma de prevenir esse tipo de ataque.

### Acesso a Sistemas Críticos

**Descrição:** Se um agente de IA tem acesso a sistemas e serviços que armazenam dados sensíveis, atacantes podem comprometer a comunicação entre o agente e esses serviços. Isso pode ocorrer por ataques diretos ou tentativas indiretas de obter informações sobre esses sistemas por meio do agente.

**Mitigação:** Os agentes de IA devem ter acesso aos sistemas apenas quando necessário para evitar esses tipos de ataques. A comunicação entre o agente e o sistema também deve ser segura. Implementar autenticação e controle de acesso é outra forma de proteger essas informações.

### Sobrecarga de Recursos e Serviços

**Descrição:** Agentes de IA podem acessar diferentes ferramentas e serviços para completar tarefas. Atacantes podem explorar essa capacidade para atacar esses serviços enviando um grande volume de solicitações por meio do agente, o que pode causar falhas no sistema ou custos elevados.

**Mitigação:** Implemente políticas para limitar o número de solicitações que um agente de IA pode fazer a um serviço. Limitar o número de interações e solicitações ao seu agente de IA é outra forma de prevenir esses tipos de ataques.

### Envenenamento da Base de Conhecimento

**Descrição:** Esse tipo de ataque não mira diretamente o agente de IA, mas sim a base de conhecimento e outros serviços que o agente utilizará. Pode envolver a corrupção dos dados ou informações que o agente usará para realizar uma tarefa, levando a respostas tendenciosas ou indesejadas para o usuário.

**Mitigação:** Realize verificações regulares dos dados que o agente de IA usará em seus fluxos de trabalho. Garanta que o acesso a esses dados seja seguro e que apenas pessoas confiáveis possam alterá-los para evitar esse tipo de ataque.

### Erros em Cascata

**Descrição:** Agentes de IA acessam várias ferramentas e serviços para completar tarefas. Erros causados por atacantes podem levar a falhas em outros sistemas conectados ao agente, fazendo com que o ataque se espalhe e se torne mais difícil de solucionar.

**Mitigação:** Uma forma de evitar isso é fazer o agente operar em um ambiente limitado, como executar tarefas em um container Docker, para prevenir ataques diretos ao sistema. Criar mecanismos de fallback e lógica de repetição quando certos sistemas responderem com erro é outra forma de evitar falhas maiores.

## Humano no Loop

Outra forma eficaz de construir sistemas confiáveis de Agentes de IA é usar o conceito de Humano no Loop. Isso cria um fluxo onde os usuários podem fornecer feedback aos agentes durante a execução. Os usuários atuam essencialmente como agentes em um sistema multiagente, aprovando ou encerrando o processo em andamento.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.br.png)

Aqui está um trecho de código usando AutoGen para mostrar como esse conceito é implementado:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Conclusão

Construir agentes de IA confiáveis requer um design cuidadoso, medidas robustas de segurança e iteração contínua. Ao implementar sistemas estruturados de meta prompting, entender as ameaças potenciais e aplicar estratégias de mitigação, os desenvolvedores podem criar agentes de IA que sejam seguros e eficazes. Além disso, incorporar a abordagem de humano no loop garante que os agentes permaneçam alinhados às necessidades dos usuários, minimizando riscos. À medida que a IA evolui, manter uma postura proativa em relação à segurança, privacidade e considerações éticas será fundamental para fomentar confiança e confiabilidade em sistemas baseados em IA.

## Recursos Adicionais

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Visão geral de IA Responsável</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Avaliação de modelos e aplicações de IA generativa</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mensagens de sistema para segurança</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modelo de Avaliação de Riscos</a>

## Aula Anterior

[Agentic RAG](../05-agentic-rag/README.md)

## Próxima Aula

[Planning Design Pattern](../07-planning-design/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.