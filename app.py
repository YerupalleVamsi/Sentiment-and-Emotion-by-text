import streamlit as st
from preprocess import preprocess_text
from model import predict_sentiment, predict_emotion
import nltk
nltk.download('stopwords')


st.title("Sentiment & Emotion Detection")

text_input = st.text_area("Enter your text here:")

if st.button("Analyze"):
    if not text_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        # Predict sentiment
        sentiment_scores = predict_sentiment(text_input)
        st.write("### Sentiment Scores:")
        st.bar_chart(sentiment_scores)

        # Predict emotion
        emotion_scores = predict_emotion(text_input)
        st.write("### Emotion Scores:")
        st.bar_chart(emotion_scores)

