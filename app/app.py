from flask import Flask, request, json
import pipelines
from scrapers.scrapeContent import getContent, htmlToText
from scrapers.fetchArticles import fetchArticles

app = Flask(__name__)

@app.route('/api/')
def connected():
    return 'Connected'

@app.route('/api/summarize', methods=['POST'])
def summarize():
    content = request.get_json()
    result = pipelines.getSummary(content['text'])
    return result

@app.route('/api/QA', methods=['POST'])
def questions():
    content = request.get_json()
    result = pipelines.getAnswer(content['question'], content['text'])
    return result

@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    content = request.get_json()
    result = pipelines.getSentiment(content['text'])
    return result

@app.route('/api/NER', methods=['POST'])
def NER():
    content = request.get_json()
    result = pipelines.getNER(content['text'])
    return result

@app.route('/api/classification', methods=['POST'])
def classification():
    content = request.get_json()
    result = pipelines.getCategory(content['text'])
    return result

####################################################
# Scraping Routes

@app.route('/api/urlToText', methods=['POST'])
def getUrlText():
    content = request.get_json()
    html = getContent(content['link'])
    text = htmlToText(html)
    return json.dumps({'text': text})

@app.route('/api/fetchArticles', methods=['POST'])
def articles():
    content = request.get_json()
    result = fetchArticles(content)
    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# for x-www-form-urlencoded POST requests
# TODO: should we be able to take both types of requests and differentiate them?

# @app.route('/api/summarize', methods=['POST'])
# def summarize():
#     result = getSummary(request.form['text'])
#     return result

# @app.route('/api/QA', methods=['POST'])
# def questions():
#     result = getAnswer(request.form['question'], request.form['text'])
#     return result

# @app.route('/api/sentiment', methods=['POST'])
# def sentiment():
#     result = getSentiment(request.form['text'])
#     return result

# @app.route('/api/NER', methods=['POST'])
# def NER():
#     result = getNER(request.form['text'])
#     return result

# @app.route('/api/classification', methods=['POST'])
# def classification():
#     result = getCategory(request.form['text'])
#     return result
