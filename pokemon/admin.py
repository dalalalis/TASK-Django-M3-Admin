from django.contrib import admin

from pokemon.models import Pokemon

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin (admin.ModelAdmin):
    list_display=("id","name","hp", "active",)
    list_display_links= ("id", "name",)
    list_filter= ("active",)
    
    fieldsets = ("general",{"fields":("name","hp", "active", "type")}),
    ("Localizations", {"fields":("name_fr", "name_ar", "name_jp",),"classes": ("collapse",)}),
    ("none",{"fields":("created_at","updated_at",)}),
                
                

    



