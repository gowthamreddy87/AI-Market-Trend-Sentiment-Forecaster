from mongo_db import insert_into_mongo
from data_loader import load_real_dataset
from cleaner import clean_text
import pandas as pd
import uuid
from datetime import datetime

def run_pipeline():
    data = load_real_dataset()

    structured_data = []

    for item in data:
        cleaned = clean_text(item["title"])

        structured_data.append({
            "source": "Kaggle Financial News",
            "original_title": item["title"],
            "cleaned_title": cleaned,
            "sentiment_label": item["sentiment"]
        })

    print("Total records:", len(structured_data))

    import pandas as pd
    return pd.DataFrame(structured_data)

    # Remove duplicates
    df = df.drop_duplicates(subset=["cleaned_title"])

    # Remove empty cleaned titles
    df = df[df["cleaned_title"] != ""]

    return df


if __name__ == "__main__":
    df = run_pipeline()

    df.to_csv("consumer_data.csv", index=False)

    print("Data cleaned and saved successfully.")
    print("Total records:", len(df))
from mongo_db import insert_into_mongo

if __name__ == "__main__":
    df = run_pipeline()

    df.to_csv("consumer_data.csv", index=False)

    data_list = df.to_dict(orient="records")

    insert_into_mongo(data_list)

    print("Pipeline completed successfully.")