from django.urls import path
from core import views

urlpatterns = [
    path('list/<int:todolist_pk>/', views.todolist_view, name="todolist"),
]
