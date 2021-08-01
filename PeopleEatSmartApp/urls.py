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

    path('recipe-search/', views.view_recipe, name='view_recipe'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='show_recipe'),
    path('recipe/keyword-search/', views.keyword_search_recipe, name='keyword_search_recipe'),
    path('recipe/rating/', views.rate_recipe, name='rate_recipe'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('advanced-search-2/', views.advanced_search_2, name='advanced_search_2'),
    path('ingredient-recipe-search/', views.match_ingredient_recipe_view, name='ingredient_recipe_search')
    # url('^', include('django.contrib.auth.urls'))
]
