# 🧠 Medical Research RAG Chatbot

A Retrieval-Augmented Generation (RAG) system that answers medical questions using information extracted from real medical research papers. The system retrieves relevant document chunks using semantic search and generates grounded answers using a Large Language Model.

---

# 🚀 Overview

This project builds a full-stack AI system capable of answering questions from medical research literature.

Instead of relying purely on an LLM (which may hallucinate), this system retrieves relevant knowledge from indexed research papers and feeds that context to the LLM before generating an answer.

The result is **more reliable, source-grounded responses**.

---

# 🏗️ System Architecture

```
Medical Research PDFs
        │
        ▼
PDF Text Extraction (PyMuPDF + OCR)
        │
        ▼
Text Chunking
        │
        ▼
Embeddings (Sentence Transformers)
        │
        ▼
Vector Database (FAISS)
        │
        ▼
Retriever
        │
        ▼
LLM (Groq Llama-3.3-70B)
        │
        ▼
Generated Answer + Source References
```

---

# 📁 Project Structure

```
medical_rag/
│
├── backend/
│   ├── main.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   ├── requirements.txt
│   └── (faiss_index.bin and chunks_metadata.pkl stored locally)
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       └── components/
│           ├── ChatWindow.jsx
│           └── Sidebar.jsx
│
├── README.md
└── .gitignore
```

---

# 🛠️ Tech Stack

| Layer           | Technology              |
| --------------- | ----------------------- |
| PDF Processing  | PyMuPDF                 |
| OCR             | Tesseract + Pytesseract |
| Embeddings      | sentence-transformers   |
| Vector Database | FAISS                   |
| LLM             | Groq (Llama-3.3-70B)    |
| Backend API     | FastAPI                 |
| Frontend        | React + Vite            |
| Deployment      | Render + Vercel         |

---

# 📊 Dataset Summary

| Item                 | Count |
| -------------------- | ----- |
| Diseases             | 19    |
| Medical PDFs         | 89    |
| Text Chunks          | 3897  |
| Embedding Dimensions | 384   |
| FAISS Vectors        | 3897  |

The dataset contains medical research documents sourced from publicly available research papers and health organization publications.

---

# ⚙️ Backend Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/medical_rag.git
cd medical_rag/backend
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment:

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add required files

Place the following files inside the `backend/` folder:

```
faiss_index.bin
chunks_metadata.pkl
```

These files contain the precomputed vector database and metadata.

---

### 5️⃣ Add Groq API key

Create a `.env` file inside the backend directory.

```
GROQ_API_KEY=your_api_key_here
```

---

### 6️⃣ Run backend server

```
uvicorn main:app --reload
```

Backend will run at:

```
http://localhost:8000
```

---

# 💻 Frontend Setup

Open a new terminal.

```
cd medical_rag/frontend
```

### Install dependencies

```
npm install
```

### Run development server

```
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description          |
| ------ | -------- | -------------------- |
| GET    | /        | Health check         |
| POST   | /chat    | Query the RAG system |

### Example Request

```
POST /chat
{
  "query": "What are the symptoms of tuberculosis?"
}
```

### Example Response

```
{
  "answer": "...generated response...",
  "sources": ["document_1.pdf", "document_2.pdf"]
}
```

---

# 🧠 How RAG Works

1. User submits a question
2. Question is converted into an embedding
3. FAISS retrieves the most relevant text chunks
4. Retrieved chunks are inserted into the LLM prompt
5. LLM generates an answer grounded in retrieved context

This approach reduces hallucinations and enables question answering over large document collections.

---

# ⚠️ Important Notes

The following files are **not uploaded to GitHub**:

```
faiss_index.bin
chunks_metadata.pkl
```

These files contain the FAISS vector index and metadata and should be stored locally or on the deployment server.

---

# 🌐 Deployment

Backend can be deployed using **Render**.

Frontend can be deployed using **Vercel**.

Ensure the backend API URL is updated inside the frontend configuration before deployment.

---

# 📌 Future Improvements

* Hybrid search (BM25 + vector search)
* Re-ranking models
* Streaming responses
* Conversation memory
* Advanced document filtering
* Evaluation metrics for RAG performance

---

# 📜 License

This project is intended for educational and research purposes.
