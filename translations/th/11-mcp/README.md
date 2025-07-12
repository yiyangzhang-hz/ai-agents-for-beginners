<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:48:03+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "th"
}
-->
# บทที่ 11: การรวม Model Context Protocol (MCP)

## แนะนำ Model Context Protocol (MCP)

Model Context Protocol (MCP) คือกรอบงานล้ำสมัยที่ออกแบบมาเพื่อมาตรฐานการสื่อสารระหว่างโมเดล AI กับแอปพลิเคชันลูกข่าย MCP ทำหน้าที่เป็นสะพานเชื่อมระหว่างโมเดล AI กับแอปพลิเคชันที่ใช้งาน โดยให้ส่วนติดต่อที่สอดคล้องกันไม่ว่าจะเป็นการใช้งานโมเดลแบบใดก็ตาม

จุดเด่นของ MCP:

- **การสื่อสารที่เป็นมาตรฐาน**: MCP สร้างภาษากลางสำหรับแอปพลิเคชันในการสื่อสารกับโมเดล AI
- **การจัดการบริบทที่ดีขึ้น**: ช่วยให้ส่งข้อมูลบริบทไปยังโมเดล AI ได้อย่างมีประสิทธิภาพ
- **รองรับหลายแพลตฟอร์ม**: ทำงานได้กับหลายภาษาโปรแกรม เช่น C#, Java, JavaScript, Python และ TypeScript
- **การรวมระบบที่ราบรื่น**: ช่วยให้นักพัฒนาสามารถผสานโมเดล AI ต่างๆ เข้ากับแอปพลิเคชันได้ง่าย

MCP มีประโยชน์อย่างยิ่งในการพัฒนา AI agent เพราะช่วยให้ agent สามารถโต้ตอบกับระบบและแหล่งข้อมูลต่างๆ ผ่านโปรโตคอลเดียวกัน ทำให้ agent มีความยืดหยุ่นและทรงพลังมากขึ้น

## วัตถุประสงค์การเรียนรู้
- เข้าใจว่า MCP คืออะไรและบทบาทของมันในการพัฒนา AI agent
- ตั้งค่าและกำหนดค่า MCP server สำหรับการรวมกับ GitHub
- สร้างระบบ multi-agent โดยใช้เครื่องมือ MCP
- นำ RAG (Retrieval Augmented Generation) มาใช้ร่วมกับ Azure Cognitive Search

## ข้อกำหนดเบื้องต้น
- Python 3.8 ขึ้นไป
- Node.js 14 ขึ้นไป
- บัญชี Azure
- บัญชี GitHub
- ความเข้าใจพื้นฐานเกี่ยวกับ Semantic Kernel

## คำแนะนำการตั้งค่า

1. **การตั้งค่าสภาพแวดล้อม**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **กำหนดค่า Azure Services**
   - สร้าง Azure Cognitive Search resource
   - ตั้งค่า Azure OpenAI service
   - กำหนด environment variables ในไฟล์ `.env`

3. **การตั้งค่า MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## โครงสร้างโปรเจกต์

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

## ส่วนประกอบหลัก

### 1. ระบบ Multi-Agent
- GitHub Agent: วิเคราะห์ repository
- Hackathon Agent: แนะนำโปรเจกต์
- Events Agent: แนะนำงานเทคโนโลยี

### 2. การรวม Azure
- Cognitive Search สำหรับการจัดทำดัชนีงานอีเวนต์
- Azure OpenAI สำหรับความฉลาดของ agent
- การใช้งานรูปแบบ RAG

### 3. เครื่องมือ MCP
- วิเคราะห์ repository บน GitHub
- ตรวจสอบโค้ด
- ดึงข้อมูลเมตา

## การอธิบายโค้ด

ตัวอย่างนี้แสดงให้เห็น:
1. การรวม MCP server
2. การประสานงาน multi-agent
3. การรวม Azure Cognitive Search
4. การใช้งานรูปแบบ RAG

ฟีเจอร์สำคัญ:
- วิเคราะห์ repository บน GitHub แบบเรียลไทม์
- แนะนำโปรเจกต์อย่างชาญฉลาด
- การจับคู่เหตุการณ์โดยใช้ Azure Search
- การตอบสนองแบบสตรีมมิ่งด้วย Chainlit

## การรันตัวอย่าง

สำหรับคำแนะนำการตั้งค่าอย่างละเอียดและข้อมูลเพิ่มเติม โปรดดูที่ [Github MCP Server Example README](./code_samples/github-mcp/README.md)

1. เริ่มต้น MCP server:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. เปิดใช้งานแอปพลิเคชัน:
   ```bash
   chainlit run app.py -w
   ```

3. ทดสอบการรวมระบบ:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## การแก้ไขปัญหา

ปัญหาที่พบบ่อยและวิธีแก้ไข:
1. ปัญหาการเชื่อมต่อ MCP
   - ตรวจสอบว่า server กำลังทำงานอยู่
   - ตรวจสอบพอร์ตว่าง
   - ยืนยัน token ของ GitHub

2. ปัญหา Azure Search
   - ตรวจสอบ connection string
   - ตรวจสอบว่ามี index อยู่หรือไม่
   - ยืนยันการอัปโหลดเอกสาร

## ขั้นตอนถัดไป
- สำรวจเครื่องมือ MCP เพิ่มเติม
- สร้าง agent แบบกำหนดเอง
- พัฒนาความสามารถ RAG
- เพิ่มแหล่งข้อมูลอีเวนต์เพิ่มเติม

## แหล่งข้อมูล
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้