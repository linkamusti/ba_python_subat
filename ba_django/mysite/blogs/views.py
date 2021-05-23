from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

# Create your views here.


def index(request):
    return HttpResponse("Hello World. You're at the blogs index page.")

def error(request):
    return HttpResponse("Unfortunately, we can't find this page.")

def all(request):
    blogs = Blog.objects.all()

    return render(request  , "blogs/all.html", {'blogs': blogs})