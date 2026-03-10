import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load everything ONCE when the server starts
print("Loading FAISS index...")
index = faiss.read_index('faiss_index.bin')

print("Loading chunk metadata...")
with open('chunks_metadata.pkl', 'rb') as f:
    all_chunks = pickle.load(f)

print("Loading embedding model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print(f"✅ Index loaded with {index.ntotal} vectors")
print(f"✅ Metadata loaded with {len(all_chunks)} chunks")


def retrieve(query, top_k=5):
    query_embedding = model.encode([query]).astype('float32')
    distances, indices = index.search(query_embedding, k=top_k)
    
    results = []
    for i, idx in enumerate(indices[0]):
        chunk = all_chunks[idx]
        results.append({
            'rank': i + 1,
            'disease': chunk['disease'],
            'category': chunk['category'],
            'filename': chunk['filename'],
            'text': chunk['text'],
            'distance': distances[0][i]
        })
    return results