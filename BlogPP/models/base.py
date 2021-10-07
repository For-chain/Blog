# @author:   zh
# @file: base.py
# @time: 2021/10/2  16:13


from django.db import models
from django.contrib.auth.models import User


class CommonInfo(models.Model):
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='用户', related_name='%(class)s_user_id')
    # 更新
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True)
    updated_by = models.ForeignKey(User, null=True, verbose_name='更新者', on_delete=models.SET_NULL, related_name='%(class)s_updated_by')
    # 排序
    sorted_by = models.IntegerField(default=1, verbose_name='排序', editable=True)
    # 是否删除
    is_delete = models.BooleanField(default=False, verbose_name='删除')
    # 描述
    desc = models.TextField(null=True, blank=True, verbose_name='描述')

    def __str__(self):
        # 检查当前对象是否有name
        if hasattr(self, 'name'):
            return self.name
        return self.desc

    class Meta:
        abstract = True  # 定义为抽象表，不会创建数据库表
        # 默认使用sorted_by排序
        ordering = ['-sorted_by']