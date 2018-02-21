from django.urls import path, re_path

from . import views
from django.conf.urls import url

urlpatterns = [

    # FOR USER PART
    url(r'^user/(?P<screen_name_start>\w+)?/?(?P<follower>[0-9]+)?/?(?P<retweet_count>[0-9]+)?/?(?P<favorite_count>[0-9]+)?/?(?P<screen_name>\w+)?'
        r'/?(?P<lang>\w+)?/?(?P<start_date>\d{4}-\d{2}-\d{2})?/?(?P<end_date>\d{4}-\d{2}-\d{2})?/?(?P<is_csv>csv)?$', views.user),

    # FOR DATE PART
    url(r'^date/(?P<start_date>\d{4}-\d{2}-\d{2})?/?(?P<end_date>\d{4}-\d{2}-\d{2})?/?(?P<follower>[0-9]+)?/?(?P<retweet_count>[0-9]+)?/?(?P<favorite_count>[0-9]+)?/?(?P<screen_name>\w+)?'
        r'/?(?P<lang>\w+)?/?(?P<is_csv>csv)?$', views.date),

    # FOR Tweet Text Search PART
    url(r'^tweettext/(?P<search_text>\w+)?/?(?P<start_date>\d{4}-\d{2}-\d{2})?/?(?P<end_date>\d{4}-\d{2}-\d{2})?/?(?P<follower>[0-9]+)?'
        r'/?(?P<retweet_count>[0-9]+)?/?(?P<favorite_count>[0-9]+)?/?(?P<screen_name>\w+)?'
        r'/?(?P<lang>\w+)?/?(?P<is_csv>csv)?$', views.tweettext),

    # FOR groupby language PART
    #url(r'^group/(?P<lang>\w+)/$', views.groupby),
    url(r'^group/(?P<lang>\w+)?/?(?P<is_csv>csv)?$', views.groupby),

]
