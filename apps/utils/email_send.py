#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by TaoYuan on 2018/5/18 0018. 
# @Link    : http://blog.csdn.net/lftaoyuan  
# Github   : https://github.com/seeways

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from DjangoEduSysDemo.settings import EMAIL_FROM


# 生成随机字符串
def random_str(random_length=8):
    my_str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        my_str += chars[random.randint(0, length)]
    return my_str


# 发送注册邮件
def send_register_email(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        if send_status:
            email_record.code = code
            email_record.email = email
            email_record.send_type = send_type
            email_record.save()
            return False
        else:
            return True
    else:
        email_record.code = code
        email_record.email = email
        email_record.send_type = send_type
        email_record.save()
        return False
