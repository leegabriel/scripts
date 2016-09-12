from urllib.request import urlopen
from bs4 import BeautifulSoup

dest = open('ucd_ug_major_names.txt', 'wb')
page = urlopen('https://www.ucdavis.edu/majors')
soup = BeautifulSoup(page, 'html.parser')

count = 0
for span in soup.find_all('span', class_='field-content'):
  # Don't want (Major) or (Major & Minor), which also have class="field-content"
  count += 1
  if count % 2 == 0:
    continue

  link = span.contents[0]
  dest.write(link.string.encode('utf-8') + ('\n').encode('utf-8'))  

dest.close()