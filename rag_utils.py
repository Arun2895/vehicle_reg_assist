from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")  # Replace with Gemini embedding if needed

def load_and_embed_regulations(jsonl_path):
    with open(jsonl_path, 'r') as f:
        data = [json.loads(line.strip()) for line in f]
    texts = [item["reason"] for item in data]
    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))
    return data, index, embeddings

def retrieve_similar_chunks(query, data, index, k=5):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)
    return [data[i] for i in I[0]]
