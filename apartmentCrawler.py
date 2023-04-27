import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import houseCrawler

RED = '\033[91m'
RESET = '\033[0m'
COLORFUL = '\033[93m'
MAIN_URL = 'https://divar.ir/s/tehran/buy-apartment/'


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


# todo: change this function and make region enum or dictionary instead of reading from file
def validate_region(region):
    with open('district.txt', 'r') as file:
        contents = file.read().split("\n")
        return region in contents


def get_region():
    while True:
        region = input("please enter region:")
        if validate_region(region):
            return region
        print('the region is incorrect')


region = get_region()
url = MAIN_URL + region

base_crawl(url)
