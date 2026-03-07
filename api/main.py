from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from embeddings.embedder import embed_query
from cache.semantic_cache import SemanticCache
from vector_db.vector_search import search_documents

app = FastAPI()

cache = SemanticCache()

class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_api(request: QueryRequest):

    query = request.query

    query_embedding = embed_query(query)

    hit, entry, similarity = cache.search(query_embedding)

    if hit:

        return {
            "query": query,
            "cache_hit": True,
            "matched_query": entry["query"],
            "similarity_score": float(similarity),
            "result": entry["result"],
            "dominant_cluster": entry["cluster"]
        }

    results = search_documents(query_embedding)

    cluster = int(np.random.randint(0,10))

    cache.add(query, query_embedding, results, cluster)

    return {
        "query": query,
        "cache_hit": False,
        "matched_query": None,
        "similarity_score": 0,
        "result": results,
        "dominant_cluster": cluster
    }


@app.get("/cache/stats")
def cache_stats():
    return cache.stats()


@app.delete("/cache")
def clear_cache():

    cache.clear()

    return {"message": "cache cleared"}