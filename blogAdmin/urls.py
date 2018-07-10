from django.contrib import admin
from django.urls import path,include
from . import views

from blogAdmin.views.blog import *
from blogAdmin.views.index import *
from blogAdmin.views.login import *

urlpatterns = [
    path('login', login.index),
    path('doLogin', login.doLogin),

    path('', index.index),
    path('index', index.index),

    path('blog', blog.index),
    path('blog_add', blog.blog_add)

    # path('article/<int:article_id>', views.article),
]