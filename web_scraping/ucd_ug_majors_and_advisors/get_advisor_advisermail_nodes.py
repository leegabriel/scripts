"""
Depends on ucd_ug_major_links.txt
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

src = open('ucd_ug_major_links.txt', 'r')
dest = open('ucd_ug_advisor_advisermail_nodes.txt', 'wb')

for line in src:
  page = urlopen(line)
  soup = BeautifulSoup(page, 'html.parser')
  div = soup.find('div', {'property' : 'schema:email'})
  if (div != None):
    advisermail_node = div.a['href'].encode('utf-8') + ('\n').encode('utf-8')
    print(('https://ucdavis.edu').encode('utf-8') + advisermail_node)
    dest.write(('https://ucdavis.edu').encode('utf-8') + advisermail_node)
  else:
    print ('N/A')
    dest.write(('N/A').encode('utf-8') + ('\n').encode('utf-8'))

dest.close()