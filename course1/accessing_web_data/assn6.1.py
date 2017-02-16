import urllib
import json

total = 0

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data

info = json.loads(str(data))
#print json.dumps(info, indent=4)

for item in info["comments"]:
    total = total + int(item['count'])

print 'Count:', len(info["comments"])
print 'Sum:', total
