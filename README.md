# Agno Course

Projeto de estudo do framework [Agno](https://github.com/agno-agi/agno) para construção de agentes de IA, desenvolvido como parte do curso da Asimov Academy.

## Sobre o Agno

Agno é um framework Python para criação de agentes de IA com suporte a múltiplos modelos de linguagem (LLMs), ferramentas e memória.

## Exemplos

| Arquivo | Descrição |
|---|---|
| `0.llm_call.py` | Chamada direta ao LLM via Groq sem agente |
| `1.1.researcher.py` | Agente com ferramenta de busca na web (Tavily) |
| `1.2.anaista.py` | Agente analista financeiro com dados do Yahoo Finance |

## Tecnologias

- **[Agno](https://github.com/agno-agi/agno)** — framework de agentes de IA
- **[Groq](https://groq.com/)** — provedor de LLM (modelo `llama-3.3-70b-versatile`)
- **[Tavily](https://tavily.com/)** — ferramenta de busca na web para agentes
- **[YFinance](https://github.com/ranaroussi/yfinance)** — dados financeiros do Yahoo Finance
- **Python 3.11+**

## Configuração

1. Clone o repositório e instale as dependências:

```bash
uv sync
```

2. Crie um arquivo `.env` na raiz do projeto com as chaves de API necessárias:

```env
GROQ_API_KEY=sua_chave_aqui
TAVILY_API_KEY=sua_chave_aqui
```

## Executando os exemplos

```bash
# Chamada direta ao LLM
uv run 0.llm_call.py

# Agente pesquisador (busca na web)
uv run 1.1.researcher.py

# Agente analista financeiro
uv run 1.2.anaista.py
```
