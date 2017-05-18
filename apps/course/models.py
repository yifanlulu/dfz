#encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoQiniu.models import QiniuField
from dfz_auth.models import DFZUser

class Teacher(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'讲师名')
    identity = models.CharField(max_length=100,verbose_name=u'身份')
    profile = UEditorField(verbose_name=u'简介',width=600,height=300,null=True,blank=True,toolbars='mini',imagePath='images/')
    avatar = QiniuField(verbose_name=u'头像地址',file_type='image',qiniu_field=u'avatar')

    def __unicode__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'讲师'
        verbose_name_plural = verbose_name

class CourseCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name=u'分类名称')

    def __unicode__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'课程分类'
        verbose_name_plural = verbose_name

class Course(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    thumbnail = QiniuField(verbose_name=u'缩略图',qiniu_field=u'thumbnail',file_type='image')
    video_url = models.URLField(verbose_name=u'视频地址')
    duration = models.CharField(verbose_name=u'时长',max_length=10)
    create_time = models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
    profile = UEditorField(verbose_name=u'课程简介',toolbars='mini')
    outline = UEditorField(verbose_name=u'课程大纲',toolbars='mini',null=True,blank=True)
    audience = UEditorField(null=True,blank=True,verbose_name=u'适宜人群',toolbars='mini')
    price = models.FloatField(verbose_name=u'价格', default=0)
    teacher = models.ForeignKey(Teacher,verbose_name=u'讲师')
    category = models.ForeignKey(CourseCategory,verbose_name=u'分类')

    def __unicode__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name


class SeriesCourse(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    courses = models.ManyToManyField(Course,verbose_name=u'所有课程')
    price = models.FloatField(verbose_name=u'价格',default=0)
    duration = models.FloatField(verbose_name=u'时长',null=True)
    create_time = models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
    course_num = models.IntegerField(verbose_name=u'课程数量',null=True)
    teacher = models.ForeignKey(Teacher,verbose_name=u'讲师')

    def __unicode__(self):
        return self.title.encode('utf-8')

    class Meta:
        verbose_name = u'系列课程'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(DFZUser,verbose_name=u'用户')
    course = models.ForeignKey(Course,verbose_name=u'课程')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'购买时间')

    def __unicode__(self):
        return self.user.username + '-' + self.course.title

    class Meta:
        verbose_name = u'购买课程记录'
        verbose_name_plural = verbose_name

class UserSeriesCourse(models.Model):
    user = models.ForeignKey(DFZUser,verbose_name=u'用户')
    series_course = models.ForeignKey(SeriesCourse,verbose_name=u'系列课程')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u'购买时间')

    def __unicode__(self):
        return self.user.username + '-' + self.series_course.title

    class Meta:
        verbose_name = u'购买系列课程记录'
        verbose_name_plural = verbose_name








