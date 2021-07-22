from django.db import models

class Ingredient(models.Model):
    ingredientid = models.IntegerField(db_column='IngredientID', primary_key=True)  # Field name made lowercase.
    ingredientname = models.CharField(db_column='IngredientName', max_length=255)  # Field name made lowercase.
    calorie = models.IntegerField(db_column='Calorie', blank=True, null=True)  # Field name made lowercase.
    protein = models.FloatField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.
    carbohydrate = models.FloatField(db_column='Carbohydrate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ingredient'
