# Generated by Django 3.2.7 on 2021-10-04 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('sorted_by', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('title', models.TextField(max_length=256, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('read_count', models.IntegerField(default=0, verbose_name='文章阅读数')),
                ('like_count', models.IntegerField(default=0, verbose_name='文章点赞数')),
                ('type', models.CharField(choices=[('Auto', '自动化测试'), ('Performance', '性能测试'), ('Function', '功能测试'), ('Security', '安全测试'), ('DevOps', '测试运维')], default='Function', max_length=32, verbose_name='文章类别')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('catalog_id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='文章目录')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='文章发表作者')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles_user_id', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '文章表',
                'ordering': ['-sorted_by'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('sorted_by', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogcatalog_user_id', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blogcatalog_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'ordering': ['-sorted_by'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('sorted_by', models.IntegerField(default=1, verbose_name='排序')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='描述')),
                ('comment_content', models.TextField(verbose_name='评论内容')),
                ('parent_comment_id', models.IntegerField(null=True, verbose_name='父评论id')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_user_id', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
                ('member_id', models.ManyToManyField(related_name='article_id', to='BlogPP.Articles', verbose_name='评论文章id')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
            options={
                'verbose_name': '评论表',
                'ordering': ['-sorted_by'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='blogcomments',
            name='article_id',
        ),
        migrations.RemoveField(
            model_name='blogcomments',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='BlogArticles',
        ),
        migrations.DeleteModel(
            name='BlogComments',
        ),
    ]
