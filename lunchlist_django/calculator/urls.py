#!/usr/bin/env python3
#antuor:Alan

from  django.conf.urls import url
from calculator import views

urlpatterns = [
    #url(r'^$',views.index,name = 'index'), #As of Django 1.10, the patterns module has been removed (it had been deprecated since 1.8).

    #url(r'^index/$',views.index,name='index'),
     url(r'^summit/$',views.summit,name='summit'),
           ]