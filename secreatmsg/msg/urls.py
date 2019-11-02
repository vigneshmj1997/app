from django.contrib import admin
from django.urls import path,include,re_path
from . import views
urlpatterns = [
    path("create",views.name,name="post"),
    re_path(r'^(?P<user_name>\D+)/$', views.home),
    re_path(r'^(?P<user_name>\D+)/(?P<password>\d+)/$', views.olala),
]
