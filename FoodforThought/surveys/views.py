from django.shortcuts import render


# Create your views here.
# functions create the views, then magic happens


# the below would be replaced by a dictionary


# no longer dummy data


def surveys(request):
    return render(request, 'surveys/foodallergies.html')
