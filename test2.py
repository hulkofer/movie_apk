# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:13:18 2018

@author: hulkofer
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url= 'http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8'

uClient = uReq(my_url)
page_html = uClient.read()


#html parser
page_soup = soup(page_html, 'html.parser')

#grabs each something
containers_2 = page_soup.findAll('div', id)
containers = page_soup.findAll('div',{'class':'"aux-content-widget-2"'})

#print(containers)
for container in containers:
    something = container.div.div.div.div.img['title']
    
uClient.close()

"""
trs = soup.find_all('tr')

for tr in trs:
    spans = tr.find_all('span')
    if spans:
        print 'title:', spans[0].text
        print 'date:',  spans[2].text


find_stuff = page_soup.findAll('ul',{'class':'quicklinks'})
#print(find_stuff)


for stuffz in find_stuff.find_all('li',{'class':'subnav_item_main'}):
    print(stuffz.text)
    
    
"""

stuffz = page_soup.find('ul',{'class':'quicklinks'}).parent
in_depth_stuffz = stuffz.find_next('ul').find_all('li')
print(in_depth_stuffz[1])