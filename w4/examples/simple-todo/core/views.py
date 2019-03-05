from django.shortcuts import render
from django.http import HttpResponse
from core.models import TodoItem


# Create your views here.
def index_view(request):
    todos = TodoItem.objects.all()
    todotext = ", ".join([todo.description for todo in todos])
    return HttpResponse(todotext)
