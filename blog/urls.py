from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.blog_title, name="blog_title"),
    re_path(r'(?P<article_id>(\d+))/$',views.blog_article,name="blog_detail")
]