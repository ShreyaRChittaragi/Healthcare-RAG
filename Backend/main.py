from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from rag_pipeline import ask

app = FastAPI()

# Allow React frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    query: str
    chat_history: Optional[List[dict]] = []
    top_k: Optional[int] = 5

# Response model
class Source(BaseModel):
    source_num: int
    disease: str
    filename: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]

@app.get("/")
def root():
    return {"status": "Medical RAG API is running!"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer, sources = ask(
        query=request.query,
        chat_history=request.chat_history,
        top_k=request.top_k
    )
    return ChatResponse(answer=answer, sources=sources)