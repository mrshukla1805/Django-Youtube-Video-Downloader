from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.down, name="downloads"),
    path('download/',views.yt_down),
]