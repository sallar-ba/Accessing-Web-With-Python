import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')
total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved {} characters'.format(len(data)))

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

for item in lst:
    count = count + 1
    t = item.find('count').text
    total = total + float(t)

print('Count: {}'.format(count))
print('Sum: {}'.format(total))