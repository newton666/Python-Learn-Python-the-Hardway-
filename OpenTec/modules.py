import urllib2
import json
response = urllib2.urlopen('http://search.twitter.com/search.json?q=python&rpp=50')
raw_data = response.read()



data = json.loads(raw_data)
print(data['query'])

wanted = "mrmdesai"

tweets = data['results'
]#for tweet in tweets:	
#	if tweet['from_user'] == wanted:
#		print (tweet['from_user'])
#	else :
#		print "Didn't find anything."

num_links = 0
for tweet in tweets:
	if "http" in tweet["text"]:
		num_links += 1


print num_links
