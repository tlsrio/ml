import newspaper
# import json
# from data.newsSites import newsSites
# from .scrapeContent import getContent
#
# # linkObj - JSON object containing links
# #    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}


# def buildLinkObj():
#
#     linkObj = {}
#
#     for site in newsSites.keys():
#         print(site);
#         print(newsSites[site])
#         paper = newspaper.build(newsSites[site])
#         print(paper.size())
#
#         links = []
#
#         for article in paper.articles:
#             print(article.url)
#             links.append(article.url)
#
#
#
#         linkObj[site] = links
#
#     return json.dumps(linkObj)


def getLinks(html, source):
    links = []
    for link in html.find_all('a', href=True):
        href = link.get('href');
        if href.find("http") != -1:
            links.append(href);
        else:
            href_1 = source + href;
            links.append(href_1);

    return links;


def buildLinkObj():

    linkObj = {}

    for site in newsSites.keys():

        siteContent = getContent(newsSites[site]);
        articleLinks = getLinks(siteContent, newsSites[site]);

        links = []

        for article in articleLinks:
            try:
                html = getContent(article);
                meta = html.findAll("meta", attrs={"content": "article", "property": "og:type"})
                if (len(meta) > 0):
                    links.append(article);
            except Exception as e:
                continue;

        linkObj[site] = links
        print(site + " " + str(len(links)))
        print(linkObj[site])

    return json.dumps(linkObj)


