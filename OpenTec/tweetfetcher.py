import json
import urllib2

base_url = "http://search.twitter.com/search.json?"

def fetchtweets(query, rpp):
	url = base_url + 'q=' + query + '&rpp=' + rpp
	response = urllib2.urlopen(url)
	raw_data = response.read()
	data = json.loads(raw_data)
	return data ['results']

print fetchtweets("cheese", "6")

