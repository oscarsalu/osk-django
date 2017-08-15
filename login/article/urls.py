from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^all/$', views.articles),
    # url(r'^hello/$', views.hello),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    url(r'^create/$', views.create),
]
