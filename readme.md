# My Copilot - Projeto de Estudo LangChain 🤖

## 🎯 Sobre o Projeto

Este projeto representa meus primeiros passos no mundo do LangChain e desenvolvimento de assistentes virtuais. Decidi criar este chatbot como forma de aprender na prática como integrar diferentes tecnologias e entender melhor o funcionamento de Large Language Models (LLMs).

## 🌱 Objetivo de Aprendizado

Meu principal objetivo foi entender:
- Como funciona o LangChain na prática
- Como criar uma interface de chat usando Streamlit
- Como implementar buscas com Elasticsearch
- Como funciona um sistema RAG (Retrieval Augmented Generation)

## 🛠️ Tecnologias que Estou Aprendendo

Neste projeto de estudo, estou utilizando:

- **Streamlit**: Minha primeira experiência criando interfaces web com Python
- **LangChain**: Aprendendo a trabalhar com esta poderosa biblioteca para LLMs
- **Elasticsearch**: Descobrindo como implementar buscas eficientes
- **Python-dotenv**: Praticando o uso seguro de variáveis de ambiente
- **RAG Pipeline**: Entendendo como combinar busca e geração de texto

## 🚀 Como Rodar o Projeto

Se você também está aprendendo, aqui está como configurar:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/my-copilot.git
cd my-copilot
```

2. Configure o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env`:
```env
OPENAI_API_KEY=sua_openai_api_key
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY=sua_langchain_apikey
ELASTICSEARCH_URL=sua_url_elasticsearch
ELASTICSEARCH_USERNAME=seu_usuario
ELASTICSEARCH_PASSWORD=sua_senha
```

5. Inicie a aplicação:
```bash
streamlit run main.py
```

## 📂 Como o Projeto está Organizado

```
my-copilot/
├── main.py                # Aplicação principal com Streamlit
├── src/
│   ├── __init__.py
│   └── rag_pipeline.py    # Implementação do RAG
├── requirements.txt       # Dependências do projeto
└── .env                  # Configurações sensíveis
```

## 💡 O Que Aprendi Até Agora

- **Streamlit**: 
  - Como criar uma interface de chat interativa
  - Como gerenciar estado da aplicação
  - Como implementar streaming de respostas

- **LangChain**:
  - Trabalhar com diferentes tipos de mensagens (AI e Human)
  - Criar um pipeline de processamento
  - Integrar com sistemas de busca

- **Elasticsearch**:
  - Configuração básica
  - Implementação de buscas
  - Integração com o pipeline RAG

## 🔄 Próximos Passos

Pretendo expandir meus conhecimentos:
- Melhorar a qualidade das respostas
- Implementar mais recursos do LangChain
- Aprofundar o conhecimento em RAG
- Explorar outras funcionalidades do Elasticsearch

## 📝 Notas de Aprendizado

Este projeto está em constante evolução conforme aprendo mais sobre:
- Melhores práticas no uso do LangChain
- Otimização de buscas no Elasticsearch
- Técnicas de prompt engineering
- Desenvolvimento com Streamlit

## 🤝 Vamos Aprender Juntos!

Se você também está estudando estas tecnologias:
- Sinta-se à vontade para fazer fork do projeto
- Abra issues com dúvidas ou sugestões
- Compartilhe suas próprias descobertas

## 📞 Contato

Se quiser trocar ideias sobre o projeto ou sobre aprendizado em IA:
- LinkedIn: https://www.linkedin.com/in/mauro-couto-de-paiva/
- Medium: https://medium.com/@mrpaiva

---

🌟 Este é um projeto em desenvolvimento, parte da minha jornada de aprendizado em IA e desenvolvimento de software!