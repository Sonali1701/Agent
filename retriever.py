from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_top_chunks(query, k=3):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Enable deserialization by setting allow_dangerous_deserialization=True
    db = FAISS.load_local("index", embeddings, allow_dangerous_deserialization=True)

    docs = db.similarity_search(query, k=k)
    return docs
