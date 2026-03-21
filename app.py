'''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommender import search_jobs

app = FastAPI()

# ✅ CORS (for now keep *, later restrict)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# ✅ FIX: default query to avoid crash
@app.get("/search")
def search(query: str = ""):
    if not query.strip():
        return {"results": []}

    results = search_jobs(query)
    return {"results": results}'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommender import search_jobs
import os
import uvicorn

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}


@app.get("/search")
def search(query: str = ""):
    if not query.strip():
        return {"results": []}

    return {"results": search_jobs(query)}


# 🔥 IMPORTANT: This ensures Render detects the port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"🚀 Starting server on port {port}")
    uvicorn.run("app:app", host="0.0.0.0", port=port)