"""
URL configuration for yummyzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from . import views  # project views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login_student/', views.login_student, name='login_student'),
    path('student_stuff/', views.student_stuff, name='student_stuff'),
    path('student_home/', views.student_home, name='student_home'),
    path('student_menu/', views.student_menu, name='student_menu'),
    path('student_orders/', views.student_orders, name='student_orders'),
    path('student_loyalty/', views.student_loyalty, name='student_loyalty'),

    path('login_staff/', views.login_staff, name='login_staff'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_inventory/', views.staff_inventory, name='staff_inventory'),
    path('update_inventory/<int:item_id>/', views.update_inventory, name='update_inventory'),
    path('staff_menu/', views.staff_menu, name='staff_menu'),
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('student/home/', views.student_home, name='student_home'),
    path('student/menu/', views.student_menu, name='student_menu'),
    path('student/orders/', views.student_orders, name='student_orders'),
    path('student/loyalty/', views.student_loyalty, name='student_loyalty'),
    path('staff/home/', views.staff_home, name='staff_home'),
    path('student', views.student, name='student'),


>>>>>>> 90e5e3b3051c9b9fe5b2d582673e2771463fad8c
]

