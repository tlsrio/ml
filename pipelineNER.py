from transformers import pipeline

def pipelineNER(sequence):
    nlp = pipeline("ner")

    result = nlp(sequence)

    return result

sequence = "Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very " \
           "close to the Manhattan Bridge which is visible from the window."

print(pipelineNER(sequence))