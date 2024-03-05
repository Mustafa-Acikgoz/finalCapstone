
# Sentiment Analysis using spaCy

## Project Description
This project implements a sentiment analysis model using spaCy.

## Installation
To install the necessary dependencies, use pip:
```bash
pip install spacy pandas
```

## Usage
### Preprocess the Text Data:
```python
reviews_data = df['reviews.text']
reviews_data = reviews_data.dropna()

def preprocess_text(text):
    processed_text = []
    doc = nlp(text)
    for token in doc:
        if not token.is_stop and token.is_alpha:
            processed_text.append(token.text.lower()) 
    return ' '.join(processed_text)

clean_data = reviews_data.apply(preprocess_text)
```

### Analyze Sentiment:
```python
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
```

### Test the Sentiment Analysis Function:
```python
sample_data = clean_data.iloc[1234]   
print("Sample data:", sample_data)
sentiment_score = analyze_sentiment(sample_data)
print("Sentiment score:", sentiment_score)
```

## Credits
- **Author:** Mustafa Acikgoz
```




 

 
 
 
 
 
