from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def index(request):
    settings = Setting.objects.latest('id')
    news  = News.objects.all()
    podcasts = Podcast.objects.all()
    addverts = Addvert.objects.all()
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'setting' : settings,
        'news' : news,
        'podcasts' : podcasts,
        'addverts': addverts,
        'page_obj': page_obj,
    }
    return render(request, 'index.html',context)

def news_detail(request,id):
    settings = Setting.objects.latest('id')
    news = News.objects.get(id=id)
    context = {
        'settings' : settings,
        'new' : news,
    }
    return render(request,'single.html',context)

def about(request):
    abouts = About.objects.all()
    context = {
        'abouts': abouts,
    }
    return render(request, 'about.html',context)