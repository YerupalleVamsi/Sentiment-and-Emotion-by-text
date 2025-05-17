
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np

# Load sentiment model
sentiment_model_name = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)

# Load emotion model
emotion_model_name = "j-hartmann/emotion-english-distilroberta-base"
emotion_tokenizer = AutoTokenizer.from_pretrained(emotion_model_name)
emotion_model = AutoModelForSequenceClassification.from_pretrained(emotion_model_name)

sentiment_labels = ['negative', 'neutral', 'positive']
emotion_labels = ['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']

def predict_sentiment(text):
    inputs = sentiment_tokenizer(text, return_tensors="pt")
    outputs = sentiment_model(**inputs)
    scores = softmax(outputs.logits.detach().numpy()[0])
    return dict(zip(sentiment_labels, scores))

def predict_emotion(text):
    inputs = emotion_tokenizer(text, return_tensors="pt")
    outputs = emotion_model(**inputs)
    scores = softmax(outputs.logits.detach().numpy()[0])
    return dict(zip(emotion_labels, scores))
