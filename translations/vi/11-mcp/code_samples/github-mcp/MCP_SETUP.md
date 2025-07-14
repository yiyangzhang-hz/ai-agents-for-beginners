<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:17:36+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "vi"
}
-->
# Hướng Dẫn Tích Hợp MCP Server

## Yêu Cầu Đầu Vào
- Đã cài đặt Node.js (phiên bản 14 trở lên)
- Trình quản lý gói npm
- Môi trường Python với các phụ thuộc cần thiết

## Các Bước Thiết Lập

1. **Cài Đặt Gói MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Khởi Động MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Server sẽ khởi động và hiển thị URL kết nối.

3. **Xác Minh Kết Nối**  
   - Tìm biểu tượng phích cắm (🔌) trong giao diện Chainlit của bạn  
   - Số (1) sẽ xuất hiện bên cạnh biểu tượng phích cắm, báo hiệu kết nối thành công  
   - Console sẽ hiển thị: "GitHub plugin setup completed successfully" (cùng với các dòng trạng thái khác)

## Khắc Phục Sự Cố

### Các Vấn Đề Thường Gặp

1. **Xung Đột Cổng**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Giải pháp: Thay đổi cổng bằng cách sử dụng:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Vấn Đề Xác Thực**  
   - Đảm bảo thông tin đăng nhập GitHub được cấu hình đúng  
   - Kiểm tra file .env có chứa các token cần thiết  
   - Xác minh quyền truy cập API GitHub

3. **Kết Nối Thất Bại**  
   - Xác nhận server đang chạy trên cổng mong đợi  
   - Kiểm tra cài đặt tường lửa  
   - Đảm bảo môi trường Python có các gói cần thiết

## Xác Minh Kết Nối

MCP server của bạn được kết nối đúng khi:  
1. Console hiển thị "GitHub plugin setup completed successfully"  
2. Nhật ký kết nối hiển thị "✓ MCP Connection Status: Active"  
3. Các lệnh GitHub hoạt động trong giao diện chat

## Biến Môi Trường

Yêu cầu trong file .env của bạn:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Kiểm Tra Kết Nối

Gửi tin nhắn kiểm tra này trong chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Phản hồi thành công sẽ hiển thị thông tin kho lưu trữ.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.