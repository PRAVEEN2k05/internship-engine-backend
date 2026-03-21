'''import os
import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess():
    # ✅ FIX: absolute paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_PATH = os.path.join(BASE_DIR, "data", "internships.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned.pkl")

    df = pd.read_csv(INPUT_PATH).fillna("")

    df["combined"] = (
        df["title"].apply(clean_text) + " " +
        df["description"].apply(clean_text) + " " +
        df["skills_desc"].apply(clean_text)
    )

    df.to_pickle(OUTPUT_PATH)
    print("✅ Preprocessing done")

if __name__ == "__main__":
    preprocess()
    '''

import os
import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    INPUT_PATH = os.path.join(BASE_DIR, "data", "internships.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "data", "internships_cleaned_small.pkl")

    df = pd.read_csv(INPUT_PATH).fillna("")

    df["combined"] = (
        df["title"].apply(clean_text) + " " +
        df["description"].apply(clean_text) + " " +
        df["skills_desc"].apply(clean_text)
    )

    df = df.sample(n=1000, random_state=42)

    df.to_pickle(OUTPUT_PATH)
    print("✅ Preprocessing done")

if __name__ == "__main__":
    preprocess()