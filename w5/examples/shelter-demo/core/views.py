from django.shortcuts import render, get_object_or_404, redirect
from core.models import Dog, Event
from core.forms import SearchForm, AdoptionApplicationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

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


# /dogs/1/favorite/


@require_http_methods(['POST'])
@login_required
def dog_favorite_view(request, dog_pk):
    dog = get_object_or_404(Dog, pk=dog_pk)

    # We want to toggle whether this dog is favorited.
    # If we find a favorite with this user and dog (i.e. it is not created
    # prior to this moment) then delete that favorite, otherwise create it.
    favorite, created = request.user.favorite_set.get_or_create(dog=dog)
    if not created:
        favorite.delete()

    # if dog in request.user.favorite_dogs():
    #     request.user.favorite_set.get(dog=dog).delete()
    # else:
    #     request.user.favorite_set.create(dog=dog)

    return redirect(dog.get_absolute_url())


def event_detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "core/event_detail.html", {"event": event})
