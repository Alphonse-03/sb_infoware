
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("dishes/",DishManagement.as_view(),name='view orders'),
]

