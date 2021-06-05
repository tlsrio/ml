from pipelines.summarization import getSummary
from pipelines.classification import getCategory
from .scrapeContent import getContent, htmlToText, getThumbnail
import json

# linkObj - JSON object containing links
#    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}

l = {
    "CBC": [
        "https://www.cbc.ca/news/world/coronavirus-covid19-canada-world-may16-2021-1.6028706",
        "https://www.cbc.ca/news/canada/ottawa/rallies-rally-ottawa-palestinian-israeli-conflict-escalating-violence-middle-east-1.6029028",
    ],
    "CNN": [
        "https://www.cnn.com/2021/05/08/business/supply-chain-shortages-pandemic/index.html",
        "https://www.cnn.com/2021/05/16/media/sanjay-gupta-cdc-mask-messaging/index.html",
    ],
    "NBC": [
        "https://www.nbcnews.com/news/world/diplomatic-efforts-ceasefire-ramp-after-strikes-claim-more-lives-israel-n1267519"
    ],
}


def fetchArticles(linkObj):
    data = []

    for source in linkObj.keys():
        for link in linkObj[source]:
            try:
                article = {}

                html = getContent(link)
                text = htmlToText(html)

                title = html.find("title").text
                article["title"] = title

                summary = json.loads(getSummary(text))
                article["summary"] = summary["summary"]
                article["reduced_by"] = summary["reducedBy"]
                article["link"] = link

                article["source"] = source

                article["image"] = getThumbnail(html)

                categories = json.loads(getCategory(text))
                catList = []
                for keyword in categories.keys():
                    if categories[keyword] >= 0.2:
                        catList.append(keyword)
                article["category"] = catList

                data.append(article)
                # print(article)

            except Exception as e:
                print(e)
                continue

    return json.dumps(data)


# d = fetchArticles(l)
# print(d)
