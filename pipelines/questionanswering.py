from transformers import pipeline
import json

context1 = """Extractive Question Answering is the task of extracting an answer from a text given a question. An 
example of a question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like 
to fine-tune a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script. """

question1 = """What is extractive question answering?"""

question2 = """What is a good example of a question answering dataset?"""


def getAnswer(question, context):
    nlp = pipeline("question-answering")

    result = nlp(question=question, context=context)

    result['score'] = round(result['score'], 5)

    return json.dumps({'question': question, 'answer': result['answer'], 'score': result['score']})



