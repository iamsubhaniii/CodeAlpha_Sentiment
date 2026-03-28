from textblob import TextBlob

# Sample reviews
reviews = [
    "This product is amazing",
    "Very bad experience",
    "It is okay, not great",
    "Excellent quality and fast delivery",
    "Worst product ever"
]

for review in reviews:
    analysis = TextBlob(review)
    
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}\n")