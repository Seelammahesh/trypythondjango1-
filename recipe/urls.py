from django.urls import path

from . import views

app_name='recipe'

urlpatterns = [
    path("", views.recipe_list_view, name="list"),
    path("create/", views.recipe_create_view, name="create"),
    path("<int:parent_id>/ingredient/<int:id>/delete/", views.recipe_ingredient_delete_view,
         name='ingredient-delete'),
    path("<int:id>/update/", views.recipe_update_view, name="update"),
    path("<int:id>/", views.recipe_detail_view, name="detail"),


    path("hx/<int:id>/delete/", views.recipe_delete_view, name='delete'),
    path("hx/<int:id>/", views.recipe_detail_hx_view, name='hx-detail'),
    path("hx/<int:parent_id>/ingredient/<int:id>/", views.recipe_ingredient_update_hx_view, name='hx-ingredient-detail'),
    path("hx-ingredient-create/<int:parent_id>/", views.recipe_ingredient_update_hx_view, name='hx-ingredient-create'),

    ]
    # Add other URL patterns as needed