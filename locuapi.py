import urllib2
import json
import locuapikey


url = 'https://api.locu.com/v1_0/venue/search/?name=restaurant&locality=New%20York&api_key=' + locuapikey.apikey
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

for item in data['objects']:
    print item["name"]
    print item["locality"]
    print item["street_address"]
    print item["country"]
    print item["phone"]
    print item["website_url"]
    print "--------------------------------------"







