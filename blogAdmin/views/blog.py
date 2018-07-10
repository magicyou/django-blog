#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
import json
from .. import models
from .. import requireLogin
from blog import models

# 文章内容页
class blog(View):

    # 首页
    @requireLogin.requir_login
    def index(request):
        # articles = models.Article.objects.all()
        return render(request, 'blogAdmin/blog.html')

    # 文章添加页
    def blog_add(request):
        title = '博客添加'
        do = 'add'
        if request.POST and request.POST['do'] == 'add':
            models.Article.objects.create(title=request.POST['title'], content=request.POST['content'])
            return render(request, 'blogAdmin/article_edit.html', {'title': title, 'do': do, 'res': '添加成功'})
        else:
            return render(request, 'blogAdmin/blog_add.html', {'title': title, 'do': do})

