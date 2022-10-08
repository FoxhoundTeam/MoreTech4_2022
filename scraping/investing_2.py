# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import datetime
# https://ru.investing.com/news/economy/article-1911143 -> 2188743
d = {'url': [], 'title': [], 'text': [], 'date': [], 'url_preview': []}
df = pd.DataFrame(data=d)
for i in range(1990457, 2030114, 1):
    url = f'https://ru.investing.com/news/economy/article-{i}'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        texts = soup.find_all('div', class_='WYSIWYG articlePage')[0]
        try:
            button_text = texts.findNext('div', 'relatedInstrumentsWrapper').text
            text = texts.text.replace(button_text, '')
        except:
            text = texts.text

        date = soup.find_all('div', class_='contentSectionDetails')[0].findNext('span').text
        if '(' in date:
            _, date = date.replace(')', '').split('(')
        date = datetime.datetime.strptime(date, '%d.%m.%Y %H:%M')
        title = soup.find_all('h1', class_='articleHeader')[0].text
        url_preview = soup.find_all('img', id='carouselImage')[0].get('src', '')
        result = {
            'url': url, 'title': title, 'text': text, 'date': date.isoformat(), 'url_preview': url_preview
        }
        df = df.append(result, ignore_index=True)
        count_rows = len(df)
        if count_rows % 10 == 0:
            df.to_csv('investing2.csv')
            print(f"{count_rows}-|{2030114-i}|-{datetime.datetime.now()}")
    except:
        continue
df.to_csv('investing2.csv')
