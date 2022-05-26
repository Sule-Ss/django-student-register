from . import views
from django.urls import path

urlpatterns = [
    path("list/", views.todo_list, name="todo")
] 