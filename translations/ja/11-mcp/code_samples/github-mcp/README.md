<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-07-12T14:20:56+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/README.md",
  "language_code": "ja"
}
-->
# Github MCP サーバーの例

## 説明

これは Microsoft Reactor 主催の AI Agents ハッカソン向けに作成されたデモです。

このツールは、ユーザーの Github リポジトリに基づいてハッカソンプロジェクトを推薦するために使われます。  
具体的には以下のように動作します：

1. **Github Agent** - Github MCP サーバーを使ってリポジトリやその情報を取得します。  
2. **Hackathon Agent** - Github Agent から得たデータをもとに、ユーザーのプロジェクトや使用言語、AI Agents ハッカソンのプロジェクトトラックに基づいて創造的なハッカソンプロジェクトのアイデアを考え出します。  
3. **Events Agent** - Hackathon Agent の提案に基づき、AI Agent ハッカソンシリーズの関連イベントを推薦します。  

## コードの実行方法

### 環境変数

このデモでは Azure Open AI Service、Semantic Kernel、Github MCP サーバー、Azure AI Search を使用しています。

これらのツールを利用するために、適切な環境変数が設定されていることを確認してください：

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Chainlit サーバーの起動

MCP サーバーに接続するために、このデモでは Chainlit をチャットインターフェースとして使用しています。

サーバーを起動するには、ターミナルで以下のコマンドを実行してください：

```bash
chainlit run app.py -w
```

これにより、`localhost:8000` で Chainlit サーバーが起動し、`event-descriptions.md` の内容で Azure AI Search インデックスが更新されます。

## MCP サーバーへの接続

Github MCP サーバーに接続するには、「Type your message here..」チャットボックスの下にある「プラグ」アイコンを選択してください：

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.9154745f51c1f0437829df7624bff2f6268272f964f260fae8c7134d54e00f50.ja.png)

次に「Connect an MCP」をクリックして、Github MCP サーバーに接続するコマンドを追加します：

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" を実際の Personal Access Token に置き換えてください。

接続が成功すると、プラグアイコンの横に (1) が表示されて接続が確認できます。表示されない場合は、`chainlit run app.py -w` で Chainlit サーバーを再起動してみてください。

## デモの使い方

ハッカソンプロジェクトの推薦エージェントワークフローを開始するには、以下のようなメッセージを入力します：

"Recommend hackathon projects for the Github user koreyspace"

Router Agent がリクエストを解析し、どのエージェント（GitHub、Hackathon、Events）の組み合わせが最適かを判断します。エージェントは連携して、GitHub リポジトリの分析、プロジェクトのアイデア出し、関連する技術イベントの推薦を通じて包括的な提案を行います。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。