from django.contrib import admin
from .models import Articles


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'content', 'updated_on', 'timestamp', 'published']
    search_fields = ['id', 'title', 'timestamp']


admin.site.register(Articles, ArticleAdmin)
