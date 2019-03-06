from django.shortcuts import render
from core.models import Dog

# Create your views here.


def index_view(request):
    dogs = Dog.objects.all()
    return render(request, "core/index.html", {"dogs": dogs})
