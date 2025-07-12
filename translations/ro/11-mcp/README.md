<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:50:40+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ro"
}
-->
# Lecția 11: Integrarea Model Context Protocol (MCP)

## Introducere în Model Context Protocol (MCP)

Model Context Protocol (MCP) este un cadru avansat creat pentru a standardiza interacțiunile dintre modelele AI și aplicațiile client. MCP funcționează ca o punte între modelele AI și aplicațiile care le utilizează, oferind o interfață consistentă indiferent de implementarea modelului de bază.

Aspecte cheie ale MCP:

- **Comunicare standardizată**: MCP stabilește un limbaj comun pentru ca aplicațiile să comunice cu modelele AI
- **Gestionare îmbunătățită a contextului**: Permite transmiterea eficientă a informațiilor contextuale către modelele AI
- **Compatibilitate cross-platform**: Funcționează în diverse limbaje de programare, inclusiv C#, Java, JavaScript, Python și TypeScript
- **Integrare fără probleme**: Permite dezvoltatorilor să integreze cu ușurință diferite modele AI în aplicațiile lor

MCP este deosebit de valoros în dezvoltarea agenților AI, deoarece permite agenților să interacționeze cu diverse sisteme și surse de date printr-un protocol unificat, făcând agenții mai flexibili și mai puternici.

## Obiective de învățare
- Înțelegerea a ceea ce este MCP și rolul său în dezvoltarea agenților AI
- Configurarea și setarea unui server MCP pentru integrarea cu GitHub
- Construirea unui sistem multi-agent folosind instrumentele MCP
- Implementarea RAG (Retrieval Augmented Generation) cu Azure Cognitive Search

## Cerințe preliminare
- Python 3.8+
- Node.js 14+
- Abonament Azure
- Cont GitHub
- Cunoștințe de bază despre Semantic Kernel

## Instrucțiuni de configurare

1. **Configurarea mediului**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurarea serviciilor Azure**
   - Creează o resursă Azure Cognitive Search
   - Configurează serviciul Azure OpenAI
   - Setează variabilele de mediu în `.env`

3. **Configurarea serverului MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Structura proiectului

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

## Componente principale

### 1. Sistem multi-agent
- GitHub Agent: Analiza depozitelor
- Hackathon Agent: Recomandări de proiecte
- Events Agent: Sugestii pentru evenimente tech

### 2. Integrare Azure
- Cognitive Search pentru indexarea evenimentelor
- Azure OpenAI pentru inteligența agenților
- Implementarea pattern-ului RAG

### 3. Instrumente MCP
- Analiza depozitelor GitHub
- Inspectarea codului
- Extracția metadatelor

## Parcurgerea codului

Exemplul demonstrează:
1. Integrarea serverului MCP
2. Orchestrarea sistemului multi-agent
3. Integrarea Azure Cognitive Search
4. Implementarea pattern-ului RAG

Caracteristici cheie:
- Analiză în timp real a depozitelor GitHub
- Recomandări inteligente de proiecte
- Potrivirea evenimentelor folosind Azure Search
- Răspunsuri în streaming cu Chainlit

## Rularea exemplului

Pentru instrucțiuni detaliate de configurare și mai multe informații, consultă [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Pornește serverul MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lansează aplicația:
   ```bash
   chainlit run app.py -w
   ```

3. Testează integrarea:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Depanare

Probleme comune și soluții:
1. Probleme de conexiune MCP
   - Verifică dacă serverul este pornit
   - Verifică disponibilitatea portului
   - Confirmă token-urile GitHub

2. Probleme Azure Search
   - Validează string-urile de conexiune
   - Verifică existența indexului
   - Confirmă încărcarea documentelor

## Pași următori
- Explorează instrumente MCP suplimentare
- Implementează agenți personalizați
- Îmbunătățește capabilitățile RAG
- Adaugă mai multe surse de evenimente

## Resurse
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.