<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:40:07+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "br"
}
-->
for resolver tarefas complexas.

## Resumo

Neste artigo, vimos um exemplo de como criar um planejador que pode selecionar dinamicamente os agentes disponíveis definidos. A saída do Planejador decompõe as tarefas e atribui os agentes para que possam ser executadas. Presume-se que os agentes tenham acesso às funções/ferramentas necessárias para realizar a tarefa. Além dos agentes, você pode incluir outros padrões como reflexão, sumarizador e chat round robin para personalizar ainda mais.

## Recursos Adicionais

* AutoGen Magnetic One - Um sistema multiagente generalista para resolver tarefas complexas que alcançou resultados impressionantes em vários benchmarks desafiadores de agentes. Referência:

. Nesta implementação, o orquestrador cria um plano específico para a tarefa e delega essas tarefas aos agentes disponíveis. Além do planejamento, o orquestrador também emprega um mecanismo de monitoramento para acompanhar o progresso da tarefa e refaz o planejamento conforme necessário.

## Aula Anterior

[Construindo Agentes de IA Confiáveis](../06-building-trustworthy-agents/README.md)

## Próxima Aula

[Padrão de Design Multi-Agente](../08-multi-agent/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.