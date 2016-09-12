"""
May take a while - go get a snack
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

src = open('major_links.txt', 'r')
dest = open('major_advisor_names.txt', 'wb')

for line in src:
  page = urlopen(line)
  soup = BeautifulSoup(page, 'html.parser')
  div = soup.find('div', {'property' : 'schema:accountablePerson'})
  if (div != None):
    name = div.string.encode('utf-8') + ('\n').encode('utf-8')
    print(name)
    dest.write(name)
  else:
    print ('N/A')
    dest.write(('N/A').encode('utf-8') + ('\n').encode('utf-8'))

dest.close()