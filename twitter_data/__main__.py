# This handles Twitter authetification and the connection to Twitter Streaming API
from . import twitter_streaming
from . import config
from tweepy import OAuthHandler
from tweepy import Stream
obj = twitter_streaming.StdOutListener()

auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_key, config.access_secret)
stream = Stream(auth, obj)

# This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
# stream.filter(track=['python', 'javascript', 'ruby'])
stream.filter(track=['TajMahal'])