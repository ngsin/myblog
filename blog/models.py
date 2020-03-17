from django.db import models

from mdeditor.fields import MDTextField


class Article(models.Model):
    title = models.CharField(max_length=332, default='Title')
    content = models.TextField(null=True)

    def __str__(self):
        return self.title


class ExampleModel(models.Model):
    name = models.CharField(max_length=30)
    content = MDTextField()

    def __str__(self):
        return self.name
