import urllib
from BeautifulSoup import *
url = raw_input('Enter - ')
start = raw_input('Enter position:')
startpos = int(start)-1
count = raw_input('Enter count:')
numcount = int(count)
namelist = list()
templist = list()
loop = 0

#get name from first URL...there has to be a better way to do this
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
ftag = soup('title')
#ugly need to fix
templist = str(ftag[0]).split()
namelist.append(templist[2])

while loop < numcount:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    #get anchor tags, pull out hrefs
    tags = soup('a')
    tag = tags[startpos]
    target = tag.get('href', None)
    #set new URL for loop
    url = target
    print target
    name = str(tag.contents[0])
    namelist.append(name)
    loop = loop +1

print namelist
