#encoding: utf-8

from xadmin import Settings
from course.models import Course,Teacher
from dfz_auth.models import DFZUser
from news.models import News,NewsComment
from payinfo.models import Payinfo

class Base(Settings):
    # 是否开启更新主题的功能
    enable_themes = True
    # 是否开启远程查看主题的功能
    use_bootswatch = True

class Comm(Settings):
    # 左边的菜单的风格，default/accordion
    menu_style = 'default'
    site_title = u'大饭桌后台管理系统'
    site_footer = u'北京大饭桌科技有限公司'
    global_search_models = [Course]
    apps_label_title = {
        'course': u'课程',
        'news': u'新闻',
        'payinfo': u'付费资讯',
        'dfz_auth': u'用户',
        'reversion': u'版本回退',
        'frontuser': u'前台用户',
        'banner': u'轮播图'
    }


