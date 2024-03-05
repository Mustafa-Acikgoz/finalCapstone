import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load("en_core_web_md")
df = pd.read_csv("Amazon_Review.csv")
spacy_text_blob = SpacyTextBlob(nlp)
nlp.add_pipe('spacytextblob')
df.head()
reviews_data = df['reviews.text']
reviews_data = reviews_data.dropna()
reviews_data.head()
def preprocess_text(text):
    processed_text = []
    doc = nlp(text)
    for token in doc:
        if not token.is_stop and token.is_alpha:
            processed_text.append(token.text.lower()) 
    return ' '.join(processed_text)
clean_data = reviews_data.apply(preprocess_text)
clean_data.head()
def analyze_sentiment(review):
    doc = nlp(review)
    polarity = doc._.polarity
    if polarity > 0:
            return "positive"
    elif polarity < 0:
            return "negative"
    else:
            return "neutral"
sentiment_scores = clean_data.apply(analyze_sentiment)
sample_data = clean_data.iloc[1234]   
print("Sample data:", sample_data)
sentiment_score = analyze_sentiment(sample_data)
print("Sentiment score:", sentiment_score)