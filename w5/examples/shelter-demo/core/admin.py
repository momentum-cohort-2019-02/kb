from django.contrib import admin

from core.models import Dog, AdoptionApplication


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'dog',
        'applicant_name',
        'applied_at',
    )
