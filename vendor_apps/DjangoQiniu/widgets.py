#coding: utf8

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.conf import settings

class QiniuWidget(forms.TextInput):

    def __init__(self,*args,**kwargs):
        self.btn_title = kwargs.pop('btn_title')
        self.qiniu_field = kwargs.pop('qiniu_field')
        self.file_type = kwargs.pop('file_type')
        super(QiniuWidget,self).__init__(*args,**kwargs)

    def render(self, name, value,attrs=None):
        context = {
            'qiniu_domain': settings.QINIU_DOMAIN,
            'qiniu_field_name': self.qiniu_field,
            'qiniu_field_value': value or '',
            'btn_title':self.btn_title,
            'file_type': self.file_type
        }
        return mark_safe(render_to_string('qiniu.html',context=context))

    def value_from_datadict(self, data, files, name):
        return data.get(name)