from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def student_stuff(request):
    return render(request, 'student_stuff.html')

