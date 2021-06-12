from pipelines.summarization import getSummary
from pipelines.classification import getCategory
from .scrapeContent import getContent, htmlToText, getThumbnail
import json

# linkObj - JSON object containing links
#    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}


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


