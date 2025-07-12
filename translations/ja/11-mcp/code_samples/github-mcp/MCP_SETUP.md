<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:15:09+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ja"
}
-->
# MCPサーバー統合ガイド

## 前提条件
- Node.jsがインストールされていること（バージョン14以上）
- npmパッケージマネージャー
- 必要な依存関係が整ったPython環境

## セットアップ手順

1. **MCPサーバーパッケージのインストール**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **MCPサーバーの起動**
   ```bash
   npx @modelcontextprotocol/server-github
   ```
   サーバーが起動し、接続用のURLが表示されるはずです。

3. **接続の確認**
   - Chainlitのインターフェースでプラグアイコン（🔌）を探してください
   - プラグアイコンの横に数字（1）が表示されていれば接続成功です
   - コンソールには「GitHub plugin setup completed successfully」（その他のステータス行も含む）が表示されます

## トラブルシューティング

### よくある問題

1. **ポートの競合**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```
   解決策：以下のコマンドでポートを変更してください
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **認証の問題**
   - GitHubの認証情報が正しく設定されているか確認してください
   - .envファイルに必要なトークンが含まれているかチェックしてください
   - GitHub APIへのアクセス権を確認してください

3. **接続失敗**
   - サーバーが指定したポートで起動しているか確認してください
   - ファイアウォールの設定を確認してください
   - Python環境に必要なパッケージがインストールされているか確認してください

## 接続確認

MCPサーバーが正しく接続されている状態は以下の通りです：
1. コンソールに「GitHub plugin setup completed successfully」と表示される
2. 接続ログに「✓ MCP Connection Status: Active」と表示される
3. チャットインターフェースでGitHubコマンドが正常に動作する

## 環境変数

.envファイルに必要な設定：
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## 接続テスト

チャットで以下のテストメッセージを送信してください：
```
Show me the repositories for username: [GitHub Username]
```
成功するとリポジトリ情報が表示されます。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。