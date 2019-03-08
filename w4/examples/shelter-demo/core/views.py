from django.shortcuts import render
from core.models import Dog
from core.forms import DogSearchForm


def index_view(request):
    form = DogSearchForm(request.GET)
    dogs = form.search()

    return render(request, "core/index.html", {
        "dogs": dogs,
        "form": form,
    })
