#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/11 0011. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    """课程"""

    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']


class LessonAdmin(object):
    """章节"""

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # 这里course__name是根据课程名称过滤
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    """视频"""

    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    """课程资源"""

    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
