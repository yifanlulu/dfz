#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.hashers import make_password,check_password


class FrontUser(models.Model):
    username = models.CharField(max_length=50)
    telephone = models.CharField(max_length=11)
    _password = models.CharField(max_length=100)

    email = models.EmailField(max_length=100,null=True,blank=True)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_pwd):
        self._password = make_password(raw_pwd)

    def check_password(self,raw_pwd):
        return check_password(raw_pwd,self._password)

    @classmethod
    def authenticate(self,telephone,password):
        user = FrontUser.objects.filter(telephone=telephone).first()
        if user and user.check_password(password):
            return user
        else:
            return None

    def __unicode__(self):
        return self.username.encode('utf-8')

    class Meta:
        verbose_name = u'前台用户'
        verbose_name_plural = verbose_name
