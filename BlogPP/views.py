import json

from django.db import transaction
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models.articles import Articles, Comments


@csrf_exempt
def dispathcer(request):            # 路由调度器
    # 处理查询操作
    if request.method == 'GET':
        return query_articles(request)
    # 处理修改操作
    elif request.method == 'PUT':
        return update_articles(request)
    # 处理新增请求
    elif request.method == 'POST':
        return add_articles(request)
    # 处理删除请求
    elif request.method == 'DELETE':
        return delete_articles(request)


def add_articles(request):
    # 处理请求消息体
    in_params = json.loads(request.body)    # in_params==字典
    try:
        info = {}       # 创建数据的参数
        # 必填参数列表
        position_keys = ['author']
        for key in position_keys:
            if key not in in_params:
                return JsonResponse({'retcode': 400, 'msg': '请求错误', 'error': f'缺少必填项{key}'})
            info[key] = in_params[key]
        # 选填参数列表
        option_keys = ['title', 'content', 'visible']
        for key in option_keys:
            if key in in_params:
                info[key] = in_params[key]
    except Exception as e:
        return JsonResponse({'retcode': 400, 'msg': '请求错误', 'error': repr(e)})
    # 新建文章
    try:
        with transaction.atomic():
            articles = Articles.objects.create(**info)
            # 找到作者id，并进行关联
            if in_params.get('author_id', None):     # 如果没有传递成员列表就不关联
                authors = [User.objects.get(pk=_id) for _id in in_params['author_id']]
                articles.author.add(*authors)
        return JsonResponse({'retcode': 200, 'msg': '新增成功', 'id': articles.id})
    except Exception as e:
        return JsonResponse({'retcode': 500, 'msg': '新增失败', 'error': repr(e)})


# 删除
def delete_articles(request):
    if request.method == 'DELETE':
        in_params = request.GET
        info = {}           # 查询字段的容器
        position_keys = ['id']
        for key in position_keys:
            if key not in in_params:
                return JsonResponse({'retcode': 400, 'msg': '请求错误', 'error': f'缺少必填项{key}'})
            info[key] = in_params[key]
        # 删除文章
        try:
            # 获取需要删除的对象id
            articles = Articles.objects.get(**info)
            articles.delete()
            return JsonResponse({'retcode': 200, 'msg': '删除成功'})
        except Exception as e:
            return JsonResponse({'retcode': 500, 'msg': '删除失败', 'error': repr(e)})


# 修改
def update_articles(request):
    # 获取待修改对象的id
    _id = request.GET.get()
    # 获取请求体参数---json
    in_params = json.loads(request.body)  # 字典
    info = {}
    option_keys = ['title', 'content', 'visible', 'desc']
    for key in option_keys:
        if key in in_params:
            info[key] = in_params[key]

    # 查询待修改数据
    try:
        articles = Articles.objects.get(pk=_id)
        # 更新多对多关系
        if in_params.get('author_id'):
            # 更新成员关系----覆盖,非新增
            author_id = in_params['author_id']       # [1, 2, 3]
            # 根据id获取用户数据对象
            autho_list = [User.objects.get(pk=_id) for _id in author_id]
            # 清除原有多对多关系
            articles.author.clear()
            # 关联成员
            articles.article_id.add(*autho_list)
        for k, v in info.items():       # 根据入参动态设置属性
            articles.__setattr__(k, v)      # (属性名,属性值)
        # 更新文章数据
        articles.save()
        return JsonResponse({'retcode': 200, 'msg': '修改成功'})

    except Exception as e:
        return JsonResponse({'retcode': 500, 'msg': '修改失败', 'error': repr(e)})


# 查询
def query_articles(request):
    # 获取查询参数
    in_params = request.GET
    info = {}       # 容器收集参数
    option_keys = ['id', 'title']
    for key in option_keys:
        if key in in_params:
            info[key] = in_params[key]
    try:
        retlist = []
        # articles = Articles.objects.filter(**info).values()        # 转成列表-->转成键值对
        articles_s = Articles.objects.filter(**info)
        for articles in articles_s:
            item = {}
            item['title'] = articles.title
            # item['content'] = articles.content
            item['type'] = articles.type
            item['create_time'] = articles.create_time.strftime('%Y-%m-%d %H:%M')
            item['update_time'] = articles.update_time.strftime('%Y-%m-%d %H:%M')
            # 将autho内容转化为字典，直接将数据对象转化为字典格式，处理嵌套响应
            item['author'] = model_to_dict(articles.author, fields=['id', 'username', 'email'])
            # 查询关联数据信息---反向查询
            retlist.append(item)
        return JsonResponse({'retcode': 200, 'msg': '查询成功', 'retlist': retlist})
    except Exception as e:
        return JsonResponse({'retcode': 500, 'msg': '查询失败', 'error': repr(e)})