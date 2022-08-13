import urllib.request, urllib.parse
import ssl
from bs4 import BeautifulSoup

# Sample: http://py4e-data.dr-chuck.net/comments_42.html
# Actual: http://py4e-data.dr-chuck.net/comments_1534732.html

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


tags = soup('span')
count = 0
nums = list()
sum = 0
for tag in tags:
    nums.append(tag.contents[0])
    count = count + 1

for num in nums:
    sum = sum + int(num)

print('Count {} \nSum {}'.format(count, sum) )
