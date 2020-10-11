from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Create! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'myusers/register.html', {'form': form})

# the @ adds functionality to the component below
@login_required
def profile(request):
    return render(request, 'myusers/profile.html')
