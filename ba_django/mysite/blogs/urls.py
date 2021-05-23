from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('error', views.error, name="error"),
    path('all', views.all, name="all")
]