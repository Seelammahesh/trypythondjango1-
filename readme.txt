video-51
Admin Inlines for foreign Keys
NOTES :
We can use admin inlines to modify  admin files in a django project
In admin inlines we have seen stackedinlines and Tabularinlines

video-52
Tests in Django are automated checks to ensure your web application behaves correctly,
 including unit tests for components, integration tests for interactions, and functional
 tests from a user perspective.

video-53
Used pint for custom measurements ..pip install pint
Handled some custom validations like UndefinedUnitError

video-54
handled some custom validations for unit measurements in test.py

video-55
Declared a quantity-as_float field in models.py
Created utils.py file to  created a function to convert number string to float Ran some tests in tests.py file for quantity_as_floa

video-56
Here we used python pint to convert units
Pip install pint
By using pint we can perform unit conversions in django accordingly

video-57
wrote some views using crud (create,update,retrieve,delete) for Recipe Model in views.py file

video-58
django urls,and include and app name,..here we added some urls created urls.py file for each app included them in project urls,py file.

video-59
created templates for recipe app, list.html,detail.html,create-update,html...

video - 60
created RecipieIngredientForm in forms.py
made some changes to  recipe_update_view

video-61
imported modelformset_factory to handle multiple forms at a time
did some changes in views.py accordingly to handle formset..

video-62
We can add form fields ,placeholders ,widgeds & css in django in two different ways
Using def __init__(self):method
We can create in forms directly in forms..py
eg:name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Recipe name"}))
made changes accordingly in forms.py (recipe app)

video-63
rendered forms and used some css stuff

video-64
added some script,added some buttons and css in create-update.html

video-65
installed django-htmx
pip install django-htmx,included it in installed_apps and middlewares of settings.py file
made some changes in create-update.html for htmx
created forms.html in recipe app and rendered create-update.html using forms.html

video-66
created partials directory in recipe and created detail.html..
used some htmx fields like hx-get,hx-trigger ....
created a new directory named fixtures and dumped all the data of recipe into it ..
(python manage.py dumpdata recipe)--by using this we get data of recipe

(python manage.py dumpdata recipe --indent 4) -- by using this we get json data..

(python manage.py dumpdata recipe --indent 4 > fixtures/recipes.json) --- this will dump data into directory

video-67
handled htmx and css at the same time  . updated the script in create-update.html..added htmx-indicator and some extrabuttons.

video-68
created two nnew files in recipe/partials
1)ingredient-form
2)ingredient-invertedform
created a view for recipe_ingredient_update_hx_view

video-69
created a auto save for saving the input data
added fields in forms.py file  "hx-post","hx-trigger", "hx-targest", "hx-swap"


video-70
htmx redirect ..made changes to  recipe_create_view to redirect headers

video-71
created an app search..
did SEARCH_TYPE_MAPPING using app models
in search app created templates for rendering data .results.html,results-view.html,search-form.html..
also seen model managers... and lookups

video-71
worked on delete-recipe and recipe ingredient ..
created a delete.html ..handled the delete views for both recipe and  recipe ingredient