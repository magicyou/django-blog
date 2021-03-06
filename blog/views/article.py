#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
import json
from .. import models

# 文章内容页
class article(View):

    # 首页
    def index(request):
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
        # return HttpResponse('hello world!')

    def article(request,article_id):
        return render(request, 'blog/article.html')
        # article = models.Article.objects.get(id=article_id)
        # return render(request,'blog/article.html',{'article':article})

    # 文章添加页
    def article_add(request):
        title = '文章添加'
        do = 'add'
        if request.POST and request.POST['do'] == 'add':
            models.Article.objects.create(title=request.POST['title'], content=request.POST['content'])
            return render(request, 'blog/article_edit.html', {'title': title, 'do': do, 'res': '添加成功'})
        else:
            return render(request, 'blog/article_edit.html', {'title': title, 'do': do})

    # 文章编辑页
    def article_edit(request, article_id):
        title = '文章编辑'
        do = 'edit'
        if request.POST and request.POST['do'] == 'edit':
            article = models.Article.objects.filter(id=request.POST['id'])
            article.update(title=request.POST['title'], content=request.POST['content'])
            return render(request, 'blog/article_edit.html', {'title': title, 'do': do, 'res': '编辑成功'})
        else:
            article = models.Article.objects.get(id=article_id)
            return render(request, 'blog/article_edit.html', {'title': title, 'do': do, 'article': article})

    # 文章内容页
    def testAjax(request):
        title = 'ajax测试'
        do = 'test'
        if request.POST and request.POST['do'] == 'test':
            res = json.dumps({'code': 1, 'msg': 'success'})
            return HttpResponse(res)
        else:
            return render(request, 'blog/testAjax.html', {'title': title, 'do': do})