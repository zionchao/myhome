#coding:utf-8
"""myhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#-*-coding:utf-8-*-
from django.conf.urls import patterns,include, url
from django.contrib import admin
from article.views import RSSFeed

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home',name='home'),
    url(r'^about/$','article.views.about',name="about"),
    url(r'^message/$','article.views.message',name="message"),
    url(r'^archive/$','article.views.archive',name="archive"),
    url(r'^feed/$', RSSFeed(), name = "RSS"),

    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<id>\d+)/$', 'article.views.detail', name="detail"),#每篇文章
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{1,2})/$','article.views.archive_month',name="archive_month"),#按月归档
    url(r'^articleClassfi/(?P<classfi>\w+)/$', 'article.views.classfiDetail', name="classfiDetail"),#每个分类页下面的文章
    url(r'^articleTag/(?P<tag>\w+)/$', 'article.views.tagDetail', name="tagDetail"),#每个标签页下面的文章
]
