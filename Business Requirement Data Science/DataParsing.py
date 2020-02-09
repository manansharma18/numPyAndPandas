import bs4
from bs4 import BeautifulSoup
import re


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup (html_doc,'html.parser')

#print(soup.prettify())
#print(soup.title.name)
#print(soup.get_text())
#print(soup.tag)
#print(type(soup))

#print(soup.find_all('p'))
#for items in soup.find_all('p'):
#    print(items.get_text())

#print(soup.find_all(id='link1'))
#print(soup.find_all(['a','p']))

#t = re.compile('a')
#for tags in soup.find_all(t):
#    print(tags.get_text())

#for tags in soup.find_all('a'):
#    print(tags.get('href'))