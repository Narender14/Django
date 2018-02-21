from django.db import models

# Create your models here.
from mongoengine import *
from mongoengine import *
connect('twitter', host='localhost', port=27017)


class Tweet(Document):

    id_str = StringField(max_length=50)
    time_stamp = StringField(max_length=50)
    created_time = DateTimeField(max_length=50)
    text = StringField(max_length=50)
    screen_name = StringField(max_length=50)
    retweet_count = IntField(default=0)
    favorite_count = IntField(default=0)
    lang = StringField(max_length=50)
    followers_count = IntField(default=0)
    user_mentions = StringField(max_length=50)
    urls = StringField(max_length=50)

    meta = {'collection': 'tweet'}

