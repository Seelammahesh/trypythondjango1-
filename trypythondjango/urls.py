"""trypythondjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from search.views import search_view
from meals.views import meal_queue_toggle_view




urlpatterns = [
    path('admin/', admin.site.urls),

    path('pantry/recipe/',include('recipe.urls')),
    path('blog/', include('articles.urls')),
    path('search/',search_view, name='search'),
path('meal-toggle/<int:recipe_id>', meal_queue_toggle_view, name='meal-toggle'),

    ]
