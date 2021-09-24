import requests
from bs4 import BeautifulSoup
import pandas as pd


newsList = []

newsNumber = 0

response = requests.get('https://www.correiobraziliense.com.br/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

news = site.findAll('article')

for news_titles in news:
    title = news_titles.find('a', attrs={'title': ''})

    if(title) != None:
        newsList.append([title.text.replace('\n', ''), newsNumber, title['href']])
    
        newsNumber += 1

        

newsTabled = pd.DataFrame(newsList, columns=['TITLE', 'NUMBER', 'LINK'])

newsTabled.to_json('newsScraping.json')

print(newsTabled)