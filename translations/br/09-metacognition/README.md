<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8cbf460468c802c7994aa62e0e0779c9",
  "translation_date": "2025-07-12T12:27:42+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "br"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.br.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Clique na imagem acima para assistir ao vídeo desta aula)_
# Metacognição em Agentes de IA

## Introdução

Bem-vindo à aula sobre metacognição em agentes de IA! Este capítulo é voltado para iniciantes que têm curiosidade sobre como agentes de IA podem refletir sobre seus próprios processos de pensamento. Ao final desta lição, você entenderá conceitos-chave e estará equipado com exemplos práticos para aplicar a metacognição no design de agentes de IA.

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

1. Compreender as implicações dos ciclos de raciocínio nas definições de agentes.
2. Utilizar técnicas de planejamento e avaliação para ajudar agentes autocorretivos.
3. Criar seus próprios agentes capazes de manipular código para realizar tarefas.

## Introdução à Metacognição

Metacognição refere-se aos processos cognitivos de ordem superior que envolvem pensar sobre o próprio pensamento. Para agentes de IA, isso significa ser capaz de avaliar e ajustar suas ações com base na autoconsciência e em experiências passadas. Metacognição, ou "pensar sobre pensar", é um conceito importante no desenvolvimento de sistemas de IA agentivos. Envolve sistemas de IA que estão cientes de seus próprios processos internos e que podem monitorar, regular e adaptar seu comportamento de acordo. Assim como fazemos quando interpretamos o ambiente ou analisamos um problema. Essa autoconsciência pode ajudar sistemas de IA a tomar decisões melhores, identificar erros e melhorar seu desempenho ao longo do tempo — voltando à discussão do teste de Turing e ao debate sobre se a IA vai dominar o mundo.

No contexto de sistemas de IA agentivos, a metacognição pode ajudar a enfrentar vários desafios, como:
- Transparência: Garantir que os sistemas de IA possam explicar seu raciocínio e decisões.
- Raciocínio: Aprimorar a capacidade dos sistemas de IA de sintetizar informações e tomar decisões sólidas.
- Adaptação: Permitir que os sistemas de IA se ajustem a novos ambientes e condições mutáveis.
- Percepção: Melhorar a precisão dos sistemas de IA no reconhecimento e interpretação de dados do ambiente.

### O que é Metacognição?

Metacognição, ou "pensar sobre pensar", é um processo cognitivo de ordem superior que envolve autoconsciência e autorregulação dos próprios processos cognitivos. No âmbito da IA, a metacognição capacita os agentes a avaliar e adaptar suas estratégias e ações, levando a uma melhora na resolução de problemas e na tomada de decisões. Ao entender a metacognição, você pode projetar agentes de IA que sejam não apenas mais inteligentes, mas também mais adaptáveis e eficientes. Na verdadeira metacognição, você veria a IA raciocinando explicitamente sobre seu próprio raciocínio.

Exemplo: “Priorizei voos mais baratos porque... posso estar perdendo voos diretos, então vou verificar novamente.”  
Acompanhar como ou por que escolheu uma determinada rota.  
- Notar que cometeu erros por confiar demais nas preferências do usuário da última vez, então modifica sua estratégia de decisão, não apenas a recomendação final.  
- Diagnosticar padrões como: “Sempre que vejo o usuário mencionar ‘muito cheio’, não devo apenas remover certas atrações, mas também refletir que meu método de escolher as ‘principais atrações’ está falho se eu sempre classifico pela popularidade.”

### Importância da Metacognição em Agentes de IA

A metacognição desempenha um papel crucial no design de agentes de IA por vários motivos:

![Importância da Metacognição](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.br.png)

- Autorreflexão: Os agentes podem avaliar seu próprio desempenho e identificar áreas para melhoria.
- Adaptabilidade: Os agentes podem modificar suas estratégias com base em experiências passadas e ambientes em mudança.
- Correção de Erros: Os agentes podem detectar e corrigir erros de forma autônoma, resultando em resultados mais precisos.
- Gestão de Recursos: Os agentes podem otimizar o uso de recursos, como tempo e poder computacional, planejando e avaliando suas ações.

## Componentes de um Agente de IA

Antes de mergulhar nos processos metacognitivos, é essencial entender os componentes básicos de um agente de IA. Um agente de IA normalmente consiste em:

- Persona: A personalidade e características do agente, que definem como ele interage com os usuários.
- Ferramentas: As capacidades e funções que o agente pode executar.
- Habilidades: O conhecimento e a expertise que o agente possui.

Esses componentes trabalham juntos para criar uma "unidade de expertise" capaz de realizar tarefas específicas.

**Exemplo**:  
Considere um agente de viagens, um serviço que não apenas planeja suas férias, mas também ajusta seu caminho com base em dados em tempo real e experiências anteriores dos clientes.

### Exemplo: Metacognição em um Serviço de Agente de Viagens

Imagine que você está projetando um serviço de agente de viagens alimentado por IA. Esse agente, "Travel Agent", ajuda os usuários a planejar suas férias. Para incorporar metacognição, o Travel Agent precisa avaliar e ajustar suas ações com base na autoconsciência e em experiências passadas. Veja como a metacognição pode atuar:

#### Tarefa Atual

A tarefa atual é ajudar um usuário a planejar uma viagem para Paris.

#### Passos para Completar a Tarefa

1. **Coletar Preferências do Usuário**: Perguntar ao usuário sobre datas de viagem, orçamento, interesses (ex.: museus, gastronomia, compras) e quaisquer requisitos específicos.
2. **Buscar Informações**: Pesquisar opções de voos, acomodações, atrações e restaurantes que correspondam às preferências do usuário.
3. **Gerar Recomendações**: Fornecer um itinerário personalizado com detalhes de voos, reservas de hotel e atividades sugeridas.
4. **Ajustar com Base no Feedback**: Pedir feedback ao usuário sobre as recomendações e fazer os ajustes necessários.

#### Recursos Necessários

- Acesso a bancos de dados de voos e hotéis.
- Informações sobre atrações e restaurantes parisienses.
- Dados de feedback de usuários de interações anteriores.

#### Experiência e Autorreflexão

O Travel Agent usa metacognição para avaliar seu desempenho e aprender com experiências passadas. Por exemplo:

1. **Analisando Feedback do Usuário**: O Travel Agent revisa o feedback para determinar quais recomendações foram bem recebidas e quais não foram, ajustando suas sugestões futuras.
2. **Adaptabilidade**: Se um usuário mencionou anteriormente que não gosta de lugares lotados, o Travel Agent evitará recomendar pontos turísticos populares em horários de pico.
3. **Correção de Erros**: Se o Travel Agent cometeu um erro em uma reserva anterior, como sugerir um hotel lotado, ele aprende a verificar a disponibilidade com mais rigor antes de recomendar.

#### Exemplo Prático para Desenvolvedores

Aqui está um exemplo simplificado de como o código do Travel Agent pode parecer ao incorporar metacognição:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Por que a Metacognição é Importante

- **Autorreflexão**: Os agentes podem analisar seu desempenho e identificar áreas para melhoria.
- **Adaptabilidade**: Os agentes podem modificar estratégias com base em feedback e condições mutáveis.
- **Correção de Erros**: Os agentes podem detectar e corrigir erros de forma autônoma.
- **Gestão de Recursos**: Os agentes podem otimizar o uso de recursos, como tempo e poder computacional.

Ao incorporar metacognição, o Travel Agent pode fornecer recomendações de viagem mais personalizadas e precisas, melhorando a experiência geral do usuário.

---

## 2. Planejamento em Agentes

O planejamento é um componente crítico do comportamento de agentes de IA. Envolve delinear os passos necessários para alcançar um objetivo, considerando o estado atual, recursos e possíveis obstáculos.

### Elementos do Planejamento

- **Tarefa Atual**: Definir claramente a tarefa.
- **Passos para Completar a Tarefa**: Dividir a tarefa em etapas gerenciáveis.
- **Recursos Necessários**: Identificar os recursos necessários.
- **Experiência**: Utilizar experiências passadas para informar o planejamento.

**Exemplo**:  
Aqui estão os passos que o Travel Agent precisa seguir para ajudar um usuário a planejar sua viagem de forma eficaz:

### Passos para o Travel Agent

1. **Coletar Preferências do Usuário**  
   - Perguntar ao usuário detalhes sobre datas de viagem, orçamento, interesses e quaisquer requisitos específicos.  
   - Exemplos: "Quando você planeja viajar?" "Qual é a sua faixa de orçamento?" "Quais atividades você gosta de fazer nas férias?"

2. **Buscar Informações**  
   - Pesquisar opções de viagem relevantes com base nas preferências do usuário.  
   - **Voos**: Procurar voos disponíveis dentro do orçamento e datas preferidas.  
   - **Acomodações**: Encontrar hotéis ou imóveis para aluguel que correspondam às preferências de localização, preço e comodidades.  
   - **Atrações e Restaurantes**: Identificar atrações populares, atividades e opções gastronômicas alinhadas aos interesses do usuário.

3. **Gerar Recomendações**  
   - Compilar as informações obtidas em um itinerário personalizado.  
   - Fornecer detalhes como opções de voo, reservas de hotel e atividades sugeridas, garantindo que as recomendações estejam alinhadas às preferências do usuário.

4. **Apresentar Itinerário ao Usuário**  
   - Compartilhar o itinerário proposto para revisão do usuário.  
   - Exemplo: "Aqui está um itinerário sugerido para sua viagem a Paris. Inclui detalhes de voos, reservas de hotel e uma lista de atividades e restaurantes recomendados. O que você acha?"

5. **Coletar Feedback**  
   - Pedir ao usuário um retorno sobre o itinerário proposto.  
   - Exemplos: "Você gostou das opções de voo?" "O hotel atende às suas necessidades?" "Há alguma atividade que você gostaria de adicionar ou remover?"

6. **Ajustar com Base no Feedback**  
   - Modificar o itinerário conforme o feedback do usuário.  
   - Fazer as alterações necessárias nas recomendações de voo, acomodação e atividades para melhor atender às preferências do usuário.

7. **Confirmação Final**  
   - Apresentar o itinerário atualizado para confirmação final do usuário.  
   - Exemplo: "Fiz os ajustes com base no seu feedback. Aqui está o itinerário atualizado. Está tudo certo para você?"

8. **Reservar e Confirmar**  
   - Após a aprovação do usuário, proceder com a reserva de voos, acomodações e atividades pré-planejadas.  
   - Enviar detalhes de confirmação ao usuário.

9. **Fornecer Suporte Contínuo**  
   - Permanecer disponível para ajudar o usuário com quaisquer mudanças ou solicitações adicionais antes e durante a viagem.  
   - Exemplo: "Se precisar de mais alguma coisa durante a viagem, pode me chamar a qualquer momento!"

### Exemplo de Interação

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Sistema Corretivo RAG

Primeiro, vamos entender a diferença entre RAG Tool e Pre-emptive Context Load

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.br.png)

### Retrieval-Augmented Generation (RAG)

RAG combina um sistema de recuperação com um modelo generativo. Quando uma consulta é feita, o sistema de recuperação busca documentos ou dados relevantes de uma fonte externa, e essa informação recuperada é usada para enriquecer a entrada do modelo generativo. Isso ajuda o modelo a gerar respostas mais precisas e contextualmente relevantes.

Em um sistema RAG, o agente recupera informações relevantes de uma base de conhecimento e as utiliza para gerar respostas ou ações apropriadas.

### Abordagem Corretiva RAG

A abordagem Corretiva RAG foca em usar técnicas RAG para corrigir erros e melhorar a precisão dos agentes de IA. Isso envolve:

1. **Técnica de Prompting**: Usar prompts específicos para guiar o agente na recuperação de informações relevantes.
2. **Ferramenta**: Implementar algoritmos e mecanismos que permitam ao agente avaliar a relevância das informações recuperadas e gerar respostas precisas.
3. **Avaliação**: Avaliar continuamente o desempenho do agente e fazer ajustes para melhorar sua precisão e eficiência.

#### Exemplo: RAG Corretivo em um Agente de Busca

Considere um agente de busca que recupera informações da web para responder a consultas dos usuários. A abordagem Corretiva RAG pode envolver:

1. **Técnica de Prompting**: Formular consultas de busca baseadas na entrada do usuário.
2. **Ferramenta**: Usar processamento de linguagem natural e algoritmos de aprendizado de máquina para classificar e filtrar os resultados da busca.
3. **Avaliação**: Analisar o feedback do usuário para identificar e corrigir imprecisões nas informações recuperadas.

### RAG Corretivo no Travel Agent

O RAG Corretivo (Retrieval-Augmented Generation) aprimora a capacidade da IA de recuperar e gerar informações enquanto corrige eventuais imprecisões. Vamos ver como o Travel Agent pode usar a abordagem Corretiva RAG para fornecer recomendações de viagem mais precisas e relevantes.

Isso envolve:

- **Técnica de Prompting:** Usar prompts específicos para guiar o agente na recuperação de informações relevantes.
- **Ferramenta:** Implementar algoritmos e mecanismos que permitam ao agente avaliar a relevância das informações recuperadas e gerar respostas precisas.
- **Avaliação:** Avaliar continuamente o desempenho do agente e fazer ajustes para melhorar sua precisão e eficiência.

#### Passos para Implementar o RAG Corretivo no Travel Agent

1. **Interação Inicial com o Usuário**  
   - O Travel Agent coleta as preferências iniciais do usuário, como destino, datas de viagem, orçamento e interesses.  
   - Exemplo:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Recuperação de Informações**  
   - O Travel Agent recupera informações sobre voos, acomodações, atrações e restaurantes com base nas preferências do usuário.  
   - Exemplo:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Geração de Recomendações Iniciais**  
   - O Travel Agent usa as informações recuperadas para gerar um itinerário personalizado.  
   - Exemplo:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Coleta de Feedback do Usuário**  
   - O Travel Agent solicita feedback do usuário sobre as recomendações iniciais.  
   - Exemplo:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Processo Corretivo RAG**  
   - **Técnica de Prompting**: O Travel Agent formula novas consultas de busca com base no feedback do usuário.  
     - Exemplo:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Ferramenta**: O Travel Agent usa algoritmos para classificar e filtrar os novos resultados de busca, enfatizando a relevância com base no feedback do usuário.  
     - Exemplo:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Avaliação**: O Travel Agent avalia continuamente a relevância e precisão de suas recomendações analisando o feedback do usuário e fazendo os ajustes necessários.  
     - Exemplo:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Exemplo Prático

Aqui está um exemplo simplificado em Python incorporando a abordagem Corretiva RAG no Travel Agent:
### Carregamento Preemptivo de Contexto

O Carregamento Preemptivo de Contexto envolve carregar informações relevantes ou de fundo no modelo antes de processar uma consulta. Isso significa que o modelo tem acesso a essas informações desde o início, o que pode ajudá-lo a gerar respostas mais informadas sem precisar buscar dados adicionais durante o processo.

Aqui está um exemplo simplificado de como um carregamento preemptivo de contexto pode ser feito para uma aplicação de agente de viagens em Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Explicação

1. **Inicialização (método `__init__`)**: A classe `TravelAgent` pré-carrega um dicionário contendo informações sobre destinos populares como Paris, Tóquio, Nova York e Sydney. Esse dicionário inclui detalhes como país, moeda, idioma e principais atrações de cada destino.

2. **Recuperação de Informações (método `get_destination_info`)**: Quando um usuário consulta sobre um destino específico, o método `get_destination_info` busca as informações relevantes no dicionário pré-carregado.

Ao pré-carregar o contexto, a aplicação do agente de viagens pode responder rapidamente às consultas dos usuários sem precisar buscar essas informações em uma fonte externa em tempo real. Isso torna a aplicação mais eficiente e responsiva.

### Inicializando o Plano com um Objetivo Antes de Iterar

Inicializar um plano com um objetivo significa começar com uma meta clara ou resultado desejado em mente. Ao definir esse objetivo desde o início, o modelo pode usá-lo como um princípio orientador durante o processo iterativo. Isso ajuda a garantir que cada iteração se aproxime do resultado esperado, tornando o processo mais eficiente e focado.

Aqui está um exemplo de como você pode inicializar um plano de viagem com um objetivo antes de iterar para um agente de viagens em Python:

### Cenário

Um agente de viagens quer planejar uma viagem personalizada para um cliente. O objetivo é criar um roteiro de viagem que maximize a satisfação do cliente com base em suas preferências e orçamento.

### Passos

1. Definir as preferências e o orçamento do cliente.  
2. Inicializar o plano inicial com base nessas preferências.  
3. Iterar para refinar o plano, otimizando para a satisfação do cliente.

#### Código Python

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Explicação do Código

1. **Inicialização (método `__init__`)**: A classe `TravelAgent` é inicializada com uma lista de destinos potenciais, cada um com atributos como nome, custo e tipo de atividade.

2. **Inicializando o Plano (método `bootstrap_plan`)**: Este método cria um plano inicial de viagem com base nas preferências e orçamento do cliente. Ele percorre a lista de destinos e os adiciona ao plano se corresponderem às preferências do cliente e estiverem dentro do orçamento.

3. **Correspondência de Preferências (método `match_preferences`)**: Este método verifica se um destino corresponde às preferências do cliente.

4. **Iterando o Plano (método `iterate_plan`)**: Este método refina o plano inicial tentando substituir cada destino no plano por uma opção melhor, considerando as preferências do cliente e as restrições orçamentárias.

5. **Calculando o Custo (método `calculate_cost`)**: Este método calcula o custo total do plano atual, incluindo um possível novo destino.

#### Exemplo de Uso

- **Plano Inicial**: O agente de viagens cria um plano inicial baseado nas preferências do cliente por passeios turísticos e um orçamento de $2000.  
- **Plano Refinado**: O agente de viagens itera o plano, otimizando para as preferências e orçamento do cliente.

Ao inicializar o plano com um objetivo claro (por exemplo, maximizar a satisfação do cliente) e iterar para refiná-lo, o agente de viagens pode criar um roteiro personalizado e otimizado para o cliente. Essa abordagem garante que o plano de viagem esteja alinhado com as preferências e orçamento do cliente desde o início e melhore a cada iteração.

### Aproveitando LLM para Reordenação e Pontuação

Modelos de Linguagem de Grande Porte (LLMs) podem ser usados para reordenar e pontuar avaliando a relevância e qualidade dos documentos recuperados ou respostas geradas. Veja como funciona:

**Recuperação:** A etapa inicial busca um conjunto de documentos ou respostas candidatas com base na consulta.

**Reordenação:** O LLM avalia esses candidatos e os reordena com base na relevância e qualidade. Essa etapa garante que as informações mais relevantes e de melhor qualidade sejam apresentadas primeiro.

**Pontuação:** O LLM atribui pontuações a cada candidato, refletindo sua relevância e qualidade. Isso ajuda a selecionar a melhor resposta ou documento para o usuário.

Ao usar LLMs para reordenação e pontuação, o sistema pode fornecer informações mais precisas e contextualmente relevantes, melhorando a experiência geral do usuário.

Aqui está um exemplo de como um agente de viagens pode usar um Modelo de Linguagem de Grande Porte (LLM) para reordenar e pontuar destinos de viagem com base nas preferências do usuário em Python:

#### Cenário - Viagem baseada em Preferências

Um agente de viagens quer recomendar os melhores destinos para um cliente com base em suas preferências. O LLM ajudará a reordenar e pontuar os destinos para garantir que as opções mais relevantes sejam apresentadas.

#### Passos:

1. Coletar as preferências do usuário.  
2. Recuperar uma lista de destinos potenciais.  
3. Usar o LLM para reordenar e pontuar os destinos com base nas preferências do usuário.

Veja como atualizar o exemplo anterior para usar os Serviços Azure OpenAI:

#### Requisitos

1. Você precisa ter uma assinatura Azure.  
2. Criar um recurso Azure OpenAI e obter sua chave de API.

#### Exemplo de Código Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Explicação do Código - Preference Booker

1. **Inicialização**: A classe `TravelAgent` é inicializada com uma lista de destinos potenciais, cada um com atributos como nome e descrição.

2. **Obtendo Recomendações (método `get_recommendations`)**: Este método gera um prompt para o serviço Azure OpenAI com base nas preferências do usuário e faz uma requisição HTTP POST para a API Azure OpenAI para obter destinos reordenados e pontuados.

3. **Gerando Prompt (método `generate_prompt`)**: Este método constrói um prompt para o Azure OpenAI, incluindo as preferências do usuário e a lista de destinos. O prompt orienta o modelo a reordenar e pontuar os destinos com base nas preferências fornecidas.

4. **Chamada à API**: A biblioteca `requests` é usada para fazer uma requisição HTTP POST ao endpoint da API Azure OpenAI. A resposta contém os destinos reordenados e pontuados.

5. **Exemplo de Uso**: O agente de viagens coleta as preferências do usuário (por exemplo, interesse em passeios turísticos e cultura diversa) e usa o serviço Azure OpenAI para obter recomendações reordenadas e pontuadas para destinos de viagem.

Certifique-se de substituir `your_azure_openai_api_key` pela sua chave real da API Azure OpenAI e `https://your-endpoint.com/...` pela URL real do endpoint da sua implantação Azure OpenAI.

Ao aproveitar o LLM para reordenação e pontuação, o agente de viagens pode fornecer recomendações de viagem mais personalizadas e relevantes para os clientes, melhorando a experiência geral.

### RAG: Técnica de Prompting vs Ferramenta

Retrieval-Augmented Generation (RAG) pode ser tanto uma técnica de prompting quanto uma ferramenta no desenvolvimento de agentes de IA. Entender a diferença entre os dois pode ajudar você a usar o RAG de forma mais eficaz em seus projetos.

#### RAG como Técnica de Prompting

**O que é?**

- Como técnica de prompting, RAG envolve formular consultas ou prompts específicos para guiar a recuperação de informações relevantes de um grande corpus ou banco de dados. Essas informações são então usadas para gerar respostas ou ações.

**Como funciona:**

1. **Formular Prompts**: Criar prompts ou consultas bem estruturadas com base na tarefa ou na entrada do usuário.  
2. **Recuperar Informações**: Usar os prompts para buscar dados relevantes em uma base de conhecimento ou conjunto de dados pré-existente.  
3. **Gerar Resposta**: Combinar as informações recuperadas com modelos generativos de IA para produzir uma resposta abrangente e coerente.

**Exemplo no Agente de Viagens**:

- Entrada do Usuário: "Quero visitar museus em Paris."  
- Prompt: "Encontre os principais museus em Paris."  
- Informação Recuperada: Detalhes sobre o Museu do Louvre, Musée d'Orsay, etc.  
- Resposta Gerada: "Aqui estão alguns dos principais museus em Paris: Museu do Louvre, Musée d'Orsay e Centre Pompidou."

#### RAG como Ferramenta

**O que é?**

- Como ferramenta, RAG é um sistema integrado que automatiza o processo de recuperação e geração, facilitando para os desenvolvedores a implementação de funcionalidades complexas de IA sem precisar criar prompts manualmente para cada consulta.

**Como funciona:**

1. **Integração**: Incorporar o RAG na arquitetura do agente de IA, permitindo que ele gerencie automaticamente as tarefas de recuperação e geração.  
2. **Automação**: A ferramenta gerencia todo o processo, desde receber a entrada do usuário até gerar a resposta final, sem necessidade de prompts explícitos para cada etapa.  
3. **Eficiência**: Melhora o desempenho do agente ao simplificar o processo de recuperação e geração, possibilitando respostas mais rápidas e precisas.

**Exemplo no Agente de Viagens**:

- Entrada do Usuário: "Quero visitar museus em Paris."  
- Ferramenta RAG: Recupera automaticamente informações sobre museus e gera uma resposta.  
- Resposta Gerada: "Aqui estão alguns dos principais museus em Paris: Museu do Louvre, Musée d'Orsay e Centre Pompidou."

### Comparação

| Aspecto                | Técnica de Prompting                                      | Ferramenta                                             |
|------------------------|----------------------------------------------------------|-------------------------------------------------------|
| **Manual vs Automático**| Formulação manual de prompts para cada consulta.         | Processo automatizado para recuperação e geração.     |
| **Controle**           | Oferece mais controle sobre o processo de recuperação.   | Simplifica e automatiza a recuperação e geração.      |
| **Flexibilidade**      | Permite prompts personalizados conforme necessidades.    | Mais eficiente para implementações em larga escala.  |
| **Complexidade**       | Requer criação e ajuste de prompts.                       | Mais fácil de integrar na arquitetura do agente de IA.|

### Exemplos Práticos

**Exemplo de Técnica de Prompting:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Exemplo de Ferramenta:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Avaliando a Relevância

Avaliar a relevância é um aspecto crucial do desempenho de agentes de IA. Isso garante que as informações recuperadas e geradas pelo agente sejam apropriadas, precisas e úteis para o usuário. Vamos explorar como avaliar a relevância em agentes de IA, incluindo exemplos práticos e técnicas.

#### Conceitos-Chave na Avaliação de Relevância

1. **Consciência de Contexto**:  
   - O agente deve entender o contexto da consulta do usuário para recuperar e gerar informações relevantes.  
   - Exemplo: Se um usuário pede "melhores restaurantes em Paris", o agente deve considerar as preferências do usuário, como tipo de culinária e orçamento.

2. **Precisão**:  
   - As informações fornecidas pelo agente devem ser factualmente corretas e atualizadas.  
   - Exemplo: Recomendar restaurantes que estejam abertos atualmente e com boas avaliações, em vez de opções desatualizadas ou fechadas.

3. **Intenção do Usuário**:  
   - O agente deve inferir a intenção do usuário por trás da consulta para fornecer a informação mais relevante.  
   - Exemplo: Se o usuário pede "hotéis econômicos", o agente deve priorizar opções acessíveis.

4. **Ciclo de Feedback**:  
   - Coletar e analisar continuamente o feedback do usuário ajuda o agente a refinar seu processo de avaliação de relevância.  
   - Exemplo: Incorporar avaliações e feedbacks dos usuários sobre recomendações anteriores para melhorar respostas futuras.

#### Técnicas Práticas para Avaliar Relevância

1. **Pontuação de Relevância**:  
   - Atribuir uma pontuação de relevância a cada item recuperado com base em quão bem ele corresponde à consulta e preferências do usuário.  
   - Exemplo:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtragem e Classificação**:  
   - Filtrar itens irrelevantes e classificar os restantes com base nas pontuações de relevância.  
   - Exemplo:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Processamento de Linguagem Natural (PLN)**:  
   - Usar técnicas de PLN para entender a consulta do usuário e recuperar informações relevantes.  
   - Exemplo:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integração de Feedback do Usuário**:  
   - Coletar feedback dos usuários sobre as recomendações fornecidas e usar isso para ajustar avaliações futuras de relevância.  
   - Exemplo:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Exemplo: Avaliando a Relevância no Agente de Viagens

Aqui está um exemplo prático de como o Agente de Viagens pode avaliar a relevância das recomendações de viagem:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Busca com Intenção

Buscar com intenção envolve entender e interpretar o propósito ou objetivo subjacente por trás da consulta do usuário para recuperar e gerar as informações mais relevantes e úteis. Essa abordagem vai além da simples correspondência de palavras-chave e foca em captar as reais necessidades e contexto do usuário.

#### Conceitos-Chave na Busca com Intenção

1. **Entendendo a Intenção do Usuário**:  
   - A intenção do usuário pode ser categorizada em três tipos principais: informacional, navegacional e transacional.  
     - **Intenção Informacional**: O usuário busca informações sobre um tema (ex.: "Quais são os melhores museus em Paris?").  
     - **Intenção Navegacional**: O usuário quer acessar um site ou página específica (ex.: "Site oficial do Museu do Louvre").  
     - **Intenção Transacional**: O usuário deseja realizar uma transação, como reservar um voo ou fazer uma compra (ex.: "Reservar voo para Paris").

2. **Consciência de Contexto**:  
   - Analisar o contexto da consulta do usuário ajuda a identificar com precisão sua intenção. Isso inclui considerar interações anteriores, preferências do usuário e detalhes específicos da consulta atual.

3. **Processamento de Linguagem Natural (PLN)**:  
   - Técnicas de PLN são usadas para entender e interpretar as consultas em linguagem natural fornecidas pelos usuários. Isso inclui tarefas como reconhecimento de entidades, análise de sentimento e parsing da consulta.

4. **Personalização**:  
   - Personalizar os resultados da busca com base no histórico, preferências e feedback do usuário melhora a relevância das informações recuperadas.
#### Exemplo Prático: Pesquisa com Intenção no Travel Agent

Vamos usar o Travel Agent como exemplo para ver como a pesquisa com intenção pode ser implementada.

1. **Coletando Preferências do Usuário**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Entendendo a Intenção do Usuário**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Consciência de Contexto**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Pesquisar e Personalizar Resultados**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Exemplo de Uso**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Gerando Código como uma Ferramenta

Agentes geradores de código usam modelos de IA para escrever e executar código, resolvendo problemas complexos e automatizando tarefas.

### Agentes Geradores de Código

Agentes geradores de código utilizam modelos generativos de IA para escrever e executar código. Esses agentes podem resolver problemas complexos, automatizar tarefas e fornecer insights valiosos ao gerar e rodar código em várias linguagens de programação.

#### Aplicações Práticas

1. **Geração Automática de Código**: Criar trechos de código para tarefas específicas, como análise de dados, web scraping ou machine learning.
2. **SQL como RAG**: Usar consultas SQL para recuperar e manipular dados em bancos de dados.
3. **Resolução de Problemas**: Criar e executar código para resolver problemas específicos, como otimizar algoritmos ou analisar dados.

#### Exemplo: Agente Gerador de Código para Análise de Dados

Imagine que você está projetando um agente gerador de código. Veja como ele poderia funcionar:

1. **Tarefa**: Analisar um conjunto de dados para identificar tendências e padrões.
2. **Passos**:
   - Carregar o conjunto de dados em uma ferramenta de análise.
   - Gerar consultas SQL para filtrar e agregar os dados.
   - Executar as consultas e obter os resultados.
   - Usar os resultados para gerar visualizações e insights.
3. **Recursos Necessários**: Acesso ao conjunto de dados, ferramentas de análise e capacidades SQL.
4. **Experiência**: Usar resultados anteriores para melhorar a precisão e relevância das análises futuras.

### Exemplo: Agente Gerador de Código para Travel Agent

Neste exemplo, vamos projetar um agente gerador de código, Travel Agent, para ajudar usuários a planejar suas viagens gerando e executando código. Esse agente pode realizar tarefas como buscar opções de viagem, filtrar resultados e montar um roteiro usando IA generativa.

#### Visão Geral do Agente Gerador de Código

1. **Coletando Preferências do Usuário**: Recolhe informações como destino, datas de viagem, orçamento e interesses.
2. **Gerando Código para Buscar Dados**: Cria trechos de código para obter informações sobre voos, hotéis e atrações.
3. **Executando o Código Gerado**: Roda o código para buscar informações em tempo real.
4. **Gerando o Roteiro**: Compila os dados obtidos em um plano de viagem personalizado.
5. **Ajustando com Base no Feedback**: Recebe feedback do usuário e regenera o código, se necessário, para refinar os resultados.

#### Implementação Passo a Passo

1. **Coletando Preferências do Usuário**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Gerando Código para Buscar Dados**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Executando o Código Gerado**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Gerando o Roteiro**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Ajustando com Base no Feedback**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Aproveitando a Consciência Ambiental e o Raciocínio

Basear-se no esquema da tabela pode, de fato, melhorar o processo de geração de consultas ao aproveitar a consciência ambiental e o raciocínio.

Veja um exemplo de como isso pode ser feito:

1. **Entendendo o Esquema**: O sistema compreende o esquema da tabela e usa essa informação para fundamentar a geração da consulta.
2. **Ajustando com Base no Feedback**: O sistema ajusta as preferências do usuário com base no feedback e raciocina sobre quais campos do esquema precisam ser atualizados.
3. **Gerando e Executando Consultas**: O sistema gera e executa consultas para buscar dados atualizados de voos e hotéis com base nas novas preferências.

Aqui está um exemplo atualizado em Python que incorpora esses conceitos:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explicação - Reserva com Base no Feedback

1. **Consciência do Esquema**: O dicionário `schema` define como as preferências devem ser ajustadas com base no feedback. Inclui campos como `favorites` e `avoid`, com ajustes correspondentes.
2. **Ajustando Preferências (método `adjust_based_on_feedback`)**: Este método ajusta as preferências com base no feedback do usuário e no esquema.
3. **Ajustes Baseados no Ambiente (método `adjust_based_on_environment`)**: Este método personaliza os ajustes com base no esquema e no feedback.
4. **Gerando e Executando Consultas**: O sistema gera código para buscar dados atualizados de voos e hotéis com base nas preferências ajustadas e simula a execução dessas consultas.
5. **Gerando o Roteiro**: O sistema cria um roteiro atualizado com base nos novos dados de voos, hotéis e atrações.

Ao tornar o sistema consciente do ambiente e raciocinar com base no esquema, ele pode gerar consultas mais precisas e relevantes, resultando em recomendações de viagem melhores e uma experiência mais personalizada para o usuário.

### Usando SQL como Técnica de Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) é uma ferramenta poderosa para interagir com bancos de dados. Quando usada como parte de uma abordagem Retrieval-Augmented Generation (RAG), o SQL pode recuperar dados relevantes para informar e gerar respostas ou ações em agentes de IA. Vamos explorar como o SQL pode ser usado como técnica RAG no contexto do Travel Agent.

#### Conceitos-Chave

1. **Interação com Banco de Dados**:
   - SQL é usado para consultar bancos de dados, recuperar informações relevantes e manipular dados.
   - Exemplo: Buscar detalhes de voos, informações de hotéis e atrações em um banco de dados de viagens.

2. **Integração com RAG**:
   - Consultas SQL são geradas com base nas entradas e preferências do usuário.
   - Os dados recuperados são usados para gerar recomendações ou ações personalizadas.

3. **Geração Dinâmica de Consultas**:
   - O agente de IA gera consultas SQL dinâmicas com base no contexto e nas necessidades do usuário.
   - Exemplo: Personalizar consultas SQL para filtrar resultados conforme orçamento, datas e interesses.

#### Aplicações

- **Geração Automática de Código**: Criar trechos de código para tarefas específicas.
- **SQL como RAG**: Usar consultas SQL para manipular dados.
- **Resolução de Problemas**: Criar e executar código para resolver problemas.

**Exemplo**:  
Um agente de análise de dados:

1. **Tarefa**: Analisar um conjunto de dados para encontrar tendências.  
2. **Passos**:  
   - Carregar o conjunto de dados.  
   - Gerar consultas SQL para filtrar dados.  
   - Executar consultas e obter resultados.  
   - Gerar visualizações e insights.  
3. **Recursos**: Acesso ao conjunto de dados, capacidades SQL.  
4. **Experiência**: Usar resultados anteriores para melhorar análises futuras.

#### Exemplo Prático: Usando SQL no Travel Agent

1. **Coletando Preferências do Usuário**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Gerando Consultas SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Executando Consultas SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Gerando Recomendações**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Exemplos de Consultas SQL

1. **Consulta de Voos**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Consulta de Hotéis**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Consulta de Atrações**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Ao aproveitar o SQL como parte da técnica Retrieval-Augmented Generation (RAG), agentes de IA como o Travel Agent podem recuperar e utilizar dados relevantes de forma dinâmica para fornecer recomendações precisas e personalizadas.

### Exemplo de Metacognição

Para demonstrar uma implementação de metacognição, vamos criar um agente simples que *reflete sobre seu processo de tomada de decisão* enquanto resolve um problema. Neste exemplo, construiremos um sistema onde um agente tenta otimizar a escolha de um hotel, mas depois avalia seu próprio raciocínio e ajusta sua estratégia quando comete erros ou faz escolhas subótimas.

Vamos simular isso usando um exemplo básico onde o agente seleciona hotéis com base em uma combinação de preço e qualidade, mas ele "reflete" sobre suas decisões e ajusta conforme necessário.

#### Como isso ilustra metacognição:

1. **Decisão Inicial**: O agente escolhe o hotel mais barato, sem considerar o impacto da qualidade.
2. **Reflexão e Avaliação**: Após a escolha inicial, o agente verifica se o hotel foi uma escolha "ruim" usando o feedback do usuário. Se perceber que a qualidade do hotel foi baixa, ele reflete sobre seu raciocínio.
3. **Ajustando a Estratégia**: O agente ajusta sua estratégia com base na reflexão, mudando de "mais barato" para "melhor qualidade", melhorando seu processo de decisão nas próximas vezes.

Aqui está um exemplo:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Habilidades de Metacognição dos Agentes

O ponto principal aqui é a capacidade do agente de:  
- Avaliar suas escolhas anteriores e seu processo de decisão.  
- Ajustar sua estratégia com base nessa reflexão, ou seja, metacognição em ação.

Esta é uma forma simples de metacognição onde o sistema é capaz de ajustar seu raciocínio com base em feedback interno.

### Conclusão

A metacognição é uma ferramenta poderosa que pode melhorar significativamente as capacidades dos agentes de IA. Ao incorporar processos metacognitivos, você pode projetar agentes mais inteligentes, adaptáveis e eficientes. Use os recursos adicionais para explorar ainda mais o fascinante mundo da metacognição em agentes de IA.

## Aula Anterior

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## Próxima Aula

[AI Agents in Production](../10-ai-agents-production/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.