from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe,RecipeIngredients,RecipeIngredientImage
# Register your models here.

user=get_user_model()
admin.site.unregister(user)



class RecipeInline(admin.StackedInline):
    model=Recipe
    extra = 0
class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 0
    readonly_fields = ['quantity_as_float','as_mks','as_imperial',]
    #fields = ['name','quantity','unit','directions']

class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ['username']

class RecipeAdmin(admin.ModelAdmin):
    inlines=[RecipeIngredientsInline]
    list_display=['name','user']
    readonly_fields = ['user','timestamp','updated']

admin.site.register(Recipe,RecipeAdmin),
admin.site.register(RecipeIngredients)
admin.site.register(user,UserAdmin)
admin.site.register(RecipeIngredientImage)



