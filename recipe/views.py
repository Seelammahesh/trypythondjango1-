from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
# Create your views here.
#crud - Create,Retrieve,update,Delete
from .models import Recipe,RecipeIngredients
from .forms import RecipeForm,RecipeIngredientForm

@login_required
def recipe_list_view(request):
    qs=Recipe.objects.all()
    context={
        "objects_list":qs
    }
    return render(request,"recipe/list.html",context)

@login_required
def recipe_detail_view(request,id=None):
    obj=get_object_or_404(Recipe,id=id,)
    context={
        "object":obj
    }
    return render(request,"recipe/detail.html",context)

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
        return redirect('recipe_detail_view',id=obj.id)
    return render(request,"recipe/create-update.html",context)

@login_required
def recipe_update_view(request,id=None):
    obj = get_object_or_404(Recipe, id=id,)
    form=RecipeForm(request.POST or None ,instance=obj)
    #form_2=RecipeIngredientForm(request.POST or None)
    #form_set=modelformset_factory(Model,form=ModelForm,extra=0)
    RecipeIngredientFormset = modelformset_factory(RecipeIngredients,form=RecipeIngredientForm,extra=0)
    qs=obj.recipeingredients_set.all()
    formset=RecipeIngredientFormset(request.POST or None ,queryset=qs)
    context = {
        "form": form,
        "formset":formset,
        #"form_2":form_2,
        "object":obj
    }

    if all([form.is_valid(),formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent
            child.save()
        context['message']="Data saved"
    return render(request, "recipe/create-update.html", context)

