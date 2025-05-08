from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_top_chunks(query, k=3):
    # Enable deserialization by setting allow_dangerous_deserialization=True
    db = FAISS.load_local("index", embedding_model, allow_dangerous_deserialization=True)

    docs = db.similarity_search(query, k=k)
    return docs
