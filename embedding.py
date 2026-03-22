'''import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def generate_embeddings():
    print("🚀 Loading model...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # ✅ FIX: absolute paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned.pkl")
    FAISS_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")
    EMBEDDINGS_PATH = os.path.join(BASE_DIR, "data", "embeddings.npy")

    print("📂 Loading data...")
    df = pickle.load(open(DATA_PATH, "rb"))

    # 🔥 Use limited dataset (important for Render memory)
    df = df.sample(n=3000, random_state=42)

    print(f"Using {len(df)} rows")

    print("🧠 Generating embeddings...")
    embeddings = model.encode(
        df["combined"].tolist(),
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    print("⚡ Creating FAISS index...")

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    print("💾 Saving FAISS index...")
    faiss.write_index(index, FAISS_PATH)

    print("💾 Saving processed dataframe...")
    df.to_pickle(DATA_PATH)

    print("💾 Saving embeddings...")
    np.save(EMBEDDINGS_PATH, embeddings)

    print("✅ DONE EVERYTHING 🚀")

if __name__ == "__main__":
    generate_embeddings()
    '''
import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def generate_embeddings():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned_small.pkl")
    FAISS_PATH = os.path.join(BASE_DIR, "data", "faiss_index.index")

    print("🚀 Loading model...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    print("📂 Loading data...")
    df = pickle.load(open(DATA_PATH, "rb"))

    print("🧠 Generating embeddings...")
    embeddings = model.encode(
        df["combined"].tolist(),
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    print("⚡ Creating FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    print("💾 Saving FAISS index...")
    faiss.write_index(index, FAISS_PATH)
    print("✅ Done!")


if __name__ == "__main__":
    generate_embeddings()