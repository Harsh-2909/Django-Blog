from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # <app>/<model>_<viewtype>.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # <app>/<model>_<viewtype>.html
    path('about/', views.about, name='blog-about'),
]