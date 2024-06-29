from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_app_home'),
    path('about/', views.about, name='blog_app_about'),
]
