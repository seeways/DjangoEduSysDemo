#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/22 0022. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways
from django.urls import path, re_path
from .views import CourseListView, CourseDetailView

# 命名空间
app_name = "course"

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),


]
