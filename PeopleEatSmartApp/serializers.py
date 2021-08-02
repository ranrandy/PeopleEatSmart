from PeopleEatSmartApp.models import *
from rest_framework import serializers
from .models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'ingredientid',
            'ingredientname',
            'calorie',
            'protein',
            'fat',
            'carbohydrate'
        )


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'recipeid',
            'name',
            'avgrating',
            'ratingcount',
            'pictureurl',
            'author',
            'cook_time_minutes',
            'description',
            'prep_time_minutes',
            'total_time_minutes',
            'ingredients',
            'instructions'
        )


class MicronutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Micronutrient
        fields = (
            'nutrientid',
            'nutrientname'
        )
