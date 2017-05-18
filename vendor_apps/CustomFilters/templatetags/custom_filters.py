#encoding: utf-8

from django import template

register = template.Library()

@register.filter
def fmt_datetime(value):
    from datetime import datetime
    if type(value) == datetime:
        now = datetime.now()
        timestamp = (now - value).total_seconds()
        if timestamp < 60:
            return u'刚刚'
        elif timestamp > 60 and timestamp < 60 * 60:
            minutes = timestamp / 60
            return u'%s分钟前' % int(minutes)
        elif timestamp > 60 * 60 and timestamp < 60 * 60 * 24:
            hours = timestamp / (60 * 60)
            return u'%s小时前' % int(hours)
        elif timestamp > 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
            days = timestamp / (60 * 60 * 24)
            return u'%s天前' % int(days)
        elif now.year == value.year:
            return value.strftime('%m-%d %H:%M:%S')
        else:
            return value.strftime('%Y-%m-%d %H:%M:%S')
    return value
