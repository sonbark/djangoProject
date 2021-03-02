from django.contrib import admin

from .models import Recipes, Products


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'products', 'recipe', 'calories', 'time')
    list_display_links = ('id', 'title', 'products')
    search_fields = ('title', 'products',)


admin.site.register(Recipes)
admin.site.register(Products)
