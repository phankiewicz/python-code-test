from django.contrib import admin

from .models import Starship


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    pass
