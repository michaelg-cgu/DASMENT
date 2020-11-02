from django import forms
from .models import Snippet, Enviromental
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class testingForm(forms.Form):
    allergy = forms.ChoiceField(choices=[('dairy', 'Dairy'), ('soy', 'Soy'), ('wheat', 'Wheat'), ('shellfish', 'Shellfish'), ('nuts', 'Nuts')])
    reaction = forms.ChoiceField(choices=[('none', 'None'), ('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe'), ('toxic', 'Toxic')])

    List_any_other_foods_that_bother_you = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('allergy1',
                  'allergy2',
                  'allergy3',
                  'allergy4',
                  'allergy5')

class EnviromentalForm(forms.ModelForm):

    class Meta:
        model = Enviromental
        fields = ('eallergy1',
                  'eallergy2',
                  'eallergy3',
                  'eallergy4',
                  'eallergy5',
                  'severity1',
                  'severity2',
                  'severity3',
                  'severity4',
                  'severity5')
