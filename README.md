
# 🧠 Sentiment and Emotion Detection App

This Streamlit app predicts **sentiment** (positive, neutral, negative) and **emotion** (happy, sad, angry, etc.) from user input using NLP models.

---

## Features

- Text preprocessing with emoji and emoticon handling
- Sentiment analysis with [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- Emotion detection with [j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)
- Interactive Streamlit interface with probability bar charts for sentiment and emotions

---
## 🚀 Live App

👉 [Click here to view live App](https://sentiment-and-emotion-by-text-huvvuev4eloijsqtrxrceh.streamlit.app/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>

2. (Optional) Create and activate a virtual environment:

    
       python3 -m venv venv
       source venv/bin/activate    # Linux/macOS
       venv\Scripts\activate       # Windows

3. Install dependencies:

       pip install -r requirements.txt
    
4. Download required NLTK data:
    
       import nltk
       nltk.download('stopwords')
