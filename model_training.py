import pandas as pd
from pymongo import MongoClient
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib


def train_sentiment_model():

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["market_trend_db"]
    collection = db["consumer_data"]

    # Fetch data
    data = list(collection.find({}, {"_id": 0}))
    df = pd.DataFrame(data)

    print("Total records (raw):", len(df))

    # Clean dataset
    df = df.dropna(subset=["cleaned_title", "sentiment_label"])
    df = df[df["cleaned_title"].str.strip() != ""]

    print("Total records (after cleaning):", len(df))

    # Features and Labels
    X = df["cleaned_title"]
    y = df["sentiment_label"]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Logistic Regression Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    # Predictions
    y_pred = model.predict(X_test_tfidf)

    # Evaluation
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Save model and vectorizer
    joblib.dump(model, "sentiment_model.pkl")
    joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

    print("\nModel saved successfully.")


if __name__ == "__main__":
    train_sentiment_model()