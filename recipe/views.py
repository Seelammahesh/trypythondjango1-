from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.urls import reverse
# Create your views here.
#crud - Create,Retrieve,update,Delete
from .models import Recipe,RecipeIngredients
from .forms import RecipeForm,RecipeIngredientForm
from django.http import HttpResponse,Http404

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.all()
    context={
        "objects_list":qs
    }
    return render(request,"recipe/list.html",context)

@login_required
def recipe_detail_view(request,id=None):
    hx_url= reverse("recipe:hx-detail", kwargs={'id':id})
    context={
        "hx_url":hx_url
    }
    return render(request,"recipe/detail.html",context)

@login_required
def recipe_delete_view(request,id=None):
    obj=get_object_or_404(Recipe,id=id)
    try:
        obj = get_object_or_404(Recipe, id=id, )
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == 'POST':
        obj.delete()
        success_url=reverse("recipe:list")
        if request.htmx:
            header = {
                'HX-Redirect': success_url
            }
            return HttpResponse("Success", headers=header)
        return redirect(success_url)
    context={
        "object":obj
    }
    return render(request,"recipe/delete.html",context)


@login_required
def recipe_ingredient_delete_view(request,parent_id=None,id=None):
    try:
        obj = RecipeIngredients.objects.get(recipe__id=parent_id, id=id, recipe__user=request.user)
    except:
        obj = None
    if obj is None:
        if request.htmx:
            return HttpResponse("Not Found")
        raise Http404
    if request.method == 'POST':
        name=obj.name
        obj.delete()
        success_url=reverse("recipe:detail",kwargs={"id":parent_id})
        if request.htmx:
            return render(request, "recipes/partials/ingredient-inline-delete-response.html", {"name": name})
        return redirect(success_url)
    context={
        "object":obj
    }
    return render(request,"recipe/delete.html",context)


@login_required
def recipe_detail_hx_view(request,id=None):
    if not request.htmx:
        raise Http404
    try:
        obj=Recipe.objects.get(id=id)
    except:
        obj=None
    if obj is None:
        return HttpResponse("Not Found")
    context={
        "object":obj
    }
    return render(request,"recipe/partials/detail.html",context)

@login_required
def recipe_create_view(request,id=None):
    form=RecipeForm(request.POST or None)
    context={
        "form":form
    }

    if form.is_valid():
        obj=form.save(commit=False)
        obj.user=request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
            # context={
            #     "object":obj
            # }
            # return render(request, "recipes/partials/detail.html", context)
        return redirect('recipe_detail_view',id=obj.id)
    return render(request,"recipe/create-update.html",context)


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id)
    form = RecipeForm(request.POST or None, instance=obj)
    #new_ingredient_url = reverse("recipe:hx-ingredient-detail", kwargs={"parent_id": 2, "id": 2})

    new_ingredient_url = reverse("recipe:hx-ingredient-detail", kwargs={"parent_id":2,'id':2})

    context = {
        "form": form,
        "object": obj,
        "new_ingredient_url": new_ingredient_url
    }

    if form.is_valid():
        form.save()
        context['message'] = "Data saved"

    if request.htmx:
        return render(request, "recipe/forms.html", context)

    return render(request, "recipe/create-update.html", context)


@login_required
def recipe_ingredient_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404

    try:
        parent_obj = get_object_or_404(Recipe, id=parent_id, user=request.user)
    except Recipe.DoesNotExist:
        return HttpResponse("Not found.")

    instance = None
    if id is not None:
        instance = get_object_or_404(RecipeIngredients, id=id, recipe=parent_obj)

    form = RecipeIngredientForm(request.POST or None, instance=instance)
    url = reverse("recipe:hx-ingredient-create", kwargs={"parent_id": parent_obj.id})

    if instance:
        url = instance.get_hx_edit_url()

    context = {
        "url": url,
        "form": form,
        "object": instance
    }

    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object'] = new_obj  # Corrected assignment in the context dictionary
        return render(request, "recipes/partials/ingredient-inline.html", context)

    return render(request, "recipes/partials/ingredient-form.html", context)