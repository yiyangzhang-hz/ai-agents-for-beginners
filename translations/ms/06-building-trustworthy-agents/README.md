<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f57852cac3a86c4a5ef47f793cc12178",
  "translation_date": "2025-07-12T10:30:17+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ms"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ms.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Membangun Ejen AI yang Boleh Dipercayai

## Pengenalan

Pelajaran ini akan merangkumi:

- Cara membina dan melancarkan Ejen AI yang selamat dan berkesan
- Pertimbangan keselamatan penting semasa membangunkan Ejen AI
- Cara mengekalkan privasi data dan pengguna semasa membangunkan Ejen AI

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu cara untuk:

- Mengenal pasti dan mengurangkan risiko semasa mencipta Ejen AI
- Melaksanakan langkah keselamatan untuk memastikan data dan akses diurus dengan betul
- Mencipta Ejen AI yang mengekalkan privasi data dan memberikan pengalaman pengguna yang berkualiti

## Keselamatan

Mari kita mulakan dengan membina aplikasi ejen yang selamat. Keselamatan bermaksud ejen AI berfungsi seperti yang direka. Sebagai pembina aplikasi ejen, kita mempunyai kaedah dan alat untuk memaksimumkan keselamatan:

### Membangun Rangka Kerja Mesej Sistem

Jika anda pernah membina aplikasi AI menggunakan Large Language Models (LLMs), anda pasti faham betapa pentingnya mereka bentuk arahan sistem atau mesej sistem yang kukuh. Arahan ini menetapkan peraturan meta, arahan, dan garis panduan bagaimana LLM akan berinteraksi dengan pengguna dan data.

Bagi Ejen AI, arahan sistem adalah lebih penting kerana Ejen AI memerlukan arahan yang sangat spesifik untuk melaksanakan tugasan yang telah kita reka.

Untuk mencipta arahan sistem yang boleh diskalakan, kita boleh menggunakan rangka kerja mesej sistem untuk membina satu atau lebih ejen dalam aplikasi kita:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ms.png)

#### Langkah 1: Cipta Mesej Sistem Meta

Arahan meta akan digunakan oleh LLM untuk menjana arahan sistem bagi ejen yang kita cipta. Kita mereka bentuknya sebagai templat supaya kita boleh mencipta pelbagai ejen dengan lebih cekap jika perlu.

Berikut adalah contoh mesej sistem meta yang akan kita berikan kepada LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Langkah 2: Cipta arahan asas

Langkah seterusnya adalah mencipta arahan asas untuk menerangkan Ejen AI. Anda harus memasukkan peranan ejen, tugasan yang akan dilaksanakan oleh ejen, dan tanggungjawab lain ejen tersebut.

Berikut adalah contohnya:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Langkah 3: Berikan Mesej Sistem Asas kepada LLM

Sekarang kita boleh mengoptimumkan mesej sistem ini dengan memberikan mesej sistem meta sebagai mesej sistem dan mesej sistem asas kita.

Ini akan menghasilkan mesej sistem yang lebih baik untuk membimbing ejen AI kita:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Langkah 4: Ulang dan Perbaiki

Nilai rangka kerja mesej sistem ini adalah untuk memudahkan skala penciptaan mesej sistem dari pelbagai ejen serta memperbaiki mesej sistem anda dari masa ke masa. Jarang sekali mesej sistem berfungsi sempurna pada percubaan pertama untuk kes penggunaan lengkap anda. Mampu membuat penyesuaian kecil dan penambahbaikan dengan mengubah mesej sistem asas dan menjalankannya melalui sistem akan membolehkan anda membanding dan menilai hasil.

## Memahami Ancaman

Untuk membina ejen AI yang boleh dipercayai, penting untuk memahami dan mengurangkan risiko serta ancaman terhadap ejen AI anda. Mari kita lihat beberapa ancaman berbeza terhadap ejen AI dan bagaimana anda boleh merancang serta bersedia dengan lebih baik.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ms.png)

### Tugasan dan Arahan

**Penerangan:** Penyerang cuba mengubah arahan atau matlamat ejen AI melalui arahan atau manipulasi input.

**Pengurangan Risiko:** Laksanakan pemeriksaan pengesahan dan penapis input untuk mengesan arahan yang berpotensi berbahaya sebelum diproses oleh Ejen AI. Oleh kerana serangan ini biasanya memerlukan interaksi kerap dengan Ejen, mengehadkan bilangan pusingan perbualan adalah satu lagi cara untuk mengelakkan jenis serangan ini.

### Akses ke Sistem Kritikal

**Penerangan:** Jika ejen AI mempunyai akses ke sistem dan perkhidmatan yang menyimpan data sensitif, penyerang boleh menjejaskan komunikasi antara ejen dan perkhidmatan tersebut. Ini boleh menjadi serangan langsung atau cubaan tidak langsung untuk mendapatkan maklumat tentang sistem tersebut melalui ejen.

**Pengurangan Risiko:** Ejen AI harus mempunyai akses kepada sistem hanya berdasarkan keperluan untuk mengelakkan jenis serangan ini. Komunikasi antara ejen dan sistem juga harus selamat. Melaksanakan pengesahan dan kawalan akses adalah cara lain untuk melindungi maklumat ini.

### Beban Berlebihan pada Sumber dan Perkhidmatan

**Penerangan:** Ejen AI boleh mengakses pelbagai alat dan perkhidmatan untuk melaksanakan tugasan. Penyerang boleh menggunakan keupayaan ini untuk menyerang perkhidmatan tersebut dengan menghantar jumlah permintaan yang tinggi melalui Ejen AI, yang boleh menyebabkan kegagalan sistem atau kos yang tinggi.

**Pengurangan Risiko:** Laksanakan polisi untuk mengehadkan bilangan permintaan yang boleh dibuat oleh ejen AI ke perkhidmatan. Mengehadkan bilangan pusingan perbualan dan permintaan kepada ejen AI anda adalah satu lagi cara untuk mengelakkan jenis serangan ini.

### Pencemaran Pangkalan Pengetahuan

**Penerangan:** Jenis serangan ini tidak menyasarkan ejen AI secara langsung tetapi menyasarkan pangkalan pengetahuan dan perkhidmatan lain yang digunakan oleh ejen AI. Ini boleh melibatkan merosakkan data atau maklumat yang digunakan oleh ejen AI untuk melaksanakan tugasan, menyebabkan respons yang berat sebelah atau tidak diingini kepada pengguna.

**Pengurangan Risiko:** Lakukan pengesahan berkala terhadap data yang akan digunakan oleh ejen AI dalam aliran kerjanya. Pastikan akses kepada data ini selamat dan hanya diubah oleh individu yang dipercayai untuk mengelakkan jenis serangan ini.

### Ralat Berantai

**Penerangan:** Ejen AI mengakses pelbagai alat dan perkhidmatan untuk melaksanakan tugasan. Ralat yang disebabkan oleh penyerang boleh menyebabkan kegagalan sistem lain yang disambungkan kepada ejen AI, menyebabkan serangan menjadi lebih meluas dan sukar untuk dibaiki.

**Pengurangan Risiko:** Salah satu cara untuk mengelakkan ini adalah dengan membenarkan Ejen AI beroperasi dalam persekitaran terhad, seperti melaksanakan tugasan dalam kontena Docker, untuk mengelakkan serangan sistem secara langsung. Mewujudkan mekanisme sandaran dan logik cuba semula apabila sistem tertentu memberi respons dengan ralat adalah cara lain untuk mengelakkan kegagalan sistem yang lebih besar.

## Manusia dalam Gelung

Satu lagi cara berkesan untuk membina sistem Ejen AI yang boleh dipercayai adalah dengan menggunakan pendekatan Manusia dalam Gelung. Ini mewujudkan aliran di mana pengguna dapat memberikan maklum balas kepada Ejen semasa proses berjalan. Pengguna bertindak sebagai ejen dalam sistem multi-ejen dengan memberikan kelulusan atau penamatan proses yang sedang berjalan.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ms.png)

Berikut adalah petikan kod menggunakan AutoGen untuk menunjukkan bagaimana konsep ini dilaksanakan:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Kesimpulan

Membangun ejen AI yang boleh dipercayai memerlukan reka bentuk yang teliti, langkah keselamatan yang kukuh, dan iterasi berterusan. Dengan melaksanakan sistem meta prompting yang tersusun, memahami ancaman yang berpotensi, dan menggunakan strategi pengurangan risiko, pembangun dapat mencipta ejen AI yang selamat dan berkesan. Selain itu, menggabungkan pendekatan manusia dalam gelung memastikan ejen AI kekal selaras dengan keperluan pengguna sambil meminimumkan risiko. Seiring AI terus berkembang, mengekalkan sikap proaktif terhadap keselamatan, privasi, dan pertimbangan etika akan menjadi kunci untuk memupuk kepercayaan dan kebolehpercayaan dalam sistem yang dipacu AI.

## Sumber Tambahan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Gambaran Keseluruhan AI Bertanggungjawab</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Penilaian Model AI Generatif dan Aplikasi AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesej Sistem Keselamatan</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Templat Penilaian Risiko</a>

## Pelajaran Sebelumnya

[Agentic RAG](../05-agentic-rag/README.md)

## Pelajaran Seterusnya

[Corak Reka Bentuk Perancangan](../07-planning-design/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.