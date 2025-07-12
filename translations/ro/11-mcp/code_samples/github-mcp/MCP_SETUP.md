<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:18:32+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "ro"
}
-->
# Ghid de integrare MCP Server

## Cerințe preliminare
- Node.js instalat (versiunea 14 sau mai nouă)
- Managerul de pachete npm
- Mediu Python cu dependențele necesare

## Pași de configurare

1. **Instalează pachetul MCP Server**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Pornește MCP Server**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Serverul ar trebui să pornească și să afișeze o adresă URL de conectare.

3. **Verifică conexiunea**  
   - Caută pictograma de priză (🔌) în interfața ta Chainlit  
   - Ar trebui să apară un număr (1) lângă pictograma de priză, indicând o conexiune reușită  
   - Consola ar trebui să afișeze: "GitHub plugin setup completed successfully" (împreună cu alte mesaje de stare)

## Depanare

### Probleme comune

1. **Conflict de port**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Soluție: schimbă portul folosind:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Probleme de autentificare**  
   - Asigură-te că datele de autentificare GitHub sunt configurate corect  
   - Verifică dacă fișierul .env conține token-urile necesare  
   - Confirmă accesul la API-ul GitHub

3. **Conexiune eșuată**  
   - Confirmă că serverul rulează pe portul așteptat  
   - Verifică setările firewall-ului  
   - Asigură-te că mediul Python are pachetele necesare instalate

## Verificarea conexiunii

Serverul tău MCP este conectat corect când:  
1. Consola afișează "GitHub plugin setup completed successfully"  
2. Jurnalele de conexiune arată "✓ MCP Connection Status: Active"  
3. Comenzile GitHub funcționează în interfața de chat

## Variabile de mediu

Necesare în fișierul tău .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testarea conexiunii

Trimite acest mesaj de test în chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Un răspuns reușit va afișa informații despre repository.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.