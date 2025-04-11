
from django.contrib import admin
from django.urls import path
from .views import OrdeStatusManagement,OrdeManagement
urlpatterns = [
    path("orders/",OrdeManagement.as_view(),name='view orders'),
    path("orders/<int:pk>/",OrdeStatusManagement.as_view(),name='order detail')
]
