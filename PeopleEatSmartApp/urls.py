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
    path('recipe/', views.search_recipe, name='search_recipe'),
    path('recipe/<int:recipe_id>/', views.show_recipe, name='show_recipe'),
    path('recipe/rating/', views.rate_recipe, name='rate_recipe'),
    path('user-signup/', views.user_signup, name='user_signup'),
    path('user-reset-pw/', views.user_reset_pw, name='user_reset_pw'),
    # url('^', include('django.contrib.auth.urls'))
]