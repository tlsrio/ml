from flask import Flask
from summarization import *

app = Flask(__name__)

@app.route('/api/')
def connected():
    return 'Connected'

@app.route('/api/summarization', methods=['POST'])
def summarize():

    return result