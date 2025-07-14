<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bbce3572338711aeab758506379ab716",
  "translation_date": "2025-07-12T13:51:25+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "sl"
}
-->
# Lekcija 11: Integracija Model Context Protocol (MCP)

## Uvod v Model Context Protocol (MCP)

Model Context Protocol (MCP) je napreden okvir, zasnovan za standardizacijo interakcij med AI modeli in odjemalskimi aplikacijami. MCP deluje kot most med AI modeli in aplikacijami, ki jih uporabljajo, ter zagotavlja enoten vmesnik ne glede na osnovno implementacijo modela.

Ključni vidiki MCP:

- **Standardizirana komunikacija**: MCP vzpostavlja skupni jezik za komunikacijo aplikacij z AI modeli
- **Izboljšano upravljanje konteksta**: Omogoča učinkovito prenašanje kontekstualnih informacij AI modelom
- **Združljivost med platformami**: Deluje v različnih programskih jezikih, vključno s C#, Java, JavaScript, Python in TypeScript
- **Brezhibna integracija**: Razvijalcem omogoča enostavno vključevanje različnih AI modelov v njihove aplikacije

MCP je še posebej dragocen pri razvoju AI agentov, saj omogoča agentom interakcijo z različnimi sistemi in viri podatkov preko enotnega protokola, kar agente naredi bolj prilagodljive in zmogljive.

## Cilji učenja
- Razumeti, kaj je MCP in kakšna je njegova vloga pri razvoju AI agentov
- Nastaviti in konfigurirati MCP strežnik za integracijo z GitHubom
- Zgraditi sistem z več agenti z uporabo MCP orodij
- Implementirati RAG (Retrieval Augmented Generation) z Azure Cognitive Search

## Predpogoji
- Python 3.8+
- Node.js 14+
- Azure naročnina
- GitHub račun
- Osnovno razumevanje Semantic Kernel

## Navodila za nastavitev

1. **Nastavitev okolja**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Konfiguracija Azure storitev**
   - Ustvarite Azure Cognitive Search vir
   - Nastavite Azure OpenAI storitev
   - Konfigurirajte okoljske spremenljivke v `.env`

3. **Nastavitev MCP strežnika**
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

## Osrednje komponente

### 1. Sistem z več agenti
- GitHub Agent: analiza repozitorijev
- Hackathon Agent: priporočila projektov
- Events Agent: predlogi tehnoloških dogodkov

### 2. Azure integracija
- Cognitive Search za indeksiranje dogodkov
- Azure OpenAI za inteligenco agentov
- Implementacija RAG vzorca

### 3. MCP orodja
- Analiza GitHub repozitorijev
- Pregled kode
- Izvleček metapodatkov

## Pregled kode

Primer prikazuje:
1. Integracijo MCP strežnika
2. Orkestracijo sistema z več agenti
3. Integracijo Azure Cognitive Search
4. Implementacijo RAG vzorca

Ključne funkcije:
- Analiza GitHub repozitorijev v realnem času
- Pametna priporočila projektov
- Ujemanje dogodkov z uporabo Azure Search
- Pretakanje odgovorov s Chainlit

## Zagon primera

Za podrobna navodila za nastavitev in več informacij si oglejte [Github MCP Server Example README](./code_samples/github-mcp/README.md).

1. Zaženite MCP strežnik:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Zaženite aplikacijo:
   ```bash
   chainlit run app.py -w
   ```

3. Preizkusite integracijo:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Reševanje težav

Pogoste težave in rešitve:
1. Težave s povezavo MCP
   - Preverite, ali strežnik deluje
   - Preverite razpoložljivost vrat
   - Potrdite GitHub žetone

2. Težave z Azure Search
   - Preverite povezovalne nize
   - Preverite obstoj indeksa
   - Potrdite nalaganje dokumentov

## Naslednji koraki
- Raziščite dodatna MCP orodja
- Implementirajte lastne agente
- Izboljšajte zmogljivosti RAG
- Dodajte več virov dogodkov

## Viri
- [MCP za začetnike](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentacija](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Dokumentacija Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Vodniki Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.