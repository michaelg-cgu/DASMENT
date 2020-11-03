from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import testingForm, AllergyForm, ReactionForm, EnvironmentalForm  # , #QuestionForm


@login_required
def surveys(request):

    if request.method == 'POST':
        form = testingForm(request.POST)
        if form.is_valid():
            allergy1 = form.cleaned_data['Allergy_1']
            allergy2 = form.cleaned_data['Allergy_2']
            allergy3 = form.cleaned_data['Allergy_3']
            allergy4 = form.cleaned_data['Allergy_4']
            allergy5 = form.cleaned_data['Allergy_5']

            reaction1 = form.cleaned_data['Reaction_1']
            reaction2 = form.cleaned_data['Reaction_2']
            reaction3 = form.cleaned_data['Reaction_3']
            reaction4 = form.cleaned_data['Reaction_4']
            reaction5 = form.cleaned_data['Reaction_5']

            form.save()

    form = testingForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


def allergy_detail(request):

    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()

    form = AllergyForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


def reaction_detail(request):

    if request.method == 'POST':
        form = ReactionForm(request.POST)
        if form.is_valid():
            form.save()

    form = ReactionForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


@login_required
def environmental_detail(request):

    if request.method == 'POST':
        eform = EnviromentalForm(request.POST)
        if eform.is_valid():
            eform.save()

    eform = EnvironmentalForm()
    return render(request, 'surveys/enviromentalallergies.html', {'eform': eform})
