from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    settings = Setting.objects.latest('id')
    news  = News.objects.all()
    context = {
        'setting' : settings,
        'news' : news
    }
    return render(request, 'index.html',context)

def news_detail(request,id):
    settings = Setting.objects.latest('id')
    news = News.objects.get(id=id)
    context = {
        'settings' : settings,
        'news' : news,
    }
    return render(request,'single.html',context)