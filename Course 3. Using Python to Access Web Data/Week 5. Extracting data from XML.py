Chapter 13. Web services and XML

#Assignment: Extracting data from XML


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter location: ')

#print('Retrieving', url)
#xml = urllib.urlopen(url).read()
#print('Retrieved', len(xml), 'characters')

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')
print(data.decode())


tree = ET.fromstring(data) #xml

counts = tree.findall('.//count') #'comments/comment/count'

sum = 0
for count in counts:
    print("Count:", int(count.text))
    sum = sum + int(count.text)

print("Counts:", len(counts))
print ("Sum:", sum)

********************************************

#Alternative 1

import urllib
import xml.etree.ElementTree as ET

# extract all the comment/count values from the url and get the sum of all of them
url = 'http://python-data.dr-chuck.net/comments_217218.xml'

# get the content of the url as a string
data = urllib.urlopen(url).read()

# transform the string content into a xml tree
tree = ET.fromstring(data)

# find all count elements
counts = tree.findall('comments/comment/count')

# extract the value of each count element and add it to the total
total = 0
for count in counts:
    total += int(count.text)

print 'total: ', total

******************************************************

#Alternative 2

import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'

total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
