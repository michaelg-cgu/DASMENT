from django import forms
from .models import Allergy, Reaction, Environmental  # , OtherAllergyQuestion
from django.forms import ModelForm, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import UserCreationForm


class testingForm(forms.Form):
    Allergy_1 = forms.ChoiceField(choices=[('dairy', 'Dairy')])
    Reaction_1 = forms.ChoiceField(choices=[(
        'none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])

    Allergy_2 = forms.ChoiceField(choices=[('soy', 'Soy')])
    Reaction_2 = forms.ChoiceField(choices=[(
        'none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])

    Allergy_3 = forms.ChoiceField(choices=[('wheat', 'Wheat')])
    Reaction_3 = forms.ChoiceField(choices=[(
        'none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])

    Allergy_4 = forms.ChoiceField(choices=[('shellfish', 'Shellfish')])
    Reaction_4 = forms.ChoiceField(choices=[(
        'none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])

    Allergy_5 = forms.ChoiceField(choices=[('nuts', 'Nuts')])
    Reaction_5 = forms.ChoiceField(choices=[(
        'none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('deadly', 'Deadly')])

    List_any_other_foods_that_bother_you = forms.CharField(widget=TextInput(attrs={'size': '20'}))


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ('allergy1',
                  'allergy2',
                  'allergy3',
                  'allergy4',
                  'allergy5')


class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ('reaction1',
                  'reaction2',
                  'reaction3',
                  'reaction4',
                  'reaction5')

# class QuestionForm(forms.ModelForm):
#    class Meta:
#        model = OtherAllergyQuestion
#        fields = ('None',)


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
