import urllib
import xml.etree.ElementTree as ET

numlist = list()
address = raw_input('Enter location: ')
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)

counts = tree.findall('.//count')
# print 'XML', counts

for count in counts:
    numlist.append(int(count.text))

print 'Count:', len(numlist)
print 'Sum:', sum(numlist)
