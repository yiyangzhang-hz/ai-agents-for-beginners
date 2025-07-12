<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ad5de6a6388d02c145a92dd04358bab",
  "translation_date": "2025-07-12T13:38:00+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "br"
}
-->
[![AI Agents In Production](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.br.png)](https://youtu.be/l4TP6IyJxmQ?si=IvCW3cbw0NJ2mUMV)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_
# Agentes de IA em Produção

## Introdução

Nesta aula, você vai aprender:

- Como planejar a implantação do seu Agente de IA em produção de forma eficaz.
- Erros comuns e problemas que podem surgir ao implantar seu Agente de IA em produção.
- Como gerenciar custos mantendo o desempenho do seu Agente de IA.

## Objetivos de Aprendizagem

Após concluir esta aula, você saberá/entenderá:

- Técnicas para melhorar o desempenho, os custos e a eficácia de um sistema de Agente de IA em produção.
- O que e como avaliar seus Agentes de IA.
- Como controlar os custos ao implantar Agentes de IA em produção.

É importante implantar Agentes de IA confiáveis. Confira também a aula "Building Trustworthy AI Agents".

## Avaliando Agentes de IA

Antes, durante e depois de implantar Agentes de IA, ter um sistema adequado para avaliá-los é fundamental. Isso garante que seu sistema esteja alinhado com seus objetivos e os dos seus usuários.

Para avaliar um Agente de IA, é importante conseguir avaliar não apenas a saída do agente, mas todo o sistema em que ele opera. Isso inclui, mas não se limita a:

- A solicitação inicial ao modelo.
- A capacidade do agente de identificar a intenção do usuário.
- A capacidade do agente de escolher a ferramenta certa para executar a tarefa.
- A resposta da ferramenta ao pedido do agente.
- A capacidade do agente de interpretar a resposta da ferramenta.
- O feedback do usuário à resposta do agente.

Isso permite identificar áreas para melhorias de forma mais modular. Você pode então monitorar o efeito das mudanças em modelos, prompts, ferramentas e outros componentes com maior eficiência.

## Problemas Comuns e Possíveis Soluções com Agentes de IA

| **Problema**                                   | **Possível Solução**                                                                                                                                                                                                       |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agente de IA não executa tarefas de forma consistente | - Refine o prompt dado ao Agente de IA; seja claro nos objetivos.<br>- Identifique onde dividir as tarefas em subtarefas e delegá-las a múltiplos agentes pode ajudar.                                                     |
| Agente de IA entra em loops contínuos          | - Garanta termos e condições claros de término para que o Agente saiba quando parar o processo.<br>- Para tarefas complexas que exigem raciocínio e planejamento, use um modelo maior especializado nessas tarefas.          |
| Chamadas de ferramentas do Agente de IA não funcionam bem | - Teste e valide a saída da ferramenta fora do sistema do agente.<br>- Refine os parâmetros definidos, prompts e nomes das ferramentas.                                                                                   |
| Sistema Multi-Agente não funciona de forma consistente | - Refine os prompts dados a cada agente para garantir que sejam específicos e distintos entre si.<br>- Construa um sistema hierárquico usando um agente "roteador" ou controlador para determinar qual agente é o correto. |

## Gerenciando Custos

Aqui estão algumas estratégias para gerenciar os custos de implantar Agentes de IA em produção:

- **Cache de Respostas** - Identificar solicitações e tarefas comuns e fornecer as respostas antes que passem pelo seu sistema agente é uma boa forma de reduzir o volume de pedidos semelhantes. Você pode até implementar um fluxo para identificar o quão semelhante uma solicitação é às suas respostas em cache usando modelos de IA mais simples.

- **Usar Modelos Menores** - Modelos de Linguagem Pequenos (SLMs) podem ter bom desempenho em certos casos de uso agente e reduzirão os custos significativamente. Como mencionado antes, construir um sistema de avaliação para determinar e comparar o desempenho em relação a modelos maiores é a melhor forma de entender como um SLM se sai no seu caso.

- **Usar um Modelo Roteador** - Uma estratégia semelhante é usar uma diversidade de modelos e tamanhos. Você pode usar um LLM/SLM ou função serverless para direcionar as solicitações, com base na complexidade, para os modelos mais adequados. Isso também ajuda a reduzir custos, garantindo desempenho nas tarefas certas.

## Parabéns

Esta é atualmente a última aula de "AI Agents for Beginners".

Planejamos continuar adicionando aulas com base no feedback e nas mudanças desta indústria em constante crescimento, então volte em breve.

Se quiser continuar aprendendo e construindo com Agentes de IA, junte-se ao <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a>.

Lá realizamos workshops, mesas-redondas comunitárias e sessões de "pergunte-me qualquer coisa".

Também temos uma coleção Learn com materiais adicionais que podem ajudar você a começar a construir Agentes de IA em produção.

## Aula Anterior

[Metacognition Design Pattern](../09-metacognition/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.