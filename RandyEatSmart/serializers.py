from RandyEatSmart.models import RandyEatSmart
from rest_framework import serializers
from .models import *

class RandySerializer(serializers.ModelSerializer):
    class Meta:
        model = RandyEatSmart
        fields = (
            'id', 
            'username', 
            'password'
        )
