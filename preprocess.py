import re
import emoji
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Lowercase
    text = text.lower()
    
    # Replace emojis with text
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # Replace common emoticons with words
    emoticons = {
        ':)': 'smile',
        ':-)': 'smile',
        ':(': 'sad',
        ':-(': 'sad',
        ';)': 'wink',
        ';-)': 'wink',
    }
    for emo, word in emoticons.items():
        text = text.replace(emo, f" {word} ")

    # Remove non-alphanumeric except spaces
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Tokenize by whitespace
    tokens = text.split()

    # Remove stopwords
    filtered = [word for word in tokens if word not in stop_words]

    return tokens, filtered
