Chapter 13: JSON and the REST Architecture

#Assignment: Extracting data from JSON

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
json_data = urllib.request.urlopen(url).read()
print('Retrieved', len(json_data), 'characters')

info = json.loads(json_data)
#print(json_data)
print('User count:', len(info))

sum = 0
total_num = 0

for item in info["comments"]:    # Instead of adding ["comments"] here, we can add info = info ["comments"] after line 9.
    #print('Name', item['name'])
    print('Count', item['count'])
    total_num =  total_num + 1
    sum = sum + int(item['count'])

print('Count:', total_num)
print('Sum:', sum)
