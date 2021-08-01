from django.urls import path, include
from .views import *
from . import views

# app_name = "PeopleEatSmart"
urlpatterns = [
    path('', HomePageView, name='view_homepage'),
    path('about/', AboutPageView, name='view_about_page'),
    path('user-signup/', views.user_signup, name='user_signup'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),

    path('user-reset-pw/', views.user_reset_pw, name='user_reset_pw'),
    path('user-delete/', views.user_delete, name='user_delete'),

    path('user-profile/', views.user_profile, name='user_profile'),



    path('recipe/', RecipeSearchPageView, name='view_recipe_search_page'),
    path('recipes/', views.view_recipe, name='view_all_recipes'),
    
    path('recipes/<int:recipe_id>/', views.show_recipe, name='show_recipe'),

    path('recipe/rating/', views.rate_recipe, name='rate_recipe'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('advanced-search-2/', views.advanced_search_2, name='advanced_search_2'),
    path('ingredient-recipe-search/', views.match_ingredient_recipe_view, name='ingredient_recipe_search'),



    path('ingredient/', IngredientSearchPageView, name='view_ingredient_search_page'),
    path('ingredients/', views.view_ingredient, name='view_all_ngredients')
    # url('^', include('django.contrib.auth.urls'))
]
