from django.urls import path
from django.views.generic import ListView
from .views import BlogList, BlogDetailView, AboutPageView

from .views import Post

urlpatterns = [
    path('post<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', BlogList.as_view(), name='home')
]
