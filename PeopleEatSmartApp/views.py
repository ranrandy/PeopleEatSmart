from django.utils.translation import templatize
from .serializers import *
from .forms import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db import connection


# def executeSQL(sql):
#     with connection.cursor() as cursor:
#         cursor.execute(sql)
#         columns = [col[0] for col in cursor.description]
#         return [
#             dict(zip(columns, row))
#             for row in cursor.fetchall()
#         ]

def search_recipe(request):
    high_rating_recipe_list = Recipe.objects.raw("SELECT * FROM Recipe WHERE avgrating = 5.0 AND ratingcount > 10")
    context = {'high_rating_recipe_list': high_rating_recipe_list}    
    return render(request, 'PeopleEatSmartApp/recipes.html', context)


def show_recipe(request, recipe_id):
    # try:
    #     # recipe = Recipe.objects.raw("SELECT * FROM Recipe WHERE RecipeID = %s", [recipe_id])[0]
    #     recipe = Recipe.objects.get(pk=recipe_id)
    # except Recipe.DoesNotExist:
    #     raise Http404("Recipe does not exist")
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'PeopleEatSmartApp/recipe_detail.html', context)


def rate_recipe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RatingCommentForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["UserName"]   
            recipename = forms.cleaned_data["RecipeName"]
            ratingvalue= form.cleaned_data["RatingValue"]
            comment= form.cleaned_data["Comment"]

            cursor = connection.cursor()
            cursor.execute("INSERT INTO RatingComment (RatingValue, COMMENT, UserName, RecipeID) VALUES (%s, '%s', '%s', (SELECT RecipeID FROM Recipe WHERE Name = '%s'));"%(ratingvalue, comment, username, recipename))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RatingCommentForm()
    context = {'form': form}
    return render(request, 'PeopleEatSmartApp/recipe_rating.html', context)


def user_signup(request):
    username = ""
    password = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["UserName"]     
            password= form.cleaned_data["Password"]
            # if not username == "" and not password == ""
            cursor = connection.cursor()
            cursor.execute("INSERT INTO LoginInfo VALUES ('%s', '%s');"%(username, password))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'PeopleEatSmartApp/user_signup.html', context)


def user_reset_pw(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["UserName"]     
            password= form.cleaned_data["Password"]
            cursor = connection.cursor()
            cursor.execute("UPDATE LoginInfo SET Password = '%s' WHERE UserName = '%s';"%(password, username))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return render(request, 'PeopleEatSmartApp/user_reset_pw.html', {'form': form})