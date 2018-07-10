#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import json

def requir_login(f):
    def wrap(request, *args, **kwargs):
        is_login = request.session.has_key('name')
        if not is_login:
            return redirect('/blogAdmin/login')
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap