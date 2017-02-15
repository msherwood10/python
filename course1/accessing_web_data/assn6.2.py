import urllib
import json

#serviceurl = 'http://python-data.dr-chuck.net/geojson?'
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #uncomment to use Google api
#modified to use google API key

address = raw_input('Enter location: ')

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
#print json.dumps(js, indent=4)

info = js["results"][0]["place_id"]
print 'Place id', info
