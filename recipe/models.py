from django.db import models
from django.conf import settings
import datetime
from .validators import validate_unit_of_measure
# Create your models here.

class Recipe(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

class RecipeIngredients(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    quantity=models.CharField(max_length=50)
    # pounds,lbs,oz,grams
    unit=models.CharField(max_length=50,validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)