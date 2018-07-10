#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from blog import models

# 文章内容页
class login(View):

    # 登录页面
    def index(request):
        # 是否登录
        is_login = request.session.has_key('name')
        if is_login:
            return redirect('/blogAdmin/index')
        return render(request, 'blogAdmin/login.html')

        # 登录页面
    def doLogin(request):
        name = request.POST['name']
        password = request.POST['password']
        userInfo = models.User.objects.filter(name=name,password=password)
        res = userInfo.count()
        if res >= 1:
            res = json.dumps({'code': 1, 'status': '登录成功'})
            request.session['name'] = userInfo[0].name
            request.session['password'] = userInfo[0].password
        else:
            res = json.dumps({'code': 0, 'status': '账号或密码错误'})
        return HttpResponse(res)

