from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from tweets.twitter import get_tweets
import json

def home(request):
    return render(request, 'tweets/index.html')
def results(request):
    tweet=None
    a=request.POST.get(str('twitter_id'))
    tweet=get_tweets(a)
    return render(request, 'tweets/results.html',{'datas':tweet,'twitter_id':a})

