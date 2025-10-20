from django.urls import path
from . import views

urlpatterns = [
    path('student_menu/', views.student_menu, name='student_menu'),
    path('order/<int:item_id>/', views.order_food, name='order_food'),
    path('student_orders/', views.student_orders, name='student_orders'),
    path('pay/<int:order_id>/', views.make_payment, name='make_payment'),
]
