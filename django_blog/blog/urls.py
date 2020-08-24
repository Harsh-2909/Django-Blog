from django.urls import path
from .views import (PostListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # <app>/<model>_<viewtype>.html
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # <app>/<model>_<viewtype>.html
    path('post/new/', PostCreateView.as_view(), name='post-create'), # <app>/<model>_<viewtype>.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # <app>/<model>_<viewtype>.html
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # <app>/<model>_<viewtype>.html
    path('about/', views.about, name='blog-about'),
]