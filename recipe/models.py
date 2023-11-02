from django.db import models
import pathlib
import uuid
from django.conf import settings
import datetime
from django.db.models import Q
from django.urls import reverse
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
# Create your models here.
import pint


class RecipeQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query == "":
            return self.none()  #[]
        lookups = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(directions__icontains=query)
        )
        return self.filter(lookups)

class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)
'''
class Article(models.Model):
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    slug=models.SlugField(unique=True,blank=True, null=True)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    publish=models.DateField(auto_now_add=False,auto_now=False, null=True,blank=True)
    objects=ArticleManager()
    def get_absolute_url(self):
        #return f'/artcles/{self.slug}/'
        return reverse("articles:detail", kwargs={"slug": self.slug})
    def save(self, *args, **kwargs):
        #obj=Article.objects.get(id=1)
        #set somthing
        # if self.slug is None:
        #     self.slug=slugify(self.title)
        # if self.slug is None:
        #     slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)
        #obj.save()
        #do another somthing
def article_pre_save(sender,instance,*args, **kwargs):
    #print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)
pre_save.connect(article_pre_save, sender=Article)
def article_post_save(sender,instance,created,*args, **kwargs):
    #print('post_save')
    if created:
        slugify_instance_title(instance,save=True)
post_save.connect(article_post_save, sender=Article) '''

class Recipe(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=220)
    description=models.TextField(blank=True,null=True)
    directions=models.TextField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)


    objects=RecipeManager()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe:detail",kwargs={"id":self.id})
    def get_hx_url(self):
        return reverse("recipe:hx-detail",kwargs={"id":self.id})

    def get_edit_url(self):
        return reverse("recipe:update",kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("recipe:delete",kwargs={"id":self.id})

    def get_ingredients_children(self):
        return self.recipeingredients_set.all()


def recipe_ingredient_image_upload_handler(instance, filename):
    fpath=pathlib.Path(filename)
    new_fname=str(uuid.uuid())  #uuid->uudid+timestamp
    return f"recipes/ingredient/{new_fname}{fpath.suffix}"


class RecipeIngredientImage(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=recipe_ingredient_image_upload_handler) #path/to/the/actual/file.png
    #image
    #extracted_text

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

    def get_delete_url(self):
        kwargs={
            "parent_id": self.recipe.id,
            "id": self.id
        }
        return reverse("recipe:ingredient-delete",kwargs=kwargs)


    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id
        }
        return reverse("recipe:hx-ingredient-detail", kwargs=kwargs)




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