#encoding: utf-8

from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.payinfo_list,name='index'),
]