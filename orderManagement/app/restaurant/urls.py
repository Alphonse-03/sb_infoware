
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("restaurants/",RestaurantsManagement.as_view(),name='view orders'),
]

