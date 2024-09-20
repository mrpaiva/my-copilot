import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from src.rag_pipeline import answer_question, answer_question_elastic

#comando para iniciar o Streamlit streamlit run main.py


load_dotenv()

# app config
st.set_page_config(page_title="MultiClubes Copilot", page_icon="https://universidade.multiclubes.com.br/o/14796/favicon/organizations%2F14796%2Ffavicon%2F1692636935694-70ivmg4s0ss-acd42bef2e03f5c71704ef5107d1e963%2FMultiClubes.png")
st.title("MultiClubes Copilot")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="""
            Olá, eu sou seu Copiloto! Estou aqui para te ajudar com suas dúvidas sobre os produtos MultiClubes.
            
            **Antes de começarmos, aqui estão algumas coisas importantes para lembrar:**

            📌 **Eu ainda estou em treinamento!** Posso ocasionalmente gerar respostas incorretas ou confusas, mas estou sempre aprendendo para melhorar. Por favor seja gentil comigo 😊 

            🔄 Atualizações constantes: Estou em constante evolução. Novas funcionalidades podem ser adicionadas ao longo do tempo para te oferecer uma experiência ainda melhor.
            
            ---

            **Pronto para começar?** 🚀        
        """),
    ]

    
# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Digite uma mensagem aqui...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        #response = st.write_stream(answer_question(user_query, st.session_state.chat_history))
        response = st.write_stream(answer_question_elastic(user_query, st.session_state.chat_history))

        # Verifique se a resposta não é None
        if response is None:
            response = "Desculpe, não consegui encontrar uma resposta para sua pergunta."

    st.session_state.chat_history.append(AIMessage(content=response))
