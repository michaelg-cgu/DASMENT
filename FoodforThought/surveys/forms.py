from django import forms
from .models import FoodAllergy, Environmental #, OtherAllergyQuestion
from django.forms import ModelForm, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class AllergyForm(forms.ModelForm):
    class Meta:
        model = FoodAllergy
        fields = ('allergy1',
                  'reaction1',
                  'allergy2',
                  'reaction2',
                  'allergy3',
                  'reaction3',
                  'allergy4',
                  'reaction4',
                  'allergy5',
                  'reaction5')

class EnvironmentalForm(forms.ModelForm):
    class Meta:
        model = Environmental
        fields = ('eallergy1',
                  'severity1',
                  'eallergy2',
                  'severity2',
                  'eallergy3',
                  'severity3',
                  'eallergy4',
                  'severity4',
                  'eallergy5',
                  'severity5')

#class QuestionForm(forms.ModelForm):
#    class Meta:
#        model = OtherAllergyQuestion
#        fields = ('None',)

#class testingForm(forms.Form):
#    Allergy_1 = forms.ChoiceField(choices=[('dairy', 'Dairy')])
#    Reaction_1 = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])
#
#    Allergy_2 = forms.ChoiceField(choices=[('soy', 'Soy')])
#    Reaction_2 = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])
#
#    Allergy_3 = forms.ChoiceField(choices=[('wheat', 'Wheat')])
#    Reaction_3 = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])
#
#
#    Allergy_4 = forms.ChoiceField(choices=[('shellfish', 'Shellfish')])
#    Reaction_4 = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])
#
#    Allergy_5 = forms.ChoiceField(choices=[('nuts', 'Nuts')])
#    Reaction_5 = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])
#
#    List_any_other_foods_that_bother_you = forms.CharField(widget=TextInput(attrs={'size':'20'}))
