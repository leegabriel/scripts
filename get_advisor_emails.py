"""
May take a while - go get a snack
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

src = open('major_links.txt', 'r')
dest = open('major_advisor_emails.txt', 'wb')

for line in src:
  page = urlopen(line)
  soup = BeautifulSoup(page, 'html.parser')
  div = soup.find('div', {'property' : 'schema:email'})
  if (div != None):
    email = div.a['href'].encode('utf-8') + ('\n').encode('utf-8')
    print(('https://ucdavis.edu').encode('utf-8') + email)
    dest.write(('https://ucdavis.edu').encode('utf-8') + email)
  else:
    print ('N/A')
    dest.write(('N/A').encode('utf-8') + ('\n').encode('utf-8'))

dest.close()