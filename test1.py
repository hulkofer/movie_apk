# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:54:11 2018

@author: hulkofer
"""

#import requests
#resp = requests.get('http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8')
#txt = resp.text

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(txt,'lxml')

#print(len(soup.find_all('p')))

#print(soup.find_all('p')[0].text)

#print(soup.find('h1').text)
"""
import requests
from bs4 import BeautifulSoup
url = 'http://imdb.com'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

urls = []
for h in soup.find_all('h3'):
    a = h.find('a')
    urls.append(a.attrs['href'])
"""

#all_divs = soup.find_all("div", class_="table-row")
#print(all_divs)

#li = soup.find_all('li')
#print(li)


#tag = soup.find(lambda tag: tag.name == 'li' and tag['subnav_item_main'] == ['value', 'price', ''])
#print(tag)

#soup.find_all("div", class=re.compile("^span3"))
"""
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/title/tt0371746/reviews?ref_=tt_urv'
res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")

main_content = urljoin(url,soup.select(".load-more-data")[0]['data-ajaxurl'])  ##extracting the link leading to the page containing everything available here
response = requests.get(main_content)
broth = BeautifulSoup(response.text,"lxml")

for item in broth.select(".review-container"):
    title = item.select(".title")[0].text
    review = item.select(".text")[0].text
    print("Title: {}\n\nReview: {}\n\n".format(title,review))
    


import bs4 as bs
import urllib.request 

sauce = urllib.request.urlopen('http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8/').read()
soup =bs.BeautifulSoup(sauce,'lxml')

nav = soup.nav

for div in soup.find_al('div', class_='body'):
    print(div.text)
    
"""
import bs4 as bs
import urllib.request
import pandas as pd


sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup =bs.BeautifulSoup(sauce,'lxml')
 

table= soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print (row)


   
#for url in soup.find_all('a'):
#    print(url.get('href'))


#nav = soup.nav

#for div in soup.find_all('div',{'class':'body'}):
    #print(div.text)


#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)
#print(nav)


#dfs = pd.read_html('http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8/')
#for df in dfs:
#    print(df)

#ul_lists = soup.find_all('ul',{'class': 'something'})


#for list_ in ul_lists.find_all('a'):
#    list_movie[list_.text] = city['href']
    
#print(ul_lists[1])