

import requests
import json


apikey = "cf5e2bc757104bddb2063ac07e7499db"
request_str = "http://congress.api.sunlightfoundation.com/legislators?per_page=all&apikey=" + apikey
r = requests.get(request_str)
content = json.loads(r.text)

with open('accounts2.tsv','w') as outfile:
	for person in content['results']:
		lastname = unicode(person['last_name'])
		firstname = unicode(person['first_name'])
		state_name = unicode(person['state_name'])
		state_short = unicode(person['state'])
		chamber = unicode(person['chamber'])
		gender = unicode(person['gender'])
		twitter_id = person[u'twitter_id'] if 'twitter_id' in person else None
		# skip line if no twitter account
		if not twitter_id: continue
		line = firstname + " " + lastname + "\t" +  state_name + "\t" + chamber + "\t" + twitter_id 
		outfile.write(line.encode("utf8") + "\n")

