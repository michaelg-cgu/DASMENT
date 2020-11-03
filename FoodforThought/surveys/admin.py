from django.contrib import admin
from .models import FoodAllergy, Environmental, OtherAllergyQuestion


admin.site.register(FoodAllergy)
admin.site.register(OtherAllergyQuestion)
admin.site.register(Environmental)
