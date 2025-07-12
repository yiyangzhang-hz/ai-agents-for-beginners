<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:45:29+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "tw"
}
-->
# Lesson 11: Model Context Protocol (MCP) Integration

## Model Context Protocol (MCP) 簡介

Model Context Protocol (MCP) 是一個先進的框架，旨在標準化 AI 模型與客戶端應用程式之間的互動。MCP 作為 AI 模型與使用它們的應用程式之間的橋樑，無論底層模型實作如何，都提供一致的介面。

MCP 的主要特點：

- **標準化通訊**：MCP 建立應用程式與 AI 模型溝通的共通語言
- **強化上下文管理**：有效傳遞上下文資訊給 AI 模型
- **跨平台相容性**：支援多種程式語言，包括 C#、Java、JavaScript、Python 和 TypeScript
- **無縫整合**：讓開發者輕鬆將不同 AI 模型整合到應用程式中

MCP 在 AI 代理開發中特別有價值，因為它允許代理透過統一協定與各種系統和資料來源互動，使代理更具彈性與功能強大。

## 學習目標
- 了解 MCP 是什麼及其在 AI 代理開發中的角色
- 設置並配置 MCP 伺服器以整合 GitHub
- 使用 MCP 工具建立多代理系統
- 實作結合 Azure Cognitive Search 的 RAG（檢索增強生成）

## 先決條件
- Python 3.8 以上版本
- Node.js 14 以上版本
- Azure 訂閱
- GitHub 帳號
- 基本的 Semantic Kernel 知識

## 設定說明

1. **環境設定**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置 Azure 服務**
   - 建立 Azure Cognitive Search 資源
   - 設定 Azure OpenAI 服務
   - 在 `.env` 中配置環境變數

3. **MCP 伺服器設定**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 專案結構

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

## 核心元件

### 1. 多代理系統
- GitHub 代理：倉庫分析
- Hackathon 代理：專案推薦
- Events 代理：技術活動建議

### 2. Azure 整合
- 使用 Cognitive Search 進行活動索引
- Azure OpenAI 提供代理智慧
- RAG 模式實作

### 3. MCP 工具
- GitHub 倉庫分析
- 程式碼檢查
- 元資料擷取

## 程式碼導覽

範例展示：
1. MCP 伺服器整合
2. 多代理協調
3. Azure Cognitive Search 整合
4. RAG 模式實作

主要功能：
- 即時 GitHub 倉庫分析
- 智慧專案推薦
- 使用 Azure Search 進行活動匹配
- 透過 Chainlit 實現串流回應

## 執行範例

詳細設定說明及更多資訊，請參考 [Github MCP Server Example README](./code_samples/github-mcp/README.md)。

1. 啟動 MCP 伺服器：
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. 啟動應用程式：
   ```bash
   chainlit run app.py -w
   ```

3. 測試整合：
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## 疑難排解

常見問題與解決方案：
1. MCP 連線問題
   - 確認伺服器是否運行中
   - 檢查埠號是否可用
   - 確認 GitHub 權杖有效

2. Azure Search 問題
   - 驗證連線字串
   - 檢查索引是否存在
   - 確認文件是否成功上傳

## 後續步驟
- 探索更多 MCP 工具
- 實作自訂代理
- 強化 RAG 功能
- 新增更多活動來源

## 資源
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。