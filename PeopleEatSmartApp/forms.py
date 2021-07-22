from django import forms

class SignUpForm(forms.Form):
    UserName = forms.CharField(label='UserName', max_length=100)
    Password = forms.CharField(label='Password', max_length=100)


class RatingCommentForm(forms.Form):
    UserName = forms.CharField(label='UserName', max_length=100)
    RecipeName = forms.CharField(label="RecipeName", max_length=1000)
    RatingValue = forms.IntegerField(label="RatingValue")
    Comment = forms.CharField(label="Comment", max_length=4096)


class KeywordSearchRecipeForm(forms.Form):
    # RecipeID = forms.IntegerField(label="RecipeID")
    Name = forms.CharField(label='Name')


class AdvancedSearchForm(forms.Form):
    NutrientName = forms.CharField(label="NutrientName", max_length=100)
