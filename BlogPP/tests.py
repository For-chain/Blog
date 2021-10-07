from django.test import TestCase
from django.contrib.auth.models import User
from .models.articles import Articles
# Create your tests here.


class TestM2MQuery(TestCase):
    def setUp(self) -> None:
        # 用户
        self.user = User.objects.create_user(username='admin', password='123456', first_name='许振虎')
        # 文章
        self.articles = Articles.objects.create(name='测试', user_id=self.user)

# 查询