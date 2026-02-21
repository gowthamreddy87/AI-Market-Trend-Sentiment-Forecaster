from mongo_db import insert_into_mongo
from news_api import fetch_news
from cleaner import clean_text
import pandas as pd
import uuid
from datetime import datetime

def run_pipeline():
    raw_data = fetch_news()

    structured_data = []

    for item in raw_data:
        if not item["title"]:
            continue

        cleaned = clean_text(item["title"])

        structured_data.append({
            "id": str(uuid.uuid4()),
            "source": item["source"],
            "original_title": item["title"],
            "cleaned_title": cleaned,
            "date": item["date"],
            "ingested_at": datetime.now()
        })

    df = pd.DataFrame(structured_data)

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