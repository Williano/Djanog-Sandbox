from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='DetailTodoAPIView'),
    path('', ListTodo.as_view(), name='ListTodoAPIView'),
]
