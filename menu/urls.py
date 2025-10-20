from django.urls import path
from . import views

urlpatterns = [

    # ==========================
    # 🎓 STUDENT SIDE
    # ==========================
    path('student/menu/', views.student_menu, name='student_menu'),
    path('student/order/<int:item_id>/', views.order_food, name='order_food'),
    path('student/orders/', views.student_orders, name='student_orders'),
    path('student/pay/<int:order_id>/', views.make_payment, name='make_payment'),

    # ==========================
    # 👨‍🍳 STAFF SIDE (MENU MANAGEMENT)
    # ==========================
    path('staff/menu/', views.staff_menu, name='staff_menu'),
    path('staff/menu/add/', views.add_food, name='add_food'),
    path('staff/menu/edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('staff/menu/delete/<int:food_id>/', views.delete_food, name='delete_food'),

    # ==========================
    # 🧾 STAFF SIDE (MANAGE ORDERS)
    # ==========================
    path('staff/orders/', views.manage_orders, name='manage_orders'),
    path('staff/orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),

path('staff/orders/', views.manage_orders, name='manage_orders'),
path('staff/orders/update/<int:order_id>/', views.update_order_status, name='update_order_status'),

]
