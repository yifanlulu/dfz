#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from dfz_auth.models import DFZUser
from frontuser.models import FrontUser
from DjangoUeditor.models import UEditorField

class News(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=200)
    content = UEditorField(verbose_name=u'内容',width=700,height=500)
    desc = models.CharField(max_length=200,verbose_name=u'简短描述')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发表时间')
    thumbnail = models.URLField(verbose_name=u'缩略图')
    author = models.ForeignKey(DFZUser,verbose_name=u'作者')
    category = models.ForeignKey('NewsCategory',verbose_name=u'分类')

    def __unicode__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'新闻'
        verbose_name_plural = verbose_name


class NewsCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'类名')

    def __unicode__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'新闻分类'
        verbose_name_plural = verbose_name


class NewsComment(models.Model):
    content = models.TextField(verbose_name=u'内容')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发表时间')
    author = models.ForeignKey(FrontUser,verbose_name=u'作者')
    news = models.ForeignKey(News,verbose_name=u'新闻')

    class Meta:
        verbose_name = u'新闻评论'
        verbose_name_plural = verbose_name

class Banner(models.Model):
    title = models.CharField(verbose_name=u'标题',max_length=100)
    thumbnail = models.URLField(max_length=100,verbose_name=u'缩略图')
    link_to = models.URLField(max_length=100,verbose_name=u'跳转到')
    index = models.SmallIntegerField(unique=True,verbose_name=u'位置')

    def __unicode__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

