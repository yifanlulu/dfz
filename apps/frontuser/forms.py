#encoding: utf-8

from django import forms
import re
from utils.captcha.hycaptcha import Captcha


class LoginForm(forms.Form):
    telephone = forms.CharField(required=True,max_length=11,min_length=11)
    password = forms.CharField(required=True)
    remember = forms.BooleanField(required=False)


class RegistForm(forms.Form):
    telephone = forms.CharField(required=True,max_length=11,min_length=11)
    username = forms.CharField(required=True)
    password1 = forms.CharField(required=True)
    password2 = forms.CharField(required=True)
    graph_captcha = forms.CharField(required=True)
    sms_captcha = forms.CharField(required=True)

    def clean_password1(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError(u'两次密码不一致！',code='password1')
        else:
            return p1

    def clean_telephone(self):
        # 手机号验证
        telephone = self.cleaned_data['telephone']
        p = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        if p.match(telephone):
            # 这里还能返回外键
            return telephone
        raise forms.ValidationError(u'手机号码格式不对！', code='telephone')

    def clean_graph_captcha(self):
        graph_captcha = self.cleaned_data.get('graph_captcha')
        if not Captcha.check_captcha(graph_captcha):
            raise forms.ValidationError(u'图形验证码错误！',code='graph_captcha')


    def clean_sms_captcha(self):
        sms_captcha = self.cleaned_data.get('sms_captcha')
        if not Captcha.check_captcha(sms_captcha):
            raise forms.ValidationError(u'短信验证码错误！',code='sms_captcha')

