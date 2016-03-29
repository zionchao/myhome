#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse,Http404
from models import Article,Classification,Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import json
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

    classfication=Classification.class_list.get_Class_list()
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
    classfication=Classification.class_list.get_Class_list()
    tagCloud=json.dumps(Tag.tag_list.get_Tag_list(),ensure_ascii=False)
    date_list=Article.date_list.get_Article_onDate()

    return render(request,'content,html',locals())

def archive_month(request,year,month):
    is_arch_month=True
    articles=Article.objects.filter(publish_time__year=year).fileter(publish_time__month=month)
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
    return render(request,'inddex.html',locals())

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
    classfication=Classification.class_list.get_Class_list()
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




