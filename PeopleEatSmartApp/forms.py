from django import forms
from django.forms.widgets import NumberInput, TextInput


class SignUpForm(forms.Form):
    UserName = forms.CharField(label='UserName', max_length=100)
    Password = forms.CharField(label='Password', max_length=100)


class RatingCommentForm(forms.Form):
    UserName = forms.CharField(label='UserName', max_length=100)
    RecipeName = forms.CharField(label="RecipeName", max_length=1000)
    RatingValue = forms.IntegerField(label="RatingValue")
    '''IMPORTANT: the name here must be exactly the same as the name in html file (within <form>)'''
    Comment = forms.CharField(label="Comment", max_length=4096, widget=forms.Textarea)


class KeywordSearchRecipeForm(forms.Form):
    # RecipeID = forms.IntegerField(label="RecipeID")
    Name = forms.CharField(label='Name')


class AdvancedSearchForm(forms.Form):
    NutrientName = forms.CharField(label="NutrientName", max_length=10000)


class MyRecipeForm(forms.Form):
    RecipeName = forms.CharField(label="RecipeName", max_length=100)


class UserDietType(forms.Form):
    DietType = forms.CharField(label="DietType", max_length=100)
    Calories = forms.IntegerField(label="Calories")
    UserName = forms.CharField(label="UserName", max_length=100)
