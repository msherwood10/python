import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#get anchor tags, pull out hrefs
tags = soup('a')

for tag in tags:
    print tag.get('href', None)
