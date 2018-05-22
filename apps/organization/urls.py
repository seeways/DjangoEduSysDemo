#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/21 0021. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

from organization.views import OrgView, AddUserAskView

from django.urls import path, re_path

# 命名空间
app_name = "organization"

urlpatterns = [
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
]
