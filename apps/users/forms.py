#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/14 0014. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

from django import forms
from captcha.fields import CaptchaField


# 登录表单验证
class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    """注册验证表单"""
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPwdForm(forms.Form):
    """忘记密码"""
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    """重置密码"""
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
