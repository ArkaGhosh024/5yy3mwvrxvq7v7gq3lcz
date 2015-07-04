'''
Created on 02-Jul-2015

@author: acer
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'activityschedule/$', views.activityschedule, name="activity schedule")
]