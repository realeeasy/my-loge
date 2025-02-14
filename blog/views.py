# 在 blog/views.py 中
from django.http import HttpResponse
# blog/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

