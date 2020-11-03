from django.db import models

allergyList = [
    ('none', 'None'),
    ('dairy', 'Dairy'),
    ('soy', 'Soy'),
    ('wheat', 'Wheat'),
    ('shellfish', 'Shellfish'),
    ('nuts', 'Nuts')
]

reactionList = [
    ('none', 'None'),
    ('mild', 'Mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
    ('toxic', 'Toxic')
]

#Food Allergies
class Allergy(models.Model):
    allergy1 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy2 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy3 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy4 = models.CharField(max_length=20, default='None', choices=allergyList)
    allergy5 = models.CharField(max_length=20, default='None', choices=allergyList)

class Reaction(models.Model):
    reaction1 = models.CharField(max_length=20, default='None', choices=reactionList)
    reaction2 = models.CharField(max_length=20, default='None', choices=reactionList)
    reaction3 = models.CharField(max_length=20, default='None', choices=reactionList)
    reaction4 = models.CharField(max_length=20, default='None', choices=reactionList)
    reaction5 = models.CharField(max_length=20, default='None', choices=reactionList)

class OtherAllergyQuestion(models.Model):
    question = models.CharField(max_length=20)


#Environmental Allergies
environmentalChoices = [
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

class Environmental(models.Model):
    eallergy1 = models.CharField(max_length=20, default='None', choices=environmentalChoices)
    severity1 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy2 = models.CharField(max_length=20, default='None', choices=environmentalChoices)
    severity2 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy3 = models.CharField(max_length=20, default='None', choices=environmentalChoices)
    severity3 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy4 = models.CharField(max_length=20, default='None', choices=environmentalChoices)
    severity4 = models.CharField(max_length=20, default='None', choices=severityChoices)
    eallergy5 = models.CharField(max_length=20, default='None', choices=environmentalChoices)
    severity5 = models.CharField(max_length=20, default='None', choices=severityChoices)
