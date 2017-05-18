#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from dfz_auth.models import DFZUser

class PayinfoCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'分类名')

    def __unicode__(self):
        return self.name.decode('utf-8')

    class Meta:
        verbose_name = u'付费资讯分类'
        verbose_name_plural = verbose_name


class Payinfo(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'资讯名称')
    profile = models.TextField(verbose_name=u'资讯简介')
    price = models.FloatField(verbose_name=u'价格(元/次)',default=0)
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发布时间')
    category = models.ForeignKey(PayinfoCategory,verbose_name=u'分类')

    def __unicode__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'付费资讯'
        verbose_name_plural = verbose_name


class UserPayinfo(models.Model):
    user = models.ForeignKey(DFZUser,verbose_name=u'用户')
    payinfo = models.ForeignKey(Payinfo,verbose_name=u'资讯')
    create_time = models.DateTimeField(verbose_name=u'购买时间',auto_now_add=True)

    def __unicode__(self):
        return (self.user.username + '-' + self.payinfo.title).encode('utf-8')

    class Meta:
        verbose_name = u'资讯购买记录'
        verbose_name_plural = verbose_name
