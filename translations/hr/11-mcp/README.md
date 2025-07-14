<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:51:13+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hr"
}
-->
# Lekcija 11: Integracija Model Context Protocol (MCP)

## Uvod u Model Context Protocol (MCP)

Model Context Protocol (MCP) je napredni okvir osmišljen za standardizaciju interakcija između AI modela i klijentskih aplikacija. MCP služi kao most između AI modela i aplikacija koje ih koriste, pružajući dosljedno sučelje bez obzira na implementaciju samog modela.

Ključni aspekti MCP-a:

- **Standardizirana komunikacija**: MCP uspostavlja zajednički jezik za komunikaciju aplikacija s AI modelima
- **Poboljšano upravljanje kontekstom**: Omogućuje učinkovito prenošenje kontekstualnih informacija AI modelima
- **Kompatibilnost na više platformi**: Radi s različitim programskim jezicima uključujući C#, Java, JavaScript, Python i TypeScript
- **Besprijekorna integracija**: Omogućuje programerima jednostavnu integraciju različitih AI modela u njihove aplikacije

MCP je posebno koristan u razvoju AI agenata jer omogućuje agentima interakciju s različitim sustavima i izvorima podataka putem jedinstvenog protokola, čineći agente fleksibilnijima i moćnijima.

## Ciljevi učenja
- Razumjeti što je MCP i njegovu ulogu u razvoju AI agenata
- Postaviti i konfigurirati MCP server za GitHub integraciju
- Izgraditi sustav s više agenata koristeći MCP alate
- Implementirati RAG (Retrieval Augmented Generation) s Azure Cognitive Search

## Preduvjeti
- Python 3.8+
- Node.js 14+
- Azure pretplata
- GitHub račun
- Osnovno razumijevanje Semantic Kernel-a

## Upute za postavljanje

1. **Postavljanje okruženja**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracija Azure servisa**  
   - Kreirajte Azure Cognitive Search resurs  
   - Postavite Azure OpenAI servis  
   - Konfigurirajte varijable okruženja u `.env`

3. **Postavljanje MCP servera**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struktura projekta

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

## Glavne komponente

### 1. Sustav s više agenata
- GitHub Agent: analiza repozitorija  
- Hackathon Agent: preporuke projekata  
- Events Agent: prijedlozi tehnoloških događaja

### 2. Azure integracija
- Cognitive Search za indeksiranje događaja  
- Azure OpenAI za inteligenciju agenata  
- Implementacija RAG obrasca

### 3. MCP alati
- Analiza GitHub repozitorija  
- Inspekcija koda  
- Ekstrakcija metapodataka

## Pregled koda

Primjer prikazuje:  
1. Integraciju MCP servera  
2. Orkestraciju više agenata  
3. Integraciju Azure Cognitive Search  
4. Implementaciju RAG obrasca

Ključne značajke:  
- Analiza GitHub repozitorija u stvarnom vremenu  
- Inteligentne preporuke projekata  
- Uparivanje događaja koristeći Azure Search  
- Streaming odgovora s Chainlit

## Pokretanje primjera

Za detaljne upute o postavljanju i dodatne informacije, pogledajte [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Pokrenite MCP server:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Pokrenite aplikaciju:  
   ```bash
   chainlit run app.py -w
   ```

3. Testirajte integraciju:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Rješavanje problema

Česti problemi i rješenja:  
1. Problemi s MCP vezom  
   - Provjerite je li server pokrenut  
   - Provjerite dostupnost porta  
   - Potvrdite GitHub tokene

2. Problemi s Azure Search  
   - Provjerite connection stringove  
   - Provjerite postoji li indeks  
   - Potvrdite prijenos dokumenata

## Sljedeći koraci
- Istražite dodatne MCP alate  
- Implementirajte prilagođene agente  
- Unaprijedite RAG mogućnosti  
- Dodajte više izvora događaja

## Resursi
- [MCP za početnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search dokumentacija](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel vodiči](https://learn.microsoft.com/semantic-kernel/)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.