from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe,RecipeIngredients
User=get_user_model()
from django.core.exceptions import ValidationError

class UserTestcase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('trypythondjango',password='123654')

    def test_user_pwd(self):
        checked = self.user_a.check_password("123654")
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('trypythondjango',password='123654')
        self.recipe_a=Recipe.objects.create(
            name='GrilledChicken',
            user=self.user_a
        )
        self.recipe_ingredient_a=RecipeIngredients.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='5',
            unit='rupees'
        )


    def test_user_count(self):
        qs=User.objects.all()
        self.assertEqual(qs.count(),1)

    def test_user_recipe_reverse_count(self):
        user=self.user_a
        qs=user.recipe_set.all()
        self.assertEqual(qs.count(),1)

    def test_user_recipe_forward_count(self):
        user=self.user_a
        qs=Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),1)

    def test_recipe_ingredient_reverse_count(self):
        recipe=self.recipe_a
        qs = recipe.recipeingredients_set.all()
        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredients.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 1)


    def test_user_two_level_relation(self):
        user=self.user_a
        qs=RecipeIngredients.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(),1)

    def test_user_two_level_reverse_relation(self):
        user = self.user_a
        recipeingredients_ids = list(user.recipe_set.all().values_list('recipeingredients__id', flat=True))
        qs=RecipeIngredients.objects.filter(id__in=recipeingredients_ids)
        self.assertEqual(qs.count(),1)
        self.assertEqual(qs.count(),1)

    def test_user_two_level_relation_via_recipe(self):
        user = self.user_a
        ids=user.recipe_set.all().values_list("id",flat=True)
        qs=RecipeIngredients.objects.filter(recipe__id__in=ids)
        self.assertEqual(qs.count(),1)

    def test_unit_measure_validation(self):
        invalid_unit="ounce"
        ingredient=RecipeIngredients(
            name='new',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_units =['nada','sadqdasd']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:

                ingredient = RecipeIngredients(
                    name='new',
                    quantity='10',
                    recipe=self.recipe_a,
                    unit=invalid_units
                )
                ingredient.full_clean()

