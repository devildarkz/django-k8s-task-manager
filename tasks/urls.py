from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('health', views.health_check, name='health'),
    path('health/', views.health_check, name='health_slash'),
    path('tasks', views.task_list_create, name='task_list_create'),
    path('tasks/', views.task_list_create, name='task_list_create_slash'),
    path('tasks/<int:pk>', views.task_detail_update_delete, name='task_detail'),
    path('tasks/<int:pk>/', views.task_detail_update_delete, name='task_detail_slash'),
]