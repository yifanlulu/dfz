"""dfz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from news import views
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^qiniu/',include('DjangoQiniu.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^$',views.index),
    url(r'^search/$',views.search,name='search'),
    url(r'^news/',include('news.urls',namespace='news')),
    url(r'^course/',include('course.urls',namespace='course')),
    url(r'^payinfo/',include('payinfo.urls',namespace='payinfo')),
    url(r'account/',include('frontuser.urls',namespace='account'))
]
