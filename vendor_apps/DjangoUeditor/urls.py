#coding:utf-8
from django.conf.urls import url

from views import get_ueditor_controller

urlpatterns = [
    url(r'^controller/$',get_ueditor_controller),
]