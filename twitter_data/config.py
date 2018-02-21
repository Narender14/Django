import os

MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = os.getenv('MONGO_PORT', 27017)
MONGO_USER = os.getenv('MONGO_USER', '')
MONGO_PASS = os.getenv('MONGO_PASS', '')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'twitter')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'tweet')

# Twitter API credentials
consumer_key = "yYaDlzvkMzxsPQq3aKvPLu8jm"
consumer_secret = "UVGdDqVxYkprPKvluMq3ArUrLlwPXd8wZ1AnNIoUl5HX5IVUea"
access_key = "1178472560-vVakpXvCgjzij4IXnjtBGRjUhHm3tvQzlZXYhNa"
access_secret = "f7tMZ63aouT6paK2yAk3310a5ukw000sUv1VOH96uQyaH"