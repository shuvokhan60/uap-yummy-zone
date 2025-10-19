"""
URL configuration for yummyzone project.
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Accounts app routes
    path('', include('accounts.urls')),

    # Student routes
    path('student/home/', views.student_home, name='student_home'),
    path('student/menu/', views.student_menu, name='student_menu'),
    path('student/orders/', views.student_orders, name='student_orders'),
    path('student/loyalty/', views.student_loyalty, name='student_loyalty'),

    # Staff routes
    path('staff/home/', views.staff_home, name='staff_home'),
    path('staff/inventory/', views.staff_inventory, name='staff_inventory'),
    path('update_inventory/<int:item_id>/', views.update_inventory, name='update_inventory'),
    path('staff/menu/', views.staff_menu, name='staff_menu'),

    # Optional — student main view
    path('student/', views.student, name='student'),
]
