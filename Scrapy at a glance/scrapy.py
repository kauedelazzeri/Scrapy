# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:52:47 2021

@author: kdelazzeri
"""
url="https://itaivan.com/busca/?finalidade=Aluguel"

import requests
from bs4 import BeautifulSoup

#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#page = requests.get("http://quotes.toscrape.com/tag/humor/")
page = requests.get(url, verify=False)
#%%
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())
#soup.find_all('p')
#%%
#soup.find_all('p')[0].get_text()
a = soup.find_all("Vila Baependi")




#%%
b = []
for i in range(len(a)):
    b.append(a[i].get_text())