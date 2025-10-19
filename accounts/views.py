from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login_student.html')

def logout_page(request):
    return render(request, 'logout.html')

def signup(request):
    return render(request, 'signup.html')

def student_stuff(request):
    return render(request, 'student_stuff.html')
def login_staff_page(request):
    return render(request, 'login_staff.html')

def staff_home(request):
    return render(request, 'staff.html')