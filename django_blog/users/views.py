from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            pfp = Profile(user= user)
            pfp.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account {username} created. You can login now.")
            return redirect('user-login')
    else:
        form  = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

@login_required
def profile(request):
    return render(request, 'users/profile.html')