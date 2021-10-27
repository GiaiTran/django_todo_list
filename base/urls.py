from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    # path('', views.taskList, name='tasks'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
]