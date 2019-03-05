from django.shortcuts import render
from django.http import HttpResponse
from core.models import TodoItem, TodoList


# Create your views here.
def index_view(request):
    todos = TodoItem.objects.all()
    return render(request, "core/index.html", {"todos": todos})


def todolist_view(request, todolist_pk):
    # raise RuntimeError(todolist_pk)
    todolist = TodoList.objects.get(pk=todolist_pk)
    return render(request, "core/todolist.html", {"todolist": todolist})
