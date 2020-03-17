from django.db import models
from mdeditor.fields import MDTextField
# Create your models here.


class ExampleModel(models.Model):
    title = models.CharField(max_length=30)
    content = MDTextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=False)
    picture = 1

    def foo(self):
        self.picture = self.create_time.second % 8 + 1
        return self.picture

    def __str__(self):
        return self.title
