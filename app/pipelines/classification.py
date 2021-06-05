from transformers import pipeline
import json

ARTICLE = (
    "LONDON (Reuters) - Short-sellers are sitting on estimated losses of $70.87 billion from their short "
    "positions in U.S. companies so far this year, data from financial data analytics firm Ortex showed on "
    "Thursday. The hefty losses come as shares of highly-shorted GameStop jumped more than 1,000% in the past "
    "week without a clear business reason, forcing short-sellers to buy back into the stock to cover potential "
    "losses -- defined as a short-squeeze -- while retail investors then piled in to benefit from the surge. "
    "Chasing shorted companies became a trend among retail traders, rippling across U.S. markets and Europe. "
    "Ortex data showed that as of Wednesday, there were loss-making short positions on more than 5,"
    "000 U.S. firms. Its data also showed that estimated losses from shorting GameStop at $1.03 billion "
    "year-to-date, while those shorting Bed, Bath & Beyond were looking at a $600 million loss. Ortex said the "
    "figures are based on the change in trading prices between the start of January to Wednesday’s close, "
    "and the number of short positions. The company sources short interest data from submissions by agent "
    "lenders, prime brokers, and broker-dealers. "
)

classifier = pipeline("zero-shot-classification")


def getCategory(text):
    # TODO: change categories
    categories = [
        "business",
        "finance",
        "entertainment",
        "family",
        "health",
        "politics",
        "religion",
        "science",
        "sports",
        "technology",
        "travel",
    ]
    res = classifier(text, categories, multi_class=True)
    res = {res["labels"][i]: res["scores"][i] for i in range(len(res["labels"]))}
    res = json.dumps(res)
    return res


# print(getCategory(ARTICLE))
