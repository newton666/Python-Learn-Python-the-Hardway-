import urllib2
import json
response = urllib2.urlopen('http://search.twitter.com/search.json?q=python&rpp=50')
raw_data = response.read()



data = json.loads(raw_data)
print(data['query'])

wanted = "mrmdesai"

tweets = data['results']

all_words = []
for tweet in tweets:
	words = tweet["text"].split(" ")
	for word in words:
		all_words.append(word)


hashtags = []
for word in all_words:
	if word.startswith("#"):
		hashtags.append(word)

hashtag_stats = {}
for hashtag in hashtags:
	if hashtag in hashtag_stats:
		old_value = hashtag_stats[hashtag]
		hashtag_stats[hashtag] = old_value + 1
	else:
		hashtag_stats[hashtag] = 1

word.lower()

print word