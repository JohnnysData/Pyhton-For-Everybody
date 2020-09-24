Chapter 12. Programs that surf the web

Assignment: Scraping HTML data using BeautifulSoup

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#print(soup)

# Retrieve all of the anchor tags

tags = soup('span')

sum = 0

for tag in tags:
    #Look at the parts of a tag
    #print("TAG:", tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    numbers = tag.contents[0]
    sum = sum + int (numbers)
print(sum)


#Alternative
#import re
#total = 0

#for tag in tags:
    ##line = str(tag)
    #numbers = re.findall('[0-9]+', str(tag))      # (......, line)
    #print(numbers)
    #for number in numbers:
        #numbers = int(number)
        #total = total + numbers
#print(total)



#Alternative
#count = 0
#for tag in tags:
	#number = tag.contents[0]
	#number= int(number)
	#count = count+ number
#print (count)

#Alternative

#numbers = []

#for tag in tags:
    #numbers.append(int(tag.string))

#print sum(numbers)
