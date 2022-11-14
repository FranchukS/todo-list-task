from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo-list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo-list:index")
