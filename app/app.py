from flask import Flask, request
from pipelines.summarization import getSummary
from pipelines.questionanswering import getAnswer
from pipelines.sentiment import getSentiment
from pipelines.ner import getNER
from pipelines.classification import getCategory

app = Flask(__name__)

@app.route('/api/')
def connected():
    return 'Connected'

@app.route('/api/summarize', methods=['POST'])
def summarize():
    result = getSummary(request.form['text'])
    return result

@app.route('/api/QA', methods=['POST'])
def questions():
    result = getAnswer(request.form['question'], request.form['text'])
    return result

@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    result = getSentiment(request.form['text'])
    return result

@app.route('/api/NER', methods=['POST'])
def NER():
    result = getNER(request.form['text'])
    return result

@app.route('/api/classification', methods=['POST'])
def classification():
    result = getCategory(request.form['text'])
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')