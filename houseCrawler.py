import requests
from bs4 import BeautifulSoup

def crawl(url):
    response = requests.get(url)
    # response.encoding = 'ISO-8859-1'
    soup = BeautifulSoup(response.content, 'html.parser')
    print('Title:', soup.title.string)

    spans = soup.find_all(
        'span',
        {'class': ['kt-group-row-item__value', 'kt-group-row-item__title kt-body kt-body--sm']})
    for span in spans:
        value = span.text.strip()
        # value = ' '. join(reversed(span.text.strip().split()))
        print('Value:', value)


crawl('https://divar.ir/v/۸۴-متر-دوخوابه-تهران-نو_آپارتمان_تهران_تهران-نو_دیوار/AZHtvASa')