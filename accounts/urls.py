from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_stuff/', views.student_stuff, name='student_stuff'),
    path('login_student/', views.login_student, name='login_student'),
    path('login_student/', views.login_student, name='login_staff'),
    path('signup/', views.signup, name='signup'),
]
