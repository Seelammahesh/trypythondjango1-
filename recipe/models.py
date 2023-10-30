from django.db import models
from django.conf import settings
import datetime
from django.urls import reverse
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
# Create your models here.
import pint

class Recipe(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipe:detail",kwargs={"id":self.id})
    def get_hx_url(self):
        return reverse("recipe:hx-detail",kwargs={"id":self.id})

    def get_edit_url(self):
        return reverse("recipe:update",kwargs={"id":self.id})

    def get_ingredients_children(self):
        return self.recipeingredients_set.all()

class RecipeIngredients(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    quantity=models.CharField(max_length=50)
    quantity_as_float=models.FloatField(null=True,blank=True)
    # pounds,lbs,oz,grams
    unit=models.CharField(max_length=50,validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()




    def convert_to_system(self,system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg=pint.UnitRegistry(system=system)
        measurement=self.quantity_as_float *ureg[self.unit]
        print(measurement)
        return measurement
    def as_mks(self):
        measurement=self.convert_to_system(system='mks')
        print(measurement)
        return measurement.to_base_units()

    def as_imperial(self):
        measurement = self.convert_to_system(system='imperial')
        print(measurement)
        return measurement.to_base_units()



    def save(self,*args,**kwargs):
        quantity=self.quantity
        qty_as_float,qty_as_float_success=number_str_to_float(quantity)
        if qty_as_float_success:
            self.quantity_as_float=qty_as_float
        else:
            self.quantity_as_float=None
        super().save(*args,**kwargs)