from django.conf.urls import url
from . import views
from django.shortcuts import render

#importing Django's function url and all of our views from the blog application.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]