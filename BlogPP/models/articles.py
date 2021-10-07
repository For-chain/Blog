'''
@author:   zh
@file: articles.py
@time: 2021/10/2  16:13
'''


from django.db import models
from django.contrib.auth.models import User
from .base import CommonInfo


# 文章表
class Articles(CommonInfo):
    article_status = (
        ('Auto', '自动化测试'),
        ('Performance', '性能测试'),
        ('Function', '功能测试'),
        ('Security', '安全测试'),
        ('DevOps', '测试运维'),
    )
    # 作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='文章发表作者', related_name='author')
    # 文章标题
    title = models.TextField(max_length=256, verbose_name='文章标题')
    # 文章内容
    content = models.TextField(verbose_name='文章内容')
    # 文章阅读数
    read_count = models.IntegerField(verbose_name='文章阅读数', default=0)
    # 文章点赞数
    like_count = models.IntegerField(verbose_name='文章点赞数', default=0)
    # 文章类别
    type = models.CharField(choices=article_status, max_length=32, default='Function', verbose_name='文章类别')
    # 是否可见
    visible = models.BooleanField(default=True, verbose_name='是否可见')
    # 文章目录
    catalog_id = models.SmallAutoField(primary_key=True, verbose_name='文章目录')

    class Meta(CommonInfo.Meta):
        # 默认使用sorted_by排序   desc倒序
        verbose_name = '文章表'


# 评论表
class Comments(CommonInfo):     # 去掉评论时间 comment_data
    # 评论文章id
    member_id = models.ManyToManyField(Articles, verbose_name='评论文章id', related_name='article_id')
    # 评论内容
    comment_content = models.TextField(verbose_name='评论内容')
    # 父评论id
    parent_comment_id = models.IntegerField(null=True, verbose_name='父评论id')

    class Meta(CommonInfo.Meta):
        verbose_name = '评论表'


# 目录表
class BlogCatalog(CommonInfo):
    catalog_name = 1
