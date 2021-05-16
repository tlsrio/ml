from transformers import pipeline
import json

def getSentiment(text):
    nlp = pipeline("sentiment-analysis")

    result = nlp(text.strip('"'))[0]

    return json.dumps({'label': result['label'], 'score': round(result['score'], 4)})
