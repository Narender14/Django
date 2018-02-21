from tweepy.streaming import StreamListener
import tweepy
from pymongo import MongoClient
import datetime
import json

#This is a basic listener that just prints received tweets to stdout.

class StdOutListener(tweepy.StreamListener):

    def __init__(self, db_host='localhost', db_port=27017, db_database='twitter', db_collection='tweet'):
        super(tweepy.StreamListener, self).__init__()
        self.db = MongoClient(db_host, db_port)
        self.collection = self.db[db_database][db_collection]

    def on_data(self, data):

        tweet = json.loads(data)

        id_str = tweet["id_str"]
        time_stamp = tweet["created_at"]
        created_time = datetime.datetime.strptime(time_stamp, '%a %b %d %H:%M:%S +0000 %Y')
        text = tweet["text"]
        screen_name = tweet["user"]["screen_name"]
        retweet_count = tweet["retweet_count"]
        favorite_count = tweet["favorite_count"]
        lang = tweet["lang"]
        followers_count = tweet["user"]["followers_count"]
        user_mentions = tweet["entities"]["user_mentions"]
        urls = tweet["entities"]["urls"]

        self.collection.insert(
                    {"_id": id_str,
                    "created_time": created_time,
                     "text":text,
                     "screen_name":screen_name,
                     "retweet_count":retweet_count,
                     "favorite_count":favorite_count,
                     "lang":lang,
                     "followers_count":followers_count,
                     "user_mentions":user_mentions,
                     "urls":urls
                    })

        print("Successfull")
        return True

    def on_error(self, status):
        print(status)

'''
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(track=['TajMahal'])
'''