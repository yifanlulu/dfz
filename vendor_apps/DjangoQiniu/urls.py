#coding: utf8

from django.conf.urls import url
from .views import qiniu_token

urlpatterns = [
    url(r'qiniu_token/',qiniu_token,name='qiniu_token')
]