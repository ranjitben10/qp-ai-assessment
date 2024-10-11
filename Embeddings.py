# from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# def embeddings_func():
#     embedding = FastEmbedEmbeddings()
#     return embedding


from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def embeddings_func():
    # Initialize the Hugging Face embeddings
    ## Embedding Using Huggingface
    huggingface_embeddings=HuggingFaceBgeEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )
    return huggingface_embeddings