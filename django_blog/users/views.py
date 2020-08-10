from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
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
    userForm = UserUpdateForm(request.POST or None, instance= request.user)
    profileForm = ProfileUpdateForm(request.POST or None, request.FILES, instance= request.user.profile)

    if userForm.is_valid() and profileForm.is_valid():
        userForm.save()
        username = userForm.cleaned_data.get('username')
        messages.success(request, f"Account {username} successfully updated!")

    context = {
        'u_form': userForm,
        'p_form': profileForm,
        'title': 'Profile'
    }
    return render(request, 'users/profile.html', context)