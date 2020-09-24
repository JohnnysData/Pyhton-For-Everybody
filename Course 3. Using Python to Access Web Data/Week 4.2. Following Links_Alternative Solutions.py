Chapter 12. Programs that surf the web

Assignment: Following links in HTML using BeautifulSoup

#Alternative solutions

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input("Enter position:"))-1
count = int(input("Enter count:"))
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

Sequence = []

tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    #print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    link = tags[position].get('href', None)
print(Sequence[-1])

********************************************************

#Alternative 2

#Importing the require modules
import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#Accessing websites

url = input('Enter url ')
cn = input('Enter count: ')
cnint = int(cn)
pos = input('Enter position: ')
posint = int(pos)
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html''''url''', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


#Retrieve all of the anchor tags

tags_lst = list()
for x in range(0,cnint):
    tags = soup('a')
    my_tags = tags[posint-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))

#Alternative
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
count = 8
position = 18
tags_lst = []

for x in xrange(count-1):
    tags = soup('a')
    my_tags = tags[position-1]
    needed_tag = my_tags.get('href', None)
    tags_lst.append(needed_tag)
    url = str(needed_tag)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

***********************************************

#Alternative 3

import urllib
from bs4 import BeautifulSoup

#url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# print soup
count = int(raw_input('Enter count: '))+1
position = int(raw_input('Enter position: '))


tags = soup('a')
# next line gets count tags starting from position
my_tags = tags[position: position+count]
tags_lst = []
for tag in my_tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
print tags_lst

*****************************************************
#Alternative 4

import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url ')
cn = input('Enter count: ')
cnint = int(cn)
pos = input('Enter position: ')
posint = int(pos)
html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html''''url''', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags_lst = list()
for x in range(0,cnint):
    tags = soup('a')
    my_tags = tags[posint-1]
    needed_tag = my_tags.get('href', None)
    url = str(needed_tag)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print(my_tags.get('href', None))

*************************************************

#Alternative 5
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
link_line = int(input("Enter position: ")) - 1
relative to first link
count = int(input("Enter count: "))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print(url)
   url = tags[link_line].get("href", None)
   count = count - 1
