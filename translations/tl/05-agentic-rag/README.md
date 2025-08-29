<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T09:49:04+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "tl"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.tl.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(I-click ang larawan sa itaas upang mapanood ang video ng araling ito)_

# Agentic RAG

Ang araling ito ay nagbibigay ng komprehensibong paliwanag tungkol sa Agentic Retrieval-Augmented Generation (Agentic RAG), isang umuusbong na paradigma sa AI kung saan ang mga large language models (LLMs) ay kusang nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na mapagkukunan. Hindi tulad ng mga static na retrieval-then-read na mga pattern, ang Agentic RAG ay gumagamit ng paulit-ulit na tawag sa LLM, na sinisingitan ng mga tawag sa tool o function at mga nakabalangkas na output. Sinusuri ng sistema ang mga resulta, pinapabuti ang mga query, gumagamit ng karagdagang mga tool kung kinakailangan, at nagpapatuloy sa siklong ito hanggang sa makamit ang isang kasiya-siyang solusyon.

## Panimula

Tatalakayin sa araling ito ang:

- **Pag-unawa sa Agentic RAG:** Alamin ang tungkol sa umuusbong na paradigma sa AI kung saan ang mga LLM ay kusang nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na mapagkukunan ng data.
- **Pag-unawa sa Iterative Maker-Checker Style:** Unawain ang loop ng paulit-ulit na tawag sa LLM, na sinisingitan ng mga tawag sa tool o function at mga nakabalangkas na output, na idinisenyo upang mapabuti ang katumpakan at maayos ang mga maling query.
- **Paggalugad ng Praktikal na Aplikasyon:** Tukuyin ang mga sitwasyon kung saan namumukod-tangi ang Agentic RAG, tulad ng mga kapaligirang inuuna ang katumpakan, kumplikadong interaksyon sa database, at mga pinalawig na workflow.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano/unawain ang:

- **Pag-unawa sa Agentic RAG:** Alamin ang tungkol sa umuusbong na paradigma sa AI kung saan ang mga LLM ay kusang nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na mapagkukunan ng data.
- **Iterative Maker-Checker Style:** Unawain ang konsepto ng loop ng paulit-ulit na tawag sa LLM, na sinisingitan ng mga tawag sa tool o function at mga nakabalangkas na output, na idinisenyo upang mapabuti ang katumpakan at maayos ang mga maling query.
- **Pagmamay-ari ng Proseso ng Pangangatwiran:** Unawain ang kakayahan ng sistema na akuin ang proseso ng pangangatwiran nito, gumagawa ng mga desisyon kung paano haharapin ang mga problema nang hindi umaasa sa mga paunang natukoy na landas.
- **Workflow:** Unawain kung paano kusang nagpapasya ang isang agentic na modelo na kumuha ng mga ulat sa trend ng merkado, tukuyin ang data ng mga kakumpitensya, iugnay ang mga panloob na sukatan ng benta, buuin ang mga natuklasan, at suriin ang estratehiya.
- **Iterative Loops, Tool Integration, at Memory:** Alamin ang pag-asa ng sistema sa isang pattern ng looped interaction, pinapanatili ang estado at memorya sa bawat hakbang upang maiwasan ang mga paulit-ulit na loop at makagawa ng mas may kaalamang mga desisyon.
- **Pagharap sa Mga Mode ng Pagkabigo at Pagwawasto sa Sarili:** Tuklasin ang matibay na mekanismo ng sistema para sa pagwawasto sa sarili, kabilang ang pag-ulit at muling pag-query, paggamit ng mga diagnostic tool, at pag-asa sa pangangasiwa ng tao.
- **Mga Hangganan ng Ahensya:** Unawain ang mga limitasyon ng Agentic RAG, na nakatuon sa domain-specific autonomy, pag-asa sa imprastraktura, at paggalang sa mga guardrail.
- **Praktikal na Mga Gamit at Halaga:** Tukuyin ang mga sitwasyon kung saan namumukod-tangi ang Agentic RAG, tulad ng mga kapaligirang inuuna ang katumpakan, kumplikadong interaksyon sa database, at mga pinalawig na workflow.
- **Pamamahala, Transparency, at Tiwala:** Alamin ang kahalagahan ng pamamahala at transparency, kabilang ang paliwanag na pangangatwiran, kontrol sa bias, at pangangasiwa ng tao.

## Ano ang Agentic RAG?

Ang Agentic Retrieval-Augmented Generation (Agentic RAG) ay isang umuusbong na paradigma sa AI kung saan ang mga LLM ay kusang nagpaplano ng kanilang mga susunod na hakbang habang kumukuha ng impormasyon mula sa mga panlabas na mapagkukunan. Hindi tulad ng mga static na retrieval-then-read na mga pattern, ang Agentic RAG ay gumagamit ng paulit-ulit na tawag sa LLM, na sinisingitan ng mga tawag sa tool o function at mga nakabalangkas na output. Sinusuri ng sistema ang mga resulta, pinapabuti ang mga query, gumagamit ng karagdagang mga tool kung kinakailangan, at nagpapatuloy sa siklong ito hanggang sa makamit ang isang kasiya-siyang solusyon. Ang iterative na “maker-checker” na istilo na ito ay nagpapabuti sa katumpakan, humahawak sa mga maling query, at tinitiyak ang mataas na kalidad na mga resulta.

Aktibong inaako ng sistema ang proseso ng pangangatwiran nito, muling isinusulat ang mga nabigong query, pumipili ng iba’t ibang paraan ng retrieval, at nagsasama ng maraming tool—tulad ng vector search sa Azure AI Search, SQL databases, o custom APIs—bago tapusin ang sagot nito. Ang natatanging katangian ng isang agentic na sistema ay ang kakayahan nitong akuin ang proseso ng pangangatwiran nito. Ang mga tradisyunal na implementasyon ng RAG ay umaasa sa mga paunang natukoy na landas, ngunit ang isang agentic na sistema ay kusang nagpapasya sa pagkakasunod-sunod ng mga hakbang batay sa kalidad ng impormasyong natuklasan nito.

## Pagpapaliwanag sa Agentic Retrieval-Augmented Generation (Agentic RAG)

Ang Agentic Retrieval-Augmented Generation (Agentic RAG) ay isang umuusbong na paradigma sa pag-develop ng AI kung saan ang mga LLM ay hindi lamang kumukuha ng impormasyon mula sa mga panlabas na mapagkukunan ng data kundi kusang nagpaplano rin ng kanilang mga susunod na hakbang. Hindi tulad ng mga static na retrieval-then-read na mga pattern o maingat na scripted na mga prompt sequence, ang Agentic RAG ay gumagamit ng loop ng paulit-ulit na tawag sa LLM, na sinisingitan ng mga tawag sa tool o function at mga nakabalangkas na output. Sa bawat hakbang, sinusuri ng sistema ang mga resulta na nakuha nito, nagpapasya kung kailangang pinuhin ang mga query, gumagamit ng karagdagang mga tool kung kinakailangan, at nagpapatuloy sa siklong ito hanggang sa makamit ang isang kasiya-siyang solusyon.

Ang iterative na “maker-checker” na istilo ng operasyon na ito ay idinisenyo upang mapabuti ang katumpakan, maayos ang mga maling query sa mga nakabalangkas na database (hal. NL2SQL), at matiyak ang balanseng, mataas na kalidad na mga resulta. Sa halip na umasa lamang sa maingat na ininhinyerong mga prompt chain, aktibong inaako ng sistema ang proseso ng pangangatwiran nito. Maaari nitong muling isulat ang mga nabigong query, pumili ng iba’t ibang paraan ng retrieval, at magsama ng maraming tool—tulad ng vector search sa Azure AI Search, SQL databases, o custom APIs—bago tapusin ang sagot nito. Tinanggal nito ang pangangailangan para sa sobrang kumplikadong mga orchestration framework. Sa halip, ang isang medyo simpleng loop ng “LLM call → tool use → LLM call → …” ay maaaring magbunga ng sopistikado at maayos na mga output.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.tl.png)

## Pagmamay-ari ng Proseso ng Pangangatwiran

Ang natatanging katangian na gumagawa sa isang sistema na “agentic” ay ang kakayahan nitong akuin ang proseso ng pangangatwiran nito. Ang mga tradisyunal na implementasyon ng RAG ay madalas na umaasa sa mga tao upang paunang tukuyin ang isang landas para sa modelo: isang chain-of-thought na nagbabalangkas kung ano ang kukunin at kailan. Ngunit kapag ang isang sistema ay tunay na agentic, ito mismo ang nagpapasya kung paano haharapin ang problema. Hindi lamang ito sumusunod sa isang script; kusang tinutukoy nito ang pagkakasunod-sunod ng mga hakbang batay sa kalidad ng impormasyong natuklasan nito.

Halimbawa, kung hihilingin itong lumikha ng isang estratehiya para sa paglulunsad ng produkto, hindi ito umaasa lamang sa isang prompt na nagdedetalye ng buong proseso ng pananaliksik at paggawa ng desisyon. Sa halip, ang agentic na modelo ay kusang nagpapasya na:

1. Kumuha ng mga ulat sa kasalukuyang trend ng merkado gamit ang Bing Web Grounding.
2. Tukuyin ang may kaugnayang data ng mga kakumpitensya gamit ang Azure AI Search.
3. Iugnay ang mga makasaysayang panloob na sukatan ng benta gamit ang Azure SQL Database.
4. Buoin ang mga natuklasan sa isang magkakaugnay na estratehiya na inayos gamit ang Azure OpenAI Service.
5. Suriin ang estratehiya para sa mga puwang o hindi pagkakapare-pareho, na nag-uudyok ng isa pang round ng retrieval kung kinakailangan.

Lahat ng mga hakbang na ito—pagpapabuti ng mga query, pagpili ng mga mapagkukunan, pag-ulit hanggang sa “masiyahan” sa sagot—ay desisyon ng modelo, hindi paunang iniskrip ng tao.

## Iterative Loops, Tool Integration, at Memory

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.tl.png)

Ang isang agentic na sistema ay umaasa sa isang pattern ng looped interaction:

- **Paunang Tawag:** Ang layunin ng user (aka. user prompt) ay ipinapakita sa LLM.
- **Paggamit ng Tool:** Kung natukoy ng modelo na may kulang na impormasyon o hindi malinaw na mga tagubilin, pumipili ito ng tool o paraan ng retrieval—tulad ng isang query sa vector database (hal. Azure AI Search Hybrid search sa pribadong data) o isang nakabalangkas na tawag sa SQL—upang makakuha ng higit pang konteksto.
- **Pagsusuri at Pagpapabuti:** Matapos suriin ang nakuha na data, nagpapasya ang modelo kung sapat na ang impormasyon. Kung hindi, pinapabuti nito ang query, sinusubukan ang ibang tool, o ina-adjust ang diskarte nito.
- **Ulitin Hanggang Masiyahan:** Ang siklong ito ay nagpapatuloy hanggang sa matukoy ng modelo na mayroon na itong sapat na kalinawan at ebidensya upang makapagbigay ng isang panghuling, maayos na sagot.
- **Memorya at Estado:** Dahil pinapanatili ng sistema ang estado at memorya sa bawat hakbang, naaalala nito ang mga naunang pagtatangka at ang mga resulta nito, na iniiwasan ang mga paulit-ulit na loop at gumagawa ng mas may kaalamang mga desisyon habang nagpapatuloy.

Sa paglipas ng panahon, lumilikha ito ng pakiramdam ng umuunlad na pag-unawa, na nagbibigay-daan sa modelo na mag-navigate sa mga kumplikado at maraming hakbang na gawain nang hindi kinakailangang patuloy na manghimasok o baguhin ng tao ang prompt.

## Pagharap sa Mga Mode ng Pagkabigo at Pagwawasto sa Sarili

Ang awtonomiya ng Agentic RAG ay kinabibilangan din ng matibay na mekanismo para sa pagwawasto sa sarili. Kapag ang sistema ay nakaranas ng mga dead end—tulad ng pagkuha ng mga hindi kaugnay na dokumento o pagharap sa mga maling query—maaari itong:

- **Mag-ulit at Muling Mag-Query:** Sa halip na magbigay ng mababang halaga na mga sagot, sinusubukan ng modelo ang mga bagong estratehiya sa paghahanap, muling isinusulat ang mga query sa database, o tumitingin sa mga alternatibong set ng data.
- **Gumamit ng Mga Diagnostic Tool:** Maaaring gumamit ang sistema ng mga karagdagang function na idinisenyo upang tulungan itong i-debug ang mga hakbang sa pangangatwiran nito o kumpirmahin ang katumpakan ng nakuha na data. Ang mga tool tulad ng Azure AI Tracing ay magiging mahalaga upang paganahin ang matibay na observability at monitoring.
- **Fallback sa Pangangasiwa ng Tao:** Para sa mga high-stakes o paulit-ulit na nabibigo na mga sitwasyon, maaaring i-flag ng modelo ang kawalan ng katiyakan at humiling ng gabay mula sa tao. Kapag nagbigay ng tamang feedback ang tao, maaaring isama ng modelo ang aral na iyon sa hinaharap.

Ang iterative at dynamic na diskarte na ito ay nagbibigay-daan sa modelo na patuloy na mapabuti, na tinitiyak na hindi lamang ito isang one-shot na sistema kundi isang sistemang natututo mula sa mga pagkakamali nito sa isang partikular na sesyon.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.tl.png)

## Mga Hangganan ng Ahensya

Sa kabila ng awtonomiya nito sa loob ng isang gawain, ang Agentic RAG ay hindi katumbas ng Artificial General Intelligence. Ang mga “agentic” na kakayahan nito ay limitado sa mga tool, mapagkukunan ng data, at mga patakaran na ibinigay ng mga developer ng tao. Hindi ito maaaring lumikha ng sarili nitong mga tool o lumampas sa mga hangganan ng domain na itinakda. Sa halip, namumukod-tangi ito sa dynamic na pag-oorganisa ng mga mapagkukunan na nasa kamay.

Ang mga pangunahing pagkakaiba mula sa mas advanced na mga anyo ng AI ay kinabibilangan ng:

1. **Domain-Specific Autonomy:** Ang mga sistema ng Agentic RAG ay nakatuon sa pagkamit ng mga layunin na itinakda ng user sa loob ng isang kilalang domain, gumagamit ng mga estratehiya tulad ng query rewriting o pagpili ng tool upang mapabuti ang mga resulta.
2. **Pag-asa sa Imprastraktura:** Ang mga kakayahan ng sistema ay nakasalalay sa mga tool at data na isinama ng mga developer. Hindi nito malalampasan ang mga hangganang ito nang walang interbensyon ng tao.
3. **Paggalang sa Mga Guardrail:** Ang mga alituntunin sa etika, mga panuntunan sa pagsunod, at mga patakaran sa negosyo ay nananatiling napakahalaga. Ang kalayaan ng agent ay palaging limitado ng mga hakbang sa kaligtasan at mga mekanismo ng pangangasiwa (sana?).

## Praktikal na Mga Gamit at Halaga

Namumukod-tangi ang Agentic RAG sa mga sitwasyong nangangailangan ng paulit-ulit na pagpapabuti at katumpakan:

1. **Mga Kapaligirang Inuuna ang Katumpakan:** Sa mga pagsusuri sa pagsunod, pagsusuri sa regulasyon, o pananaliksik sa legal, maaaring paulit-ulit na i-verify ng agentic na modelo ang mga katotohanan, kumonsulta sa maraming mapagkukunan, at muling isulat ang mga query hanggang sa makabuo ito ng isang masusing sinuring sagot.
2. **Kumplikadong Interaksyon sa Database:** Kapag humaharap sa mga nakabalangkas na data kung saan madalas mabigo o kailangang ayusin ang mga query, maaaring kusang pinuhin ng sistema ang mga query nito gamit ang Azure SQL o Microsoft Fabric OneLake, na tinitiyak na ang huling retrieval ay naaayon sa layunin ng user.
3. **Pinalawig na Workflow:** Ang mga mas mahabang sesyon ay maaaring umunlad habang lumilitaw ang bagong impormasyon. Ang Agentic RAG ay maaaring patuloy na isama ang bagong data, binabago ang mga estratehiya habang natututo ito nang higit pa tungkol sa espasyo ng problema.

## Pamamahala, Transparency, at Tiwala

Habang ang mga sistemang ito ay nagiging mas awtonomo sa kanilang pangangatwiran, mahalaga ang pamamahala at transparency:

- **Paliwanag na Pangangatwiran:** Maaaring magbigay ang modelo ng audit trail ng mga query na ginawa nito, ang mga mapagkukunan na kinonsulta nito, at ang mga hakbang sa pangangatwiran na ginawa nito upang maabot ang konklusyon nito. Ang mga tool tulad ng Azure AI Content Safety at Azure AI Tracing / GenAIOps ay makakatulong na mapanatili ang transparency at mabawasan ang mga panganib.
- **Kontrol sa Bias at Balanseng Retrieval:** Maaaring i-tune ng mga developer ang mga estratehiya sa retrieval upang matiyak na isinasaalang-alang ang balanseng, kinatawang mga mapagkukunan ng data, at regular na i-audit ang mga output upang matukoy ang bias o skewed na mga pattern gamit ang mga custom na modelo para sa mga advanced na organisasyon sa agham ng data gamit ang Azure Machine Learning.
- **Pangangasiwa ng Tao at Pagsunod:** Para sa mga sensitibong gawain, mahalaga ang pagsusuri ng tao. Ang Agentic RAG ay hindi pumapalit sa paghatol ng tao sa mga desisyong may mataas na panganib—ito ay umaakma dito sa pamamagitan ng paghahatid ng mas masusing sinuring mga opsyon.

Ang pagkakaroon ng mga tool na nagbibigay ng malinaw na talaan ng mga
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementasyon ng Retrieval Augmented Generation (RAG) gamit ang Azure OpenAI Service: Alamin kung paano gamitin ang sarili mong data sa Azure OpenAI Service. Ang Microsoft Learn module na ito ay nagbibigay ng komprehensibong gabay sa pag-implement ng RAG  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Pagsusuri ng mga generative AI application gamit ang Azure AI Foundry: Ang artikulong ito ay tumatalakay sa pagsusuri at paghahambing ng mga modelo sa mga pampublikong dataset, kabilang ang Agentic AI applications at RAG architectures</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Ano ang Agentic RAG | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Isang Kumpletong Gabay sa Agent-Based Retrieval Augmented Generation – Balita mula sa generation RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: Pabilisin ang iyong RAG gamit ang query reformulation at self-query! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Pagdaragdag ng Agentic Layers sa RAG</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Ang Hinaharap ng Knowledge Assistants: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Paano Bumuo ng Agentic RAG Systems</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Paggamit ng Azure AI Foundry Agent Service para i-scale ang iyong AI agents</a>  

### Mga Akademikong Papel  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Isang Survey sa Agentic RAG</a>  

## Nakaraang Aralin  

[Tool Use Design Pattern](../04-tool-use/README.md)  

## Susunod na Aralin  

[Pagbuo ng Mapagkakatiwalaang AI Agents](../06-building-trustworthy-agents/README.md)  

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.