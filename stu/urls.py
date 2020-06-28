# coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login_view),
    url(r'^loginon/', views.login),
    url(r'^register/', views.register_view),
    url(r'^show/', views.show_view)
]
