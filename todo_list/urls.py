from django.contrib import admin
from django.urls import path

from todo_list.views import index


urlpatterns = [
    path("", index, name="index")
]

app_name = "todo-list"
