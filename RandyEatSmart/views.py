from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection

# from rest_framework.decorators import api_view

def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

class RandyViewSet(viewsets.ModelViewSet):
    serializer_class = RandySerializer

    def get_queryset(self):
        queryset = RandyEatSmart.objects.all()
        return queryset

    def create(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        try:
            user = RandyEatSmart.objects.get(username=username) 
            # user = RandyEatSmart.objects.raw("SELECT password from RandyEatSmart_randyeatsmart where username = %s", [username])

        except RandyEatSmart.DoesNotExist:
            new_user = RandyEatSmart(username=username, password=password)
            new_user.save()
            return Response({"response": {"error":"OK", "id": new_user.id, 
                                                        "username": new_user.username, 
                                                        "password": new_user.password}, 
                                                        "status": 201}, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"response": {"error":"This username already exists."}, "status": 400}, status=status.HTTP_400_BAD_REQUEST)
    
class RandyView(APIView):
    serializer_class = RandySerializer

    def get(self, request):
        loginInfo = [ {"name": user.name,"password": user.password} 
        for user in RandyEatSmart.objects.all()]

        return Response(loginInfo)
  
    def post(self, request):
        serializer = RandySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    


class RobertViewSet (viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    def retrieve(self, request, pk):
        print("debug: RobertViewSet#retrieve")
        try:
            ing = Ingredient.objects.get(ingredientid=pk)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"id": ing.ingredientid, "name": ing.ingredientname})
