from django.shortcuts import render
import datetime
# Create your views here.
from .models import Tweet
from django.http import HttpResponse
from .models import Tweet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv


@api_view(['GET'])
def user(request, screen_name_start, follower=None, retweet_count=None, favorite_count=None, screen_name=None, lang=None, start_date=None, end_date=None, is_csv=None):

    filter_final = Tweet.objects.filter(screen_name__startswith=screen_name_start)

    if follower is not None:
        filter_final = filter_final.filter(followers_count__gte=int(follower))
    if retweet_count is not None:
        filter_final = filter_final.filter(retweet_count__gte=int(retweet_count))
    if favorite_count is not None:
        filter_final = filter_final.filter(favorite_count__gte=int(favorite_count))
    if screen_name is not None:
        filter_final = filter_final.filter(screen_name=screen_name)
    if lang is not None:
        filter_final = filter_final.filter(lang=lang)
    if start_date is not None:
        filter_final = Tweet.objects.filter(created_time__gte=start_date)
    if end_date is not None:
        end = datetime.datetime(*map(int, end_date.split('-')))
        filter_final = filter_final.filter(created_time__lte=end)

    if is_csv is None:
        filter_final = filter_final.values_list('screen_name', 'followers_count')
        return Response(data=filter_final,  status=status.HTTP_200_OK)
    else:
        response = HttpResponse(filter_final, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=user.csv'
        writer = csv.writer(response, delimiter='\t')
        writer.writerow("\n")
        for item in filter_final:
            result = item.screen_name, item.followers_count, item.created_time, str(item.text)
            writer.writerow(result)
            writer.writerow("\n")
        return response


@api_view(['GET'])
def date(request, start_date, end_date=None, follower=None, retweet_count=None, favorite_count=None, screen_name=None, lang=None, is_csv=None):

    start = datetime.datetime(*map(int, start_date.split('-')))
    filter_final = Tweet.objects.filter(created_time__gte=start)

    if end_date is not None:
        end = datetime.datetime(*map(int, end_date.split('-')))
        filter_final = filter_final.filter(created_time__lte=end)
    if follower is not None:
        filter_final = filter_final.filter(followers_count__gte=int(follower))
    if retweet_count is not None:
        filter_final = filter_final.filter(retweet_count__gte=int(retweet_count))
    if favorite_count is not None:
        filter_final = filter_final.filter(favorite_count__gte=int(favorite_count))
    if screen_name is not None:
        filter_final = filter_final.filter(screen_name=screen_name)
    if lang is not None:
        filter_final = filter_final.filter(lang=lang)
    print("here")
    print(is_csv)
    print("there")
    if is_csv is None:
        filter_final = filter_final.values_list('screen_name', 'followers_count')
        return Response(data=filter_final,  status=status.HTTP_200_OK)
    else:
        response = HttpResponse(filter_final, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=date.csv'
        writer = csv.writer(response, delimiter='\t')
        writer.writerow("\n")
        for item in filter_final:
            result = item.screen_name, item.followers_count, item.created_time, str(item.text)
            writer.writerow(result)
            writer.writerow("\n")
        return response


@api_view(['GET'])
def tweettext(request, search_text, start_date=None, end_date=None, follower=None, retweet_count=None, favorite_count=None, screen_name=None, lang=None, is_csv=None):

    filter_final = Tweet.objects.filter(text__contains=search_text).values_list('followers_count', 'retweet_count')
    if start_date is not None:
        filter_final = Tweet.objects.filter(created_time__gte=start_date)
    if end_date is not None:
        end = datetime.datetime(*map(int, end_date.split('-')))
        filter_final = filter_final.filter(created_time__lte=end)
    if follower is not None:
        filter_final = filter_final.filter(followers_count__gte=int(follower))
    if retweet_count is not None:
        filter_final = filter_final.filter(retweet_count__gte=int(retweet_count))
    if favorite_count is not None:
        filter_final = filter_final.filter(favorite_count__gte=int(favorite_count))
    if screen_name is not None:
        filter_final = filter_final.filter(screen_name=screen_name)
    if lang is not None:
        filter_final = filter_final.filter(lang=lang)

    if is_csv is None:
        filter_final = filter_final.values_list('screen_name', 'followers_count')
        return Response(data=filter_final,  status=status.HTTP_200_OK)
    else:
        response = HttpResponse(filter_final, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=tweettext.csv'
        writer = csv.writer(response, delimiter='\t')
        writer.writerow("\n")
        for item in filter_final:
            result = item.screen_name, item.followers_count, item.created_time, str(item.text)
            writer.writerow(result)
            writer.writerow("\n")
        return response


@api_view(['GET'])
def groupby(request, lang, is_csv=None):

    filter_final = Tweet.objects.filter(lang=lang).aggregate({'$group': {'_id': '$lang', 'lang': {'$push': {'retweet': '$retweet_count', 'screen': '$screen_name'}}}})

    if is_csv is None:
        return Response(data=filter_final, status=status.HTTP_200_OK)
    else:
        response = HttpResponse(filter_final, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=group_by.csv'
        writer = csv.writer(response, delimiter='\t')
        writer.writerow("\n")
        for item in filter_final:
            result = item.screen_name, item.followers_count, item.created_time, str(item.text)
            writer.writerow(result)
            writer.writerow("\n")
        return response
