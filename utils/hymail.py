#coding: utf8

from flask_mail import Message
from exts import mail

# receivers：字符串或者数组
def send_mail(subject,receivers,body=None,html=None):
    # 必须要有接收者，没有就断言失败
    assert receivers
    # 如果body和html都为空，那么就返回False，因为没有东西可以发送
    if not body and not html:
        return False
    # 如果是字符串，要包裹成数组
    if isinstance(receivers,str) or isinstance(receivers,unicode):
        receivers = [receivers]
    msg = Message(subject=subject,recipients=receivers,body=body,html=html)
    try:
        mail.send(msg)
    except:
        return False
    return True