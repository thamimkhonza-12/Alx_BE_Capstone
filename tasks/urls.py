from django.urls import path
from .views import TaskListCreate, TaskDetail

urlpatterns = [
    path('', TaskListCreate.as_view()),
    path('<int:pk>/', TaskDetail.as_view()),
]