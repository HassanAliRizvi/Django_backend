from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdate

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdate.as_view(), name='task-retrieve-update'),
]




