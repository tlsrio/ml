# Use file for testing individual modules to avoid import conflicts
from scrapers.scrapeLinks_v2 import buildLinkObj
from scrapers.scrapeContent import getContent

# html = getContent("https://www.forbes.com/?sh=26f1f3b32254")
# getLinks(html, "https://www.forbes.com/?sh=26f1f3b32254")
buildLinkObj()
