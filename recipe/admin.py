from django.contrib import admin
from .models import Recipe,RecipeIngredients
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display=['name','user']
    readonly_fields = ['user','timestamp'
                       ]

admin.site.register(Recipe,RecipeAdmin),
admin.site.register(RecipeIngredients)





