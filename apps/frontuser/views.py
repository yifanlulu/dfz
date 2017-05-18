#encoding: utf-8
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views.generic.base import View
from .forms import LoginForm,RegistForm
from .models import FrontUser
from django.conf import settings
from utils.captcha.hycaptcha import Captcha
from utils import hyjson,hycache
from django.conf import settings
import top
try:
    from StringIO import StringIO
except:
    from io import BytesIO as StringIO

class LoginView(View):

    def get(self,request,message=None):
        return render(request,'account/login.html',context={'message':message})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = FrontUser.authenticate(telephone,password)
            if user:
                request.session[settings.FRONT_SESSION_KEY] = user.id
                if not remember:
                    # 默认如果不设置过期时间，那么将在2个星期后过期。
                    # 如果设置了过期时间未0，则浏览器一旦关闭就会过期
                    request.session.set_expiry(0)
                return HttpResponseRedirect('news:index')
            else:
                return self.get(request,u'用户名或密码错误！')
        else:
            return self.get(request,form.errors)


class RegistView(View):

    def get(self,request,message=None):
        return render(request,'account/regist.html',context={'message':message})

    def post(self,request):
        form = RegistForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = FrontUser(telephone=telephone,password=password,username=username)
            user.save()
            return hyjson.json_result()
        else:
            print form.errors
            return hyjson.json_params_error(message=form.errors)


def graph_captcha(request):
    text, image = Captcha.gene_code()
    # StringIO相当于是一个管道
    out = StringIO()
    # 把image塞到StingIO这个管道中
    image.save(out, 'png')
    # 将StringIO的指针指向开始的位置
    out.seek(0)

    # 生成一个响应
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    response['Content-length'] = out.tell()

    return response

def sms_captcha(request):
    telephone = request.GET.get('telephone')
    if not telephone:
        return hyjson.json_params_error(message=u'必须指定手机号码！')

    if hycache.get(telephone):
        return hyjson.json_params_error(message=u'验证码已发送，请1分钟后重复发送！')

    app_key = settings.ALIDAYU_APP_KEY
    app_secret = settings.ALIDAYU_APP_SECRET
    top.setDefaultAppInfo(app_key, app_secret)
    req = top.api.AlibabaAliqinFcSmsNumSendRequest()
    req.extend = ""
    req.sms_type = 'normal'
    req.sms_free_sign_name = settings.ALIDAYU_SIGN_NAME
    captcha = Captcha.gene_text()
    req.sms_param = "{code:%s}" % captcha
    req.rec_num = telephone.decode('utf-8').encode('ascii')
    req.sms_template_code = settings.ALIDAYU_TEMPLATE_CODE
    try:
        resp = req.getResponse()
        hycache.set(telephone,captcha)
        return hyjson.json_result()
    except Exception, e:
        print e
        return hyjson.json_server_error()
