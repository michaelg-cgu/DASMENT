from django.contrib import admin
from .models import Allergy
from .models import Reaction
from .models import OtherAllergyQuestion
from .models import Environmental


# Register your models here.

admin.site.register(Allergy)
admin.site.register(Reaction)
admin.site.register(OtherAllergyQuestion)
admin.site.register(Environmental)
