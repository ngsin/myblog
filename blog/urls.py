from django.urls import re_path, path

from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    re_path('article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    re_path('edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    path('edit/action/', views.edit_action, name='edit_action'),
    path('test/',views.blog_templates)
]
