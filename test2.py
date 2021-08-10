import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

html_doc = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/showtype?keywords=lagos&page='

df = pd.DataFrame()

# loop through entire web pages

    
pages = rq.get(html_doc)
data = bs(pages.text, 'html.parser')
soup = data.find_all('div', {'class' : 'wp-block property list'})

print(soup)

#for each in soup:
   # name = each.find(itemprop="url").text
   # print(name)