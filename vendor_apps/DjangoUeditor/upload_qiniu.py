#encoding: utf-8
from django.conf import settings
from datetime import datetime
import urllib
import os


def upload_to_qiniu(post_file,file_path):
    from qiniu import Auth, put_data, etag, urlsafe_base64_encode
    QINIU_CONFIG = settings.DJANGO_UEDITOR_QINIU
    # 需要填写你的 Access Key 和 Secret Key
    access_key = QINIU_CONFIG.get('QINIU_ACCESS_KEY')
    secret_key = QINIU_CONFIG.get('QINIU_SECRET_KEY')
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = QINIU_CONFIG.get('QINIU_BUCKET_NAME')
    # 上传到七牛后保存的文件名
    key = urlsafe_base64_encode(file_path) + os.path.splitext(file_path)[1]
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    ret, info = put_data(token, key, post_file)
    result = {}
    if info.status_code == 200:
        result['state'] = u'SUCCESS'
        result['url'] = urllib.basejoin(QINIU_CONFIG.get('QINIU_DOMAIN'),ret.get('key'))
    else:
        result['state'] = u'UPLOAD ERROR'
    return result