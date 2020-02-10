import bs4
from bs4 import BeautifulSoup
import re
import urllib.request

#url = 'https://flipp.com/en-ca/waterloo-on/flyer/3295150-farm-boy-weekly?postal_code=N2L6P4'
#url = 'https://www.tutorialspoint.com/index.htm'
#url = 'https://flipp.com/search/tomato'
#url = 'https://flipp.com/en-ca/waterloo-on/item/474492105-farm-boy-weekly'
url = 'https://analytics.usa.gov'
#url = 'https://lxml.de'
#url = 'https://gateflipp.flippback.com/bf/flipp/items/search?locale=en-ca&postal_code=N2L6P4&sid=&q=tomato'

res = urllib.request.urlopen(url).read()

soup = BeautifulSoup (res,'html.parser')

#print(type(soup))
#print(req)
#print(soup.prettify()[0:5000])

#for id in soup.find_all(id = 'agency-selector'):
#    print (id)
#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())

#for link in soup.find_all('a',attrs={'href': re.compile('^http')}):
#    print(link)

#print(soup.get_text())
#print(soup.prettify())

#for link in soup.find_all(attrs={'pre_price_text'}):
#    print(link)

#print(res)

#price = soup.find_all(attrs={'items'})

#print(price)

#data = res.json()
#print(data)