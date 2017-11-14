import csv
import json
import sys

pagename = sys.argv[1]

with open('timeline.json') as f:
    tweets = json.loads(f.read())

tweet = tweets[0]

fields = ['retweetCount', 'favoriteCount', 'text','time']

with open(pagename + '-tweets.csv', 'w') as csvfile:
    fieldnames = ['retweetCount', 'favoriteCount', 'text','time']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for tweet in tweets:
        writer.writerow([tweet[field] for field in fields])
