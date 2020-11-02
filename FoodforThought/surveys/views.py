from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import testingForm, SnippetForm, EnviromentalForm


# Create your views here.
# functions create the views, then magic happens


# the below would be replaced by a dictionary


# no longer dummy data


def surveys(request):

    if request.method == 'POST':
        form = testingForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            body = form.cleaned_data['body']

            print(gender, body)

    form = testingForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})


def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetForm()
    return render(request, 'surveys/foodallergies.html', {'form': form})

def enviromental_detail(request):

    if request.method == 'POST':
        eform = EnviromentalForm(request.POST)
        if eform.is_valid():
            eform.save()

    eform = EnviromentalForm()
    return render(request, 'surveys/enviromentalallergies.html', {'eform': eform})
