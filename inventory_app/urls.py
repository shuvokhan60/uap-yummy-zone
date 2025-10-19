from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_home, name='staff_home'),
    path('staff/inventory/', views.staff_inventory, name='staff_inventory'),
    path('staff/inventory/update/<int:item_id>/', views.update_inventory, name='update_inventory'),
]
