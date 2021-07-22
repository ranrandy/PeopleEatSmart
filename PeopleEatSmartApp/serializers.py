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
            'pictureurl'
        )


class LoginInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logininfo
        fields = (
            'username',
            'password'
        )


class MicronutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Micronutrient
        fields = (
            'nutrientid',
            'nutrientname'
        )
