from transformers import pipeline

def pipelineQA(question, context):
    nlp = pipeline("question-answering")

    result = nlp(question=question, context=context)

    del result['start']
    del result['end']

    result['question'] = question
    result['score'] = round(result['score'], 5)

    return result