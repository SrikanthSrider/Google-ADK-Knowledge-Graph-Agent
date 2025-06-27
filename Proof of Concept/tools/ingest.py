from langchain_community.document_loaders import WebBaseLoader, PyMuPDFLoader
import os

def load_article(source:str) -> str:
    if source.startswith("http"):
        loader = WebBaseLoader(source)
        docs = loader.load()
        return docs[0].page_content
    elif source.endswith(".pdf") and os.path.exists(source):
        loader = PyMuPDFLoader(source)
        docs = loader.load()
        return "\n".join([doc.page_content for doc in docs])
    else:
        raise ValueError("Invalid input. Must be a valid URL or PDF path")