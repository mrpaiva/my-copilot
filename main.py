import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
from src.rag_pipeline import answer_question, answer_question_elastic

#comando para iniciar o Streamlit streamlit run main.py


load_dotenv()

# app config
st.set_page_config(page_title="Meu copilo", page_icon="🤖")
st.title("Copiloto")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Oi, eu sou seu assistente. Como posso te ajudar?"),
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
