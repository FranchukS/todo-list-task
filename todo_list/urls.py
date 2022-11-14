from django.urls import path

from todo_list.views import (
    TaskListView, TaskCreateView,
    TaskUpdateView, TaskDeleteView,
    complete_or_undo, TagListView,
    TagCreateView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/complete-or-undo/", complete_or_undo, name="task-complete-or-undo"),

    path("tags", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),

]

app_name = "todo-list"
