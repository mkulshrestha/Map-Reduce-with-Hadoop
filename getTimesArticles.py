from nytimesarticle import articleAPI
from bs4 import BeautifulSoup
import requests
api = articleAPI("MqGpINkbKmy15GOA36p7DYm09JTXSAaO")
f=open('nytarticlesday.txt','w')
links=[]
articles = api.search(q='cold',begin_date = 20190101,page=100)
#f=open('sports.txt','w')
for i in range(0,10):
    
    url = articles['response']['docs'][i]['web_url']
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    soup.prettify()
    for i in range((len(soup.find_all('p')))-3):
     
      f.write(soup.find_all('p')[i].get_text())
    
    print(url)
    links.append(url)
f.close()
import os
path = os.path.join(os.path.expanduser('~'), 'Desktop', 'file.txt')
print (path)