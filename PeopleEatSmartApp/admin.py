from django.contrib import admin

from .models import *

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Logininfo)
admin.site.register(Ratingcomment)
admin.site.register(Micronutrient)
admin.site.register(Diet)
admin.site.register(Contains)