from django.urls import path, include
from .views import *
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'randy', RandyViewSet, basename = "test")
# router.register(r'robert', RobertViewSet, basename = "test2")
# router.register(r'robert/<int:key>', RobertViewSet, basename = "test2")

# router.register(r'app/', PeopleEatSmartAppViewSet, basename="app")
# router.register(r'app/<int: recipeid>/results/', PeopleEatSmartAppViewSet, basename='recipe')

# urlpatterns = router.urls

# app_name = "PeopleEatSmart"
urlpatterns = [
    path('recipe/', views.view_recipe, name='view_recipe'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='show_recipe'),
    path('recipe/keyword-search/', views.keyword_search_recipe, name='keyword_search_recipe'),
    path('recipe/rating/', views.rate_recipe, name='rate_recipe'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
    path('user-signup/', views.user_signup, name='user_signup'),
    path('user-reset-pw/', views.user_reset_pw, name='user_reset_pw'),
    path('user-delete/', views.user_delete, name='user_delete'),
    # url('^', include('django.contrib.auth.urls'))
]
