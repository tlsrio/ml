import newspaper
import json
from data.newsSites import newsSites
from .scrapeContent import getContent
import re

# linkObj - JSON object containing links
#    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}


def extract_date(url):
        return re.findall(
            r'(-|/)(\d{4})(-|/)(\d{1,2})(-|/)(\d{1,2})(-|/)',
            url);


def isArticle(url, articleRe):
    if len(extract_date(url)) > 0:
        return True;
    elif len(articleRe) > 0:
        for pattern in articleRe:
            if re.match(pattern, url):
                return True;
    else:
        return False;


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

    for source in newsSites.keys():

        articleRe = newsSites[source]["articleRe"];
        links = []

        for site in newsSites[source]["links"]:

            siteContent = getContent(site);
            articleLinks = getLinks(siteContent, site);

            for article in articleLinks:
                try:
                    if isArticle(article, articleRe):
                        links.append(article);
                except Exception as e:
                    continue;

        linkObj[source] = links
        print(source + " " + str(len(links)))
        print(linkObj[source])

    return json.dumps(linkObj)