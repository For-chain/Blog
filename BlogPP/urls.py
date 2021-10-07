# @author:   zh
# @file: urls.py
# @time: 2021/10/3  13:13

from django.urls import path
from .views import dispathcer

urlpatterns = [
    path('articles/', dispathcer),        # 文章的增删改查

]