#encoding: utf-8


import xadmin
from .models import Course,CourseCategory,Teacher,SeriesCourse



class CourseAdmin(object):
    list_display = ['title','create_time','price','teacher']
    search_fields = ['title']
    style_fields = {
        'profile': 'ueditor',
        'audience': 'ueditor',
        'outline': 'ueditor'
    }
    form_layout = [
        'title','thumbnail','price','video_url','duration','teacher','category','profile','outline','audience'
    ]

class CourseCategoryAdmin(object):
    list_display = ['name']
    list_editable = ['name']

class TeacherAdmin(object):
    list_display = ['name','identity']
    search_fields = ['name']

    style_fields = {
        'profile': 'ueditor'
    }

    form_layout = [
        'name','identity','avatar','profile'
    ]

class SeriesCourseAdmin(object):
    list_display = ['title','price','courses']

xadmin.sites.site.register(Course,CourseAdmin)
xadmin.sites.site.register(CourseCategory,CourseCategoryAdmin)
xadmin.sites.site.register(Teacher,TeacherAdmin)
xadmin.sites.site.register(SeriesCourse,SeriesCourseAdmin)

