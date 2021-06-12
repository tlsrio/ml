# News Site array
# Array of site object:
# <siteName>: {
#   links: [<array of links to scrape for site>]
#   articlePatterns:[<array of pa to scrape for site>]
# }

# newsSites = {
#     "CNN": "https://www.cnn.com",
#     "BBC": "https://www.bbc.com",
#     "CBC": "https://www.cbc.ca",
#     "AP": "https://apnews.com",
#     "C-SPAN": "https://www.c-span.org",
#     "The Bureau of Investigative Journalism": "https://www.thebureauinvestigates.com/stories",
#     "NPR": "https://www.npr.org/sections/news/",
#     "Reuters": "https://www.reuters.com",
#     "USA Today": "https://www.usatoday.com",
#     "Mashable": "https://mashable.com",
#     "TechCrunch": "https://techcrunch.com",
#     "The Verge": "https://www.theverge.com",
#     "digitaltrends": "https://www.digitaltrends.com",
#     "TNW": "https://thenextweb.com",
#     "VentureBeat": "https://venturebeat.com",
#     "GIZMODO": "https://gizmodo.com",
#     "techradar": "https://www.techradar.com",
#     "INSIDER": "https://www.businessinsider.com",
#     "Futurism": "https://futurism.com",
#     "recode": "https://www.vox.com/recode",
#     "Vox": "https://www.vox.com",
# }

newsSites = {
    "CNN": {
        "links": ["https://www.cnn.com", "https://money.cnn.com/data/markets",
                  "https://www.cnn.com/business/tech", "https://www.cnn.com/world"],
        "articleRe": [],
    },
    "BBC": {
        "links": ["https://www.bbc.com"],
        "articleRe": [".*/news/.*-(\d*)"],
    },
    "CBC": {
        "links": ["https://www.cbc.ca"],
        "articleRe": [".*/news/.*-1\.(\d*)"],
    },
    "AP News": {
        "links": ["https://apnews.com"],
        "articleRe": [".*/article/.+"],
    },
    "The Bureau of Investigative Journalism": {
        "links": ["https://www.thebureauinvestigates.com/stories"],
        "articleRe": [],
    },
    "NPR": {
        "links": ["https://www.npr.org/sections/news",],
        "articleRe": [],
    },
    "Reuters": {
        "links": ["https://www.reuters.com"],
        "articleRe": [],
    },
    "USA Today": {
        "links": ["https://www.usatoday.com"],
        "articleRe": [],
    },
    "Mashable": {
        "links": ["https://mashable.com/tech", "https://mashable.com/science",
                  "https://mashable.com/culture", "https://mashable.com/entertainment"],
        "articleRe": [".*/article/.+"],
    },
    "TechCrunch": {
        "links": ["https://techcrunch.com"],
        "articleRe": [],
    },
    "The Verge": {
        "links": ["https://www.theverge.com"],
        "articleRe": [],
    },
    "digitaltrends": {
        "links": ["https://www.digitaltrends.com/news"],
        "articleRe": [".*/news/.+", ".*/gaming/.+", ".*/computing/.+", ".*/mobile/.+"],
    },
    "TNW": {
        "links": ["https://thenextweb.com"],
        "articleRe": [".*/news/.+"],
    },
    "VentureBeat": {
        "links": ["https://venturebeat.com"],
        "articleRe": [],
    },
    "GIZMODO":  {
        "links": ["https://gizmodo.com"],
        "articleRe": [".*-(\d{10})"],
    },
    "techradar": {
        "links": ["https://www.techradar.com"],
        "articleRe": [".*/news/.+"],
    },
    "INSIDER": {
        "links": ["https://www.businessinsider.com"],
        "articleRe": [".*-(\d{4})-(\d{1,2})"],
    },
    "Futurism": {
        "links": ["https://futurism.com"],
        "articleRe": [".*/the-byte/.+", ".*/neoscope/.+"],
    },
    "recode": {
        "links": ["https://www.vox.com/recode"],
        "articleRe": [],
    },
    "Vox":  {
        "links": ["https://www.vox.com"],
        "articleRe": [],
    },
}
