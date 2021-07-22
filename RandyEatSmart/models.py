from django.db import models

class RandyEatSmart(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
