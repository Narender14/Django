from pprint import pprint
import json
with open("test.json",  'r+') as file:
    for line in file:
        try:
            tweet = json.loads(line)
            print(tweet["text"])
            print(tweet["user"]["screen_name"])
            print(tweet["retweet_count"])
            print(tweet["favorite_count"])
            print(tweet["lang"])
            print(tweet["followers_count"])
            print(tweet["user"]["user_mentions"])
            print(tweet["user"]["urls"])
            print(tweet["created_at"]) #Sun Feb 18 12:04:03 +0000 2018
        except:
            continue