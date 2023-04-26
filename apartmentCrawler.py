import requests
from bs4 import BeautifulSoup


RED = '\033[91m'
RESET = '\033[0m'
COLORFUL = '\033[93m'

counter = 0
numberOfNeighborhood = 0

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print('Title:', soup.title.string)

    with open('district.txt', 'w') as f:
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                if "/v/" in href:
                    print(RED, 'Link:', href, RESET)
                    global counter
                    counter += 1
                elif "/s/tehran/buy-apartment" in href:
                    district = href.rsplit('/', 1)[-1]
                    f.write(district + "\n")
                    print(COLORFUL, 'link:', href, RESET)
                    global numberOfNeighborhood
                    numberOfNeighborhood += 1
                else:
                    print('Link:', href)


crawl('https://divar.ir/s/tehran/buy-apartment/tehran-now')
print("links:", counter)
print("neighborhoods:", numberOfNeighborhood)
