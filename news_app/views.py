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