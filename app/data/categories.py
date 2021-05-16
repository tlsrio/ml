from bs4 import BeautifulSoup
import requests


res = requests.get('https://www.newsmaker.com.au/category/index')
soup = BeautifulSoup(res.content, 'html.parser')

