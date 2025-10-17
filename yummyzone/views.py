from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

# Signup page
def signup(request):
    return render(request, 'signup.html')

# Student Stuff page
def student_stuff(request):
    return render(request, 'student_stuff.html')

# Student Login
def login_student(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Example authentication
        if username == "student" and password == "12345":
            return redirect('student_home')
        else:
            error = "Invalid username or password"
            return render(request, 'login_student.html', {'error': error})
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
def student_loyalty(request):
    # Example data for now
    current_points = 240
    current_level = "Silver"
    next_level = "Gold"
    points_to_next = 260
    progress_percent = (current_points / 500) * 100  # Example logic

    context = {
        'current_points': current_points,
        'current_level': current_level,
        'next_level': next_level,
        'points_to_next': points_to_next,
        'progress_percent': progress_percent,
    }

    return render(request, 'student_loyalty.html', context)
