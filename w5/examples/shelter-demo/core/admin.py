from django.contrib import admin

from core.models import Dog, AdoptionApplication, Event, DogBreed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'dog',
        'applicant',
        'applied_at',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(DogBreed)
class DogBreedAdmin(admin.ModelAdmin):
    pass
