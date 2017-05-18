#encoding: utf-8

from django.shortcuts import render,HttpResponse
from .models import Banner,NewsCategory,News
from django.conf import settings
from utils import hyjson

def index(request):
    context = {
        'banners': Banner.objects.order_by('index').all(),
        'categories': NewsCategory.objects.all(),
        'newses': News.objects.order_by('-create_time').all()[0:settings.COUNT_PER_PAGE]
    }
    return render(request,'news/index.html',context)

def news_list(request):
    category_id = int(request.GET.get('c'),0)
    page = int(request.GET.get('p'),0)
    start = settings.COUNT_PER_PAGE * page
    end = start + settings.COUNT_PER_PAGE
    newses = None
    # 如果category_id为0，则选择所有的，并按照时间倒序排序
    if category_id == 0:
        newses = News.objects.order_by('-create_time')[start:end].values()
    else:
        newses = News.objects.order_by('-create_time').filter(category__id=category_id)[start:end].values()

    context = {
        'newses': list(newses)
    }
    return hyjson.json_result(data=context)


def news_detail(request,news_id):
    context = {
        'news': News.objects.filter(pk=news_id).first()
    }
    return render(request,'news/news_detail.html',context)

def search(request):
    return render(request,'search/search.html')