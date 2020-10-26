from django.db import models

allergyList = [
    ('none', 'None'),
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
    ('toxic', 'Toxic'),
]


# Create your models here.
class Snippet(models.Model):
    allergy1 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy2 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy3 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy4 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy5 = models.CharField(max_length=20, default='None', choices=allergyList)

    # def __str__(self):
    #     return self.name
# asdf
