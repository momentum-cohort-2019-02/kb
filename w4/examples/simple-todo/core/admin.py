from django.contrib import admin
from core.models import TodoItem, TodoList

# Register your models here.


class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'todolist',
        'due_on',
        'done',
    )


admin.site.register(TodoList)
admin.site.register(TodoItem, TodoItemAdmin)
