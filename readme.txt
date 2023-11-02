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

video-72
worked on delete-recipe and recipe ingredient ..
created a delete.html ..handled the delete views for both recipe and  recipe ingredient

video-73
added some error handlers in recipe_delete_view,recipe_ingredient_delete_view..created a template name base.html in templates .
added a new html template in recipes/partials  name ingredient-inline-delete-response.html..

video-74
created static folder in recipe app and inside it created a directory recipes ..inside it created recipes-htmx.html file
 recipe/static/recipes-htmx.html
 handled some css in recipes.htmx.html file

video-75
created python directory named cdn  .in that cdn created python files backends.py,conf.py ..
installed storages from ..pip install django-storages
included storages in settings.py ...installed apps
created StaticRootS3Boto3Storage and MediaRootS3Boto3Storage in backends.py file and set locations
and also included some aws related stuff in conf.py file.

video-76
installed django-storages,boto3 and pillow for media
added them to installed_apps
created recipe_ingredient_image_upload_handler,RecipeIngredientImage in recipe/models
declared media root ,MEDIA_ROOT=BASE_DIR/"staticfiles-cdn"/"uploads"


video -77
Created new RecipeIngredientImageForm
Created new html image-form.html
ran migrations...
Created new view in views.py recipe_ingredient_image_upload_view

video-78
created image-upload-form.html,upload-image.html...
made changes to recipe_ingredient_image_upload_view

video-79
added models.jsonField to RecipeIngredientImage
created services.py in recipes app
installed requests, using pip install requests


video 80
installed doctl cli
installed doctl using ,Invoke-WebRequest https://github.com/digitalocean/doctl/releases/download/v1.100.0/doctl-1.100.0-windows-amd64.zip -OutFile ~\doctl-1.100.0-windows-amd64.zip
extracted binary by running
Expand-Archive -Path ~\doctl-1.100.0-windows-amd64.zip
created app (doctl apps create--spec.do/app.yaml)