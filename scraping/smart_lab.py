# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime

d = {'url': [], 'title': [], 'text': [], 'date': [], 'url_preview': []}
df = pd.DataFrame(data=d)
x = datetime.datetime(2019, 10, 6)
for i in range(0, 1095):
    x = x + datetime.timedelta(days=1)
    iso = x.isoformat()
    day = str(x.day)
    if len(day) == 1:
        day =f"0{day}"
    month = str(x.month)
    if len(month) == 1:
        month = f"0{month}"
    year = x.year
    url = f'https://smart-lab.ru/news/date/{year}-{month}-{day}/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_='inside')
    except:
        continue
    for i in quotes:
        tag_data = i.findNext('a')
        link = tag_data.get('href', '/')
        title = tag_data.get('title', '/')
        url_preview = ''
        url = 'https://smart-lab.ru' + link
        try:
            response = requests.get(url)
        except:
            continue
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('div', class_=lambda value: value and value.startswith("topic bluid"))[0].find_all('div', class_='content')[0].text
        result = {
            'url': url, 'title': title, 'text': text, 'date': iso, 'url_preview': url_preview
        }
        df = df.append(result, ignore_index=True)
        count_rows = len(df)
        if count_rows % 10 == 0:
            print(f"{count_rows}-|{year}-{month}-{day}|-{datetime.datetime.now()}")

    df.to_csv('smart_lab.csv')
df.to_csv('smart_lab.csv')
