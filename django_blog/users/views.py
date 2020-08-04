from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form  = UserCreationForm()

    return render(request, 'users/register.html', {'form': form.as_p()})