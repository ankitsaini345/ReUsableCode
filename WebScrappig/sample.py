# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

# to open local files
#with open('test.html') as htmlFile:
#         soup = BeautifulSoup(htmlFile,'lxml')
   
# for online html file
source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source,'lxml')

# To find a tag and print    
article = soup.find('article')
#print(article.h2.a.text)

# to find a class within a tag and print its element
summary = article.find('div', class_='entry-content')
#print(summary.text)

# to make output readable
#print(article.prettify())

# to print an attribute of a tag
vidSrc = article.find('iframe')['src']
#print(vidSrc)

vidId = vidSrc.split('/')[4]
#print(vidId)

vidLink = f'https://youtube.com/watch?v={vidId}'
#print(vidLink)

# To find all the article tag
for art in soup.find_all('article'):
    try:
        vsrc = art.find('iframe')['src']
        id = vsrc.split('/')[4]
        link = f'https://youtube.com/watch?v={id}'
        print(link)
    except:
        print("No video link found")