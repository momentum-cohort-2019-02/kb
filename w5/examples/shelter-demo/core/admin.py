from django.contrib import admin

from core.models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass
