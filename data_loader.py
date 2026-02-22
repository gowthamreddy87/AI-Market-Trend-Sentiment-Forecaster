import pandas as pd

def load_real_dataset():
    df = pd.read_csv("data/all-data.csv", encoding="latin1", header=None)
    
    # Assign proper column names
    df.columns = ["sentiment", "title"]

    print("Dataset shape:", df.shape)

    data = []

    for _, row in df.iterrows():
        data.append({
            "title": row["title"],
            "sentiment": row["sentiment"]
        })

    return data