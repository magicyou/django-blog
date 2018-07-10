from django.contrib import admin
from django.urls import path,include

from blog.views.article import *

urlpatterns = [
    path('', article.index),
    path('article/<int:article_id>', article.article),
    path('article_edit/<int:article_id>', article.article_edit),
    path('article_add', article.article_add),
    path('testAjax', article.testAjax, name='testAjax'),
]