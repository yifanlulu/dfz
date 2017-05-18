#encoding: utf-8

import xadmin
from .models import News,NewsCategory,NewsComment
from .models import Banner

class NewsAdmin(object):
    list_display = ['title','create_time','author','category']
    style_fields = {
        'content': 'ueditor'
    }


class NewsCategoryAdmin(object):
    pass

class NewsCommentAdmin(object):
    list_display = ['content','create_time','author','news']

class BannerAdmin(object):
    list_display = ['title','link_to','index']
    list_editable = ['index']


xadmin.sites.site.register(News,NewsAdmin)
xadmin.sites.site.register(NewsCategory,NewsCategoryAdmin)
xadmin.sites.site.register(NewsComment,NewsCommentAdmin)
xadmin.sites.site.register(Banner,BannerAdmin)