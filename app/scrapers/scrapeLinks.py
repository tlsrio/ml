import newspaper
import json
from data.newsSites import newsSites

# linkObj - JSON object containing links
#    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}


def buildLinkObj():

    linkObj = {}

    for site in newsSites.keys():
        print(site);
        print(newsSites[site])
        paper = newspaper.build(newsSites[site])
        print(paper.size())

        links = []

        for article in paper.articles:
            print(article.url)
            links.append(article.url)


        linkObj[site] = links

    return json.dumps(linkObj)


