import requests
from bs4 import BeautifulSoup
import saveInfoToDatabase

persian_to_english_table = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')


def calculate_main_details(spans):
    area = spans[0].text.strip().translate(persian_to_english_table)
    year = calculate_year(spans[1].text.strip())
    number_of_rooms = spans[2].text.strip().translate(persian_to_english_table)
    elevator = False if spans[3].text.strip() == "آسانسور ندارد" else True
    parking = False if spans[4].text.strip() == "پارکینگ ندارد" else True
    cellar = False if spans[5].text.strip() == "انباری ندارد" else True
    return area, year, number_of_rooms, elevator, parking, cellar


# return exact year or -1370 if the build year is less than 1370
def calculate_year(text):
    if len(text) == 4:
        return text.translate(persian_to_english_table)
    else:
        return -1370


def calculate_main_info(base_info):
    total_price = base_info[0].text.split()[0].translate(persian_to_english_table).replace("٬", "")
    total_price = int(total_price)
    price = base_info[1].text.split()[0].translate(persian_to_english_table).replace("٬", "")
    price = int(price)
    if len(base_info[-1].text.split()) == 3:
        words = base_info[-1].text.split()
        floor = words[0].translate(persian_to_english_table) + " from " + words[2].translate(persian_to_english_table)
    else:
        floor = base_info[-1].text.strip().translate(persian_to_english_table)
    return total_price, price, floor


def save_all(info):
    saveInfoToDatabase.save_house_info(info)


def crawl(url, short_link):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string

    date_div = soup.find('div', {'class': 'kt-page-title__subtitle kt-page-title__subtitle--responsive-sized'})
    exactDate = calculate_date(date_div)

    spans = soup.find_all(
        'span',
        # {'class': ['kt-group-row-item__value', 'kt-group-row-item__title kt-body kt-body--sm']})
        {'class': 'kt-group-row-item__value'})
    area, year, number_of_rooms, elevator, parking, cellar = calculate_main_details(spans)

    base_info = soup.find_all('p', {'class': 'kt-unexpandable-row__value'})
    total_price, price, floor = calculate_main_info(base_info)

    details = soup.find('p', {'class': 'kt-description-row__text kt-description-row__text--primary'})
    details = details.text.strip()

    info = {
        "title": title,
        "exactDate": exactDate,
        "area": area,
        "year": year,
        "number_of_rooms": number_of_rooms,
        "elevator": elevator,
        "parking": parking,
        "cellar": cellar,
        "totalPrice": total_price,
        "price": price,
        "floor": floor,
        "shortLink": short_link,
        "details": details
    }

    save_all(info)


def calculate_date(dateDiv):
    if dateDiv == None:
        return "ok"
    else:
        dateDivString = dateDiv.text.strip()
        words = dateDivString.split()
        exactDate = ' '.join(words[:3])
        return exactDate


