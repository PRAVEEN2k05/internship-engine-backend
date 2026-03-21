'''import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import re

# ✅ Paths fix
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned.pkl")
FAISS_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")

# 🚀 Load model ONCE
print("🚀 Loading model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 📂 Load data
print("📂 Loading data...")
df = pickle.load(open(DATA_PATH, "rb"))

# ⚡ Load FAISS index
print("⚡ Loading FAISS index...")
index = faiss.read_index(FAISS_PATH)


# 🔥 Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


# 🔥 Search function
def search_jobs(query, top_k=10):
    query = clean_text(query)

    # ✅ IMPORTANT: normalize embeddings
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # 🔍 Search
    distances, indices = index.search(query_embedding, top_k)

    # 📊 Get results
    results = df.iloc[indices[0]]

    return results[["title", "company_name", "location"]].to_dict(orient="records")
    '''

import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned_small.pkl")
FAISS_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")

print("📂 Loading dataset...")

# ✅ SAFE LOAD DATA
if os.path.exists(DATA_PATH):
    df = pickle.load(open(DATA_PATH, "rb"))
else:
    print("❌ Dataset missing")
    df = None

# ✅ SAFE LOAD FAISS
if os.path.exists(FAISS_PATH):
    print("⚡ Loading FAISS index...")
    index = faiss.read_index(FAISS_PATH)
else:
    print("⚠️ FAISS not found → fallback mode")
    index = None

# 🔥 LAZY MODEL
model = None


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def search_jobs(query, top_k=10):
    global model

    if df is None:
        return []

    query = clean_text(query)

    # Load model only when needed
    if model is None:
        print("🚀 Loading model...")
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Fallback if FAISS missing
    if index is None:
        return df.head(10)[["title", "company_name", "location"]].to_dict(orient="records")

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    distances, indices = index.search(query_embedding, top_k)

    results = df.iloc[indices[0]]

    return results[["title", "company_name", "location"]].to_dict(orient="records")