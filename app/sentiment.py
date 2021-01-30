from transformers import pipeline

def getSentiment(text):
    nlp = pipeline("sentiment-analysis")

    result = nlp(text)[0]

    return result
