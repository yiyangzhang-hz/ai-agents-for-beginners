<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-07-12T14:16:02+00:00",
  "source_file": "11-mcp/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "pt"
}
-->
# Guia de Integração do Servidor MCP

## Pré-requisitos
- Node.js instalado (versão 14 ou superior)
- Gestor de pacotes npm
- Ambiente Python com as dependências necessárias

## Passos de Configuração

1. **Instalar o Pacote do Servidor MCP**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Iniciar o Servidor MCP**  
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   O servidor deverá arrancar e mostrar uma URL de ligação.

3. **Verificar a Ligação**  
   - Procure o ícone de ficha (🔌) na sua interface Chainlit  
   - Deve aparecer um número (1) ao lado do ícone da ficha, indicando ligação bem-sucedida  
   - A consola deverá mostrar: "GitHub plugin setup completed successfully" (juntamente com outras linhas de estado)

## Resolução de Problemas

### Problemas Comuns

1. **Conflito de Porta**  
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Solução: Altere a porta usando:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemas de Autenticação**  
   - Certifique-se de que as credenciais do GitHub estão corretamente configuradas  
   - Verifique se o ficheiro .env contém os tokens necessários  
   - Confirme o acesso à API do GitHub

3. **Falha na Ligação**  
   - Confirme que o servidor está a correr na porta esperada  
   - Verifique as definições do firewall  
   - Assegure que o ambiente Python tem os pacotes necessários

## Verificação da Ligação

O seu servidor MCP está corretamente ligado quando:  
1. A consola mostra "GitHub plugin setup completed successfully"  
2. Os registos de ligação indicam "✓ MCP Connection Status: Active"  
3. Os comandos do GitHub funcionam na interface de chat

## Variáveis de Ambiente

Obrigatórias no seu ficheiro .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Testar Ligação

Envie esta mensagem de teste no chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Uma resposta bem-sucedida mostrará informações do repositório.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.