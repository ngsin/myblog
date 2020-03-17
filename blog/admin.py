from django.contrib import admin

from blog.models import Article, ExampleModel

admin.site.register(Article)

admin.site.register(ExampleModel)
