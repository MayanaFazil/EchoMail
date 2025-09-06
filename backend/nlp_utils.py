from transformers import pipeline
import re

# Load sentiment analysis pipeline (uses DistilBERT by default)
sentiment_analyzer = pipeline("sentiment-analysis")

# Priority keywords
PRIORITY_KEYWORDS = ["immediately", "urgent", "critical", "asap", "cannot access", "important"]

def analyze_sentiment(text):
    result = sentiment_analyzer(text[:512])[0]  # Limit to 512 chars for speed
    label = result['label']
    if label == "POSITIVE":
        return "Positive"
    elif label == "NEGATIVE":
        return "Negative"
    else:
        return "Neutral"

def detect_priority(text):
    text_lower = text.lower()
    for kw in PRIORITY_KEYWORDS:
        if kw in text_lower:
            return "Urgent"
    return "Not urgent"

def extract_contact_details(text):
    # Simple regex for phone and email
    phone = re.findall(r'\b\d{10,}\b', text)
    email_matches = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return {
        "phone": phone,
        "alternate_email": email_matches
    }

def extract_customer_requirements(text):
    # Simple extraction: return sentences with "need", "require", "want", "issue"
    requirements = []
    for sentence in re.split(r'(?<=[.!?])\s+', text):
        if any(word in sentence.lower() for word in ["need", "require", "want", "issue", "problem", "request"]):
            requirements.append(sentence)
    return requirements

def extract_sentiment_indicators(text):
    # Return positive/negative words found
    positive_words = ["thank", "appreciate", "great", "happy", "satisfied"]
    negative_words = ["frustrated", "angry", "disappointed", "problem", "issue", "bad", "cannot"]
    found_positive = [w for w in positive_words if w in text.lower()]
    found_negative = [w for w in negative_words if w in text.lower()]
    return {
        "positive_words": found_positive,
        "negative_words": found_negative
    }

def process_email_content(text: str):
    return {
        "sentiment": analyze_sentiment(text),
        "priority": detect_priority(text),
        "contact_details": extract_contact_details(text),
        "customer_requirements": extract_customer_requirements(text),
        "sentiment_indicators": extract_sentiment_indicators(text)
    }