# Generated by Django 3.2.7 on 2021-10-01 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticles',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('sorted_by', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('article_title', models.TextField(max_length=256, verbose_name='文章标题')),
                ('article_content', models.TextField(verbose_name='文章内容')),
                ('article_read_count', models.IntegerField(max_length=10, verbose_name='文章阅读数')),
                ('article_like_count', models.IntegerField(max_length=10, verbose_name='文章点赞数')),
                ('article_type', models.CharField(choices=[('Auto', '自动化测试'), ('Performance', '性能测试'), ('Function', '功能测试'), ('Security', '安全测试'), ('DevOps', '测试运维')], default='Function', max_length=32, verbose_name='文章类别')),
                ('article_visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('catalog_id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='文章目录')),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章表',
                'ordering': ['-sorted_by'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('sorted_by', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('parent_comment_id', models.IntegerField(max_length=10, null=True, verbose_name='父评论id')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_id', to='BlogPP.blogarticles', verbose_name='评论文章id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL, verbose_name='评论者用户id')),
            ],
            options={
                'verbose_name': '评论表',
                'ordering': ['-sorted_by'],
                'abstract': False,
            },
        ),
    ]