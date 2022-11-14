from django.contrib import admin
from django.urls import path

from todo_list.views import (
    TaskListView, TaskCreateView,
    TaskUpdateView, TaskDeleteView,
    complete_or_undo,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/complete-or-undo/", complete_or_undo, name="task-complete-or-undo"),
]

app_name = "todo-list"
