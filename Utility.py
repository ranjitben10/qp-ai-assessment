

from langchain_community.llms import Ollama

from Embeddings import embeddings_func
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PDFPlumberLoader

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

from TextSplitter import text_splitter_func

def prompt():
    template = """ 
    <s>[INST] You are a technical assistant good at searching docuemnts. If you do not have an answer from the provided information say so. [/INST] </s>
    [INST] {input}
           Context: {context}
           Answer:
    [/INST]
    """
    return template

def load_llm():
    cached_llm = Ollama(model="llama3.1")
    return cached_llm

def vector_store_func(folder_path):
    embedding = embeddings_func()
    vector_store = FAISS.load_local('faiss_index', embedding,allow_dangerous_deserialization=True)
    return vector_store

def retreiver_func(folder_path):
    vector_store = vector_store_func(folder_path)
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 3,
            "score_threshold": 0.1,
        },
    )

    return retriever


def get_response_from_query(query,folder_path):
    raw_prompt = prompt()
    retriever = retreiver_func(folder_path)
    cached_llm = load_llm()
    prompt_ = PromptTemplate.from_template(raw_prompt)
    document_chain = create_stuff_documents_chain(cached_llm, prompt_)
    chain = create_retrieval_chain(retriever, document_chain)

    result = chain.invoke({"input": query})

    print(result)

    sources = []
    for doc in result["context"]:
        sources.append(
            {"source": doc.metadata["source"], "page_content": doc.page_content}
        )

    response_answer = {"answer": result["answer"], "sources": sources}

    return response_answer



def load_split_embed_save_vector_store_func(save_file,folder_path,file_name):
    text_splitter = text_splitter_func()
    embedding = embeddings_func()

    loader=PyPDFDirectoryLoader("pdf")

    documents=loader.load()
    print(documents)
    final_documents=text_splitter.split_documents(documents)
    print("documents:  ",final_documents)
    vector_store = FAISS.from_documents(
        final_documents, embedding
    )

    vector_store.save_local("faiss_index")

    response = {
        "status": "Successfully Uploaded...",
        "filename": file_name,
    }

    return response
