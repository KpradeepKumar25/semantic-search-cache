import faiss
import numpy as np
import pickle

# Load FAISS index
index = faiss.read_index("data/faiss.index")

# Load documents
with open("data/documents.pkl", "rb") as f:
    documents = pickle.load(f)

# Load cluster memberships
clusters = np.load("data/clusters.npy")

def search_documents(query_embedding, top_k=5):

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(documents[idx])

    return results