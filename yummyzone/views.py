
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

# Signup page
def signup(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already used!")
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=fullname
        )
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login_student')

    return render(request, 'signup.html')

# Student Stuff page
def student_stuff(request):
    return render(request, 'student_stuff.html')


# Student Login
def login_student(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django authentication check
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Django built-in login
            messages.success(request, f"Welcome, {user.first_name}!")
            return redirect('student_home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login_student.html')

# Student Home page
def student_home(request):
    return render(request, 'student.html')

# Student Menu page
def student_menu(request):
    # Example menu items
    menu_items = [
        {'name': 'Burger', 'price': 120},
        {'name': 'Pizza', 'price': 200},
        {'name': 'Pasta', 'price': 200},
        {'name': 'Salad', 'price': 60},
    ]
    return render(request, 'menu.html', {'menu_items': menu_items})

# Staff Login

    return render(request, 'login_student.html')


def login_staff(request):
    if request.method == "POST":
        username = request.POST.get('username')

        password = request.POST.get('password')
        if username == "staff" and password == "12345":
            return redirect('staff_home')
        else:
            error = "Invalid username or password"
            return render(request, 'login_staff.html', {'error': error})

    return render(request, 'login_staff.html')

def staff_home(request):
    return render(request, 'staff.html')
def student_orders(request):
    # Example data
    orders = [
        {'order': 'Burger', 'date': '2025-10-15', 'status': 'Delivered', 'amount': '120'},
        {'order': 'Pizza', 'date': '2025-10-14', 'status': 'Pending', 'amount': '200'},
        {'order': 'Salad', 'date': '2025-10-13', 'status': 'Cancelled', 'amount': '60'},
    ]
    return render(request, 'student_orders.html', {'orders': orders})

def student_stuff(request):
    return render(request, 'student_stuff.html')

def student(request):
    return render(request, 'student.html')

