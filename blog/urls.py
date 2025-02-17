# 在 blog/urls.py 中
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')

]