from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge base
with open("knowledge_base.json") as f:
    kb = json.load(f)

# Convert KB into text chunks
documents = []

documents.append(f"Basic plan costs {kb['pricing']['basic']['price']} with features {', '.join(kb['pricing']['basic']['features'])}")
documents.append(f"Pro plan costs {kb['pricing']['pro']['price']} with features {', '.join(kb['pricing']['pro']['features'])}")
documents.append(f"Refund policy: {kb['policies']['refund']}")
documents.append(f"Support policy: {kb['policies']['support']}")

# Create embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Retrieval function
def retrieve(query, k=1):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)

    results = [documents[i] for i in indices[0]]
    return "\n".join(results)