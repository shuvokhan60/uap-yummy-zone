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
from django.urls import path, include
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),

    path('login_student/', views.login_student, name='login_student'),
    path('login_staff/', views.login_staff, name='login_staff'),
=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
>>>>>>> b14492c (shuvo)

    path('student/home/', views.student_home, name='student_home'),
    path('student/menu/', views.student_menu, name='student_menu'),
    path('student/orders/', views.student_orders, name='student_orders'),

    path('staff/home/', views.staff_home, name='staff_home'),

    path('student_stuff/', views.student_stuff, name='student_stuff'),
]
