from django.shortcuts import render, get_object_or_404
from core.models import Dog
from core.forms import SearchForm

# Create your views here.


def index_view(request):
    if request.GET:
        form = SearchForm(request.GET)
        dogs = form.search()
    else:
        form = SearchForm()
        dogs = Dog.objects.all()

    response = render(request, 'core/index.html', {
        "dogs": dogs,
        "search_form": form,
    })
    return response


def dog_detail_view(request, dog_pk):
    # dog = Dog.objects.get(pk=dog_pk)
    dog = get_object_or_404(Dog, pk=dog_pk)
    return render(request, "core/dog_detail.html", {"dog": dog})
