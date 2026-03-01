import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.set_page_config(page_title="AI Market Sentiment Analyzer", layout="centered")

st.title("📊 AI Market Trend & Sentiment Analyzer")
st.markdown("### Powered by Machine Learning (Logistic Regression + TF-IDF)")

st.write("Model Accuracy: **73%**")
st.write("Dataset Size: **4,800+ Financial Headlines**")

st.divider()

headline = st.text_area("Enter Financial News Headline")

col1, col2 = st.columns(2)

with col1:
    if st.button("📈 Example Positive"):
        headline = "Company reports strong quarterly profits and revenue growth"
        st.session_state["headline"] = headline

with col2:
    if st.button("📉 Example Negative"):
        headline = "Market crashes due to global recession fears"
        st.session_state["headline"] = headline

if st.button("Predict Sentiment"):

    if headline.strip() == "":
        st.warning("Please enter a headline.")
    else:
        text_tfidf = vectorizer.transform([headline])
        prediction = model.predict(text_tfidf)[0]
        probabilities = model.predict_proba(text_tfidf)[0]
        confidence = np.max(probabilities) * 100

        st.subheader("Prediction Result")

        if prediction == "positive":
            st.success(f"Predicted Sentiment: {prediction.upper()} 📈")
        elif prediction == "negative":
            st.error(f"Predicted Sentiment: {prediction.upper()} 📉")
        else:
            st.info(f"Predicted Sentiment: {prediction.upper()} ⚖️")

        st.write(f"Confidence Score: **{confidence:.2f}%**")

st.divider()
st.caption("AI Market Trend & Consumer Sentiment Forecaster | Milestone 2 Demo")