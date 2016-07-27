import urllib2
import json
import locuapikey


flburger = "https://api.locu.com/v1_0/venue/search/?name=burger&region=FL&api_key=" + locuapikey.apikey

json_objs = urllib2.urlopen(flburger)

data2 = json.load(json_objs)

for item in data2['objects']:
    print item["name"]
    print item["locality"]
    print item["street_address"]
    print item["country"]
    print item["phone"]
    print item["website_url"]
    print "--------------------------------------"
    
    
