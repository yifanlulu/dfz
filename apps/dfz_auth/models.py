#encoding: utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractUser


class DFZUser(AbstractUser):
    telephone = models.CharField(max_length=11)


    def __unicode__(self):
        return self.username.encode('utf-8')

    class Meta:
        verbose_name = u'后台用户'
        verbose_name_plural = verbose_name