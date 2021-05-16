from .summarization import getSummary
from .classification import getCategory
from bs4 import BeautifulSoup
import requests
import json

# linkObj - JSON object containing links
#    {source1: [link1, link2, ...], source2: [link1, link2, ...], ...}

l = {'CNN': ['https://www.cnn.com/2021/05/08/business/supply-chain-shortages-pandemic/index.html'],
	 'BBC': ['https://www.bbc.com/news/world-europe-57039362']}

def getContent(url):
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        return soup


def htmlToText(html):
    text = html.get_text()
    return text.strip()


def fetchArticles(linkObj):
	data = []

	for source in linkObj.keys():
		for link in linkObj[source]:
			try:
				article = {}

				html = getContent(link)
				text = htmlToText(html)

				title = html.find('title').text
				article['title'] = title

				summary = json.loads(getSummary(text))
				article['summary'] = summary['summary']
				article['reduced_by'] = summary['reducedBy']
				article['link'] = link

				article['source'] = source

				categories = json.loads(getCategory(text))
				catList = []
				for keyword in categories.keys():
					if categories[keyword] >= 0.2:
						catList.append(keyword)
				article['category'] = catList

				data.append(article)
				#print(article)

			except Exception as e:
				print(e)
				continue

	return json.dumps(data)


#d = fetchArticles(l)
#print(d)



