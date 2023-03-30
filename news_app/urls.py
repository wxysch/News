from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('detail/<int:id>',views.news_detail,name='news_detail'),
    path('about/',views.about,name='about'),
]
