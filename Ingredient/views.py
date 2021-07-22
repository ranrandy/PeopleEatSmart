from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.db import connection

def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class IngredientViewSet(viewsets.ModelViewSet):
    # def list(self,request):
    #     queryset = Ingredient.objects.all()
    #     serializer = IngredientSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Ingredient.objects.all()
    #     info = get_object_or_404(queryset,pk=pk)
    #     serializer = IngredientSerializer(info)
    #     return Response(serializer.data)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    @action(detail = False, methods=['post'])
    def search_name(self, request, pk= None):
        ingredientid = request.data.get('ingredientid')

        try:
            info = Ingredient.objects.get(ingredientid=ingredientid)

        except Ingredient.DoesNotExist:
            return Response({"response": {"error":"IngredientID not existent"}, "status": 400}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # instance = Ingredient.objects.raw('SELECT * FROM Ingredient where IngredientID = %s', [ingredientid])
            return Response({"response": {"error":"OK", "ingredientid": info.ingredientid, "ingredientname": info.ingredientname}, "status": 201}, status=status.HTTP_201_CREATED)
