# @author:   zh
# @file: test_articles_api.py
# @time: 2021/10/3  13:21

import requests

host = 'http://127.0.0.1:8000'
path = '/api/articles/'


# 新增文章
def test_add():
    url = f'{host}{path}'
    payload = {
        'author_id': '',
        'title': '文章标题',
        'content': '文章内容',
        'visible': True,
    }
    resp = requests.post(url=url, json=payload)
    print(resp.text)


# 删除
def test_delete():
    url = f'{host}{path}?id=1'
    resp = requests.delete(url=url)
    print(resp.json())


# 修改
def test_update(_id):
    url = f'{host}{path}?id={_id}'
    payload = {
        'title': '许壁虎',
        'desc': '爬山爱好者',
    }
    resp = requests.put(url=url, json=payload)
    print(resp.json())


# 查询
def test_query(**params):
    url = f'{host}{path}'
    resp = requests.get(url=url, params=params)
    print(resp.json())


if __name__ == '__main__':
    test_add()