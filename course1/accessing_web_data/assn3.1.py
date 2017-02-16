import urllib
from BeautifulSoup import *
comments = list()
url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#get span tags, pull out contents
tags = soup('span')

for tag in tags:
    comments.append(int(tag.contents[0]))

numcomments = len(comments)
sumcomments = sum(comments)

print 'Count', numcomments, '\n', 'Sum', sumcomments
