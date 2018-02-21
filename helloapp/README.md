# Django

##System Requirement

1. It uses MongoDB with mongoengine
2. Django Restframework
3. Python 3

MongoDB version - 3.2.19
MongoEngine version - 0.15.0
Django Version - 2.0.2
djangorestframework - 3.7.7
tweepy==3.5.0


There are 4 end-points present.
1. user - It allows to fetch the date of user whose screen_name startswith = "screen_name_start".
2. date - It allows to fetch the date with in range of date.
3. tweettext - It allows twitter text search by including single word which is searched in text.
4. group - It allows groupby language ('en', 'hi')

The filters supported are :

1. followers_count, favorite_count, retweet_count
2. screen_name, lang
3. date range

It also allows the option to download the .csv file.

##Example
USER API

1. **http://localhost:8000/user/RAJENDERPra/0/0/0/RAJENDERPrash10/en/2018-02-17/2018-02-19**
    - The parameter order are :
        -> screen_name_start, follower, retweet_count, favorite_count, screen_name, lang, start_date, end_date, is_csv.
    - Only *screen_name_start* is compulsary other paraters are all optional
    - For saving the result in .csv,  add csv behind the querey.
        -> **http://localhost:8000/user/RAJENDERPra/0/0/0/RAJENDERPrash10/en/2018-02-17/2018-02-19/csv**

DATE API

2. **http://localhost:8000/date/2018-02-17/2018-02-19/0/0/0/RAJENDERPrash10/en**
    - The parameter order are :
        -> start_date, end_date, follower, retweet_count, favorite_count, screen_name, lang, is_csv.
    - Only *start_date* is compulsary other paraters are all optional.
    - For saving the result in .csv,  add csv behind the querey.
        -> **http://localhost:8000/date/2018-02-17/2018-02-19/0/0/0/RAJENDERPrash10/en/csv**

TWEET TEXT API

3. **http://localhost:8000/tweettext/India/2018-02-17/2018-02-19/0/0/0/RAJENDERPrash10/en/**
    - The parameter order are :
        -> search_text, start_date, end_date, follower, retweet_count, favorite_count, screen_name, lang, is_csv
    - Only *search_text* is compulsary other paraters are all optional.
    - For saving the result in .csv,  add csv behind the querey.
        -> **http://localhost:8000/tweettext/India/2018-02-17/2018-02-19/0/0/0/RAJENDERPrash10/en/csv**

GROUP BY LANG

4. **http://localhost:8000/group/en/**
    - The parameter order are :
        -> lang, is_csv
    - Only *lang* is compulsary other paraters are all optional.
    - For saving the result in .csv,  add csv behind the querey.
        -> **http://localhost:8000/group/en/csv**

