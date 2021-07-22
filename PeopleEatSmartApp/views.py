from django.utils.translation import templatize
from .serializers import *
from .forms import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.http import Http404
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
    return render(request, 'PeopleEatSmartApp/index.html', context)


def show_recipe(request, recipe_id):
    # try:
    #     # recipe = Recipe.objects.raw("SELECT * FROM Recipe WHERE RecipeID = %s", [recipe_id])[0]
    #     recipe = Recipe.objects.get(pk=recipe_id)
    # except Recipe.DoesNotExist:
    #     raise Http404("Recipe does not exist")
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return HttpResponse(recipe.name + ' ' + str(recipe.avgrating))


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
            cursor = connection.cursor()
            cursor.execute("INSERT INTO LoginInfo VALUES ('%s', '%s');"%(username, password))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()
    return render(request, 'PeopleEatSmartApp/user_signup.html', {'form': form})


class PeopleEatSmartAppViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.raw("SELECT * FROM Recipe WHERE avgrating = 5.0 AND ratingcount > 10")

    # def search_recipe(request):
    #     return Response(Recipe.objects.raw("SELECT * FROM Recipe WHERE avgrating = 5.0 AND ratingcount > 10"))
        