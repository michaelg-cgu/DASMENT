from django import forms
from .models import Snippet, Enviromental
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class testingForm(forms.Form):
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    body = forms.CharField(widget=forms.Textarea)

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
