import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
import os

def generate_sentiment_dashboard():

    client = MongoClient("mongodb://localhost:27017/")
    db = client["market_trend_db"]
    collection = db["consumer_data"]

    data = list(collection.find({}, {"_id": 0}))

    if not data:
        print("No data found in MongoDB.")
        return

    df = pd.DataFrame(data)

    print("\nTotal records:", len(df))

    sentiment_counts = df["sentiment_label"].value_counts()

    print("\nSentiment Distribution:")
    print(sentiment_counts)

    # ---- BAR CHART ----
    plt.figure(figsize=(8,5))
    sentiment_counts.plot(kind="bar")
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), "sentiment_bar_chart.png"))
    plt.close()

    # ---- PIE CHART ----
    plt.figure(figsize=(6,6))
    sentiment_counts.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sentiment Percentage Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), "sentiment_pie_chart.png"))
    plt.close()

    print("\nDashboard images saved in project folder.")

if __name__ == "__main__":
    generate_sentiment_dashboard()