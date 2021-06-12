from bs4 import BeautifulSoup
import requests


def getContent(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup


def htmlToText(html):
    text = html.get_text()
    return text.strip()


def getThumbnail(html):
    # default thumbnail to grey square
    thumbnail = "https://media.tarkett-image.com/large/TH_24567080_24594080_24596080_24601080_24563080_24565080_24588080_001.jpg"
    try:
        meta = html.findAll(attrs={"property": "og:image"})
        thumbnail = meta[0].get("content")
    except Exception as e:
        return thumbnail
    return thumbnail
