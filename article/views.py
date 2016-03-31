#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,Http404
from models import Article,Classification,Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.syndication.views import Feed
import json
from django.core import serializers
# Create your views here.

def home(request):
    is_home=True
    articles=Article.objects.all()
    paginator=Paginator(articles,6)
    page_num=request.GET.get('page')
    try:
        articles=paginator.page(page_num)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)

    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)

    date_list=Article.date_list.get_Article_onDate()
    return render(request,'index.html',locals())
    # return render_to_response('index.html',
    #         locals(), #它返回的字典对所有局部变量的名称与值进行映射。
    #         context_instance=RequestContext(request))


def detail(request,year,month,day,id):
    try:
        article=Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()

    return render(request,'content.html',locals())

def archive_month(request,year,month):
    is_arch_month=True
    articles=Article.objects.filter(publish_time__year=year).fileter(publish_time__month=month)
    paginator=Paginator(articles,6)
    page_num=request.GET.get('page')
    date_list=Article.date_list.get_Article_onDate()
    try:
        articles=paginator.page(page_num)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)

    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    return render(request,'index.html',locals())

def classfiDetail(request,classfi):
    is_classfi=True
    temp=Classification.objects.get(name=classfi)
    articles=temp.article_set.all()
    paginator=Paginator(articles,6)
    page_num=request.GET.get('page')
    try:
        articles=paginator.page(page_num)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()

    return render(request,'index.html',locals())

def tagDetail(request,tag):
    is_tag=True
    temp=Tag.objects.get(name=tag)
    articles=temp.article_set.all()
    paginator=Paginator(articles,6)
    page_num=request.GET.get('page')
    try:
        articles=paginator.page(page_num)
    except PageNotAnInteger:
        articles=paginator.page(1)
    except EmptyPage:
        articles=paginator.page(paginator.num_pages)
    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()
    return render(request,'index.html',locals())
	
def about(request):
    classfication=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()
    return render(request,'about.html',locals())
	
def archive(request):
    archive=Article.date_list.get_Article_OnArchive()
    ar_newpost=Article.objects.order_by('-publis_time')[:10]
    classfication=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()
    return render(request,'archive.html',locals())
	
class RSSFeed(Feed):
    title='RSS feed - zionchao'
    link="feeds/posts/"
    description="RSS Feed -blog posts"

    def items(self):
        return Article.objects.order_by('-publish_time')

    def item_title(self,item):
        return item.title

    def item_pubdate(self,item):
        return item.publish_time

    def item_description(self,item):
        return item.content
		
def blog_search(request):
    is_search=True
    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()
    error=False
    if 's' in request.GET:
        s=request.GET['s']
        if not s:
            return render(request,'index.html')
        else:
            articles=Article.objects.filter(title__icontains=s)
            if len(articles)==0:
                error=True
	return render(request,'index.html',locals())
	
def message(request):
    classification=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()
    return render(request,'message.html',locals())