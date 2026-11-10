from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail'),
]