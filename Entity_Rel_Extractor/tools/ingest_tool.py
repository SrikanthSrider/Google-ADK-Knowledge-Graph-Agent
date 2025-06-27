import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders.pdf import PyMuPDFLoader

def ingest_text_from_source(inputs: dict) -> dict:
    source = inputs.get("source")
    if not source:
        raise ValueError("Missing 'source' in input.")
    if source.startswith("http"):
        loader = WebBaseLoader(source)
        docs = loader.load()
        text = docs[0].page_content
    elif source.endswith(".pdf") and os.path.exists(source):
        loader = PyMuPDFLoader(source)
        docs = loader.load()
        text = "\n".join(doc.page_content for doc in docs)
    else:
        raise ValueError("Source must be a valid URL or path to a local PDF.")

    # Clean and truncate
    cleaned = " ".join(text.strip().split())
    return {"cleaned_text": cleaned[:24000]}  # trim for LLM input limits