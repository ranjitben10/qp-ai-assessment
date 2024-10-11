
from langchain_text_splitters import RecursiveCharacterTextSplitter


def text_splitter_func():
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024, chunk_overlap=80
    )
    return text_splitter