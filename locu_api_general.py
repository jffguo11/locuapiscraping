import urllib2
import json
import locuapikey

locality="category=restaurant&locality=Chicago"

def locu_search(query):
    locality = query.replace(" ", "%20")
    final_url = "https://api.locu.com/vi_0/venue/search/?api_key=" + locuapikey.apikey + "&" + locality
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    return data["objects"]
    
for item in locu_search(locality):
    print item["name"]



        


    