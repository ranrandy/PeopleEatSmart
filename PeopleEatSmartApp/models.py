# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contains(models.Model):
    nutrientid = models.OneToOneField('Micronutrient', models.DO_NOTHING, db_column='NutrientID', primary_key=True)  # Field name made lowercase.
    ingredientid = models.ForeignKey('Ingredient', models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contains'
        unique_together = (('nutrientid', 'ingredientid'),)


class Desires(models.Model):
    username = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserName')  # Field name made lowercase.
    nutrientid = models.ForeignKey('Micronutrient', models.DO_NOTHING, db_column='NutrientID')  # Field name made lowercase.
    quantity = models.FloatField(db_column='Quantity')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Desires'


class Diet(models.Model):
    diettype = models.CharField(db_column='DietType', primary_key=True, max_length=100)  # Field name made lowercase.
    carbohydrate = models.FloatField(db_column='Carbohydrate', blank=True, null=True)  # Field name made lowercase.
    protein = models.FloatField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.diettype

    class Meta:
        managed = False
        db_table = 'Diet'


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


class Ingredientof(models.Model):
    recipename = models.CharField(db_column='RecipeName', primary_key=True, max_length=500)  # Field name made lowercase.
    ingredientname = models.CharField(db_column='IngredientName', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IngredientOf'
        unique_together = (('recipename', 'ingredientname'),)


class IngredientofAutoGenerated(models.Model):
    ingredientid = models.IntegerField(db_column='IngredientID', primary_key=True)  # Field name made lowercase.
    recipeid = models.IntegerField(db_column='RecipeID')  # Field name made lowercase.

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'IngredientOf_auto_generated'
        unique_together = (('ingredientid', 'recipeid'),)


class Micronutrient(models.Model):
    nutrientid = models.IntegerField(db_column='NutrientID', primary_key=True)  # Field name made lowercase.
    nutrientname = models.CharField(db_column='NutrientName', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.nutrientname

    class Meta:
        managed = False
        db_table = 'Micronutrient'



class Prefers(models.Model):
    username = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='UserName')  # Field name made lowercase.
    diettype = models.ForeignKey(Diet, models.DO_NOTHING, db_column='DietType')  # Field name made lowercase.
    carbohydrate = models.FloatField(db_column='Carbohydrate', blank=True, null=True)  # Field name made lowercase.
    protein = models.FloatField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.
    fat = models.FloatField(db_column='Fat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Prefers'


class Ratingcomment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ratingvalue = models.IntegerField(db_column='RatingValue')  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recipeid = models.ForeignKey('Recipe', models.DO_NOTHING, db_column='RecipeID', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.recipeid) + ', ' + str(self.ratingvalue) + ', ' + self.username

    class Meta:
        managed = False
        db_table = 'RatingComment'


class Recipe(models.Model):
    recipeid = models.AutoField(db_column='RecipeID', primary_key=True)  # Field name made lowercase.
    author = models.TextField(db_column='Author', blank=True, null=True)  # Field name made lowercase.
    cook_time_minutes = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pictureurl = models.TextField(db_column='PictureURL', blank=True, null=True)  # Field name made lowercase.
    prep_time_minutes = models.IntegerField(blank=True, null=True)
    avgrating = models.FloatField(db_column='AvgRating', blank=True, null=True)  # Field name made lowercase.
    ratingcount = models.IntegerField(db_column='RatingCount', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    total_time_minutes = models.IntegerField(blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Recipe'


class Requires(models.Model):
    diettype = models.OneToOneField(Diet, models.DO_NOTHING, db_column='DietType', primary_key=True)  # Field name made lowercase.
    ingredientid = models.ForeignKey(Ingredient, models.DO_NOTHING, db_column='IngredientID')  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Requires'
        unique_together = (('diettype', 'ingredientid'),)


class Userrecipes(models.Model):
    username = models.OneToOneField('AuthUser', models.DO_NOTHING, db_column='Username', primary_key=True)  # Field name made lowercase.
    recipeid = models.ForeignKey(Recipe, models.DO_NOTHING, db_column='RecipeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserRecipes'
        unique_together = (('username', 'recipeid'),)


class AccountEmailaddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    id = models.BigAutoField(primary_key=True)
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'
