from django.contrib import admin

from pokemon.models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin (admin.ModelAdmin):
    list_display=("id","name","hp", "active")
    list_display_links= ("id", "name")
    list_filter= ("active",)
    



