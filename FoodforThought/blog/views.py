from django.shortcuts import render
from .models import Post

#below is not needed
#from django.http import HttpResponse

# Create your views here.
# functions create the views, then magic happens


# the below would be replaced by a dictionary


# no longer dummy data


def home(request):
    context = {
        'posts': Post.objects.all()  # this queries the data base using the local commas
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
