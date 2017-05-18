#encoding: utf-8


from django.conf.urls import url,include
import views

urlpatterns = [
    url(r'^$', views.course_list,name='index'),
    url(r'^detail/(?P<course_id>\d+)/$', views.course_detail,name='detail'),
]