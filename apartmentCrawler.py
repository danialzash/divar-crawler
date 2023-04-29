import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import houseCrawler

MAX_NUMBER_OF_HOUSE_PER_PAGE = 24
RED = '\033[91m'
RESET = '\033[0m'
COLORFUL = '\033[93m'
ANOTHER_COLOR = '\033[96m'
MAIN_URL = 'https://divar.ir/s/tehran/buy-apartment/'
is_last_page = False
pager_number = 0


def base_crawl(url):
    house_number = 0
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if "/v/" in href:
                house_number += 1
                new_href = href[3:-9]
                new_link = 'https://divar.ir/v/' + quote(new_href) + '/' + href[-8:]
                # print(new_link.strip())
                print(RED, house_number, RESET, COLORFUL, href[-8:], RESET)
                try:
                    houseCrawler.crawl(new_link, href[-8:])
                except Exception as e:
                    print("An error has occurred: ", e)

    if house_number < MAX_NUMBER_OF_HOUSE_PER_PAGE:
        global is_last_page
        is_last_page = True


# todo: change this function and make region enum or dictionary instead of reading from file
def validate_region(input_region):
    with open('district.txt', 'r') as file:
        contents = file.read().split("\n")
        return input_region in contents


def get_region():
    while True:
        input_region = input("please enter region:")
        if validate_region(input_region):
            return input_region
        print('the region is incorrect')


region = get_region()
url = MAIN_URL + region

while True:
    if is_last_page:
        break
    if pager_number == 0:
        print(ANOTHER_COLOR, pager_number, RESET)
        base_crawl(url)
    else:
        print(ANOTHER_COLOR, pager_number, RESET)
        base_crawl(url + "?page=" + str(pager_number))
    pager_number += 1

# base_crawl(url)
