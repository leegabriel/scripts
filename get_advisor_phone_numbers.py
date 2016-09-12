"""
May take a while - go get a snack
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

src = open('major_links.txt', 'r')
dest = open('major_advisor_phone_numbers.txt', 'wb')

for line in src:
  page = urlopen(line)
  soup = BeautifulSoup(page, 'html.parser')
  div = soup.find('div', {'property' : 'schema:telephone'})
  if (div != None):
    number = div.string.encode('utf-8') + ('\n').encode('utf-8')
    print(number)
    dest.write(number)
  else:
    print ('N/A')
    dest.write(('N/A').encode('utf-8') + ('\n').encode('utf-8'))

dest.close()