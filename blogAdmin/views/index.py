#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import json
from .. import models
from .. import requireLogin
from blog import models

# 首页
class index(View):
    # 首页
    @requireLogin.requir_login
    def index(request):
        # articles = models.Article.objects.all()
        return render(request, 'blogAdmin/index.html')
        # return HttpResponse('hello world!')

