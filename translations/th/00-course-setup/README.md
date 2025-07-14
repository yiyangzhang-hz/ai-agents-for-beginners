<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "76945069b52a49cd0432ae3e0b0ba22e",
  "translation_date": "2025-07-12T07:50:58+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "th"
}
-->
ในบัญชี GitHub ของคุณ

เลือกตัวเลือก `Fine-grained tokens` ที่ด้านซ้ายของหน้าจอ

จากนั้นเลือก `Generate new token`

![Generate Token](../../../translated_images/generate-token.9748d7585dd004cb4119b5aac724baff49c3a85791701b5e8ba3274b037c5b66.th.png)

ระบบจะให้คุณกรอกชื่อสำหรับโทเค็นของคุณ เลือกวันหมดอายุ (แนะนำ: 30 วัน) และเลือกขอบเขตสำหรับโทเค็นของคุณ (Public Repositories)

นอกจากนี้ยังจำเป็นต้องแก้ไขสิทธิ์ของโทเค็นนี้: Permissions -> Models -> อนุญาตการเข้าถึง GitHub Models

คัดลอกโทเค็นใหม่ที่คุณเพิ่งสร้างขึ้น จากนั้นเพิ่มโทเค็นนี้ลงในไฟล์ `.env` ที่รวมอยู่ในคอร์สนี้

### ขั้นตอนที่ 2: สร้างไฟล์ `.env` ของคุณ

เพื่อสร้างไฟล์ `.env` ให้รันคำสั่งต่อไปนี้ในเทอร์มินัลของคุณ

```bash
cp .env.example .env
```

คำสั่งนี้จะคัดลอกไฟล์ตัวอย่างและสร้างไฟล์ `.env` ในไดเรกทอรีของคุณ ซึ่งคุณจะกรอกค่าตัวแปรสภาพแวดล้อม

เมื่อคุณคัดลอกโทเค็นแล้ว ให้เปิดไฟล์ `.env` ในโปรแกรมแก้ไขข้อความที่คุณชื่นชอบ และวางโทเค็นของคุณลงในช่อง `GITHUB_TOKEN`

ตอนนี้คุณควรจะสามารถรันตัวอย่างโค้ดของคอร์สนี้ได้แล้ว

## การตั้งค่าสำหรับตัวอย่างที่ใช้ Azure AI Foundry และ Azure AI Agent Service

### ขั้นตอนที่ 1: ดึง Endpoint ของโปรเจกต์ Azure ของคุณ

ทำตามขั้นตอนการสร้างฮับและโปรเจกต์ใน Azure AI Foundry ได้ที่นี่: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

เมื่อคุณสร้างโปรเจกต์เสร็จแล้ว คุณจะต้องดึงสตริงการเชื่อมต่อของโปรเจกต์

สามารถทำได้โดยไปที่หน้า **Overview** ของโปรเจกต์ในพอร์ทัล Azure AI Foundry

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.th.png)

### ขั้นตอนที่ 2: สร้างไฟล์ `.env` ของคุณ

เพื่อสร้างไฟล์ `.env` ให้รันคำสั่งต่อไปนี้ในเทอร์มินัลของคุณ

```bash
cp .env.example .env
```

คำสั่งนี้จะคัดลอกไฟล์ตัวอย่างและสร้างไฟล์ `.env` ในไดเรกทอรีของคุณ ซึ่งคุณจะกรอกค่าตัวแปรสภาพแวดล้อม

เมื่อคุณคัดลอกสตริงการเชื่อมต่อแล้ว ให้เปิดไฟล์ `.env` ในโปรแกรมแก้ไขข้อความที่คุณชื่นชอบ และวางสตริงการเชื่อมต่อในช่อง `PROJECT_ENDPOINT`

### ขั้นตอนที่ 3: ลงชื่อเข้าใช้ Azure

เพื่อความปลอดภัย เราจะใช้ [การยืนยันตัวตนแบบไม่ใช้คีย์](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) เพื่อยืนยันตัวตนกับ Azure OpenAI ผ่าน Microsoft Entra ID ก่อนอื่นคุณต้องติดตั้ง **Azure CLI** ตาม [คำแนะนำการติดตั้ง](https://learn.microsoft.com/cli/azure/install-azure-cli?WT.mc_id=academic-105485-koreyst) สำหรับระบบปฏิบัติการของคุณ

จากนั้นเปิดเทอร์มินัลและรันคำสั่ง `az login --use-device-code` เพื่อเข้าสู่ระบบบัญชี Azure ของคุณ

เมื่อเข้าสู่ระบบแล้ว ให้เลือกการสมัครใช้งานของคุณในเทอร์มินัล

## ตัวแปรสภาพแวดล้อมเพิ่มเติม - Azure Search และ Azure OpenAI

สำหรับบทเรียน Agentic RAG - บทเรียนที่ 5 - มีตัวอย่างที่ใช้ Azure Search และ Azure OpenAI

หากคุณต้องการรันตัวอย่างเหล่านี้ คุณจะต้องเพิ่มตัวแปรสภาพแวดล้อมต่อไปนี้ในไฟล์ `.env` ของคุณ:

### หน้า Overview (โปรเจกต์)

- `AZURE_SUBSCRIPTION_ID` - ตรวจสอบ **รายละเอียดโปรเจกต์** ในหน้า **Overview** ของโปรเจกต์คุณ

- `AZURE_AI_PROJECT_NAME` - ดูที่ด้านบนของหน้า **Overview** ของโปรเจกต์คุณ

- `AZURE_OPENAI_SERVICE` - หาได้ในแท็บ **Included capabilities** สำหรับ **Azure OpenAI Service** ในหน้า **Overview**

### ศูนย์จัดการ

- `AZURE_OPENAI_RESOURCE_GROUP` - ไปที่ **คุณสมบัติโปรเจกต์** ในหน้า **Overview** ของ **ศูนย์จัดการ**

- `GLOBAL_LLM_SERVICE` - ภายใต้ **Connected resources** หา ชื่อการเชื่อมต่อ **Azure AI Services** หากไม่มี ให้ตรวจสอบใน **Azure portal** ภายใต้กลุ่มทรัพยากรของคุณสำหรับชื่อทรัพยากร AI Services

### หน้า Models + Endpoints

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - เลือกรูปแบบ embedding ของคุณ (เช่น `text-embedding-ada-002`) และจดชื่อ **Deployment name** จากรายละเอียดโมเดล

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - เลือกรูปแบบแชทของคุณ (เช่น `gpt-4o-mini`) และจดชื่อ **Deployment name** จากรายละเอียดโมเดล

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - หา **Azure AI services** คลิกเข้าไป จากนั้นไปที่ **Resource Management**, **Keys and Endpoint** เลื่อนลงไปที่ "Azure OpenAI endpoints" และคัดลอกอันที่เขียนว่า "Language APIs"

- `AZURE_OPENAI_API_KEY` - จากหน้าจอเดียวกัน คัดลอก KEY 1 หรือ KEY 2

- `AZURE_SEARCH_SERVICE_ENDPOINT` - หาแหล่งข้อมูล **Azure AI Search** ของคุณ คลิกเข้าไป และดูที่ **Overview**

- `AZURE_SEARCH_API_KEY` - จากนั้นไปที่ **Settings** แล้วเลือก **Keys** เพื่อคัดลอกคีย์ผู้ดูแลระบบหลักหรือรอง

### เว็บเพจภายนอก

- `AZURE_OPENAI_API_VERSION` - เยี่ยมชมหน้า [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) ภายใต้หัวข้อ **Latest GA API release**

### ตั้งค่าการยืนยันตัวตนแบบไม่ใช้คีย์

แทนที่จะเขียนข้อมูลรับรองของคุณลงในโค้ด เราจะใช้การเชื่อมต่อแบบไม่ใช้คีย์กับ Azure OpenAI โดยนำเข้า `DefaultAzureCredential` และเรียกใช้ฟังก์ชัน `DefaultAzureCredential` เพื่อรับข้อมูลรับรอง

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## ติดขัดตรงไหน?

หากคุณมีปัญหาในการตั้งค่านี้ สามารถเข้าร่วมใน

หรือ

.

## บทเรียนถัดไป

ตอนนี้คุณพร้อมที่จะรันโค้ดสำหรับคอร์สนี้แล้ว ขอให้สนุกกับการเรียนรู้เพิ่มเติมเกี่ยวกับโลกของ AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้