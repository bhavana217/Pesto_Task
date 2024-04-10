from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy, index

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]
