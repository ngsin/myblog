from django.urls import path ,re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path('single/(?P<single_id>[0-9]+)$', views.single_page, name='single'),
    # path('pre/', views.pre_page, name='pre'),
    # path('next/', views.next_page, name='next'),

]
