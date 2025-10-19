from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Login successful!")
            return redirect('student_home')
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'login_student.html')

def logout_page(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = fullname
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login_student')

    return render(request, 'signup.html')

def student_stuff(request):
    return render(request, 'student_stuff.html')
<<<<<<< HEAD
def login_staff_page(request):
    return render(request, 'login_staff.html')

def staff_home(request):
    return render(request, 'staff.html')
=======

def menu(request):
    return render(request, 'menu.html')

def login_staff(request):
    return render(request, 'login_staff.html')

def login_staff(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Login successful!")
            return redirect('/admin/')
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'login_staff.html')
>>>>>>> 90e5e3b3051c9b9fe5b2d582673e2771463fad8c
