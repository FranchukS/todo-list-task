from django.contrib import admin
from django.urls import path

from todo_list.views import TaskListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "todo-list"
