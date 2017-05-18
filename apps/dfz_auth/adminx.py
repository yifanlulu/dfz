#encoding: utf-8

import xadmin
from .models import DFZUser

class UserAdmin(object):
    list_display = ['username','telephone','email','is_active','is_staff']
    show_detail_fields = ['username']



xadmin.sites.site.unregister(DFZUser)
xadmin.sites.site.register(DFZUser,UserAdmin)
