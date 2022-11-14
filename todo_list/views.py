from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo_list/index.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:index")


class TaskUpdateView(generic.UpdateView):
    queryset = Task.objects.all()
    form_class = TaskForm
    success_url = reverse_lazy("todo-list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo-list:index")


def complete_or_undo(request, pk):
    task = Task.objects.get(pk=pk)
    if task.is_done:
        task.is_done = False
        task.save()
    else:
        task.is_done = True
        task.save()
    return HttpResponseRedirect(reverse_lazy("todo-list:index"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo-list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo-list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo-list:tag-list")
