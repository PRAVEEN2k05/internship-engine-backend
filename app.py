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
    return {"results": results}
'''

import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recommender import search_jobs

app = FastAPI()

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)