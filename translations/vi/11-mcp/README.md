<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:49:15+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "vi"
}
-->
# Bài học 11: Tích hợp Model Context Protocol (MCP)

## Giới thiệu về Model Context Protocol (MCP)

Model Context Protocol (MCP) là một khung công tác tiên tiến được thiết kế để chuẩn hóa các tương tác giữa các mô hình AI và ứng dụng khách. MCP đóng vai trò như cầu nối giữa các mô hình AI và các ứng dụng sử dụng chúng, cung cấp một giao diện nhất quán bất kể cách triển khai mô hình bên dưới.

Các điểm chính của MCP:

- **Giao tiếp chuẩn hóa**: MCP thiết lập một ngôn ngữ chung để các ứng dụng giao tiếp với mô hình AI
- **Quản lý ngữ cảnh nâng cao**: Cho phép truyền thông tin ngữ cảnh hiệu quả đến các mô hình AI
- **Tương thích đa nền tảng**: Hoạt động trên nhiều ngôn ngữ lập trình như C#, Java, JavaScript, Python và TypeScript
- **Tích hợp liền mạch**: Giúp các nhà phát triển dễ dàng tích hợp các mô hình AI khác nhau vào ứng dụng của họ

MCP đặc biệt hữu ích trong phát triển agent AI vì nó cho phép các agent tương tác với nhiều hệ thống và nguồn dữ liệu khác nhau thông qua một giao thức thống nhất, giúp các agent linh hoạt và mạnh mẽ hơn.

## Mục tiêu học tập
- Hiểu MCP là gì và vai trò của nó trong phát triển agent AI
- Thiết lập và cấu hình server MCP cho tích hợp GitHub
- Xây dựng hệ thống đa agent sử dụng công cụ MCP
- Triển khai RAG (Retrieval Augmented Generation) với Azure Cognitive Search

## Yêu cầu trước
- Python 3.8+
- Node.js 14+
- Tài khoản Azure
- Tài khoản GitHub
- Hiểu biết cơ bản về Semantic Kernel

## Hướng dẫn thiết lập

1. **Thiết lập môi trường**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Cấu hình dịch vụ Azure**
   - Tạo tài nguyên Azure Cognitive Search
   - Thiết lập dịch vụ Azure OpenAI
   - Cấu hình biến môi trường trong `.env`

3. **Thiết lập server MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Cấu trúc dự án

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

## Các thành phần chính

### 1. Hệ thống đa agent
- GitHub Agent: Phân tích kho lưu trữ
- Hackathon Agent: Đề xuất dự án
- Events Agent: Gợi ý sự kiện công nghệ

### 2. Tích hợp Azure
- Cognitive Search để lập chỉ mục sự kiện
- Azure OpenAI cho trí tuệ agent
- Triển khai mô hình RAG

### 3. Công cụ MCP
- Phân tích kho lưu trữ GitHub
- Kiểm tra mã nguồn
- Trích xuất metadata

## Giải thích mã nguồn

Ví dụ minh họa:
1. Tích hợp server MCP
2. Điều phối đa agent
3. Tích hợp Azure Cognitive Search
4. Triển khai mô hình RAG

Các tính năng chính:
- Phân tích kho lưu trữ GitHub theo thời gian thực
- Đề xuất dự án thông minh
- Ghép sự kiện bằng Azure Search
- Phản hồi streaming với Chainlit

## Chạy ví dụ

Để biết hướng dẫn thiết lập chi tiết và thông tin thêm, tham khảo [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Khởi động server MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Khởi chạy ứng dụng:
   ```bash
   chainlit run app.py -w
   ```

3. Kiểm tra tích hợp:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Khắc phục sự cố

Các vấn đề thường gặp và cách giải quyết:
1. Sự cố kết nối MCP
   - Kiểm tra server đã chạy chưa
   - Kiểm tra cổng có sẵn
   - Xác nhận token GitHub

2. Sự cố Azure Search
   - Xác thực chuỗi kết nối
   - Kiểm tra sự tồn tại của chỉ mục
   - Xác nhận tải tài liệu thành công

## Bước tiếp theo
- Khám phá thêm công cụ MCP
- Triển khai agent tùy chỉnh
- Nâng cao khả năng RAG
- Thêm nhiều nguồn sự kiện hơn

## Tài nguyên
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.