# Django

##System Requirement

1. It twitter streaming API.
2. Pymongo client for Connecting to MongoDB
3. Python 3


1. MongoDB version - 3.2.19
2. tweepy - 3.5.0
3. pymongo - 3.6.0

The configuration values are defined in the **config.py** file like Mongo Host, Port, Collection, DB name, twitter keys.

It will fetch the data and store into MongoDB. It structure of data storage is:

-              * {
                "_id": id_str,
                "created_time": created_time,
                "text":text,
                "screen_name":screen_name,
                "retweet_count":retweet_count,
                "favorite_count":favorite_count,
                "lang":lang,
                "followers_count":followers_count,
                "user_mentions":user_mentions,
                "urls":urls
                }*

The twitter module can be run :
- **python3 -m twitter_data**
