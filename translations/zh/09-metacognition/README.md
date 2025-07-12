<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8cbf460468c802c7994aa62e0e0779c9",
  "translation_date": "2025-07-12T11:59:42+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "zh"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.zh.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(点击上方图片观看本课视频)_
# AI 代理中的元认知

## 介绍

欢迎来到关于 AI 代理元认知的课程！本章面向对 AI 代理如何思考自身思维过程感兴趣的初学者。通过本课学习，你将理解关键概念，并掌握将元认知应用于 AI 代理设计的实用示例。

## 学习目标

完成本课后，你将能够：

1. 理解代理定义中推理循环的影响。
2. 使用规划和评估技术帮助自我纠正的代理。
3. 创建能够操作代码以完成任务的代理。

## 元认知简介

元认知指的是对自身思维进行思考的高级认知过程。对于 AI 代理来说，这意味着能够基于自我意识和过去经验评估并调整其行为。元认知，即“对思维的思考”，是构建具代理性的 AI 系统中的重要概念。它涉及 AI 系统对自身内部过程的认知，能够监控、调节并相应地调整行为。就像我们在观察环境或分析问题时所做的那样。这种自我意识能帮助 AI 系统做出更优决策，识别错误，并随着时间提升表现——这也与图灵测试及 AI 是否会接管的争论相关联。

在具代理性的 AI 系统中，元认知有助于解决多个挑战，例如：
- 透明性：确保 AI 系统能解释其推理和决策过程。
- 推理能力：增强 AI 系统综合信息并做出合理决策的能力。
- 适应性：使 AI 系统能适应新环境和变化的条件。
- 感知能力：提升 AI 系统识别和解读环境数据的准确性。

### 什么是元认知？

元认知，或称“对思维的思考”，是一种涉及自我意识和自我调节的高级认知过程。在 AI 领域，元认知使代理能够评估并调整其策略和行为，从而提升解决问题和决策的能力。理解元认知后，你可以设计出不仅更智能，而且更具适应性和高效性的 AI 代理。在真正的元认知中，你会看到 AI 明确地对自己的推理过程进行推理。

示例：“我优先选择了更便宜的航班，因为……但我可能错过了直飞航班，得重新检查一下。”
跟踪它为何选择某条路线。
- 注意到它犯了错误，因为过度依赖上次用户偏好，因此它不仅修改最终推荐，还调整了决策策略。
- 诊断模式，比如“每当用户提到‘太拥挤’时，我不仅要去除某些景点，还要反思如果总是按人气排名‘热门景点’，我的选择方法可能有缺陷。”

### 元认知在 AI 代理中的重要性

元认知在 AI 代理设计中扮演关键角色，原因包括：

![Importance of Metacognition](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.zh.png)

- 自我反思：代理能评估自身表现并识别改进空间。
- 适应性：代理能根据过去经验和环境变化调整策略。
- 错误纠正：代理能自主检测并修正错误，提升准确性。
- 资源管理：代理能通过规划和评估优化时间和计算资源的使用。

## AI 代理的组成部分

在深入元认知过程前，先了解 AI 代理的基本组成部分。AI 代理通常包括：

- Persona：代理的个性和特征，定义其与用户的交互方式。
- Tools：代理能执行的功能和能力。
- Skills：代理拥有的知识和专长。

这些组成部分协同工作，形成一个能执行特定任务的“专业单元”。

**示例**：
想象一个旅行代理服务，不仅帮你规划假期，还能根据实时数据和过往客户旅程经验调整行程。

### 示例：旅行代理服务中的元认知

假设你设计了一个由 AI 驱动的旅行代理服务。该代理“Travel Agent”帮助用户规划假期。为了融入元认知，Travel Agent 需要基于自我意识和过往经验评估并调整其行为。元认知在其中的作用如下：

#### 当前任务

帮助用户规划一次巴黎之旅。

#### 完成任务的步骤

1. **收集用户偏好**：询问用户旅行日期、预算、兴趣（如博物馆、美食、购物）及特殊需求。
2. **检索信息**：搜索符合用户偏好的航班、住宿、景点和餐厅。
3. **生成推荐**：提供包含航班详情、酒店预订和建议活动的个性化行程。
4. **根据反馈调整**：征求用户对推荐的反馈并做相应调整。

#### 所需资源

- 航班和酒店预订数据库访问权限。
- 巴黎景点和餐厅信息。
- 以往交互中的用户反馈数据。

#### 经验与自我反思

Travel Agent 利用元认知评估表现并从经验中学习。例如：

1. **分析用户反馈**：审查反馈，判断哪些推荐受欢迎，哪些不受欢迎，并据此调整未来建议。
2. **适应性**：如果用户曾表示不喜欢拥挤场所，Travel Agent 会避免在高峰时段推荐热门景点。
3. **错误纠正**：如果之前推荐了已满员的酒店，Travel Agent 会学会在推荐前更严格地检查可用性。

#### 开发者实用示例

以下是融入元认知的 Travel Agent 代码简化示例：

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

#### 元认知的重要性

- **自我反思**：代理能分析表现并识别改进点。
- **适应性**：代理能根据反馈和环境变化调整策略。
- **错误纠正**：代理能自主发现并修正错误。
- **资源管理**：代理能优化时间和计算资源的使用。

通过引入元认知，Travel Agent 能提供更个性化、更精准的旅行建议，提升整体用户体验。

---

## 2. 代理中的规划

规划是 AI 代理行为的关键组成部分。它涉及制定实现目标所需的步骤，考虑当前状态、资源和可能的障碍。

### 规划要素

- **当前任务**：明确任务定义。
- **完成任务的步骤**：将任务拆解为可管理的步骤。
- **所需资源**：识别必要资源。
- **经验**：利用过往经验指导规划。

**示例**：
以下是 Travel Agent 协助用户有效规划行程所需的步骤：

### Travel Agent 的步骤

1. **收集用户偏好**
   - 询问用户旅行日期、预算、兴趣及特殊需求。
   - 示例：“你计划什么时候出行？”“你的预算范围是多少？”“假期喜欢做哪些活动？”

2. **检索信息**
   - 根据用户偏好搜索相关旅行选项。
   - **航班**：查找符合预算和日期的航班。
   - **住宿**：寻找符合位置、价格和设施偏好的酒店或租赁房。
   - **景点和餐厅**：确定符合用户兴趣的热门景点、活动和餐饮选择。

3. **生成推荐**
   - 将检索到的信息整合成个性化行程。
   - 提供航班、酒店预订和建议活动详情，确保推荐符合用户偏好。

4. **向用户展示行程**
   - 将建议行程分享给用户审阅。
   - 示例：“这是为你规划的巴黎行程，包括航班详情、酒店预订及推荐的活动和餐厅。请告诉我你的想法！”

5. **收集反馈**
   - 询问用户对行程的反馈。
   - 示例：“你喜欢这些航班选项吗？”“酒店符合你的需求吗？”“有想添加或删除的活动吗？”

6. **根据反馈调整**
   - 根据用户反馈修改行程。
   - 对航班、住宿和活动推荐做必要调整，更贴合用户偏好。

7. **最终确认**
   - 将更新后的行程呈现给用户确认。
   - 示例：“我已根据你的反馈做了调整，这是最新行程。你觉得怎么样？”

8. **预订并确认**
   - 用户确认后，进行航班、住宿及预定活动的预订。
   - 发送确认信息给用户。

9. **提供持续支持**
   - 在旅行前及旅行期间，随时协助用户处理变更或额外需求。
   - 示例：“如果旅行中需要任何帮助，随时联系我！”

### 示例交互

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

## 3. 纠正型 RAG 系统

首先，我们先了解 RAG 工具和预加载上下文的区别。

![RAG vs Context Loading](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.zh.png)

### 检索增强生成（RAG）

RAG 结合了检索系统和生成模型。当收到查询时，检索系统从外部来源获取相关文档或数据，这些检索到的信息被用来增强生成模型的输入，帮助模型生成更准确且符合上下文的回答。

在 RAG 系统中，代理从知识库检索相关信息，并利用这些信息生成合适的响应或行动。

### 纠正型 RAG 方法

纠正型 RAG 方法侧重于利用 RAG 技术纠正错误，提升 AI 代理的准确性。其包含：

1. **提示技术**：使用特定提示引导代理检索相关信息。
2. **工具**：实现算法和机制，使代理能评估检索信息的相关性并生成准确回答。
3. **评估**：持续评估代理表现并调整以提升准确性和效率。

#### 示例：搜索代理中的纠正型 RAG

考虑一个从网络检索信息以回答用户查询的搜索代理。纠正型 RAG 可能包括：

1. **提示技术**：根据用户输入构造搜索查询。
2. **工具**：利用自然语言处理和机器学习算法对搜索结果进行排序和筛选。
3. **评估**：分析用户反馈，识别并纠正检索信息中的不准确之处。

### 旅行代理中的纠正型 RAG

纠正型 RAG（检索增强生成）提升 AI 检索和生成信息的能力，同时纠正错误。来看 Travel Agent 如何利用纠正型 RAG 提供更准确、更相关的旅行建议。

包括：

- **提示技术**：使用特定提示引导代理检索相关信息。
- **工具**：实现算法和机制，评估检索信息的相关性并生成准确回答。
- **评估**：持续评估代理表现，做出调整以提升准确性和效率。

#### 在 Travel Agent 中实现纠正型 RAG 的步骤

1. **初始用户交互**
   - Travel Agent 收集用户的初步偏好，如目的地、旅行日期、预算和兴趣。
   - 示例：

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **信息检索**
   - Travel Agent 根据用户偏好检索航班、住宿、景点和餐厅信息。
   - 示例：

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **生成初步推荐**
   - Travel Agent 利用检索信息生成个性化行程。
   - 示例：

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **收集用户反馈**
   - Travel Agent 征求用户对初步推荐的反馈。
   - 示例：

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **纠正型 RAG 过程**
   - **提示技术**：Travel Agent 根据用户反馈构造新的搜索查询。
     - 示例：

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **工具**：Travel Agent 使用算法对新搜索结果进行排序和筛选，重点考虑用户反馈的相关性。
     - 示例：

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **评估**：Travel Agent 通过分析用户反馈持续评估推荐的相关性和准确性，并做必要调整。
     - 示例：

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### 实用示例

以下是一个简化的 Python 代码示例，展示如何在 Travel Agent 中融入纠正型 RAG 方法：
### 预先加载上下文

预先加载上下文是指在处理查询之前，将相关的上下文或背景信息加载到模型中。这意味着模型从一开始就能访问这些信息，有助于它生成更有依据的回答，而无需在过程中额外检索数据。

下面是一个简化的示例，展示了在 Python 中如何为旅游代理应用实现预先加载上下文：

#### 说明

1. **初始化（`__init__` 方法）**：`TravelAgent` 类预加载了一个包含热门目的地信息的字典，如巴黎、东京、纽约和悉尼。该字典包括每个目的地的国家、货币、语言和主要景点等详细信息。

2. **获取信息（`get_destination_info` 方法）**：当用户查询特定目的地时，`get_destination_info` 方法会从预加载的上下文字典中获取相关信息。

通过预加载上下文，旅游代理应用可以快速响应用户查询，而无需实时从外部来源检索信息，从而提高应用的效率和响应速度。

### 在迭代前以目标启动计划

以目标启动计划是指从明确的目标或预期结果开始。通过事先定义这个目标，模型可以在整个迭代过程中以此为指导原则，确保每次迭代都更接近实现预期结果，使过程更高效、更有针对性。

下面是一个示例，展示如何在 Python 中为旅游代理在迭代前以目标启动旅行计划：

### 场景

旅游代理希望为客户规划一个定制的假期。目标是根据客户的偏好和预算，制定一个最大化客户满意度的旅行行程。

### 步骤

1. 定义客户的偏好和预算。
2. 根据这些偏好启动初始计划。
3. 通过迭代优化计划，以提升客户满意度。

#### Python 代码

#### 代码说明

1. **初始化（`__init__` 方法）**：`TravelAgent` 类初始化时包含一个潜在目的地列表，每个目的地有名称、费用和活动类型等属性。

2. **启动计划（`bootstrap_plan` 方法）**：该方法根据客户的偏好和预算创建初始旅行计划。它遍历目的地列表，将符合客户偏好且预算允许的目的地加入计划。

3. **匹配偏好（`match_preferences` 方法）**：该方法检查某个目的地是否符合客户的偏好。

4. **迭代计划（`iterate_plan` 方法）**：该方法通过尝试用更符合客户偏好和预算限制的目的地替换计划中的每个目的地，来优化初始计划。

5. **计算费用（`calculate_cost` 方法）**：该方法计算当前计划的总费用，包括可能的新目的地。

#### 示例用法

- **初始计划**：旅游代理根据客户对观光的偏好和2000美元的预算创建初始计划。
- **优化计划**：旅游代理通过迭代优化计划，以更好地满足客户的偏好和预算。

通过以明确目标（如最大化客户满意度）启动计划并迭代优化，旅游代理能够为客户制定定制且优化的旅行行程。这种方法确保旅行计划从一开始就符合客户的偏好和预算，并随着每次迭代不断改进。

### 利用大型语言模型进行重排序和评分

大型语言模型（LLM）可以用于重排序和评分，通过评估检索到的文档或生成的回答的相关性和质量。其工作流程如下：

**检索：** 初始检索步骤根据查询获取一组候选文档或回答。

**重排序：** LLM 评估这些候选项，并根据相关性和质量对它们进行重新排序，确保最相关且高质量的信息优先呈现。

**评分：** LLM 为每个候选项分配分数，反映其相关性和质量，帮助选择最佳回答或文档。

通过利用 LLM 进行重排序和评分，系统能够提供更准确且符合上下文的信息，提升整体用户体验。

下面是一个示例，展示旅游代理如何基于用户偏好，使用大型语言模型（LLM）对旅游目的地进行重排序和评分（Python）：

#### 场景 - 基于偏好的旅行推荐

旅游代理希望根据客户的偏好推荐最佳旅游目的地。LLM 将帮助对目的地进行重排序和评分，确保呈现最相关的选项。

#### 步骤：

1. 收集用户偏好。
2. 检索潜在旅游目的地列表。
3. 使用 LLM 根据用户偏好对目的地进行重排序和评分。

下面展示如何将之前的示例更新为使用 Azure OpenAI 服务：

#### 要求

1. 需要拥有 Azure 订阅。
2. 创建 Azure OpenAI 资源并获取 API 密钥。

#### 示例 Python 代码

#### 代码说明 - 偏好预订器

1. **初始化**：`TravelAgent` 类初始化时包含潜在旅游目的地列表，每个目的地有名称和描述等属性。

2. **获取推荐（`get_recommendations` 方法）**：该方法根据用户偏好生成 Azure OpenAI 服务的提示，并通过 HTTP POST 请求调用 Azure OpenAI API，获取重排序和评分后的目的地列表。

3. **生成提示（`generate_prompt` 方法）**：该方法构建发送给 Azure OpenAI 的提示，包含用户偏好和目的地列表，引导模型根据偏好对目的地进行重排序和评分。

4. **API 调用**：使用 `requests` 库向 Azure OpenAI API 端点发送 HTTP POST 请求，响应中包含重排序和评分后的目的地。

5. **示例用法**：旅游代理收集用户偏好（如对观光和多元文化的兴趣），并使用 Azure OpenAI 服务获取重排序和评分后的旅游推荐。

请确保将 `your_azure_openai_api_key` 替换为实际的 Azure OpenAI API 密钥，将 `https://your-endpoint.com/...` 替换为实际的 Azure OpenAI 部署端点 URL。

通过利用 LLM 进行重排序和评分，旅游代理能够为客户提供更个性化且相关的旅行推荐，提升整体体验。

### RAG：提示技术与工具的区别

检索增强生成（RAG）既可以作为一种提示技术，也可以作为开发 AI 代理的工具。理解两者的区别有助于更有效地利用 RAG。

#### 作为提示技术的 RAG

**是什么？**

- 作为提示技术，RAG 涉及设计特定的查询或提示，引导从大型语料库或数据库中检索相关信息，然后利用这些信息生成回答或执行操作。

**工作原理：**

1. **设计提示**：根据任务或用户输入创建结构化的提示或查询。
2. **检索信息**：使用提示从已有知识库或数据集中搜索相关数据。
3. **生成回答**：结合检索到的信息和生成式 AI 模型，产出全面且连贯的回答。

**旅游代理示例：**

- 用户输入：“我想参观巴黎的博物馆。”
- 提示：“查找巴黎的顶级博物馆。”
- 检索信息：卢浮宫、奥赛博物馆等详情。
- 生成回答：“这里有一些巴黎的顶级博物馆：卢浮宫、奥赛博物馆和蓬皮杜中心。”

#### 作为工具的 RAG

**是什么？**

- 作为工具，RAG 是一个集成系统，自动化检索和生成过程，方便开发者无需为每个查询手动设计提示即可实现复杂的 AI 功能。

**工作原理：**

1. **集成**：将 RAG 嵌入 AI 代理架构，自动处理检索和生成任务。
2. **自动化**：工具管理从接收用户输入到生成最终回答的整个流程，无需为每步显式设计提示。
3. **高效性**：通过简化检索和生成过程，提高代理性能，实现更快更准确的响应。

**旅游代理示例：**

- 用户输入：“我想参观巴黎的博物馆。”
- RAG 工具：自动检索博物馆信息并生成回答。
- 生成回答：“这里有一些巴黎的顶级博物馆：卢浮宫、奥赛博物馆和蓬皮杜中心。”

### 对比

| 方面                   | 提示技术                                               | 工具                                                  |
|------------------------|--------------------------------------------------------|-------------------------------------------------------|
| **手动 vs 自动**       | 每个查询需手动设计提示。                               | 检索和生成过程自动化。                                 |
| **控制权**             | 对检索过程有更多控制。                                 | 简化并自动化检索和生成。                               |
| **灵活性**             | 可根据具体需求定制提示。                               | 更适合大规模实现。                                     |
| **复杂度**             | 需要设计和调整提示。                                   | 更易集成到 AI 代理架构中。                             |

### 实际示例

**提示技术示例：**

**工具示例：**

### 评估相关性

评估相关性是 AI 代理性能的关键，确保代理检索和生成的信息对用户来说是合适、准确且有用的。下面介绍如何评估 AI 代理的相关性，包括实用示例和技术。

#### 评估相关性的关键概念

1. **上下文感知**：
   - 代理必须理解用户查询的上下文，才能检索和生成相关信息。
   - 示例：用户询问“巴黎最好的餐厅”，代理应考虑用户的口味和预算。

2. **准确性**：
   - 代理提供的信息应事实准确且最新。
   - 示例：推荐当前营业且评价良好的餐厅，而非过时或已关闭的选项。

3. **用户意图**：
   - 代理应推断用户查询背后的意图，提供最相关的信息。
   - 示例：用户询问“经济型酒店”，代理应优先推荐价格实惠的酒店。

4. **反馈循环**：
   - 持续收集和分析用户反馈，帮助代理优化相关性评估。
   - 示例：结合用户对之前推荐的评分和反馈，改进未来回答。

#### 评估相关性的实用技术

1. **相关性评分**：
   - 根据与用户查询和偏好的匹配程度，为每个检索项分配相关性分数。
   - 示例：

2. **过滤与排序**：
   - 过滤掉无关项，根据相关性分数对剩余项排序。
   - 示例：

3. **自然语言处理（NLP）**：
   - 利用 NLP 技术理解用户查询，检索相关信息。
   - 示例：

4. **用户反馈整合**：
   - 收集用户对推荐的反馈，用于调整未来的相关性评估。
   - 示例：

#### 示例：旅游代理中的相关性评估

下面是旅游代理如何评估旅行推荐相关性的实用示例：

### 带意图的搜索

带意图的搜索是指理解和解析用户查询背后的目的或目标，以检索和生成最相关且有用的信息。这种方法不仅仅是匹配关键词，更注重把握用户的真实需求和上下文。

#### 带意图搜索的关键概念

1. **理解用户意图**：
   - 用户意图可分为三类：信息型、导航型和交易型。
     - **信息型意图**：用户寻求某个主题的信息（如“巴黎最好的博物馆有哪些？”）。
     - **导航型意图**：用户想访问特定网站或页面（如“卢浮宫官网”）。
     - **交易型意图**：用户希望完成某项交易，如预订机票或购买商品（如“预订飞往巴黎的机票”）。

2. **上下文感知**：
   - 分析用户查询的上下文，有助于准确识别意图，包括考虑之前的交互、用户偏好和当前查询的具体细节。

3. **自然语言处理（NLP）**：
   - 利用 NLP 技术理解和解析用户的自然语言查询，包括实体识别、情感分析和查询解析等任务。

4. **个性化**：
   - 根据用户历史、偏好和反馈个性化搜索结果，提升检索信息的相关性。
#### 实践示例：在 Travel Agent 中实现意图搜索

以 Travel Agent 为例，看看如何实现基于意图的搜索。

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **理解用户意图**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **上下文感知**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **搜索并个性化结果**

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

5. **示例用法**

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

## 4. 作为工具的代码生成

代码生成代理使用 AI 模型编写和执行代码，解决复杂问题并自动化任务。

### 代码生成代理

代码生成代理利用生成式 AI 模型编写和执行代码。这些代理能够解决复杂问题、自动化任务，并通过生成和运行多种编程语言的代码提供有价值的见解。

#### 实际应用

1. **自动代码生成**：为特定任务生成代码片段，如数据分析、网页抓取或机器学习。
2. **SQL 作为 RAG**：使用 SQL 查询从数据库中检索和操作数据。
3. **问题解决**：创建并执行代码以解决特定问题，如优化算法或数据分析。

#### 示例：用于数据分析的代码生成代理

假设你正在设计一个代码生成代理，流程可能是：

1. **任务**：分析数据集以识别趋势和模式。
2. **步骤**：
   - 将数据集加载到数据分析工具中。
   - 生成 SQL 查询以筛选和汇总数据。
   - 执行查询并获取结果。
   - 利用结果生成可视化和洞察。
3. **所需资源**：访问数据集、数据分析工具和 SQL 功能。
4. **经验积累**：利用过去的分析结果提升未来分析的准确性和相关性。

### 示例：用于 Travel Agent 的代码生成代理

本例中，我们设计一个代码生成代理 Travel Agent，帮助用户规划旅行，通过生成和执行代码完成任务。该代理可以处理获取旅行选项、筛选结果和编制行程等任务，利用生成式 AI 实现。

#### 代码生成代理概述

1. **收集用户偏好**：收集用户输入，如目的地、旅行日期、预算和兴趣。
2. **生成获取数据的代码**：生成代码片段以检索航班、酒店和景点信息。
3. **执行生成的代码**：运行生成的代码以获取实时信息。
4. **生成行程**：将获取的数据编制成个性化旅行计划。
5. **根据反馈调整**：接收用户反馈，必要时重新生成代码以优化结果。

#### 逐步实现

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成获取数据的代码**

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

3. **执行生成的代码**

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

4. **生成行程**

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

5. **根据反馈调整**

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

### 利用环境感知和推理

基于表的 schema 确实可以通过环境感知和推理来增强查询生成过程。

示例如下：

1. **理解 Schema**：系统理解表的 schema，并利用这些信息为查询生成提供依据。
2. **根据反馈调整**：系统根据反馈调整用户偏好，并推理哪些字段需要更新。
3. **生成并执行查询**：系统生成并执行查询，以根据新偏好获取更新的航班和酒店数据。

以下是结合这些概念的 Python 代码示例：

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

#### 说明 - 基于反馈的预订

1. **Schema 感知**：`schema` 字典定义了如何根据反馈调整偏好，包括 `favorites` 和 `avoid` 等字段及其对应调整。
2. **调整偏好（`adjust_based_on_feedback` 方法）**：该方法根据用户反馈和 schema 调整偏好。
3. **基于环境的调整（`adjust_based_on_environment` 方法）**：该方法根据 schema 和反馈定制调整内容。
4. **生成并执行查询**：系统根据调整后的偏好生成代码，获取更新的航班和酒店数据，并模拟执行查询。
5. **生成行程**：系统基于新的航班、酒店和景点数据创建更新后的行程。

通过使系统具备环境感知能力并基于 schema 进行推理，可以生成更准确、更相关的查询，从而提供更优质的旅行推荐和更个性化的用户体验。

### 使用 SQL 作为检索增强生成（RAG）技术

SQL（结构化查询语言）是与数据库交互的强大工具。作为检索增强生成（RAG）方法的一部分，SQL 可用于从数据库中检索相关数据，以支持 AI 代理生成响应或执行操作。下面探讨 SQL 在 Travel Agent 中作为 RAG 技术的应用。

#### 关键概念

1. **数据库交互**：
   - 使用 SQL 查询数据库，检索相关信息并操作数据。
   - 例如：从旅游数据库中获取航班详情、酒店信息和景点数据。

2. **与 RAG 集成**：
   - 根据用户输入和偏好生成 SQL 查询。
   - 利用检索到的数据生成个性化推荐或执行相应操作。

3. **动态查询生成**：
   - AI 代理根据上下文和用户需求动态生成 SQL 查询。
   - 例如：根据预算、日期和兴趣定制 SQL 查询以筛选结果。

#### 应用场景

- **自动代码生成**：为特定任务生成代码片段。
- **SQL 作为 RAG**：使用 SQL 查询操作数据。
- **问题解决**：创建并执行代码解决问题。

**示例**：
数据分析代理：

1. **任务**：分析数据集以发现趋势。
2. **步骤**：
   - 加载数据集。
   - 生成 SQL 查询筛选数据。
   - 执行查询并获取结果。
   - 生成可视化和洞察。
3. **资源**：数据集访问权限、SQL 功能。
4. **经验**：利用过去结果提升未来分析。

#### 实践示例：在 Travel Agent 中使用 SQL

1. **收集用户偏好**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **生成 SQL 查询**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **执行 SQL 查询**

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

4. **生成推荐**

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

#### 示例 SQL 查询

1. **航班查询**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **酒店查询**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **景点查询**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

通过将 SQL 作为检索增强生成（RAG）技术的一部分，像 Travel Agent 这样的 AI 代理能够动态检索并利用相关数据，提供准确且个性化的推荐。

### 元认知示例

为了演示元认知的实现，我们创建一个简单代理，它在解决问题时*反思自己的决策过程*。本例中，代理尝试优化酒店选择，但会评估自身推理并在出现错误或次优选择时调整策略。

我们用一个基础示例模拟：代理根据价格和质量组合选择酒店，但会“反思”决策并据此调整。

#### 这如何体现元认知：

1. **初始决策**：代理选择最便宜的酒店，未考虑质量影响。
2. **反思与评估**：初次选择后，代理通过用户反馈检查酒店是否为“差”选择。如果发现质量过低，代理会反思其推理。
3. **调整策略**：代理基于反思调整策略，从“最便宜”切换到“最高质量”，从而提升未来决策。

示例如下：

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

#### 代理的元认知能力

关键在于代理能够：
- 评估之前的选择和决策过程。
- 基于反思调整策略，即元认知的体现。

这是一种简单的元认知形式，系统能够根据内部反馈调整推理过程。

### 结论

元认知是极具潜力的工具，能显著提升 AI 代理的能力。通过引入元认知过程，你可以设计出更智能、更灵活、更高效的代理。利用附加资源，深入探索 AI 代理中的元认知世界。

## 上一课

[Multi-Agent Design Pattern](../08-multi-agent/README.md)

## 下一课

[AI Agents in Production](../10-ai-agents-production/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。