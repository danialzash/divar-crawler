import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import houseCrawler

RED = '\033[91m'
RESET = '\033[0m'
COLORFUL = '\033[93m'


def base_crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print('Title:', soup.title.string)
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if "/v/" in href:
                # new_link = 'https://divar.ir' + quote(href)
                # houseCrawler.crawl(new_link)
                print(href)


base_crawl('https://divar.ir/s/tehran/buy-apartment/tehran-now')
