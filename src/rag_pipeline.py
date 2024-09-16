from config.config import OPENAI_API_KEY
from langchain_community.vectorstores import FAISS
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import hub

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

# Carregar o documento PDF
loader = PyPDFLoader("data/pdfs/documento1.pdf")
docs = loader.load()

def answer_question(user_query, chat_history):
    # Criar embeddings e o FAISS vectorstore
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    # Recuperar documentos relevantes
    relevant_docs = retriever.get_relevant_documents(user_query)

    # Criar uma lista de strings para os documentos relevantes
    relevant_texts = "\n".join([doc.page_content for doc in relevant_docs])

    template = """
    You are a helpful assistant. Answer the following questions considering the history of the conversation and the relevant documents:

    Chat history: {chat_history}

    Relevant documents: {relevant_documents}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI()
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "relevant_documents": relevant_texts,
        "user_question": user_query,
    })


def answer_question_elastic(user_query, chat_history):
    # Criar embeddings e o FAISS vectorstore
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = ElasticsearchStore(
        es_url="http://localhost:9200",
        index_name="langchain_index",
        embedding=embeddings,
        es_user="elastic",
        es_password="magrela01!",
    )

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.2}
    )

    # Recuperar documentos relevantes
    relevant_docs = retriever.get_relevant_documents(user_query)

    # Criar uma lista de strings para os documentos relevantes
    relevant_texts = "\n".join([doc.page_content for doc in relevant_docs])

    template = """
    Você é um assistente útil. Responda às seguintes perguntas considerando o histórico da conversa e os documentos relevantes:

    Chat history: {chat_history}

    Relevant documents: {relevant_documents}

    User question: {user_question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI()
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.stream({
        "chat_history": chat_history,
        "relevant_documents": relevant_texts,
        "user_question": user_query,
    })