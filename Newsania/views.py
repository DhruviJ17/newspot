from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
from .forms import *
import requests

def home(request):
    context = {}
    return render(request, 'Newsania/main.html', context)

def News(request):
    res = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=3a523cd35bc44d258e911e25cc27596d').json()
    publishers_list = []
    titles_list = []
    description_list = []
    image_list = []
    for i in res['articles']:
        publishers_list.append(i['source'])
        titles_list.append(i['title'])
        description_list.append(i['description'])
        image_list.append(i['urlToImage'])
    newws = zip(publishers_list, titles_list, description_list, image_list)
    context ={'newws': newws}
    return render(request, 'Newsania/all.html', context)


def Title(request):
    res = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=3a523cd35bc44d258e911e25cc27596d').json()
    titles_list = []
    for i in res['articles']:
        titles_list.append(i['title'])
        titles = len(titles_list)
    context = {'titles': titles_list}
    return render(request, 'Newsania/title.html', context)

def Image(request):
    res = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=3a523cd35bc44d258e911e25cc27596d').json()
    images_list = []
    for i in res['articles']:
        images_list.append(i['urlToImage'])
        images = len(images_list)
    context = {'images': images_list}
    return render(request, 'Newsania/image.html', context)








