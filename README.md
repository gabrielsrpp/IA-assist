# IA Assist - 🤖

#
<img width="704" height="764" alt="image" src="https://github.com/user-attachments/assets/1131b84f-996c-4685-83d1-65bceb135b6c" />

Este projeto simples consiste num assistente de Inteligência Artificial desenvolvido para rodar totalmente de forma local. Utiliza modelos de linguagem de última geração (LLMs) para responder a dúvidas técnicas, garantindo privacidade de dados e custo zero de API.

#

## 🚀 Diferenciais Técnicos
- **Privacidade:** O modelo roda localmente; nenhum dado sai da máquina do utilizador.
- **Eficiência:** Utilização de modelos quantizados para rodar em hardware comum.
- **Interface Web:** Interface amigável construída com Streamlit.
- 
#

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** [Python](https://www.python.org/)
- **Interface:** [Streamlit](https://streamlit.io/)
- **Orquestração de IA:** [Ollama](https://ollama.com/)
- **Modelo:** Phi-3 (Microsoft) - um modelo leve e potente de 3.8B de parâmetros, podendo rodar em maquinas de baixo desempenho.

#

## 📋 Pré-requisitos
Antes de rodar o projeto, precisa de ter instalado:
1. [Python 3.10+](https://www.python.org/downloads/)
2. [Ollama](https://ollama.com/)

3. #

## 🔧 Configuração e Instalação

#

1. **Descarregar o Modelo:**
   Abra o seu terminal e execute:
   ```bash
   ollama run phi3

2. **Rodar a interface web:**
   Abra o seu terminal e execute:
   ```bash
   streamlit run main.py
