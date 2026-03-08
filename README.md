# Semantic Search System with Semantic Cache
### Trademarkia AI/ML Engineer Assignment

This project implements a **lightweight semantic search system** using the **20 Newsgroups dataset**.  
It combines **vector embeddings, fuzzy clustering, and a semantic caching layer** exposed through a **FastAPI service**.

The goal is to demonstrate how semantic understanding of queries can improve search performance and reduce redundant computation.

---

# Project Overview

Traditional keyword search systems fail when queries are phrased differently but have the same meaning.

Example:

Query 1:
"space shuttle launch"

Query 2:
"how do rockets launch into space"

Both mean the same thing but keyword search treats them as different.

This project solves that problem using:

- **Sentence embeddings**
- **Vector similarity search**
- **Fuzzy clustering**
- **Semantic cache**

---

# System Architecture

```

User Query
↓
Sentence Transformer Embedding
↓
Semantic Cache Lookup
↓
(Cache Hit → Return Cached Result)

(Cache Miss → FAISS Vector Search)
↓
Retrieve Relevant Documents
↓
Store Result in Cache
↓
Return Response via FastAPI

```

---

# Dataset

Dataset used:

**20 Newsgroups Dataset**

https://archive.ics.uci.edu/dataset/113/twenty+newsgroups

Characteristics:

- ~20,000 documents
- 20 topic categories
- Noisy text data
- Overlapping semantic themes

This makes it suitable for **semantic clustering and search experiments**.

---

# Technologies Used

| Component | Technology |
|--------|--------|
API Framework | FastAPI |
Embedding Model | Sentence Transformers (all-MiniLM-L6-v2) |
Vector Database | FAISS |
Clustering | Fuzzy C-Means |
Language | Python |
Deployment | Docker |
Frontend (Testing) | Swagger UI |

---

# Part 1 – Embedding & Vector Database

Documents are converted into **dense vector embeddings** using:

```

sentence-transformers/all-MiniLM-L6-v2

```

Why this model?

- Lightweight
- Fast inference
- Strong semantic performance

Embeddings are stored in a **FAISS index** for efficient similarity search.

Saved artifacts:

```

data/
embeddings.npy
clusters.npy
documents.pkl
faiss.index

```

These files allow the API to **load instantly without recomputing embeddings**.

---

# Part 2 – Fuzzy Clustering

Instead of assigning documents to a **single cluster**, fuzzy clustering assigns **probability distributions**.

Example:

```

Document: "Gun laws and political policy"

Cluster Membership:

Politics → 0.65
Firearms → 0.35

```

This better reflects the **true semantic overlap of topics**.

Clustering benefits:

- Helps identify **semantic structure**
- Improves **cache lookup efficiency**
- Allows analysis of **boundary cases**

---

# Part 3 – Semantic Cache

Traditional caches rely on **exact string matching**.

Example:

```

Query A:
"space shuttle launch"

Query B:
"rocket launch to space"

```

These are semantically similar but textually different.

Our **semantic cache** works as follows:

1. Convert query to embedding
2. Compare with cached query embeddings
3. If similarity > threshold → cache hit

Similarity metric:

```

Cosine Similarity

```

Configurable threshold:

```

similarity_threshold = 0.85

```

Cache structure stores:

```

query
embedding
result
cluster id

````

---

# Part 4 – FastAPI Service

The system exposes three endpoints.

---

## POST /query

Accepts a natural language query.

Example request:

```json
{
 "query": "space shuttle launch"
}
````

Example response:

```json
{
 "query": "space shuttle launch",
 "cache_hit": true,
 "matched_query": "space shuttle launch",
 "similarity_score": 1.0,
 "result": "...documents...",
 "dominant_cluster": 3
}
```

---

## GET /cache/stats

Returns cache statistics.

Example response:

```json
{
 "total_entries": 5,
 "hit_count": 3,
 "miss_count": 2,
 "hit_rate": 0.6
}
```

---

## DELETE /cache

Clears the semantic cache.

---

# Running the Project

## 1. Clone Repository

```

git clone https://github.com/KpradeepKumar25/semantic-search-cache.git
cd semantic-search-cache

```

---

## 2. Install Dependencies

```

pip install -r requirements.txt

```

---

## 3. Run FastAPI Server

```

uvicorn api.main:app --reload

```

---

## 4. Open API Documentation

```

http://127.0.0.1:8000/docs

```

---

# Docker Deployment (Bonus)

Build container:

```

docker build -t semantic-search .

```

Run container:

```

docker run -p 8000:8000 semantic-search

```

Access API:

```

http://localhost:8000/docs

```

---

# Project Structure

```

semantic-search-cache
│
├ api
│ └ main.py
│
├ cache
│ └ semantic_cache.py
│
├ vector_db
│ └ vector_search.py
│
├ embeddings
│
├ ui
│
├ data
│ ├ embeddings.npy
│ ├ clusters.npy
│ ├ documents.pkl
│ └ faiss.index
│
├ Dockerfile
├ requirements.txt
└ README.md

```

---

# Document With screenshot


https://docs.google.com/document/d/15jmfPY773QMkFmf-EflDsb2tAzbxM6vWMEGLmKnzymQ/edit?usp=sharing



# Example Workflow

First query:

```

"space shuttle launch"

```

Response:

```

cache_hit = false

```

Second query:

```

"space shuttle launch"

```

Response:

```

cache_hit = true

```

This demonstrates **semantic caching functionality**.

---

# Key Features

* Semantic vector search
* Fuzzy clustering
* Custom semantic cache implementation
* FastAPI microservice
* FAISS vector database
* Docker container support

---

# Future Improvements

Possible enhancements include:

* Cluster-aware cache indexing
* Redis distributed cache
* Query expansion techniques
* Approximate nearest neighbor optimizations

---

# Author

**Pradeep Kumar(23BLC1240)**

AI/ML Engineering Project
Trademarkia Internship Assignment

```


