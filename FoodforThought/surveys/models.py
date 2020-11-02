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

#Enviromental Allergies
enviromentalChoices = [
    ('none', 'None'),
    ('grass', 'Grass'),
    ('dust', 'Dust'),
    ('pollen', 'Pollen'),
    ('pet dander', 'Pet Dander'),
    ('mold', 'Mold'),
    ('insect bites', 'Insect Bites')
]

severityChoices = [
    ('none', 'None'),
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
    ('deadly', 'Deadly')
]

class Enviromental(models.Model):
    eallergy1 = models.CharField(max_length=20, default='None', choices=enviromentalChoices)
    severity1 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy2 = models.CharField(max_length=20, default='None', choices=enviromentalChoices)
    severity2 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy3 = models.CharField(max_length=20, default='None', choices=enviromentalChoices)
    severity3 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy4 = models.CharField(max_length=20, default='None', choices=enviromentalChoices)
    severity4 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy5 = models.CharField(max_length=20, default='None', choices=enviromentalChoices)
    severity5 = models.CharField(max_length=20, default='None', choices=severityChoices)
