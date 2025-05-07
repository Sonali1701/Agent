# RAG-powered Multi-Agent Q&A Assistant

A modular and intelligent Retrieval-Augmented Generation (RAG) system that uses a multi-agent architecture to answer complex queries using uploaded documents.

##  Features

-  Document Ingestion and Chunking
-  Vector Store Retrieval using embeddings
-  Multi-Agent Reasoning with LangChain Agents
-  LLM-powered Q&A (using Groq + Mixtral)
-  Simple Flask-based Web Interface
-  Deployable on Render

---

##  Tech Stack

- **Backend**: Python, Flask
- **LLM**: Mixtral via Groq API
- **Agent Framework**: LangChain
- **Vector Store**: FAISS
- **Frontend**: HTML/CSS (Jinja2 Templates)
- **Deployment**: Render.com

---

## 📂 Project Structure
```bash
├── app.py # Flask application
├── agent.py # Agent orchestration
├── retrieval.py # RAG pipeline logic
├── vectorstore/ # Stores FAISS index
├── templates/
│ └── index.html # UI template
├── requirements.txt
└── README.md                                   
```

---

##  Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set environment variables**
Create a .env file or export the following:
```bash
GROQ_API_KEY=your_groq_api_key
```

4. **Run the application**
```bash
python app.py
```

Access the app
Navigate to http://localhost:10000 in your browser.

## Example Query Flow

Ask a question like:

"what is return policy?"

Agents retrieve, reason, and respond based on document context

## License

This project is licensed under the [MIT License](LICENSE).







