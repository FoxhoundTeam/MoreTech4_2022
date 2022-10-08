# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime
# https://www.banki.ru/news/lenta/?id=10906999
d = {'url': [], 'title': [], 'text': [], 'date': [], 'url_preview': []}
df = pd.DataFrame(data=d)
for i in range(10942089, 10973497, 5):
    url = f'https://www.banki.ru/news/lenta/?id={i}'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('div', class_='l0654fd42')[0].text
        date = soup.find_all('span', class_='l51e0a7a5')[0].text.replace('\n','').replace('\t', '')
        date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
        title = soup.find_all('div', class_='lf4cbd87d ld6d46e58 lf732513f')[0].text.replace('\n','').replace('\t','')
        url_preview = soup.find_all('meta', property='og:image')[0].get('content','')
        result = {
            'url': url, 'title': title, 'text': text, 'date': date.isoformat(), 'url_preview': url_preview
        }
        df = df.append(result, ignore_index=True)
        count_rows = len(df)
        if count_rows % 10 == 0:
            df.to_csv('banki.csv')
            print(f"{count_rows}-|{10973497-i}|-{datetime.datetime.now()}")
    except:
        continue
df.to_csv('banki.csv')
