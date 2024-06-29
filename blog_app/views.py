from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

posts = [
    {
        "author": "Enside",
        "title": "Chomikuj",
        "content": "Chomik.",
        "date": "August 16, 2024"
    },
    {
        "author": "Pilleow",
        "title": "Chomikowanie",
        "content": "Chomik ale w project zomboid.",
        "date": "August 15, 2024"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog_app/home.html", context)


def about(request):
    context = {
        'title': "About"
    }
    return render(request, "blog_app/about.html", context)
