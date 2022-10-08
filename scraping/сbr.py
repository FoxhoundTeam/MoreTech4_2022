# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
import datetime


def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())\

def get_month_int(month):
    a = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12,
    }
    return a[month]


# https://www.cbr.ru/press/event/?id=14224
d = {'url': [], 'title': [], 'text': [], 'date': [], 'url_preview': []}
df = pd.DataFrame(data=d)
for i in range(6000, 14224):
    url = f'https://www.cbr.ru/press/event/?id={i}'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find_all('h1')[0].text.replace('\n', '')
        if not match(title) or title == 'Новость':
            continue
        print(f"{i}-{title}")
        text = soup.find_all('div', class_='lead-text')[0].text.replace('\n', '')
        day, month, year, _ = soup.find_all('div', class_='col-md-6 col-12 news-info-line_date')[0].text.replace('\n', '').split()
        month = get_month_int(month)
        date = datetime.datetime.strptime(f"{month}/{day}/{year}", "%m/%d/%Y")

        url_preview = ''
        result = {
            'url': url, 'title': title, 'text': text, 'date': date.isoformat(), 'url_preview': url_preview
        }
        df = df.append(result, ignore_index=True)
        count_rows = len(df)
        if count_rows % 10 == 0:
            df.to_csv('cbr.csv')
            print(f"{count_rows}-|{10973497 - i}|-{datetime.datetime.now()}")
    except:
        continue
df.to_csv('cbr.csv')
