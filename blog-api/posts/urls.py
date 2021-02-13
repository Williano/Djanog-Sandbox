from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog-api'

urlpatterns = [
    
    path('<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path('', PostList.as_view(), name="post-list")
]