from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load saved model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = FastAPI(title="Sentiment Prediction API")

class HeadlineRequest(BaseModel):
    headline: str

@app.get("/")
def home():
    return {"message": "Sentiment Prediction API is running"}

@app.post("/predict")
def predict_sentiment(request: HeadlineRequest):

    text = [request.headline]

    text_tfidf = vectorizer.transform(text)

    prediction = model.predict(text_tfidf)[0]

    return {
        "input_headline": request.headline,
        "predicted_sentiment": prediction
    }