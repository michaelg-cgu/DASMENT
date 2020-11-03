from django.contrib import admin
from .models import Profile, UserRegDemographics

# Register your models here.
# register profile model

admin.site.register(Profile)
admin.site.register(UserRegDemographics)
