<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:45:38+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ja"
}
-->
# レッスン11: Model Context Protocol (MCP) 統合

## Model Context Protocol (MCP) の紹介

Model Context Protocol (MCP) は、AIモデルとクライアントアプリケーション間のやり取りを標準化するために設計された最先端のフレームワークです。MCPはAIモデルとそれを利用するアプリケーションの橋渡し役を果たし、基盤となるモデルの実装に関わらず一貫したインターフェースを提供します。

MCPの主な特徴：

- **標準化された通信**：アプリケーションがAIモデルと共通の言語でやり取りできるようにします
- **高度なコンテキスト管理**：AIモデルに効率的にコンテキスト情報を渡すことが可能です
- **クロスプラットフォーム対応**：C#、Java、JavaScript、Python、TypeScriptなど様々なプログラミング言語で動作します
- **シームレスな統合**：開発者が異なるAIモデルを簡単にアプリケーションに組み込めるようにします

MCPは特にAIエージェント開発において価値が高く、エージェントが統一されたプロトコルを通じて様々なシステムやデータソースと連携できるため、より柔軟で強力なエージェントを実現します。

## 学習目標
- MCPとは何か、AIエージェント開発における役割を理解する
- GitHub統合のためのMCPサーバーのセットアップと設定を行う
- MCPツールを使ったマルチエージェントシステムを構築する
- Azure Cognitive Searchを用いたRAG（Retrieval Augmented Generation）を実装する

## 前提条件
- Python 3.8以上
- Node.js 14以上
- Azureサブスクリプション
- GitHubアカウント
- Semantic Kernelの基本知識

## セットアップ手順

1. **環境設定**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azureサービスの設定**
   - Azure Cognitive Searchリソースの作成
   - Azure OpenAIサービスのセットアップ
   - `.env`ファイルに環境変数を設定

3. **MCPサーバーのセットアップ**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## プロジェクト構成

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

## コアコンポーネント

### 1. マルチエージェントシステム
- GitHubエージェント：リポジトリ分析
- ハッカソンエージェント：プロジェクト推薦
- イベントエージェント：技術イベントの提案

### 2. Azure統合
- イベントインデックス用のCognitive Search
- エージェントの知能向上のためのAzure OpenAI
- RAGパターンの実装

### 3. MCPツール
- GitHubリポジトリ分析
- コード検査
- メタデータ抽出

## コード解説

このサンプルでは以下を示しています：
1. MCPサーバーの統合
2. マルチエージェントのオーケストレーション
3. Azure Cognitive Searchの統合
4. RAGパターンの実装

主な特徴：
- リアルタイムのGitHubリポジトリ分析
- インテリジェントなプロジェクト推薦
- Azure Searchを使ったイベントマッチング
- Chainlitによるストリーミングレスポンス

## サンプルの実行方法

詳細なセットアップ手順や情報は、[Github MCP Server Example README](./code_samples/github-mcp/README.md)を参照してください。

1. MCPサーバーを起動：
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. アプリケーションを起動：
   ```bash
   chainlit run app.py -w
   ```

3. 統合のテスト：
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## トラブルシューティング

よくある問題と解決策：
1. MCP接続の問題
   - サーバーが起動しているか確認
   - ポートの空き状況をチェック
   - GitHubトークンの確認

2. Azure Searchの問題
   - 接続文字列の検証
   - インデックスの存在確認
   - ドキュメントのアップロード確認

## 次のステップ
- 追加のMCPツールを探る
- カスタムエージェントを実装する
- RAG機能を強化する
- さらに多くのイベントソースを追加する

## リソース
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。