#encoding: utf-8

from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^list/$',views.news_list,name='list'),
    url(r'^detail/(?P<news_id>\d+)/$', views.news_detail,name='detail'),
]
