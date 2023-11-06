from django.contrib.auth import get_user_model
from django.db.models import Sum

from meals.models import Meal
from recipe.models import RecipeIngredients

User = get_user_model()
j = User.objects.first()

queue = Meal.objects.by_user(j).pending().prefetch_related('recipe__recipeingredients')
ids = queue.values_list("recipe__recipeingredients__id", flat=True)
qs = RecipeIngredients.objects.filter(id__in=ids)
data = qs.values("name", "unit").annotate(total=Sum("quantity_as_float"))


for d in data:
    print(d['total'], d['unit'], d['name'])

