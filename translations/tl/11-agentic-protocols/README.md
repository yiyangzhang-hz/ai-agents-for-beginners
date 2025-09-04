<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T08:57:06+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "tl"
}
-->
# Paggamit ng Agentic Protocols (MCP, A2A at NLWeb)

[![Agentic Protocols](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.tl.png)](https://youtu.be/X-Dh9R3Opn8)

Habang lumalawak ang paggamit ng mga AI agent, tumataas din ang pangangailangan para sa mga protocol na nagtitiyak ng standardisasyon, seguridad, at suporta para sa bukas na inobasyon. Sa araling ito, tatalakayin natin ang 3 protocol na naglalayong tugunan ang pangangailangang ito - Model Context Protocol (MCP), Agent to Agent (A2A), at Natural Language Web (NLWeb).

## Panimula

Sa araling ito, tatalakayin natin:

• Paano pinapahintulutan ng **MCP** ang mga AI Agent na ma-access ang mga panlabas na tool at data upang maisakatuparan ang mga gawain ng user.

• Paano pinapagana ng **A2A** ang komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agent.

• Paano dinadala ng **NLWeb** ang mga natural na interface ng wika sa anumang website, na nagbibigay-daan sa mga AI Agent na matuklasan at makipag-ugnayan sa nilalaman.

## Mga Layunin sa Pagkatuto

• **Tukuyin** ang pangunahing layunin at benepisyo ng MCP, A2A, at NLWeb sa konteksto ng mga AI agent.

• **Ipaliwanag** kung paano pinapadali ng bawat protocol ang komunikasyon at interaksyon sa pagitan ng mga LLM, tool, at iba pang agent.

• **Kilalanin** ang natatanging papel ng bawat protocol sa pagbuo ng mga komplikadong agentic system.

## Model Context Protocol

Ang **Model Context Protocol (MCP)** ay isang bukas na pamantayan na nagbibigay ng standardisadong paraan para sa mga aplikasyon na magbigay ng konteksto at mga tool sa mga LLM. Pinapagana nito ang isang "universal adaptor" para sa iba't ibang pinagmumulan ng data at mga tool na maaaring ikonekta ng mga AI Agent sa isang pare-parehong paraan.

Tingnan natin ang mga bahagi ng MCP, ang mga benepisyo nito kumpara sa direktang paggamit ng API, at isang halimbawa kung paano maaaring gumamit ng MCP server ang mga AI agent.

### Mga Pangunahing Bahagi ng MCP

Ang MCP ay gumagana sa isang **client-server architecture** at ang mga pangunahing bahagi nito ay:

• **Hosts**: Mga LLM application (halimbawa, isang code editor tulad ng VSCode) na nagsisimula ng koneksyon sa isang MCP Server.

• **Clients**: Mga bahagi sa loob ng host application na nagpapanatili ng one-to-one na koneksyon sa mga server.

• **Servers**: Mga magagaan na programa na naglalantad ng mga partikular na kakayahan.

Kasama sa protocol ang tatlong pangunahing primitive na siyang mga kakayahan ng isang MCP Server:

• **Tools**: Mga tiyak na aksyon o function na maaaring tawagin ng isang AI agent upang magsagawa ng isang gawain. Halimbawa, maaaring magbigay ang isang weather service ng "get weather" tool, o maaaring magbigay ang isang e-commerce server ng "purchase product" tool. Ang mga MCP server ay nag-aanunsyo ng pangalan, deskripsyon, at input/output schema ng bawat tool sa kanilang capabilities listing.

• **Resources**: Mga read-only na data item o dokumento na maaaring ibigay ng isang MCP server, at maaaring kunin ng mga client kapag kinakailangan. Halimbawa nito ay mga nilalaman ng file, mga talaan ng database, o mga log file. Ang mga resource ay maaaring text (tulad ng code o JSON) o binary (tulad ng mga imahe o PDF).

• **Prompts**: Mga pre-defined na template na nagbibigay ng mga mungkahing prompt, na nagpapahintulot ng mas komplikadong workflow.

### Mga Benepisyo ng MCP

Nag-aalok ang MCP ng mga makabuluhang benepisyo para sa mga AI Agent:

• **Dynamic Tool Discovery**: Maaaring makatanggap ang mga agent ng listahan ng mga available na tool mula sa isang server kasama ang mga deskripsyon ng kanilang ginagawa. Naiiba ito sa tradisyunal na mga API na karaniwang nangangailangan ng static coding para sa mga integration, na nangangahulugang anumang pagbabago sa API ay nangangailangan ng pag-update ng code. Ang MCP ay nag-aalok ng "integrate once" na diskarte, na nagdudulot ng mas mataas na adaptability.

• **Interoperability Across LLMs**: Gumagana ang MCP sa iba't ibang LLM, na nagbibigay ng flexibility upang lumipat ng mga pangunahing modelo para sa mas mahusay na performance.

• **Standardized Security**: Kasama sa MCP ang isang standard na paraan ng authentication, na nagpapabuti sa scalability kapag nagdaragdag ng access sa karagdagang MCP server. Mas simple ito kaysa sa pamamahala ng iba't ibang key at uri ng authentication para sa iba't ibang tradisyunal na API.

### Halimbawa ng MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.tl.png)

Isipin na nais ng isang user na mag-book ng flight gamit ang isang AI assistant na pinapagana ng MCP.

1. **Koneksyon**: Ang AI assistant (ang MCP client) ay kumokonekta sa isang MCP server na ibinigay ng isang airline.

2. **Tool Discovery**: Tinanong ng client ang MCP server ng airline, "Anong mga tool ang available sa inyo?" Sumagot ang server ng mga tool tulad ng "search flights" at "book flights".

3. **Tool Invocation**: Sinabi mo sa AI assistant, "Paki-search ng flight mula Portland papuntang Honolulu." Ang AI assistant, gamit ang LLM nito, ay natukoy na kailangan nitong tawagin ang "search flights" tool at ipasa ang mga kaugnay na parameter (origin, destination) sa MCP server.

4. **Execution at Tugon**: Ang MCP server, bilang wrapper, ay gumagawa ng aktwal na tawag sa internal booking API ng airline. Tinatanggap nito ang impormasyon ng flight (hal., JSON data) at ipinapadala ito pabalik sa AI assistant.

5. **Karagdagang Interaksyon**: Ipinapakita ng AI assistant ang mga opsyon sa flight. Kapag pumili ka ng flight, maaaring tawagin ng assistant ang "book flight" tool sa parehong MCP server upang makumpleto ang booking.

## Agent-to-Agent Protocol (A2A)

Habang ang MCP ay nakatuon sa pagkonekta ng mga LLM sa mga tool, ang **Agent-to-Agent (A2A) protocol** ay nagdadala nito sa mas mataas na antas sa pamamagitan ng pagpapagana ng komunikasyon at kolaborasyon sa pagitan ng iba't ibang AI agent. Pinapagana ng A2A ang koneksyon ng mga AI agent sa iba't ibang organisasyon, kapaligiran, at teknolohiya upang makumpleto ang isang ibinahaging gawain.

Tatalakayin natin ang mga bahagi at benepisyo ng A2A, kasama ang isang halimbawa kung paano ito maaaring gamitin sa ating travel application.

### Mga Pangunahing Bahagi ng A2A

Ang A2A ay nakatuon sa pagpapagana ng komunikasyon sa pagitan ng mga agent at pagpapagawa sa kanila ng magkakasamang gawain para sa user. Ang bawat bahagi ng protocol ay may kontribusyon dito:

#### Agent Card

Katulad ng kung paano nagbabahagi ang isang MCP server ng listahan ng mga tool, ang isang Agent Card ay naglalaman ng:
- Pangalan ng Agent.
- **Deskripsyon ng mga pangkalahatang gawain** na natatapos nito.
- **Listahan ng mga partikular na kasanayan** na may mga deskripsyon upang matulungan ang ibang agent (o maging ang mga user) na maunawaan kung kailan at bakit nila tatawagin ang agent na iyon.
- Ang **kasalukuyang Endpoint URL** ng agent.
- Ang **bersyon** at **kakayahan** ng agent tulad ng streaming responses at push notifications.

#### Agent Executor

Ang Agent Executor ang responsable sa **pagpapasa ng konteksto ng user chat sa remote agent**, na kailangan ng remote agent upang maunawaan ang gawain na kailangang tapusin. Sa isang A2A server, gumagamit ang isang agent ng sarili nitong Large Language Model (LLM) upang i-parse ang mga papasok na request at isagawa ang mga gawain gamit ang sarili nitong mga internal tool.

#### Artifact

Kapag natapos ng remote agent ang hinihinging gawain, ang produkto ng trabaho nito ay nililikha bilang isang artifact. Ang artifact ay **naglalaman ng resulta ng trabaho ng agent**, isang **deskripsyon ng natapos**, at ang **text context** na ipinadala sa protocol. Kapag naipadala na ang artifact, ang koneksyon sa remote agent ay isinasara hanggang sa muli itong kailanganin.

#### Event Queue

Ang bahaging ito ay ginagamit para sa **pag-handle ng mga update at pagpapasa ng mga mensahe**. Mahalaga ito sa produksyon para sa mga agentic system upang maiwasan ang pagsasara ng koneksyon sa pagitan ng mga agent bago matapos ang isang gawain, lalo na kung ang oras ng pagkumpleto ng gawain ay maaaring tumagal.

### Mga Benepisyo ng A2A

• **Pinahusay na Kolaborasyon**: Pinapagana nito ang mga agent mula sa iba't ibang vendor at platform na makipag-ugnayan, magbahagi ng konteksto, at magtulungan, na nagpapadali ng seamless automation sa mga tradisyunal na disconnected na sistema.

• **Flexibility sa Model Selection**: Ang bawat A2A agent ay maaaring magdesisyon kung aling LLM ang gagamitin nito upang i-service ang mga request, na nagpapahintulot ng optimized o fine-tuned na mga modelo bawat agent, hindi tulad ng isang single LLM connection sa ilang MCP scenario.

• **Built-in Authentication**: Ang authentication ay direktang isinama sa A2A protocol, na nagbibigay ng matibay na security framework para sa mga interaksyon ng agent.

### Halimbawa ng A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.tl.png)

Palawakin natin ang ating travel booking scenario, ngunit sa pagkakataong ito gamit ang A2A.

1. **Request ng User sa Multi-Agent**: Nakikipag-ugnayan ang isang user sa isang "Travel Agent" A2A client/agent, marahil sa pagsasabing, "Paki-book ng buong biyahe papuntang Honolulu para sa susunod na linggo, kasama ang flight, hotel, at rental car."

2. **Orkestrasyon ng Travel Agent**: Tinatanggap ng Travel Agent ang kumplikadong request na ito. Ginagamit nito ang LLM nito upang mag-reason tungkol sa gawain at matukoy na kailangan nitong makipag-ugnayan sa iba pang specialized agent.

3. **Komunikasyon sa pagitan ng mga Agent**: Ginagamit ng Travel Agent ang A2A protocol upang kumonekta sa mga downstream agent, tulad ng isang "Airline Agent," "Hotel Agent," at "Car Rental Agent" na nilikha ng iba't ibang kumpanya.

4. **Delegated Task Execution**: Ipinapadala ng Travel Agent ang mga partikular na gawain sa mga specialized agent na ito (hal., "Maghanap ng flight papuntang Honolulu," "Mag-book ng hotel," "Mag-rent ng kotse"). Ang bawat isa sa mga specialized agent na ito, na nagpapatakbo ng sarili nilang LLM at gumagamit ng sarili nilang mga tool (na maaaring MCP server din), ay gumagawa ng partikular na bahagi ng booking.

5. **Pinagsamang Tugon**: Kapag natapos ng lahat ng downstream agent ang kanilang mga gawain, pinagsasama-sama ng Travel Agent ang mga resulta (mga detalye ng flight, kumpirmasyon ng hotel, booking ng car rental) at ipinapadala ang isang komprehensibong, chat-style na tugon pabalik sa user.

## Natural Language Web (NLWeb)

Matagal nang pangunahing paraan ang mga website para ma-access ng mga user ang impormasyon at data sa internet.

Tingnan natin ang iba't ibang bahagi ng NLWeb, ang mga benepisyo nito, at isang halimbawa kung paano gumagana ang NLWeb sa ating travel application.

### Mga Bahagi ng NLWeb

- **NLWeb Application (Core Service Code)**: Ang sistema na nagpoproseso ng mga natural language na tanong. Kinokonekta nito ang iba't ibang bahagi ng platform upang makabuo ng mga tugon. Maaari mo itong isipin bilang ang **makina na nagpapagana sa mga natural language na feature** ng isang website.

- **NLWeb Protocol**: Isang **pangunahing hanay ng mga patakaran para sa natural language na interaksyon** sa isang website. Nagpapadala ito ng mga tugon sa JSON format (madalas gamit ang Schema.org). Layunin nitong lumikha ng simpleng pundasyon para sa “AI Web,” katulad ng kung paano ginawa ng HTML na posible ang pagbabahagi ng mga dokumento online.

- **MCP Server (Model Context Protocol Endpoint)**: Ang bawat NLWeb setup ay gumagana rin bilang isang **MCP server**. Nangangahulugan ito na maaari itong **magbahagi ng mga tool (tulad ng isang “ask” method) at data** sa iba pang AI system. Sa praktika, ginagawa nitong magagamit ng mga AI agent ang nilalaman at kakayahan ng website, na nagbibigay-daan sa site na maging bahagi ng mas malawak na “agent ecosystem.”

- **Embedding Models**: Ginagamit ang mga modelong ito upang **i-convert ang nilalaman ng website sa mga numerikal na representasyon na tinatawag na vectors** (embeddings). Ang mga vector na ito ay kumukuha ng kahulugan sa paraang maaaring ikumpara at hanapin ng mga computer. Iniimbak ang mga ito sa isang espesyal na database, at maaaring pumili ang mga user kung aling embedding model ang nais nilang gamitin.

- **Vector Database (Retrieval Mechanism)**: Ang database na ito ay **nag-iimbak ng embeddings ng nilalaman ng website**. Kapag may nagtanong, sinusuri ng NLWeb ang vector database upang mabilis na mahanap ang pinaka-kaugnay na impormasyon. Nagbibigay ito ng mabilis na listahan ng mga posibleng sagot, niraranggo ayon sa pagkakatulad. Gumagana ang NLWeb sa iba't ibang vector storage system tulad ng Qdrant, Snowflake, Milvus, Azure AI Search, at Elasticsearch.

### Halimbawa ng NLWeb

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.tl.png)

Isaalang-alang ang ating travel booking website muli, ngunit sa pagkakataong ito, pinapagana ito ng NLWeb.

1. **Data Ingestion**: Ang umiiral na mga katalogo ng produkto ng travel website (hal., mga flight listing, deskripsyon ng hotel, mga tour package) ay na-format gamit ang Schema.org o na-load sa pamamagitan ng RSS feeds. Ang mga tool ng NLWeb ay nag-i-ingest ng structured data na ito, lumilikha ng embeddings, at iniimbak ang mga ito sa isang lokal o remote na vector database.

2. **Natural Language Query (Human)**: Ang isang user ay bumisita sa website at, sa halip na mag-navigate sa mga menu, nagta-type sa isang chat interface: "Maghanap ng family-friendly na hotel sa Honolulu na may pool para sa susunod na linggo."

3. **Pagpoproseso ng NLWeb**: Tinatanggap ng NLWeb application ang query na ito. Ipinapadala nito ang query sa isang LLM para maunawaan at sabay na hinahanap ang vector database nito para sa mga kaugnay na hotel listing.

4. **Tumpak na Resulta**: Tinutulungan ng LLM na i-interpret ang mga resulta ng paghahanap mula sa database, tukuyin ang pinakamahusay na mga tugma batay sa "family-friendly," "pool," at "Honolulu" na pamantayan, at pagkatapos ay i-format ang isang natural language na tugon. Mahalagang tandaan na ang tugon ay tumutukoy sa aktwal na mga hotel mula sa katalogo ng website, na iniiwasan ang mga gawa-gawang impormasyon.

5. **Interaksyon ng AI Agent**: Dahil ang NLWeb ay nagsisilbing isang MCP server, maaaring kumonekta ang isang panlabas na AI travel agent sa NLWeb instance ng website na ito. Maaaring gamitin ng AI agent ang `ask` MCP method upang direktang magtanong sa website: `ask("Mayroon bang mga vegan-friendly na restaurant sa lugar ng Honolulu na inirerekomenda ng hotel?")`. Ipoproseso ito ng NLWeb instance, gamit ang database ng impormasyon ng restaurant (kung na-load), at magbabalik ng isang structured JSON response.

### May Karagdagang Tanong Tungkol sa MCP/A2A/NLWeb?

Sumali sa [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.

## Mga Resources

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.