<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5c05bcdfb163dfa2493db39dfb45ad9a",
  "translation_date": "2025-09-04T09:11:26+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "ro"
}
-->
# Utilizarea Protocoalelor Agentice (MCP, A2A și NLWeb)

[![Protocoale Agentice](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.ro.png)](https://youtu.be/X-Dh9R3Opn8)

Pe măsură ce utilizarea agenților AI crește, la fel crește și nevoia de protocoale care să asigure standardizarea, securitatea și să sprijine inovația deschisă. În această lecție, vom analiza 3 protocoale care încearcă să răspundă acestei nevoi - Model Context Protocol (MCP), Agent to Agent (A2A) și Natural Language Web (NLWeb).

## Introducere

În această lecție, vom acoperi:

• Cum **MCP** permite agenților AI să acceseze instrumente și date externe pentru a îndeplini sarcinile utilizatorilor.

• Cum **A2A** facilitează comunicarea și colaborarea între diferiți agenți AI.

• Cum **NLWeb** aduce interfețe în limbaj natural pe orice site web, permițând agenților AI să descopere și să interacționeze cu conținutul.

## Obiective de Învățare

• **Identificarea** scopului principal și a beneficiilor MCP, A2A și NLWeb în contextul agenților AI.

• **Explicarea** modului în care fiecare protocol facilitează comunicarea și interacțiunea între LLM-uri, instrumente și alți agenți.

• **Recunoașterea** rolurilor distincte pe care fiecare protocol le joacă în construirea sistemelor agentice complexe.

## Model Context Protocol

**Model Context Protocol (MCP)** este un standard deschis care oferă o modalitate standardizată pentru aplicații de a furniza context și instrumente către LLM-uri. Acest lucru permite un "adaptor universal" pentru diferite surse de date și instrumente la care agenții AI se pot conecta într-un mod consistent.

Să analizăm componentele MCP, beneficiile comparativ cu utilizarea directă a API-urilor și un exemplu despre cum agenții AI ar putea utiliza un server MCP.

### Componentele de Bază ale MCP

MCP funcționează pe o **arhitectură client-server**, iar componentele de bază sunt:

• **Gazdele** sunt aplicații LLM (de exemplu, un editor de cod precum VSCode) care inițiază conexiunile către un server MCP.

• **Clienții** sunt componente din cadrul aplicației gazdă care mențin conexiuni unu-la-unu cu serverele.

• **Serverele** sunt programe ușoare care expun capabilități specifice.

Protocolul include trei primitive de bază care reprezintă capabilitățile unui server MCP:

• **Instrumente**: Acestea sunt acțiuni sau funcții discrete pe care un agent AI le poate apela pentru a efectua o acțiune. De exemplu, un serviciu meteo ar putea expune un instrument "get weather", sau un server de e-commerce ar putea expune un instrument "purchase product". Serverele MCP listează numele fiecărui instrument, descrierea și schema de intrare/ieșire în lista lor de capabilități.

• **Resurse**: Acestea sunt elemente de date sau documente doar pentru citire pe care un server MCP le poate furniza, iar clienții le pot prelua la cerere. Exemple includ conținuturi de fișiere, înregistrări din baze de date sau fișiere jurnal. Resursele pot fi text (cum ar fi cod sau JSON) sau binare (cum ar fi imagini sau PDF-uri).

• **Șabloane**: Acestea sunt șabloane predefinite care oferă sugestii de solicitări, permițând fluxuri de lucru mai complexe.

### Beneficiile MCP

MCP oferă avantaje semnificative pentru agenții AI:

• **Descoperirea Dinamică a Instrumentelor**: Agenții pot primi dinamic o listă de instrumente disponibile de la un server, împreună cu descrieri ale funcționalităților acestora. Acest lucru contrastează cu API-urile tradiționale, care necesită adesea codificare statică pentru integrare, ceea ce înseamnă că orice modificare a API-ului necesită actualizări de cod. MCP oferă o abordare "integrează o dată", ceea ce duce la o adaptabilitate mai mare.

• **Interoperabilitate între LLM-uri**: MCP funcționează cu diferite LLM-uri, oferind flexibilitate pentru a schimba modelele de bază pentru o performanță mai bună.

• **Securitate Standardizată**: MCP include o metodă standard de autentificare, îmbunătățind scalabilitatea atunci când se adaugă acces la servere MCP suplimentare. Acest lucru este mai simplu decât gestionarea diferitelor chei și tipuri de autentificare pentru diverse API-uri tradiționale.

### Exemplu MCP

![Diagrama MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.ro.png)

Imaginați-vă că un utilizator dorește să rezerve un zbor folosind un asistent AI alimentat de MCP.

1. **Conexiune**: Asistentul AI (clientul MCP) se conectează la un server MCP furnizat de o companie aeriană.

2. **Descoperirea Instrumentelor**: Clientul întreabă serverul MCP al companiei aeriene: "Ce instrumente aveți disponibile?" Serverul răspunde cu instrumente precum "search flights" și "book flights".

3. **Invocarea Instrumentului**: Utilizatorul îi cere asistentului AI: "Te rog, caută un zbor de la Portland la Honolulu." Asistentul AI, folosindu-și LLM-ul, identifică faptul că trebuie să apeleze instrumentul "search flights" și transmite parametrii relevanți (origine, destinație) către serverul MCP.

4. **Executare și Răspuns**: Serverul MCP, acționând ca un intermediar, face apelul efectiv către API-ul intern al companiei aeriene. Primește informațiile despre zbor (de exemplu, date JSON) și le trimite înapoi asistentului AI.

5. **Interacțiune Ulterioară**: Asistentul AI prezintă opțiunile de zbor. Odată ce utilizatorul selectează un zbor, asistentul poate invoca instrumentul "book flight" pe același server MCP, finalizând rezervarea.

## Protocolul Agent-la-Agent (A2A)

În timp ce MCP se concentrează pe conectarea LLM-urilor la instrumente, **protocolul Agent-la-Agent (A2A)** merge mai departe, permițând comunicarea și colaborarea între diferiți agenți AI. A2A conectează agenți AI din diferite organizații, medii și stive tehnologice pentru a îndeplini o sarcină comună.

Vom analiza componentele și beneficiile A2A, împreună cu un exemplu despre cum ar putea fi aplicat în aplicația noastră de călătorii.

### Componentele de Bază ale A2A

A2A se concentrează pe facilitarea comunicării între agenți și pe colaborarea acestora pentru a îndeplini o sub-sarcină a utilizatorului. Fiecare componentă a protocolului contribuie la acest scop:

#### Cardul Agentului

Similar cu modul în care un server MCP partajează o listă de instrumente, un Card al Agentului conține:
- Numele agentului.
- O **descriere a sarcinilor generale** pe care le îndeplinește.
- O **listă de abilități specifice** cu descrieri pentru a ajuta alți agenți (sau chiar utilizatorii umani) să înțeleagă când și de ce ar dori să apeleze acel agent.
- **URL-ul endpoint-ului curent** al agentului.
- **Versiunea** și **capabilitățile** agentului, cum ar fi răspunsurile în flux și notificările push.

#### Executorul Agentului

Executorul Agentului este responsabil pentru **transmiterea contextului conversației utilizatorului către agentul la distanță**, astfel încât acesta să înțeleagă sarcina care trebuie îndeplinită. Într-un server A2A, un agent folosește propriul său LLM pentru a analiza cererile primite și pentru a executa sarcini utilizând propriile sale instrumente interne.

#### Artefactul

Odată ce un agent la distanță a finalizat sarcina solicitată, produsul muncii sale este creat sub forma unui artefact. Un artefact **conține rezultatul muncii agentului**, o **descriere a ceea ce a fost realizat** și **contextul textului** care este transmis prin protocol. După ce artefactul este trimis, conexiunea cu agentul la distanță este închisă până când este necesară din nou.

#### Coada de Evenimente

Această componentă este utilizată pentru **gestionarea actualizărilor și transmiterea mesajelor**. Este deosebit de importantă în producție pentru sistemele agentice, pentru a preveni închiderea conexiunii între agenți înainte ca o sarcină să fie finalizată, mai ales atunci când timpii de finalizare a sarcinilor pot fi mai lungi.

### Beneficiile A2A

• **Colaborare Îmbunătățită**: Permite agenților din diferiți furnizori și platforme să interacționeze, să partajeze context și să colaboreze, facilitând automatizarea fără întreruperi între sisteme tradițional deconectate.

• **Flexibilitate în Alegerea Modelului**: Fiecare agent A2A poate decide ce LLM utilizează pentru a răspunde cererilor, permițând optimizarea sau ajustarea fină a modelelor pentru fiecare agent, spre deosebire de o conexiune unică LLM în unele scenarii MCP.

• **Autentificare Integrată**: Autentificarea este integrată direct în protocolul A2A, oferind un cadru de securitate robust pentru interacțiunile între agenți.

### Exemplu A2A

![Diagrama A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.ro.png)

Să extindem scenariul nostru de rezervare a călătoriilor, dar de această dată folosind A2A.

1. **Cererea Utilizatorului către Multi-Agent**: Un utilizator interacționează cu un "Agent de Călătorii" client/agent A2A, poate spunând: "Te rog, rezervă o călătorie completă la Honolulu pentru săptămâna viitoare, incluzând zboruri, un hotel și o mașină de închiriat".

2. **Orchestrarea de către Agentul de Călătorii**: Agentul de Călătorii primește această cerere complexă. Folosește propriul său LLM pentru a raționa despre sarcină și a determina că trebuie să interacționeze cu alți agenți specializați.

3. **Comunicare între Agenți**: Agentul de Călătorii utilizează protocolul A2A pentru a se conecta la agenți specializați, cum ar fi un "Agent Aerian", un "Agent Hotelier" și un "Agent de Închirieri Auto", creați de companii diferite.

4. **Executarea Sarcinilor Delegat**: Agentul de Călătorii trimite sarcini specifice acestor agenți specializați (de exemplu, "Găsește zboruri către Honolulu", "Rezervă un hotel", "Închiriază o mașină"). Fiecare dintre acești agenți specializați, rulând propriile lor LLM-uri și utilizând propriile lor instrumente (care ar putea fi servere MCP în sine), își îndeplinește partea specifică a rezervării.

5. **Răspuns Consolidat**: Odată ce toți agenții specializați își finalizează sarcinile, Agentul de Călătorii compilează rezultatele (detalii despre zbor, confirmarea hotelului, rezervarea mașinii) și trimite un răspuns complet, în stil conversațional, înapoi utilizatorului.

## Natural Language Web (NLWeb)

Site-urile web au fost mult timp modalitatea principală prin care utilizatorii accesează informații și date pe internet.

Să analizăm diferitele componente ale NLWeb, beneficiile NLWeb și un exemplu despre cum funcționează NLWeb, analizând aplicația noastră de călătorii.

### Componentele NLWeb

- **Aplicația NLWeb (Codul Serviciului de Bază)**: Sistemul care procesează întrebările în limbaj natural. Conectează diferitele părți ale platformei pentru a crea răspunsuri. Poate fi considerat **motorul care alimentează funcțiile de limbaj natural** ale unui site web.

- **Protocolul NLWeb**: Acesta este un **set de reguli de bază pentru interacțiunea în limbaj natural** cu un site web. Trimite răspunsuri în format JSON (adesea folosind Schema.org). Scopul său este de a crea o fundație simplă pentru "AI Web", în același mod în care HTML a făcut posibilă partajarea documentelor online.

- **Server MCP (Punctul de Acces al Model Context Protocol)**: Fiecare configurare NLWeb funcționează și ca un **server MCP**. Acest lucru înseamnă că poate **partaja instrumente (cum ar fi o metodă "ask") și date** cu alte sisteme AI. În practică, acest lucru face ca conținutul și abilitățile site-ului să fie utilizabile de agenții AI, permițând site-ului să devină parte a "ecosistemului agentic" mai larg.

- **Modele de Încorporare**: Aceste modele sunt utilizate pentru a **converti conținutul site-ului web în reprezentări numerice numite vectori** (încorporări). Acești vectori captează semnificația într-un mod pe care computerele îl pot compara și căuta. Sunt stocați într-o bază de date specială, iar utilizatorii pot alege ce model de încorporare doresc să utilizeze.

- **Baza de Date Vectorială (Mecanism de Regăsire)**: Această bază de date **stochează încorporările conținutului site-ului web**. Când cineva pune o întrebare, NLWeb verifică baza de date vectorială pentru a găsi rapid cele mai relevante informații. Oferă o listă rapidă de posibile răspunsuri, clasificate după similaritate. NLWeb funcționează cu diferite sisteme de stocare vectorială, cum ar fi Qdrant, Snowflake, Milvus, Azure AI Search și Elasticsearch.

### NLWeb prin Exemplu

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.ro.png)

Să luăm în considerare din nou site-ul nostru de rezervări de călătorii, dar de această dată, alimentat de NLWeb.

1. **Ingestia Datelor**: Cataloagele existente ale produselor site-ului de călătorii (de exemplu, listele de zboruri, descrierile hotelurilor, pachetele turistice) sunt formatate folosind Schema.org sau încărcate prin feed-uri RSS. Instrumentele NLWeb preiau aceste date structurate, creează încorporări și le stochează într-o bază de date vectorială locală sau la distanță.

2. **Interogare în Limbaj Natural (Uman)**: Un utilizator vizitează site-ul și, în loc să navigheze prin meniuri, introduce într-o interfață de chat: "Găsește-mi un hotel prietenos cu familiile în Honolulu, cu piscină, pentru săptămâna viitoare".

3. **Procesarea NLWeb**: Aplicația NLWeb primește această interogare. Trimite interogarea către un LLM pentru înțelegere și, simultan, caută în baza sa de date vectorială pentru listele de hoteluri relevante.

4. **Rezultate Precise**: LLM-ul ajută la interpretarea rezultatelor căutării din baza de date, identifică cele mai bune potriviri pe baza criteriilor "prietenos cu familiile", "piscină" și "Honolulu", și apoi formatează un răspuns în limbaj natural. Esențial, răspunsul se referă la hoteluri reale din catalogul site-ului, evitând informațiile inventate.

5. **Interacțiunea cu Agenții AI**: Deoarece NLWeb servește ca un server MCP, un agent AI extern de călătorii ar putea, de asemenea, să se conecteze la instanța NLWeb a acestui site. Agentul AI ar putea apoi să utilizeze metoda `ask` MCP pentru a interoga direct site-ul: `ask("Există restaurante prietenoase cu veganii în zona Honolulu recomandate de hotel?")`. Instanța NLWeb ar procesa acest lucru, utilizând baza sa de date cu informații despre restaurante (dacă este încărcată), și ar returna un răspuns structurat în format JSON.

### Ai Mai Multe Întrebări despre MCP/A2A/NLWeb?

Alătură-te [Discordului Azure AI Foundry](https://aka.ms/ai-agents/discord) pentru a te întâlni cu alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările tale despre agenții AI.

## Resurse

- [MCP pentru Începători](https://aka.ms/mcp-for-beginners)  
- [Documentația MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repo-ul NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Ghiduri Semantic Kernel](https://learn.microsoft.com

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.