import os

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USER = os.getenv('MONGO_USER', '')
MONGO_PASS = os.getenv('MONGO_PASS', '')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'twitter')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'tweet')

#Twitter API credentials
consumer_key = "c_key"
consumer_secret = "c_s"
access_key = "a_key"
access_secret = "a_s"
