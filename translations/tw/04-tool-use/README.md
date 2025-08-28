<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-28T09:20:14+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "tw"
}
-->
[![如何設計優秀的 AI 代理](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.tw.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(點擊上方圖片觀看本課程的影片)_

# 工具使用設計模式

工具之所以有趣，是因為它們能讓 AI 代理具備更廣泛的能力。透過添加工具，代理不再局限於一組有限的操作，而是能執行多種多樣的操作。在本章中，我們將探討工具使用設計模式，該模式描述了 AI 代理如何使用特定工具來實現其目標。

## 簡介

在本課程中，我們將回答以下問題：

- 什麼是工具使用設計模式？
- 它可以應用於哪些使用場景？
- 實現該設計模式需要哪些元素/構建模塊？
- 使用工具使用設計模式構建可信賴的 AI 代理需要考慮哪些特殊事項？

## 學習目標

完成本課程後，您將能夠：

- 定義工具使用設計模式及其目的。
- 識別適用於工具使用設計模式的使用場景。
- 理解實現該設計模式所需的關鍵元素。
- 認識到確保使用該設計模式的 AI 代理可信賴的考量因素。

## 什麼是工具使用設計模式？

**工具使用設計模式**專注於賦予大型語言模型（LLMs）與外部工具交互的能力，以實現特定目標。工具是代理可以執行操作的代碼，可能是簡單的函數（如計算器）或第三方服務的 API 調用（如股票價格查詢或天氣預報）。在 AI 代理的上下文中，工具被設計為由代理根據**模型生成的函數調用**來執行。

## 它可以應用於哪些使用場景？

AI 代理可以利用工具完成複雜任務、檢索信息或做出決策。工具使用設計模式通常用於需要與外部系統（如數據庫、網絡服務或代碼解釋器）進行動態交互的場景。這種能力適用於多種使用場景，包括：

- **動態信息檢索**：代理可以查詢外部 API 或數據庫以獲取最新數據（例如，查詢 SQLite 數據庫進行數據分析，獲取股票價格或天氣信息）。
- **代碼執行與解釋**：代理可以執行代碼或腳本來解決數學問題、生成報告或進行模擬。
- **工作流程自動化**：通過集成任務調度器、電子郵件服務或數據管道等工具，自動化重複性或多步驟的工作流程。
- **客戶支持**：代理可以與 CRM 系統、工單平台或知識庫交互以解決用戶查詢。
- **內容生成與編輯**：代理可以利用語法檢查器、文本摘要工具或內容安全評估器等工具來協助完成內容創建任務。

## 實現工具使用設計模式需要哪些元素/構建模塊？

這些構建模塊使 AI 代理能夠執行多種任務。以下是實現工具使用設計模式所需的關鍵元素：

- **函數/工具架構**：詳細定義可用工具，包括函數名稱、用途、所需參數和預期輸出。這些架構使 LLM 能夠理解有哪些工具可用以及如何構造有效的請求。
- **函數執行邏輯**：根據用戶意圖和對話上下文，管理工具的調用方式和時機。這可能包括規劃模塊、路由機制或動態確定工具使用的條件流程。
- **消息處理系統**：管理用戶輸入、LLM 回應、工具調用和工具輸出的對話流程的組件。
- **工具集成框架**：連接代理與各種工具的基礎設施，無論是簡單的函數還是複雜的外部服務。
- **錯誤處理與驗證**：處理工具執行中的失敗，驗證參數並管理意外響應的機制。
- **狀態管理**：跟蹤對話上下文、先前的工具交互和持久數據，以確保多輪交互的一致性。

接下來，我們將更詳細地探討函數/工具調用。

### 函數/工具調用

函數調用是讓大型語言模型（LLMs）與工具交互的主要方式。您經常會看到“函數”和“工具”這兩個詞互換使用，因為“函數”（可重用代碼塊）就是代理用來執行任務的“工具”。為了調用函數的代碼，LLM 必須將用戶的請求與函數的描述進行比較。為此，包含所有可用函數描述的架構會被發送給 LLM。LLM 然後選擇最適合該任務的函數，並返回其名稱和參數。選定的函數被調用，其響應被發送回 LLM，LLM 使用該信息來回應用戶的請求。

開發者要為代理實現函數調用，需要：

1. 支持函數調用的 LLM 模型
2. 包含函數描述的架構
3. 每個描述函數的代碼

以下是一個以獲取城市當前時間為例的說明：

1. **初始化支持函數調用的 LLM：**

    並非所有模型都支持函數調用，因此需要確認您使用的 LLM 是否支持。<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> 支持函數調用。我們可以從初始化 Azure OpenAI 客戶端開始。

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **創建函數架構**：

    接下來，我們將定義一個 JSON 架構，其中包含函數名稱、函數用途的描述以及函數參數的名稱和描述。
    然後，我們將此架構與用戶請求一起傳遞給之前創建的客戶端，以查找舊金山的時間。需要注意的是，返回的是一個**工具調用**，而**不是**問題的最終答案。如前所述，LLM 返回的是它為任務選擇的函數名稱以及將傳遞給它的參數。

    ```python
    # Function description for the model to read
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **執行任務所需的函數代碼：**

    現在，LLM 已選擇需要運行的函數，接下來需要實現並執行執行該任務的代碼。
    我們可以用 Python 實現獲取當前時間的代碼。我們還需要編寫代碼，從 response_message 中提取名稱和參數以獲取最終結果。

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Handle function calls
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Second API call: Get the final response from the model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

函數調用是大多數（如果不是全部）代理工具使用設計的核心，然而從頭實現它有時可能具有挑戰性。
正如我們在[第 2 課](../../../02-explore-agentic-frameworks)中學到的，代理框架為我們提供了實現工具使用的預構建模塊。

## 使用代理框架的工具使用範例

以下是如何使用不同代理框架實現工具使用設計模式的一些範例：

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> 是一個開源的 AI 框架，適用於使用大型語言模型（LLMs）的 .NET、Python 和 Java 開發者。它通過自動向模型描述函數及其參數（稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">序列化</a>）簡化了函數調用的過程。它還處理模型與代碼之間的往返通信。使用像 Semantic Kernel 這樣的代理框架的另一個優勢是，它允許您訪問預構建工具，例如<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">文件搜索</a>和<a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">代碼解釋器</a>。

以下圖表說明了使用 Semantic Kernel 進行函數調用的過程：

![函數調用](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.tw.png)

在 Semantic Kernel 中，函數/工具被稱為<a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">插件</a>。我們可以將之前看到的 `get_current_time` 函數轉換為插件，方法是將其轉換為包含該函數的類。我們還可以導入 `kernel_function` 裝飾器，該裝飾器接收函數的描述。當您使用 GetCurrentTimePlugin 創建內核時，內核將自動序列化函數及其參數，並在此過程中創建要發送給 LLM 的架構。

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> 是一個較新的代理框架，旨在幫助開發者安全地構建、部署和擴展高質量且可擴展的 AI 代理，而無需管理底層的計算和存儲資源。它特別適用於企業應用，因為它是一個具有企業級安全性的完全託管服務。

與直接使用 LLM API 開發相比，Azure AI Agent Service 提供了一些優勢，包括：

- 自動工具調用——無需解析工具調用、調用工具和處理響應；所有這些現在都在服務端完成。
- 安全管理數據——您可以依賴線程存儲所有所需信息，而無需管理自己的對話狀態。
- 開箱即用的工具——可用於與數據源交互的工具，例如 Bing、Azure AI 搜索和 Azure 函數。

Azure AI Agent Service 中可用的工具分為兩類：

1. 知識工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing 搜索基礎</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">文件搜索</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI 搜索</a>

2. 行動工具：
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">函數調用</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">代碼解釋器</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI 定義的工具</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure 函數</a>

Agent Service 允許我們將這些工具作為一個 `toolset` 一起使用。它還利用 `threads` 來跟蹤特定對話的消息歷史。

假設您是 Contoso 公司的一名銷售代理，您希望開發一個能回答有關銷售數據問題的對話代理。

以下圖片說明了如何使用 Azure AI Agent Service 分析您的銷售數據：

![代理服務實際應用](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.tw.jpg)

要使用服務中的任何工具，我們可以創建一個客戶端並定義一個工具或工具集。實際實現時，我們可以使用以下 Python 代碼。LLM 將能夠查看工具集，並根據用戶請求決定是使用用戶創建的函數 `fetch_sales_data_using_sqlite_query` 還是預構建的代碼解釋器。

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## 使用工具使用設計模式構建可信賴 AI 代理需要考慮哪些特殊事項？

LLM 動態生成的 SQL 的一個常見問題是安全性，特別是 SQL 注入或惡意操作（如刪除或篡改數據庫）的風險。雖然這些問題確實存在，但可以通過正確配置數據庫訪問權限有效緩解。對於大多數數據庫，這涉及將數據庫配置為只讀。對於像 PostgreSQL 或 Azure SQL 這樣的數據庫服務，應為應用分配只讀（SELECT）角色。

在安全環境中運行應用進一步增強了保護。在企業場景中，數據通常從操作系統中提取並轉換到只讀數據庫或數據倉庫中，並具有用戶友好的架構。這種方法確保數據安全、性能優化且易於訪問，同時應用的訪問權限受到限制，僅限於只讀。

### 對工具使用設計模式有更多問題嗎？
加入 [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)，與其他學習者交流，參加辦公時間，並獲得有關 AI Agents 的問題解答。

## 額外資源

## 上一課程

[了解代理設計模式](../03-agentic-design-patterns/README.md)

## 下一課程

[代理式 RAG](../05-agentic-rag/README.md)

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。