from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import  AllergyForm, EnvironmentalForm  #testingForm, QuestionForm


@login_required
def surveys(request):

    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            allergy1 = form.cleaned_data['Allergy_1']
            allergy2 = form.cleaned_data['Allergy_2']
            allergy3 = form.cleaned_data['Allergy_3']
            allergy4 = form.cleaned_data['Allergy_4']
            allergy5 = form.cleaned_data['Allergy 5']

            reaction1 = form.cleaned_data['Reaction_1']
            reaction2 = form.cleaned_data['Reaction_2']
            reaction3 = form.cleaned_data['Reaction_3']
            reaction4 = form.cleaned_data['Reaction_4']
            reaction5 = form.cleaned_data['Reaction_5']

            form.save()
<<<<<<< HEAD
=======
            messages.success(request, f'Your Account has been Create! You are now able to login')
    else:
        form = testingForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


def allergy_detail(request):

    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            form.save()
>>>>>>> samahbasit-master

    form = AllergyForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


@login_required
def environmental_detail(request):

    if request.method == 'POST':
        eform = EnvironmentalForm(request.POST)
        if eform.is_valid():
            eform.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    eform = EnvironmentalForm()
    return render(request, 'surveys/enviromentalallergies.html', {'eform': eform})
