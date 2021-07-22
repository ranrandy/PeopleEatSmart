from Ingredient.models import Ingredient
from rest_framework import serializers
from .models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'ingredientid',
            'ingredientname'
        )
