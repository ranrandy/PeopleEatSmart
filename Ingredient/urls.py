from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'ingredient', IngredientViewSet, basename = "IngredientInfo")

urlpatterns = router.urls
