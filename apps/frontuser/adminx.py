#encoding: utf-8

import xadmin
from .models import FrontUser

class FrontUserAdmin(object):
    list_display = ['username','telephone','email']
    show_detail_fields = ['username']

xadmin.sites.site.register(FrontUser,FrontUserAdmin)
