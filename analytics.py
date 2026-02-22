import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient
import sys


def generate_sentiment_dashboard():
    try:
        # -----------------------------
        # MongoDB Connection
        # -----------------------------
        client = MongoClient("mongodb://localhost:27017/")
        db = client["market_trend_db"]
        collection = db["consumer_data"]

        # -----------------------------
        # Fetch Data
        # -----------------------------
        data = list(collection.find({}, {"_id": 0}))

        if not data:
            print("No data found in MongoDB collection.")
            sys.exit()

        df = pd.DataFrame(data)

        if "sentiment_label" not in df.columns:
            print("Column 'sentiment_label' not found in dataset.")
            sys.exit()

        print("\nTotal records:", len(df))

        # -----------------------------
        # Sentiment Distribution
        # -----------------------------
        sentiment_counts = df["sentiment_label"].value_counts()

        print("\nSentiment Distribution:")
        print(sentiment_counts)

        # -----------------------------
        # BAR CHART
        # -----------------------------
        plt.figure(figsize=(8, 5))
        sentiment_counts.plot(kind="bar")
        plt.title("Sentiment Distribution")
        plt.xlabel("Sentiment")
        plt.ylabel("Count")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("sentiment_bar_chart.png")
        plt.close()

        # -----------------------------
        # PIE CHART
        # -----------------------------
        plt.figure(figsize=(6, 6))
        sentiment_counts.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Sentiment Percentage Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig("sentiment_pie_chart.png")
        plt.close()

        print("\nDashboard generated successfully.")

    except Exception as e:
        print("Error occurred:", e)


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    generate_sentiment_dashboard()