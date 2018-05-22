#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/21 0021. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

from django import forms
from operation.models import UserAsk
import re


class UserAskForm(forms.ModelForm):
    """我要咨询"""

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        regex_mobile = "^1[358]\d{9}$|^147\d{8}$|176\d{8}$"
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
