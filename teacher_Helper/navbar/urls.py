from django.urls import path
from . import views

urlpatterns = [
    path('', views.navbar, name='navbar'),
]