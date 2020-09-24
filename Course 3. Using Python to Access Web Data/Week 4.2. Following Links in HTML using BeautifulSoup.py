Chapter 12. Programs that surf the web

Assignment: Following links in HTML using BeautifulSoup

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#Importing the require modules

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
count = input('Enter count : ')
position = input('Enter position : ')


#Retrieve all of the anchor tags
for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[int(position)-1].get('href', None)
print(url)
