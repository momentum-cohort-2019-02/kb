from django.shortcuts import render, get_object_or_404, redirect
from core.models import Dog, Event
from core.forms import SearchForm, AdoptionApplicationForm

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

    # if form is submitted
    if request.method == "POST":
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')
    else:
        form = AdoptionApplicationForm(initial={"dog": dog})

    return render(request, "core/dog_detail.html", {
        "dog": dog,
        "application_form": form,
    })


def event_detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "core/event_detail.html", {"event": event})
