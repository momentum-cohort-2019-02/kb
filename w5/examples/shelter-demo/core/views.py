from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from core.forms import AdoptionApplicationForm, SearchForm
from core.models import Dog, Event

# Create your views here.


def index_view(request):
    if request.GET:
        form = SearchForm(request.GET)
        dogs = form.search()
    else:
        form = SearchForm()
        dogs = Dog.objects.all()

    if request.GET.get('sort'):
        dogs = dogs.order_by(request.GET.get('sort'))

    paginator = Paginator(dogs, 6)
    page = request.GET.get('page', 1)
    dogs = paginator.get_page(page)

    response = render(request, 'core/index.html', {
        "dogs": dogs,
        "search_form": form,
    })
    return response


def dog_detail_view(request, dog_pk):
    # dog = Dog.objects.get(pk=dog_pk)
    dog = get_object_or_404(Dog, pk=dog_pk)

    # if form is submitted
    if request.method == "POST" and request.user.is_authenticated:
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.save()
            messages.success(
                request,
                f"We have received your application to adopt {dog.name}. We will contact you within 5 business days."
            )
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

    if created:
        messages.success(request, f"You have favorited {dog.name}.")
    else:
        messages.info(request, f"You have unfavorited {dog.name}.")
        favorite.delete()

    # if dog in request.user.favorite_dogs():
    #     request.user.favorite_set.get(dog=dog).delete()
    # else:
    #     request.user.favorite_set.create(dog=dog)

    return redirect(dog.get_absolute_url())


def event_detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "core/event_detail.html", {"event": event})
