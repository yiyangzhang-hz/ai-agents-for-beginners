<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:53:36+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "vi"
}
-->
bạn nên có phiên bản fork riêng của khóa học này tại liên kết sau:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.vi.png)

## Chạy Mã

Khóa học này cung cấp một loạt các Jupyter Notebooks mà bạn có thể chạy để có trải nghiệm thực hành xây dựng các AI Agents.

Các mẫu mã sử dụng một trong các loại sau:

**Yêu cầu Tài khoản GitHub - Miễn phí**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Được đánh dấu là (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Được đánh dấu là (autogen.ipynb)

**Yêu cầu Đăng ký Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Được đánh dấu là (azureaiagent.ipynb)

Chúng tôi khuyến khích bạn thử cả ba loại ví dụ để xem loại nào phù hợp nhất với bạn.

Dù bạn chọn phương án nào, nó sẽ quyết định các bước thiết lập bạn cần làm theo bên dưới:

## Yêu Cầu

- Python 3.12+
  - **LƯU Ý**: Nếu bạn chưa cài Python 3.12, hãy đảm bảo cài đặt nó. Sau đó tạo môi trường ảo (venv) bằng python3.12 để đảm bảo các phiên bản đúng được cài từ file requirements.txt.
- Tài khoản GitHub - Để truy cập GitHub Models Marketplace
- Đăng ký Azure - Để truy cập Azure AI Foundry
- Tài khoản Azure AI Foundry - Để truy cập Azure AI Agent Service

Chúng tôi đã bao gồm file `requirements.txt` ở thư mục gốc của kho lưu trữ này chứa tất cả các gói Python cần thiết để chạy các mẫu mã.

Bạn có thể cài đặt chúng bằng cách chạy lệnh sau trong terminal tại thư mục gốc của kho:

```bash
pip install -r requirements.txt
```

Chúng tôi khuyên bạn nên tạo môi trường ảo Python để tránh xung đột và sự cố.

## Thiết Lập VSCode

Hãy chắc chắn rằng bạn đang sử dụng đúng phiên bản Python trong VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Thiết Lập cho Mẫu sử dụng GitHub Models

### Bước 1: Lấy GitHub Personal Access Token (PAT) của bạn

Hiện tại, khóa học này sử dụng GitHub Models Marketplace để cung cấp truy cập miễn phí tới các Large Language Models (LLMs) dùng để tạo AI Agents.

Để truy cập dịch vụ này, bạn cần tạo một GitHub Personal Access Token.

Điều này có thể thực hiện bằng cách vào tài khoản GitHub của bạn.

Chọn tùy chọn `Fine-grained tokens` ở bên trái màn hình.

Sau đó chọn `Generate new token`.

![Generate Token](../../../translated_images/generate-token.9748d7585dd004cb4119b5aac724baff49c3a85791701b5e8ba3274b037c5b66.vi.png)

Bạn sẽ được yêu cầu nhập tên cho token, chọn ngày hết hạn (Khuyến nghị: 30 ngày), và chọn phạm vi cho token (Public Repositories).

Bạn cũng cần chỉnh sửa quyền của token này: Permissions -> Models -> Cho phép truy cập GitHub Models

Sao chép token mới bạn vừa tạo. Bây giờ bạn sẽ thêm token này vào file `.env` đi kèm trong khóa học này.

### Bước 2: Tạo file `.env` của bạn

Để tạo file `.env`, chạy lệnh sau trong terminal.

```bash
cp .env.example .env
```

Lệnh này sẽ sao chép file mẫu và tạo file `.env` trong thư mục của bạn, nơi bạn điền các giá trị cho biến môi trường.

Sau khi sao chép token, mở file `.env` bằng trình soạn thảo văn bản yêu thích và dán token vào trường `GITHUB_TOKEN`.

Bây giờ bạn có thể chạy các mẫu mã của khóa học.

## Thiết Lập cho Mẫu sử dụng Azure AI Foundry và Azure AI Agent Service

### Bước 1: Lấy Endpoint Dự Án Azure của bạn

Thực hiện theo các bước tạo hub và dự án trong Azure AI Foundry tại đây: [Tổng quan tài nguyên Hub](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Sau khi tạo dự án, bạn cần lấy chuỗi kết nối cho dự án.

Điều này có thể thực hiện bằng cách vào trang **Overview** của dự án trong cổng Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.vi.png)

### Bước 2: Tạo file `.env` của bạn

Chạy lệnh sau trong terminal để tạo file `.env`.

```bash
cp .env.example .env
```

Lệnh này sẽ sao chép file mẫu và tạo file `.env` trong thư mục của bạn, nơi bạn điền các giá trị cho biến môi trường.

Mở file `.env` và dán chuỗi kết nối vào trường `PROJECT_ENDPOINT`.

### Bước 3: Đăng nhập Azure

Theo thực hành bảo mật tốt, chúng ta sẽ sử dụng [xác thực không cần khóa](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) để xác thực với Azure OpenAI qua Microsoft Entra ID. Trước tiên, bạn cần cài đặt **Azure CLI** theo [hướng dẫn cài đặt](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) phù hợp với hệ điều hành của bạn.

Tiếp theo, mở terminal và chạy `az login --use-device-code` để đăng nhập vào tài khoản Azure.

Sau khi đăng nhập, chọn đăng ký (subscription) của bạn trong terminal.

## Biến Môi Trường Bổ Sung - Azure Search và Azure OpenAI

Đối với Bài học Agentic RAG - Bài 5 - có các mẫu sử dụng Azure Search và Azure OpenAI.

Nếu bạn muốn chạy các mẫu này, bạn cần thêm các biến môi trường sau vào file `.env`:

### Trang Tổng Quan (Dự Án)

- `AZURE_SUBSCRIPTION_ID` - Kiểm tra **Chi tiết dự án** trên trang **Overview** của dự án.

- `AZURE_AI_PROJECT_NAME` - Xem phía trên cùng trang **Overview** của dự án.

- `AZURE_OPENAI_SERVICE` - Tìm trong tab **Included capabilities** cho **Azure OpenAI Service** trên trang **Overview**.

### Trung Tâm Quản Lý

- `AZURE_OPENAI_RESOURCE_GROUP` - Vào **Thuộc tính dự án** trên trang **Overview** của **Trung tâm quản lý**.

- `GLOBAL_LLM_SERVICE` - Dưới **Connected resources**, tìm tên kết nối **Azure AI Services**. Nếu không có, kiểm tra trong **Azure portal** ở nhóm tài nguyên của bạn cho tên dịch vụ AI.

### Trang Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Chọn mô hình embedding (ví dụ: `text-embedding-ada-002`) và ghi lại **Deployment name** từ chi tiết mô hình.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chọn mô hình chat (ví dụ: `gpt-4o-mini`) và ghi lại **Deployment name** từ chi tiết mô hình.

### Cổng Azure

- `AZURE_OPENAI_ENDPOINT` - Tìm **Azure AI services**, nhấp vào, vào **Resource Management**, **Keys and Endpoint**, cuộn xuống phần "Azure OpenAI endpoints", sao chép endpoint ghi "Language APIs".

- `AZURE_OPENAI_API_KEY` - Từ cùng màn hình, sao chép KEY 1 hoặc KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Tìm tài nguyên **Azure AI Search**, nhấp vào và xem **Overview**.

- `AZURE_SEARCH_API_KEY` - Vào **Settings** rồi **Keys** để sao chép khóa quản trị chính hoặc phụ.

### Trang Web Bên Ngoài

- `AZURE_OPENAI_API_VERSION` - Truy cập trang [vòng đời phiên bản API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) dưới phần **Latest GA API release**.

### Thiết lập xác thực không cần khóa

Thay vì mã hóa cứng thông tin đăng nhập, chúng ta sẽ dùng kết nối không cần khóa với Azure OpenAI. Để làm điều này, ta sẽ import `DefaultAzureCredential` và gọi hàm `DefaultAzureCredential` để lấy thông tin xác thực.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Bị Kẹt Ở Đâu?

Nếu bạn gặp bất kỳ vấn đề nào khi chạy thiết lập này, hãy tham gia vào cộng đồng của chúng tôi

hoặc

.

## Bài Học Tiếp Theo

Bạn đã sẵn sàng chạy mã cho khóa học này. Chúc bạn học vui và khám phá thêm về thế giới AI Agents!

[Giới thiệu về AI Agents và các trường hợp sử dụng Agent](../01-intro-to-ai-agents/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.