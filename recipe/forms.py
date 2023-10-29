from django import forms
from .models import Recipe,RecipeIngredients


class RecipeForm(forms.ModelForm):
    error_css_class ='error-field'
    required_css_class ='requried-field'
    name=forms.CharField(help_text='This is Your Help !<a href="/contact">Contact Us</a>')
    description=forms.CharField(widget=forms.Textarea(attrs={"rows":3,"placeholder":"Recipe Description"}))
    directions = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Recipe Direction"}))
    class Meta:
        model=Recipe
        fields=['name','description','directions']

    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            new_data={
                "palceholder" : f"Recipe{str(field)}",
                "class":'form-control'

            }
            self.fields[str(field)].widgets.attrs.update(new_data)

        #self.fields['name'].label=""
        #self.fields['name'].widgets.attrs.update({"class":"form-control-2"})
        self.fields['description'].widgets.attrs.update({"rows": "2"})
        self.fields['directions'].widgets.attrs.update({"rows": "4"})




class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model=RecipeIngredients
        fields=['name','quantity','unit']