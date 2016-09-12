from urllib.request import urlopen
from bs4 import BeautifulSoup

dest = open('ucd_ug_engineering_org_names.txt', 'wb')
page = urlopen('http://engineering.ucdavis.edu/undergraduate/organizations/')
soup = BeautifulSoup(page, 'html.parser')

for h3 in soup.find_all('h3'):
  if h3.string != None:
    dest.write(h3.string.encode('utf-8') + ('\n').encode('utf-8'))
  else:
    print(h3)
    # dest.write(link.string.encode('utf-8') + ('\n').encode('utf-8'))
  
dest.close()