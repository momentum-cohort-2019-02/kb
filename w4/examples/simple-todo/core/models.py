from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    todolist = models.ForeignKey(
        to=TodoList, on_delete=models.CASCADE, null=True, related_name='items')
    description = models.CharField(max_length=255)
    done_at = models.DateTimeField(null=True, blank=True)
    due_on = models.DateField(null=True, blank=True)

    def done(self):
        return self.done_at is not None

    def __str__(self):
        return self.description
