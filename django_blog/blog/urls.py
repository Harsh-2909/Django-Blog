from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Blog-Home'),
    path('about/', views.about, name='About-Page'),
]