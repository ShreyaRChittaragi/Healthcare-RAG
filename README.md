# 🧠 Medical Research RAG Assistant

A full-stack Retrieval-Augmented Generation (RAG) system that answers medical questions using real research literature.

The system retrieves relevant information from curated medical research papers and clinical guidelines, then generates grounded answers using a large language model.

Instead of relying solely on an LLM (which may hallucinate), this system performs **semantic retrieval from trusted medical sources before generating responses**.

---

# 🚀 Features

* Retrieval-Augmented Generation (RAG) pipeline
* Semantic search over medical research papers
* Answers grounded in retrieved sources
* Source references returned with responses
* Modern full-stack architecture
* Deployable backend and frontend

---

# 🏗️ System Architecture

```text
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
LLM (Groq - Llama 3.3 70B)
        │
        ▼
Answer + Source Citations
```

---

# 📁 Project Structure

```text
medical_rag/
│
├── backend/
│   ├── main.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   └── requirements.txt
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

Note: Large generated files like the FAISS index are not stored in the repository.

---

# 🛠️ Tech Stack

| Layer           | Technology                               |
| --------------- | ---------------------------------------- |
| PDF Processing  | PyMuPDF                                  |
| OCR             | Tesseract + Pytesseract                  |
| Embeddings      | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Database | FAISS                                    |
| LLM             | Groq (Llama-3.3-70B-versatile)           |
| Backend         | FastAPI + Uvicorn                        |
| Frontend        | React + Vite                             |
| Deployment      | Render (backend) + Vercel (frontend)     |

---

# 📊 Dataset Summary

| Item                  | Count |
| --------------------- | ----- |
| Diseases Covered      | 19    |
| Total Research PDFs   | 89    |
| Extracted Text Chunks | 3897  |
| Embedding Dimensions  | 384   |
| FAISS Vectors         | 3897  |

---

# 📚 Dataset Sources

The dataset was manually curated from authoritative medical and public health sources.

### Sources Used

1. **Official Clinical Guidelines**

   * World Health Organization (WHO)
   * Indian Council of Medical Research (ICMR)
   * Ministry of Health & Family Welfare (MoHFW)

2. **Clinical Management Guidelines**

   * National Institute for Health and Care Excellence (NICE)

3. **Research Evidence**

   * Peer-reviewed systematic reviews or meta-analyses
   * Retrieved from PubMed
   * Published after 2018

4. **Public Health and Prevention Guidance**

   * World Health Organization (WHO)
   * Centers for Disease Control and Prevention (CDC)

These documents include clinical guidelines, systematic reviews, and public health advisories.

---

# 📥 Dataset Download

The dataset contains large PDF files and therefore is **not stored directly in this repository**.

Download it here:

DATASET_LINK_HERE   : https://drive.google.com/drive/folders/12hxAU_YbbJgLUem6a_HWwdzZ3nyaHU7K?usp=drive_link

After downloading, place the files in the project directory:

```text
data/
└── medical_papers/
    ├── hypertension/
    ├── tuberculosis/
    ├── malaria/
    └── ...
```

---

# ⚙️ Backend Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/medical_rag.git
cd medical_rag/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac / Linux:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Required Files

Place the following generated files inside the backend directory:

```text
backend/
├── faiss_index.bin
└── chunks_metadata.pkl
```

---

## 5. Add API Key

Create a `.env` file inside the backend folder.

```text
GROQ_API_KEY=your_api_key_here
```

---

## 6. Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

# 💻 Frontend Setup

Open a new terminal.

```bash
cd medical_rag/frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description                   |
| ------ | -------- | ----------------------------- |
| GET    | `/`      | Health check                  |
| POST   | `/chat`  | Send query and receive answer |

Example request:

```json
{
  "query": "What are the symptoms of tuberculosis?"
}
```

Example response:

```json
{
  "answer": "...generated response...",
  "sources": ["document_1.pdf", "document_2.pdf"]
}
```

---

# 🧠 How the RAG System Works

1. User submits a question
2. Question is converted into an embedding
3. FAISS retrieves the most relevant text chunks
4. Retrieved context is injected into the prompt
5. The LLM generates a grounded answer using retrieved knowledge

This approach significantly reduces hallucinations and allows querying large research collections.

---

# ⚠️ Important Notes

The following files are **not included in the repository**:

* faiss_index.bin
* chunks_metadata.pkl
* dataset PDFs

These must be downloaded or generated locally.

---

# 🌐 Deployment

Backend can be deployed on **Render**.

Frontend can be deployed on **Vercel**.

Ensure the backend API URL is updated in the frontend configuration before deployment.

---

# 🔮 Future Improvements

* Hybrid search (BM25 + vector search)
* Re-ranking models
* Streaming responses
* Conversation memory
* Document filtering
* RAG evaluation metrics

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

If you find issues or want to improve the project:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

# 💬 Support

If you need help using or running this project, you can:

* Open an **Issue** in this repository
* Submit feature requests or bug reports
* Reach out through GitHub discussions

---

# 📜 License

This project is licensed under the **Apache License 2.0**.

You are free to use, modify, and distribute the code according to the terms of the license.
