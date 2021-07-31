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


def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def cssView(request):
    return render(request, 'PeopleEatSmartApp/css/mdb.min.css')

def cssView(request):
    return render(request, 'PeopleEatSmartApp/js/mdb.min.js')

# Homepage of the website
def view_homepage(request):
    return render(request, 'PeopleEatSmartApp/index.html')


# Show all the recipes, but has a limitation of 100 in 1 page.
def view_recipe(request):
    high_rating_recipe_list = Recipe.objects.raw("SELECT * FROM Recipe limit 100")
    context = {'high_rating_recipe_list': high_rating_recipe_list}
    return render(request, 'PeopleEatSmartApp/recipes.html', context)


# Show certain recipe based on its RecipeID added at the end of the URL.
def show_recipe(request, recipe_id):
    # try:
    #     # recipe = Recipe.objects.raw("SELECT * FROM Recipe WHERE RecipeID = %s", [recipe_id])[0]
    #     recipe = Recipe.objects.get(pk=recipe_id)
    # except Recipe.DoesNotExist:
    #     raise Http404("Recipe does not exist")
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'PeopleEatSmartApp/recipe_detail.html', context)


# Add ratings and comments for recipes.
def rate_recipe(request):
    recipename = ""
    username = "randy"
    ratingvalue = -1
    comment = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RatingCommentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["UserName"]
            recipename = form.cleaned_data["RecipeName"]
            ratingvalue= form.cleaned_data["RatingValue"]
            comment= form.cleaned_data["Comment"]
            cursor = connection.cursor()
            cursor.execute("INSERT INTO RatingComment (RatingValue, COMMENT, UserName, RecipeID) VALUES ({}, \"{}\", \"{}\", (SELECT RecipeID FROM Recipe WHERE Name = \"{}\"));".format(str(ratingvalue), comment, username, recipename))
            return HttpResponse("Successful Comment!")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RatingCommentForm()
    context = {'recipename': recipename, 'username': username, 'ratingvalue': ratingvalue, 'comment': comment}
    return render(request, 'PeopleEatSmartApp/recipe_rating.html', context)


# Search recipe based on keyword, using SQL technique "LIKE '%[keyword]%'".
def keyword_search_recipe(request):
    recipeInfo = []
    if request.method == 'POST':
        form = KeywordSearchRecipeForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data["Name"]
            recipeInfo = Recipe.objects.raw("SELECT * FROM Recipe where Name LIKE '%%{}%%' LIMIT 50;".format(recipe_name))
    else:
        form = KeywordSearchRecipeForm()
    context = {'recipeInfo': recipeInfo}
    return render(request, 'PeopleEatSmartApp/recipe_search.html', context)


# First advanced query from stage 3.
def advanced_search(request):
    recipeInfo = []
    if request.method == 'POST':
        form = AdvancedSearchForm(request.POST)
        if form.is_valid():
            nutrient_name = form.cleaned_data["NutrientName"]
            recipeInfo = executeSQL("SELECT DISTINCT r.Name, AvgRating, RecipeID FROM Ingredient i NATURAL JOIN Contains c NATURAl JOIN Micronutrient m NATURAL JOIN IngredientOf ino NATURAL JOIN Recipe r WHERE (m.NutrientName = '{}' OR m.NutrientName LIKE '%%{}%%') AND r.AvgRating >= (SELECT AVG(AvgRating) FROM Recipe) LIMIT 50;".format(nutrient_name, nutrient_name))
    else:
        form = KeywordSearchRecipeForm()
    context = {'recipeInfo': recipeInfo}
    return render(request, 'PeopleEatSmartApp/advanced_search.html', context)


# Second advanced query from stage 3.
def advanced_search_2(request):
    query_result = []
    if request.method == 'POST':
        form = AdvancedSearchForm(request.POST)
        if form.is_valid():
            nutrient_name = form.cleaned_data["NutrientName"]
            query = "SELECT IngredientName, COUNT(RecipeID) as CountOfRecipe FROM IngredientOf NATURAL JOIN Ingredient NATURAL JOIN Recipe NATURAL JOIN Contains NATURAL JOIN Micronutrient m WHERE AvgRating > 3 AND Quantity > 5 AND m.NutrientName = '{}' OR m.NutrientName LIKE '%{}%' GROUP BY IngredientID ORDER BY COUNT(RecipeID) DESC LIMIT 50;".format(nutrient_name, nutrient_name)
            query_result = executeSQL(query)
    else:
        form = KeywordSearchRecipeForm()
    context = {'query_result': query_result}
    return render(request, 'PeopleEatSmartApp/advanced_search_2.html', context)


# Add a new user to the database
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


# Let user change the password
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


# Let user delete his / her account (username)
def user_delete(request):
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
            cursor.execute("DELETE FROM LoginInfo WHERE UserName = '{}' AND Password = '{}';".format(username, password))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'PeopleEatSmartApp/user_delete.html', context)

