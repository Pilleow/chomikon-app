from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog_app/home.html", context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, "blog_app/about.html", context)
