from textblob import TextBlob
# from textblob_fr import PatternTagger, PatternAnalyzer
import nltk
import spacy
import string
from textblob import TextBlob
from transformers import pipeline
emotion_classifier = pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')


# Initialize the emotion detection pipeline


# Function to analyze text
def analyze_sentiment(sentence):
    # Sentiment Analysis
    blob = TextBlob(sentence)
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity
    
    # Emotion Detection
    emotions = emotion_classifier(sentence)

    # Extract top emotion
    top_emotion = max(emotions, key=lambda x: x['score'])
    
    return {
        'polarity': polarity,
        'subjectivity': subjectivity,
        'top_emotion': top_emotion['label'],
        'emotion_score': top_emotion['score']
    }

