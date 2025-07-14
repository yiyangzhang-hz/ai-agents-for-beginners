<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:20:43+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "hk"
}
-->
# Github MCP 伺服器範例

## 說明

這是為 Microsoft Reactor 舉辦的 AI Agents Hackathon 所製作的示範。

這個工具用來根據使用者的 Github 倉庫推薦 hackathon 專案。  
流程如下：

1. **Github Agent** - 使用 Github MCP Server 取得倉庫及相關資訊。  
2. **Hackathon Agent** - 根據 Github Agent 提供的資料，結合使用者的專案、使用的程式語言以及 AI Agents hackathon 的專案主題，提出創意的 hackathon 專案點子。  
3. **Events Agent** - 根據 Hackathon Agent 的建議，推薦 AI Agent Hackathon 系列中相關的活動。

## 執行程式碼

### 環境變數

此示範使用 Azure Open AI Service、Semantic Kernel、Github MCP Server 以及 Azure AI Search。

請確保已設定好相應的環境變數以使用這些工具：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## 啟動 Chainlit 伺服器

此示範使用 Chainlit 作為聊天介面來連接 MCP 伺服器。

在終端機輸入以下指令啟動伺服器：

```bash
chainlit run app.py -w
```

這會在 `localhost:8000` 啟動 Chainlit 伺服器，並將 `event-descriptions.md` 的內容匯入 Azure AI Search Index。

## 連接 MCP 伺服器

要連接 Github MCP Server，請點選「Type your message here..」聊天框下方的「plug」圖示：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.hk.png)

接著點選「Connect an MCP」以新增連接 Github MCP Server 的指令：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

將 "[YOUR PERSONAL ACCESS TOKEN]" 替換成你的個人存取權杖。

連接成功後，plug 圖示旁會顯示 (1) 以確認連線。如果沒有，請嘗試用 `chainlit run app.py -w` 重新啟動 Chainlit 伺服器。

## 使用示範

要啟動推薦 hackathon 專案的代理流程，可以輸入類似以下的訊息：

「Recommend hackathon projects for the Github user koreyspace」

Router Agent 會分析你的請求，判斷由哪組代理（GitHub、Hackathon 和 Events）來處理最合適。這些代理會協同合作，根據 Github 倉庫分析、專案構思及相關技術活動，提供完整的推薦。

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。