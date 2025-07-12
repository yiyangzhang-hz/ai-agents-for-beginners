<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:45:01+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "zh"
}
-->
# 第11课：模型上下文协议（MCP）集成

## 模型上下文协议（MCP）简介

模型上下文协议（MCP）是一种前沿框架，旨在规范AI模型与客户端应用之间的交互。MCP作为AI模型与使用它们的应用之间的桥梁，提供了一致的接口，无论底层模型实现如何。

MCP的关键特点：

- **标准化通信**：MCP建立了应用与AI模型之间的通用语言
- **增强的上下文管理**：支持高效传递上下文信息给AI模型
- **跨平台兼容**：支持包括C#、Java、JavaScript、Python和TypeScript等多种编程语言
- **无缝集成**：使开发者能够轻松将不同AI模型集成到应用中

MCP在AI代理开发中尤为重要，因为它允许代理通过统一协议与各种系统和数据源交互，使代理更加灵活和强大。

## 学习目标
- 理解MCP是什么及其在AI代理开发中的作用
- 搭建并配置用于GitHub集成的MCP服务器
- 使用MCP工具构建多代理系统
- 利用Azure认知搜索实现RAG（检索增强生成）

## 先决条件
- Python 3.8及以上
- Node.js 14及以上
- Azure订阅
- GitHub账号
- 具备Semantic Kernel基础知识

## 设置说明

1. **环境搭建**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **配置Azure服务**
   - 创建Azure认知搜索资源
   - 设置Azure OpenAI服务
   - 在`.env`文件中配置环境变量

3. **MCP服务器搭建**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## 项目结构

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

## 核心组件

### 1. 多代理系统
- GitHub代理：仓库分析
- Hackathon代理：项目推荐
- 事件代理：技术活动建议

### 2. Azure集成
- 使用认知搜索进行活动索引
- 利用Azure OpenAI提升代理智能
- 实现RAG模式

### 3. MCP工具
- GitHub仓库分析
- 代码检查
- 元数据提取

## 代码讲解

示例演示了：
1. MCP服务器集成
2. 多代理协调
3. Azure认知搜索集成
4. RAG模式实现

主要功能：
- 实时GitHub仓库分析
- 智能项目推荐
- 使用Azure搜索进行活动匹配
- 通过Chainlit实现流式响应

## 运行示例

有关详细的设置说明和更多信息，请参阅[Github MCP Server Example README](./code_samples/github-mcp/README.md)。

1. 启动MCP服务器：
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. 启动应用程序：
   ```bash
   chainlit run app.py -w
   ```

3. 测试集成：
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## 故障排除

常见问题及解决方案：
1. MCP连接问题
   - 确认服务器已启动
   - 检查端口是否可用
   - 确认GitHub令牌有效

2. Azure搜索问题
   - 验证连接字符串
   - 检查索引是否存在
   - 确认文档已上传

## 后续步骤
- 探索更多MCP工具
- 实现自定义代理
- 增强RAG功能
- 添加更多活动来源

## 资源
- [MCP入门](https://aka.ms/mcp-for-beginners)  
- [MCP文档](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure认知搜索文档](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel指南](https://learn.microsoft.com/semantic-kernel/)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。