# -*- coding: utf-8 -*-
# @Time        : 2017/9/30 9:21
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : urls.py
# @Description : STOP wishing START doing. 

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)$', views.show)
]
