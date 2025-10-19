from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_stuff/', views.student_stuff, name='student_stuff'),
    path('login_student/', views.login_student, name='login_student'),
    path('login_staff/', views.login_staff, name='login_staff'),
    path('signup/', views.signup, name='signup'),
    path('menu/', views.menu, name='menu'),
    path('logout/', views.logout, name='logout'),
]
