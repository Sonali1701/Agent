import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document


# Function to load all text documents from the 'data/' folder
def load_documents_from_folder(folder_path="data/"):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                text = file.read()
                # Wrap each text file into a Document object
                documents.append(Document(page_content=text, metadata={"source": filename}))
    return documents


# Function to create and save the FAISS index
def create_faiss_index(documents):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Optional: Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunked_docs = text_splitter.split_documents(documents)

    # Create a FAISS index from the chunked documents
    faiss_index = FAISS.from_documents(chunked_docs, embeddings)

    # Save the index to the 'index' folder
    faiss_index.save_local("index")
    print("FAISS index has been saved to 'index' folder")


# Load documents from the 'data/' folder
documents = load_documents_from_folder()

# Create the FAISS index
create_faiss_index(documents)
