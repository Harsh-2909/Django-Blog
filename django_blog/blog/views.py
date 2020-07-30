from django.shortcuts import render
from django.http import HttpResponse


posts= [
    {
        'author': 'Harsh Agarwal',
        'topic': 'Data Science',
        'date_posted': '30 July 2020',
        'content': 'Content no 1'
    },
    {
        'author': 'John Doe',
        'topic': 'Data Science',
        'date_posted': '31 July 2020',
        'content': 'Content no 2'
    }
]

# Create your views here.
def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})