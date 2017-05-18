#encoding: utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$',views.LoginView.as_view(),name='login'),
    url(r'^regist/$',views.RegistView.as_view(),name='regist'),
    url(r'^graph_captcha/$',views.graph_captcha,name='graph_captcha'),
    url(r'^sms_captcha/$',views.sms_captcha,name='sms_captcha'),
]