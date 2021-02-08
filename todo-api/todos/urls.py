from django.urls import path
from .views import ListTodo, DetailTodo

app_name = 'todo_api'

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='DetailTodoAPIView'),
    path('', ListTodo.as_view(), name='ListTodoAPIView'),
]
