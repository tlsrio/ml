from transformers import pipeline
import string
import re
import json

ARTICLE = "LONDON (Reuters) - Short-sellers are sitting on estimated losses of $70.87 billion from their short " \
          "positions in U.S. companies so far this year, data from financial data analytics firm Ortex showed on " \
          "Thursday. The hefty losses come as shares of highly-shorted GameStop jumped more than 1,000% in the past " \
          "week without a clear business reason, forcing short-sellers to buy back into the stock to cover potential " \
          "losses -- defined as a short-squeeze -- while retail investors then piled in to benefit from the surge. " \
          "Chasing shorted companies became a trend among retail traders, rippling across U.S. markets and Europe. " \
          "Ortex data showed that as of Wednesday, there were loss-making short positions on more than 5," \
          "000 U.S. firms. Its data also showed that estimated losses from shorting GameStop at $1.03 billion " \
          "year-to-date, while those shorting Bed, Bath & Beyond were looking at a $600 million loss. Ortex said the " \
          "figures are based on the change in trading prices between the start of January to Wednesday’s close, " \
          "and the number of short positions. The company sources short interest data from submissions by agent " \
          "lenders, prime brokers, and broker-dealers. "

summarizer = pipeline("summarization")

def _countwords(text):
    num_words = sum([i.strip(string.punctuation).isalpha() for i in text.split()])
    return num_words

def _formattext(text):
    # fix period spacing and adds capitalization after punctuation
    text = text.replace(" .", ".")
    punctuation_expression = re.compile('([.!?;]\s*)')
    split_punctuation = punctuation_expression.split(text)
    for i, j in enumerate(split_punctuation):
        if len(j) > 1:
            split_punctuation[i] = j[0].upper() + j[1:]
    text = ''.join(split_punctuation)
    return text

def getSummary(text):

    summary = summarizer(text, max_length=200, min_length=20)[0]['summary_text']
    summary = _formattext(summary)

    text_length = _countwords(text);
    summary_length = _countwords(summary);

    # maybe leave this as a percentage
    reduced_by = "Original text reduced by " + str(round((text_length - summary_length) / text_length * 100)) + "%. "
    # reduced_by = round((text_length - summary_length) / text_length * 100);

    return json.dumps({'summary': summary, 'reducedBy': reduced_by});

