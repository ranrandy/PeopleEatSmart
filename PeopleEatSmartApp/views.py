from decimal import Context
from django.utils.translation import templatize
from .serializers import *
from .forms import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db import connection
from json import dumps
import re


def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


# Static Pages
# Homepage of the website
def HomePageView(request):
    return render(request, 'PeopleEatSmartApp/index.html')

# About page of the website


def AboutPageView(request):
    return render(request, 'PeopleEatSmartApp/about.html')


# User Related Pages
# Sign up page of the website
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/about')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'PeopleEatSmartApp/user/user_signup.html', context)

# Log in page of the website


def user_login(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # valid_user = executeSQL("SELECT count(*) FROM auth_user WHERE username = '{}';".format(user.username))
            # if not valid_user:
            #     context['valid_user'] = False
            # else:
            # correct_password = executeSQL("SELECT * FROM auth_user WHERE username = '{}';".format(user.username))
            # if user.password == correct_password:
            login(request, user)
            context['wrong_password'] = True
            return redirect('/about')
            # else:
            #     context['wrong_password'] = True
    else:
        form = AuthenticationForm()
    context['form'] = form
    return render(request, 'PeopleEatSmartApp/user/user_login.html', context)

# User profile page


def user_ratings(request):
    ratingInfo = []
    context = {}
    user = request.user
    if request.method == 'POST':
        ratingInfo = executeSQL(
            "Select RecipeID, RatingValue, COMMENT Where UserName Like '%%{}%%';".format(user))
    context = {'ratingInfo': ratingInfo}
    return render(request, 'PeopleEatSmartApp/user/user_profile.html', context)


def user_profile(request):
    user = request.user
    dietInfo = []
    calorie = 0
    context = {}
    carb = 0
    protein = 0
    fat = 0
    if request.method == 'POST':
        form = UserDietType(request.POST)
        if form.is_valid():
            diet = form.cleaned_data["DietType"]
            calorie = form.cleaned_data["Calories"]
            user = form.cleaned_data["UserName"]
            dietInfo = executeSQL(
                "SELECT * FROM Diet where DietType= '{}';".format(diet))
            if len(dietInfo):
                dietInfo = dietInfo[0]
                carb = dietInfo['Carbohydrate'] * calorie / 4
                protein = dietInfo['Protein'] * calorie / 4
                fat = dietInfo['Fat'] * calorie / 9
                diet = dietInfo['DietType']
                cursor = connection.cursor()
                temp = executeSQL(
                    "Select * from Prefers where UserName = '{}' and DietType = '{}';" .format(user, diet))
                if len(temp):
                    cursor.execute("UPDATE Prefers SET Carbohydrate = {}, Protein = {}, Fat = {} WHERE UserName = '{}' and DietType = '{}';" .format(
                        carb, protein, fat, user, diet))
                else:
                    cursor.execute("INSERT INTO Prefers (UserName, DietType, Carbohydrate, Protein, Fat) VALUES(\"{}\", \"{}\",{},{},{});" .format(
                        user, diet, carb, protein, fat))
    else:
        form = UserDietType()
    context = {'user': user}

    context['DietTypes'] = executeSQL("SELECT DietType FROM Diet")
    context['Macros'] = {'carb': carb, 'fat': fat, 'Protein': protein}

    return render(request, 'PeopleEatSmartApp/user/user_profile.html', context)


# Log out of the user's current account
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/user-logout')
    return render(request, 'PeopleEatSmartApp/user/user_logout.html')

# TODO: Let user change the password


def user_reset_pw(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["UserName"]
            password = form.cleaned_data["Password"]
            cursor = connection.cursor()
            cursor.execute("UPDATE LoginInfo SET Password = '%s' WHERE UserName = '%s';" % (
                password, username))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return render(request, 'PeopleEatSmartApp/user/user_reset_pw.html', {'form': form})

# TODO: Let user delete his / her account (username)


def user_delete(request):
    username = ""
    password = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["UserName"]
            password = form.cleaned_data["Password"]
            # if not username == "" and not password == ""
            cursor = connection.cursor()
            cursor.execute("DELETE FROM LoginInfo WHERE UserName = '{}' AND Password = '{}';".format(
                username, password))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'PeopleEatSmartApp/user/user_delete.html', context)


# My recipe page
def MyRecipePage(request):
    user = request.user
    context = {}
    if request.method == 'POST':
        form = MyRecipeForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data["RecipeName"]
            description = form.cleaned_data["Description"]
            picture_url = form.cleaned_data["PictureURL"]
            cook_time_minutes = form.cleaned_data["CookTimeMinutes"]
            prep_time_minutes = form.cleaned_data["PrepTimeMinutes"]
            total_time_minutes = form.cleaned_data["TotalTimeMinutes"]
            ingredient = form.cleaned_data["ingredient"].split(';')
            instruction = form.cleaned_data["instruction"].split(';')
            
            ingredients = " && ".join(ingredient)
            instructions = " && ".join(instruction)
            
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Recipe(Name, Author, description, PictureURL, cook_time_minutes, prep_time_minutes, total_time_minutes, ingredients, instructions) VALUES ('{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}')".format(recipe_name, user.username, description, picture_url, cook_time_minutes, prep_time_minutes, total_time_minutes, ingredients, instructions))
            max_recipeID = executeSQL("SELECT MAX(RecipeID) AS max_id FROM Recipe;")
            new_recipeID = max_recipeID[0]['max_id']
            cursor.execute("INSERT INTO UserRecipes VALUES ('{}', {})".format(user.username, new_recipeID))
    else:
        form = KeywordSearchRecipeForm()
    
    my_recipes = executeSQL("SELECT * FROM UserRecipes NATURAL JOIN Recipe;")
    context["my_recipes"] = my_recipes
    
    for recipe in my_recipes:
        neat_ingredients = recipe["ingredients"].replace("\n", " && ").replace("\r", " && ").split(" && ")
        neater_ingredients = []
        for i in neat_ingredients:
            if i:
                neater_ingredients.append(i)
        
        neat_instructions = recipe["instructions"].replace("\n", " && ").replace("\r", " && ").split(" && ")
        neater_instructions = []
        for i in neat_instructions:
            if i:
                neater_instructions.append(i)

        recipe["ingredient_list"] = neater_ingredients
        recipe["instruction_list"] =  neater_instructions
    context['user'] = user
    return render(request, 'PeopleEatSmartApp/my_recipe.html', context)

# My menu page


def MyMenuPage(request):
    return render(request, 'PeopleEatSmartApp/my_menu.html')

# Recipe Display Related Pages
# Search recipe based on keyword, using SQL technique "LIKE '%[keyword]%'".


def RecipeSearchPageView(request):
    recipeInfo = []
    context = {}
    if request.method == 'POST':
        form = KeywordSearchRecipeForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data["Name"]
            recipeInfo = executeSQL(
                "SELECT * FROM Recipe where Name LIKE '%%{}%%' LIMIT 1000;".format(recipe_name))
            context['keyword_entered'] = recipe_name
    else:
        form = KeywordSearchRecipeForm()
    recipes_1 = []
    recipes_2 = []
    recipes_3 = []
    for i in range(len(recipeInfo)):
        if i % 3 == 1:
            recipes_1.append(recipeInfo[i])
        elif i % 3 == 2:
            recipes_2.append(recipeInfo[i])
        else:
            recipes_3.append(recipeInfo[i])
        i += 1
    context['recipe_1'] = recipes_1
    context['recipe_2'] = recipes_2
    context['recipe_3'] = recipes_3
    return render(request, 'PeopleEatSmartApp/recipe.html', context)

# Show all the recipes, TODO: but has a limitation of 100 in 1 page.


def view_recipe(request):
    recipes_all = executeSQL("SELECT * FROM Recipe limit 1000")
    # recipes_all_json = dumps(recipes_all)
    recipes_1 = []
    recipes_2 = []
    recipes_3 = []
    for i in range(len(recipes_all)):
        if i % 3 == 1:
            recipes_1.append(recipes_all[i])
        elif i % 3 == 2:
            recipes_2.append(recipes_all[i])
        else:
            recipes_3.append(recipes_all[i])
        i += 1
    context = {'recipe_1': recipes_1,
               'recipe_2': recipes_2, 'recipe_3': recipes_3}
    return render(request, 'PeopleEatSmartApp/recipes_all.html', context)

# Show certain recipe based on its RecipeID added at the end of the URL.


def show_recipe(request, recipe_id):
    try:
        recipe = executeSQL(
            "SELECT * FROM Recipe WHERE RecipeID = {}".format(recipe_id))[0]
        ingredients_list = recipe['ingredients'].split(' && ')
        instructions_list = recipe['instructions'].split(' && ')
        # recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")
    # recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe, 'ingredients_list': ingredients_list,
               'instructions_list': instructions_list}
    return render(request, 'PeopleEatSmartApp/recipe_detail.html', context)


# Ingredient Display Related Pages
# Search ingredient based on keyword, using SQL technique "LIKE '$[keyword]%'"
def IngredientSearchPageView(request):
    ingredientInfo = []
    context = {}
    if request.method == 'POST':
        form = KeywordSearchRecipeForm(request.POST)
        if form.is_valid():
            ingredient_name = form.cleaned_data["Name"]
            ingredientInfo = executeSQL(
                "SELECT * FROM Ingredient where IngredientName LIKE '%%{}%%' LIMIT 1000;".format(ingredient_name))
            context['keyword_entered'] = ingredient_name
    else:
        form = KeywordSearchRecipeForm()

    context['ingredientInfo'] = ingredientInfo
    return render(request, 'PeopleEatSmartApp/ingredient.html', context)

# Show all the ingredients


def view_ingredient(request):
    ingredients_all = executeSQL("SELECT * FROM Ingredient limit 1000;")
    context = {'ingredients_all': ingredients_all}
    return render(request, 'PeopleEatSmartApp/ingredients_all.html', context)


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
            ratingvalue = form.cleaned_data["RatingValue"]
            comment = form.cleaned_data["Comment"]
            cursor = connection.cursor()
            cursor.execute("INSERT INTO RatingComment (RatingValue, COMMENT, UserName, RecipeID) VALUES ({}, \"{}\", \"{}\", (SELECT RecipeID FROM Recipe WHERE Name = \"{}\"));".format(
                str(ratingvalue), comment, username, recipename))
            return HttpResponse("Successful Comment!")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RatingCommentForm()
    context = {'recipename': recipename, 'username': username,
               'ratingvalue': ratingvalue, 'comment': comment}
    return render(request, 'PeopleEatSmartApp/recipe_rating.html', context)

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
            query = "SELECT IngredientName, COUNT(RecipeID) as CountOfRecipe FROM IngredientOf NATURAL JOIN Ingredient NATURAL JOIN Recipe NATURAL JOIN Contains NATURAL JOIN Micronutrient m WHERE AvgRating > 3 AND Quantity > 5 AND m.NutrientName = '{}' OR m.NutrientName LIKE '%{}%' GROUP BY IngredientID ORDER BY COUNT(RecipeID) DESC LIMIT 50;".format(
                nutrient_name, nutrient_name)
            query_result = executeSQL(query)
    else:
        form = KeywordSearchRecipeForm()
    context = {'query_result': query_result}
    return render(request, 'PeopleEatSmartApp/advanced_search_2.html', context)


def match_ingredient_recipe_view(request):
    query = "SELECT IngredientName FROM Ingredient;"
    ingredient_names = executeSQL(query)
    keyword_list = []
    for i in ingredient_names:
        if ingredient_names.index(i) < 15:
            keyword = i['IngredientName'].split(', ')
            improved_keyword = []
            for k in keyword:
                if k not in ('raw', 'uncooked', 'dried'):
                    improved_keyword.append(k)
            # keyword_list.append(keyword)
            where_clauses = ""
            for k in range(len(improved_keyword)):
                if k == 0:
                    where_clause = " IngredientName LIKE \"% {} %\" ".format(
                        improved_keyword[k])
                else:
                    where_clause = " OR IngredientName LIKE \"% {} %\" ".format(
                        improved_keyword[k])
                where_clauses += where_clause
            sub_query = "SELECT * FROM ingredientOf_source WHERE {};".format(
                where_clauses)
            query_result = executeSQL(sub_query)
            # keyword_list.append(sub_query)
            keyword_list.append(ingredient_names.index(i))

    # context = {'keyword': keyword_list}
    context = {'query_result': query_result, 'test': keyword_list}
    return render(request, 'PeopleEatSmartApp/ingredient_recipe_search.html', context)
