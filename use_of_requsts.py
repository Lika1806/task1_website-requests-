from my_requests import get_text
from bs4 import BeautifulSoup

architects = dict()

url1 = 'https://en.wikipedia.org/wiki/List_of_Armenian_architects'
content = get_text(url1)
soup = BeautifulSoup(content, 'html')
architects_info = soup.find('ul', class_=lambda x: not x or not x.startswith("vector"))
for p in architects_info.find_all('li'):
    info = p.find('a')
    architects[info['title']] = info['href']


url_list = ["https://en.wikipedia.org/wiki/Category:Armenian_architects",
           "https://en.wikipedia.org/wiki/Category:Ethnic_Armenian_architects"]
x=0
for url in url_list:
    content = get_text(url)
    if content is None:
        continue
    soup = BeautifulSoup(content, 'html')
    full_list = soup.find('div', class_='mw-category mw-category-columns')
    for info in full_list.find_all('a'):
        name = info['title'] 
        link = info['href']
        if name in architects:
            continue
        architects[name]=link
    
architects = {a:'https://en.wikipedia.org'+v for a,v in architects.items()}

import pandas as pd

new_df = pd.DataFrame(architects.items(), columns= ['architect', 'wikipedia link'])
new_df.to_csv('arm_architects.csv', index = False)

