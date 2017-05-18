#coding: utf8

from django.http import JsonResponse
import qiniu
from django.conf import settings


def qiniu_token(request):
    q = qiniu.Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)

    # 选择七牛的云空间
    bucket_name = settings.QINIU_BUCKET_NAME

    # 生成token
    token = q.upload_token(bucket_name)

    return JsonResponse({'uptoken':token})